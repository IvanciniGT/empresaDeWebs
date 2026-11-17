"""Mapas estáticos de OpenStreetMap, sin navegador.

La vista incrustada de openstreetmap.org necesita WebGL y Chrome headless no lo
tiene, así que componemos las teselas a mano.

Cumple la política de teselas de OSM (operations.osmfoundation.org/policies/tiles):
User-Agent propio, caché local de al menos 7 días con petición condicional al
caducar, y atribución visible. En un PDF la atribución tiene que llevar impresa
la dirección openstreetmap.org/copyright, así que va dentro de la imagen.

Uso:
  .venv/bin/python herramientas/mapa.py LAT LON salida.png [zoom]
  .venv/bin/python herramientas/mapa.py LAT LON salida.png ZOOM puntos.json RADIO_M
      puntos.json: lista de [dx_m, dy_m, destacado, nombre] relativa a LAT, LON.

Variables de entorno (opcionales):
  OSM_TESELAS  plantilla de URL del servidor de teselas (por defecto, el de OSM)
  OSM_CACHE    carpeta de la caché (por defecto ~/Library/Caches/empresaDeWebs/teselas-osm)
"""
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AGENTE = "empresaDeWebs/0.2 (+mailto:ivan.osuna.ayuste@gmail.com)"
# La política pide poder cambiar de servidor sin tocar el código.
SERVIDOR = os.environ.get("OSM_TESELAS", "https://tile.openstreetmap.org/{z}/{x}/{y}.png")
CACHE = Path(os.environ.get("OSM_CACHE", Path.home() / "Library/Caches/empresaDeWebs/teselas-osm"))
CADUCIDAD_S = 7 * 24 * 3600
TESELA = 256
ROJO, NARANJA, AZUL = (200, 30, 45), (181, 90, 30), (30, 42, 58)
ATRIBUCION = "© Colaboradores de OpenStreetMap · openstreetmap.org/copyright"


def _a_pixel(lat, lon, zoom):
    n = 2 ** zoom
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x * TESELA, y * TESELA


def _descargar(x, y, zoom):
    fichero = CACHE / str(zoom) / str(x) / f"{y}.png"
    if fichero.exists() and time.time() - fichero.stat().st_mtime < CADUCIDAD_S:
        return Image.open(fichero).convert("RGB")
    fichero.parent.mkdir(parents=True, exist_ok=True)
    temporal = fichero.with_suffix(".descarga")
    # curl y no urllib: el Python de python.org en macOS no trae certificados raíz.
    # Con -z, si la tesela no ha cambiado, el servidor responde 304 sin enviarla.
    orden = ["curl", "-sS", "-m", "20", "-A", AGENTE, "-o", str(temporal), "-w", "%{http_code}"]
    if fichero.exists():
        orden += ["-z", str(fichero)]
    codigo = subprocess.run(orden + [SERVIDOR.format(z=zoom, x=x, y=y)],
                            capture_output=True, text=True, check=True).stdout.strip()
    if codigo == "304":
        temporal.unlink(missing_ok=True)
        fichero.touch()
    elif codigo == "200":
        temporal.replace(fichero)
    else:
        temporal.unlink(missing_ok=True)
        raise RuntimeError(f"El servidor de teselas ha respondido {codigo} para {zoom}/{x}/{y}")
    return Image.open(fichero).convert("RGB")


def _fuente(tam):
    for ruta in ("/System/Library/Fonts/Avenir Next.ttc", "/System/Library/Fonts/Helvetica.ttc"):
        try:
            return ImageFont.truetype(ruta, tam)
        except OSError:
            continue
    return ImageFont.load_default()


