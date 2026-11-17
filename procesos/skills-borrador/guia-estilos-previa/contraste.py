"""Contraste WCAG 2.2 entre pares de colores, con el veredicto que usamos.

Comprueba también el 3 : 1 de lo que no es texto (bordes de botones y campos,
iconos, indicador de foco: criterio 1.4.11), que es justo lo que se olvida al
mirar solo el texto.

Uso (sin dependencias, vale el python3 del sistema):
    python3 contraste.py "#1F2A37:#F6F0E6" "#FFFFFF:#9A5B2E"
    python3 contraste.py --minimo 4.5 "#9A5B2E:#F6F0E6"   # sale con error si alguno no llega

El primer color de cada par es el de delante (texto, borde, icono) y el segundo,
el del fondo.
"""
import argparse
import re
import sys

TEXTO_NORMAL = 4.5
TEXTO_GRANDE = 3.0   # ≥ 24 px, o ≥ 18,66 px en negrita
NO_TEXTO = 3.0


def _canal_lineal(valor):
    v = valor / 255
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def luminancia(hexa):
    if not re.fullmatch(r"#?[0-9a-fA-F]{6}", hexa):
        raise ValueError(f"Color no válido: {hexa!r} (formato #RRGGBB)")
    hexa = hexa.lstrip("#")
    r, g, b = (_canal_lineal(int(hexa[i:i + 2], 16)) for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(delante, fondo):
    claro, oscuro = sorted((luminancia(delante), luminancia(fondo)), reverse=True)
    return (claro + 0.05) / (oscuro + 0.05)


def veredicto(ratio):
    if ratio >= TEXTO_NORMAL:
        return "Texto de cualquier tamaño"
    if ratio >= TEXTO_GRANDE:
        return "Solo texto grande, bordes e iconos"
    return "Solo decoración"


def _coma(numero):
    # Truncar y no redondear: 4,496 redondeado da «4,5» y parece que pasa cuando no pasa.
    return f"{int(numero * 100) / 100:.2f}".replace(".", ",")


def main(argumentos=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("pares", nargs="+", help='"#DELANTE:#FONDO"')
    p.add_argument("--minimo", type=float, help="falla (código 1) si algún par no llega a este contraste")
    a = p.parse_args(argumentos)

    resultados = []
    for par in a.pares:
        delante, _, fondo = par.partition(":")
        try:
            resultados.append((delante, fondo, contraste(delante, fondo)))
        except ValueError as error:
            p.error(f"{error} en {par!r}")

    print("| Delante | Fondo | Contraste | Sirve para |")
    print("|---|---|---|---|")
    fallos = 0
    for delante, fondo, r in resultados:
        if a.minimo and r < a.minimo:
            fallos += 1
        print(f"| `{delante.upper()}` | `{fondo.upper()}` | {_coma(r)} : 1 | {veredicto(r)} |")
    if fallos:
        print(f"\n{fallos} par(es) por debajo de {_coma(a.minimo)} : 1", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
