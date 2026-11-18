"""Busca frases vigiladas en un borrador antes de pasárselo a Puri.

No aprueba nada: señala dónde mirar. Cada aviso «B» se quita o se reescribe; cada
«R» se justifica con su fuente en el expediente o se convierte en hueco.

Uso:
  python3 vigilar_frases.py borrador.html [otro.md …]
  python3 vigilar_frases.py --frase "Le cortamos el pelo a tu padre."

Sale con 1 si hay algún aviso B, con 0 si solo hay R o nada.
Solo usa la biblioteca estándar de Python.
"""
import argparse
import html
import re
import sys
from pathlib import Path

LISTA = Path(__file__).resolve().parent / "frases-vigiladas.txt"


def cargar(lista=LISTA):
    reglas = []
    for numero, linea in enumerate(lista.read_text(encoding="utf-8").splitlines(), 1):
        if not linea.strip() or linea.startswith("#"):
            continue
        nivel, resto = linea.split(" ", 1)
        patron, motivo = resto.split(" ## ", 1)
        if nivel not in ("B", "R"):
            raise ValueError(f"{lista.name}:{numero}: nivel «{nivel}» desconocido")
        reglas.append((nivel, re.compile(patron, re.IGNORECASE), motivo.strip()))
    return reglas


def _texto_visible(linea):
    return html.unescape(re.sub(r"<[^>]+>", " ", linea))


def revisar(texto, reglas):
    avisos = []
    for numero, linea in enumerate(texto.splitlines(), 1):
        visible = _texto_visible(linea)
        for nivel, patron, motivo in reglas:
            for m in patron.finditer(visible):
                avisos.append((numero, nivel, m.group(0), motivo))
    return avisos


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ficheros", nargs="*", type=Path)
    p.add_argument("--frase", action="append", default=[])
    a = p.parse_args(argv)
    reglas = cargar()
    fuentes = [(f.name, f.read_text(encoding="utf-8")) for f in a.ficheros]
    fuentes += [(f"frase {i}", f) for i, f in enumerate(a.frase, 1)]
    bloquea = 0
    for nombre, texto in fuentes:
        for numero, nivel, encontrado, motivo in revisar(texto, reglas):
            bloquea += nivel == "B"
            print(f"{nombre}:{numero}: [{nivel}] «{encontrado}» · {motivo}")
    print(f"— {bloquea} que bloquean. Esto no aprueba nada: lo revisa Puri.", file=sys.stderr)
    return 1 if bloquea else 0


if __name__ == "__main__":
    sys.exit(main())