def componer(lat, lon, zoom, ancho, alto, apagar=0.0):
    """Devuelve el lienzo y una función metros→píxel centrada en (lat, lon)."""
    px, py = _a_pixel(lat, lon, zoom)
    izq, arr = px - ancho / 2, py - alto / 2
    lienzo = Image.new("RGB", (ancho, alto))
    for tx in range(int(izq // TESELA), int((izq + ancho) // TESELA) + 1):
        for ty in range(int(arr // TESELA), int((arr + alto) // TESELA) + 1):
            lienzo.paste(_descargar(tx, ty, zoom), (int(tx * TESELA - izq), int(ty * TESELA - arr)))
    if apagar:
        # Aclara el mapa para que los puntos destaquen sobre él.
        lienzo = Image.blend(lienzo, Image.new("RGB", lienzo.size, "white"), apagar)
    metros_por_pixel = 156543.03392 * math.cos(math.radians(lat)) / 2 ** zoom

    def metros_a_pixel(dx, dy):
        return ancho / 2 + dx / metros_por_pixel, alto / 2 - dy / metros_por_pixel

    return lienzo, metros_a_pixel, metros_por_pixel


def atribucion(lienzo):
    dibujo = ImageDraw.Draw(lienzo)
    ancho, alto = lienzo.size
    texto = ATRIBUCION
    fuente = _fuente(14)
    caja = dibujo.textbbox((0, 0), texto, font=fuente)
    w, h = caja[2] - caja[0], caja[3] - caja[1]
    dibujo.rectangle((ancho - w - 16, alto - h - 12, ancho, alto), fill="white")
    dibujo.text((ancho - w - 8, alto - h - 8), texto, fill=(60, 60, 60), font=fuente)


def marcador(dibujo, x, y, r=16):
    dibujo.ellipse((x - r, y - r, x + r, y + r), fill=ROJO, outline="white", width=4)


def mapa_simple(lat, lon, salida, zoom=17):
    lienzo, _, _ = componer(lat, lon, zoom, 1200, 700)
    marcador(ImageDraw.Draw(lienzo), 600, 350)
    atribucion(lienzo)
    lienzo.save(salida)


def mapa_competencia(lat, lon, salida, zoom, puntos, radio_m):
    lado = 1100
    lienzo, a_px, mpp = componer(lat, lon, zoom, lado, lado, apagar=0.45)
    capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    dibujo = ImageDraw.Draw(capa)
    fuente = _fuente(18)
    for anillo in (250, 500, 1000, radio_m):
        r = anillo / mpp
        c = lado / 2
        dibujo.ellipse((c - r, c - r, c + r, c + r), outline=(30, 42, 58, 170), width=2)
        etiqueta = f"{anillo} m" if anillo < 1000 else f"{anillo / 1000:g} km".replace(".", ",")
        caja = dibujo.textbbox((c + 8, c - r + 6), etiqueta, font=fuente)
        dibujo.rounded_rectangle((caja[0] - 5, caja[1] - 3, caja[2] + 5, caja[3] + 3), 6, fill=(255, 255, 255, 230))
        dibujo.text((c + 8, c - r + 6), etiqueta, fill=(30, 42, 58, 255), font=fuente)
    for dx, dy, destacado, _nombre in puntos:
        if math.hypot(dx, dy) > radio_m or (dx, dy) == (0, 0):
            continue
        x, y = a_px(dx, dy)
        color = (*NARANJA, 235) if destacado else (*AZUL, 200)
        dibujo.ellipse((x - 6, y - 6, x + 6, y + 6), fill=color, outline=(255, 255, 255, 230), width=2)
    lienzo = Image.alpha_composite(lienzo.convert("RGBA"), capa).convert("RGB")
    marcador(ImageDraw.Draw(lienzo), lado / 2, lado / 2, 18)
    atribucion(lienzo)
    lienzo.save(salida)


def main():
    lat, lon, salida = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
    zoom = int(sys.argv[4]) if len(sys.argv) > 4 else 17
    if len(sys.argv) > 6:
        with open(sys.argv[5]) as f:
            puntos = json.load(f)
        mapa_competencia(lat, lon, salida, zoom, puntos, int(sys.argv[6]))
    else:
        mapa_simple(lat, lon, salida, zoom)
    print(salida)


if __name__ == "__main__":
    main()
