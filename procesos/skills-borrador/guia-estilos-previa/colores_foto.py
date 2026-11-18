"""Colores dominantes de una foto (o de una zona), para partir de los colores
reales del cliente: rótulo, fachada, local. Hace de cuentagotas sin ventanas.

Uso:
    .venv/bin/python procesos/skills-borrador/guia-estilos-previa/colores_foto.py foto.jpg
    .venv/bin/python .../colores_foto.py foto.jpg --zona 10,20,50,15 -n 5
        --zona izquierda,arriba,ancho,alto en % de la foto (p. ej. solo el rótulo)

Devuelve una tabla Markdown con cada color, su proporción y su contraste con
blanco y con negro, para saber si sirve para texto o solo para superficies.
La luz engaña: mejor varias fotos o varias zonas del mismo elemento.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contraste import contraste, _coma  # noqa: E402


def colores(ruta, zona=None, n=6):
    imagen = Image.open(ruta).convert("RGB")
    if zona:
        x, y, w, h = zona
        ancho, alto = imagen.size
        imagen = imagen.crop((int(ancho * x / 100), int(alto * y / 100),
                              int(ancho * (x + w) / 100), int(alto * (y + h) / 100)))
    # Reducir antes acelera y quita el ruido de la compresión.
    imagen.thumbnail((300, 300))
    # La mediana sola corta por número de píxeles y mezcla colores (con 70 % marrón
    # y 30 % blanco devolvía un marrón claro que no existe); unas pasadas de
    # k-medias lo devuelven a los colores reales.
    reducida = imagen.quantize(colors=n, method=Image.Quantize.MEDIANCUT, kmeans=5)
    paleta = reducida.getpalette()
    cuentas = sorted(reducida.getcolors(), reverse=True)
    total = sum(c for c, _ in cuentas)
    resultado = []
    for cuenta, indice in cuentas:
        r, g, b = paleta[indice * 3:indice * 3 + 3]
        resultado.append((f"#{r:02X}{g:02X}{b:02X}", cuenta / total))
    return resultado


def main(argumentos=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("foto")
    p.add_argument("--zona", help="izquierda,arriba,ancho,alto en %%")
    p.add_argument("-n", type=int, default=6, help="cuántos colores (6 por defecto)")
    a = p.parse_args(argumentos)
    zona = None
    if a.zona:
        try:
            zona = [float(v) for v in a.zona.split(",")]
            assert len(zona) == 4 and all(0 <= v <= 100 for v in zona)
        except (ValueError, AssertionError):
            p.error("--zona necesita cuatro números entre 0 y 100: izquierda,arriba,ancho,alto")
    print("| Color | Proporción | Contraste con blanco | Contraste con negro |")
    print("|---|---|---|---|")
    for hexa, proporcion in colores(a.foto, zona, a.n):
        print(f"| `{hexa}` | {round(proporcion * 100)} % | {_coma(contraste(hexa, '#FFFFFF'))} : 1 "
              f"| {_coma(contraste(hexa, '#000000'))} : 1 |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
