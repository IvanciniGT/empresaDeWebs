"""Mapas estáticos de OpenStreetMap, sin navegador.

La vista incrustada de openstreetmap.org necesita WebGL y Chrome headless no lo
tiene, así que componemos las teselas a mano. La licencia ODbL obliga a citar
a los colaboradores de OpenStreetMap: la atribución va dentro de la imagen.

Uso:
  .venv/bin/python herramientas/mapa.py LAT LON salida.png [zoom]
  .venv/bin/python herramientas/mapa.py LAT LON salida.png ZOOM puntos.json RADIO_M
      puntos.json: lista de [dx_m, dy_m, destacado, nombre] relativa a LAT, LON.
"""
import io
import json
import math
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

AGENTE = "empresaDeWebs-prueba/0.1 (ivan.osuna.ayuste@gmail.com)"
TESELA = 256
ROJO, NARANJA, AZUL = (200, 30, 45), (181, 90, 30), (30, 42, 58)


def _a_pixel(lat, lon, zoom):
    n = 2 ** zoom
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x * TESELA, y * TESELA


def _descargar(x, y, zoom):
    # curl y no urllib: el Python de python.org en macOS no trae certificados raíz.
    datos = subprocess.run(
        ["curl", "-sf", "-m", "20", "-A", AGENTE, f"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png"],
        capture_output=True, check=True,
    ).stdout
    return Image.open(io.BytesIO(datos)).convert("RGB")


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
    texto = "© Colaboradores de OpenStreetMap"
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
