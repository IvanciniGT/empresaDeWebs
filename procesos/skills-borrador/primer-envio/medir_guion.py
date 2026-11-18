#!/usr/bin/env python3
"""Comprueba que el guion de WhatsApp de la tanda A sigue al catálogo de Reme.

Uso:
    /usr/bin/python3 procesos/skills-borrador/primer-envio/medir_guion.py
    /usr/bin/python3 medir_guion.py --guion OTRO.md --catalogo OTRO.md

Termina con código 1 si algo falla. Solo usa la biblioteca estándar.
"""
import argparse
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
LIMITE = 300
LIMITE_CON_OPCIONES = 450
TECLA = "\ufe0f\u20e3"  # el «️⃣» de 1️⃣, 2️⃣…
ID = r"A \d\.\d(?:–\d\.\d)?"


def version_catalogo(texto):
    hallado = re.search(r"BORRADOR v(\d+(?:\.\d+)+)", texto)
    return hallado.group(1) if hallado else None


def version_en_guion(texto):
    hallado = re.search(r"\*\*Catálogo:\*\*\s*v(\d+(?:\.\d+)+)", texto)
    return hallado.group(1) if hallado else None


def tanda_a(catalogo):
    # Solo la tanda A, sin la tabla de lo retirado, que lleva ID antiguos.
    inicio = catalogo.index("## Tanda A")
    fin = catalogo.index("### Lo que ha salido", inicio)
    return catalogo[inicio:fin]


def ids_y_opciones_catalogo(seccion):
    ids, opciones = set(), {}
    for linea in seccion.splitlines():
        if not linea.startswith("|"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        posicion = next((i for i, c in enumerate(celdas)
                         if re.fullmatch(rf"\*\*({ID})\*\*", c)), None)
        if posicion is None:
            continue
        ident = re.fullmatch(rf"\*\*({ID})\*\*", celdas[posicion]).group(1)
        ids.add(ident)
        # En la tabla de obligatorias, la columna de opciones va detrás de la pregunta.
        if posicion == 1 and len(celdas) > 3:
            numeros = re.findall(r"(?:^|· )(\d+) ", celdas[3])
            if numeros:
                opciones[ident] = len(numeros)
    return ids, opciones


def bloques_guion(guion):
    """Devuelve {ID: texto de su apartado} a partir de los encabezados ### y ####."""
    bloques, actual, lineas = {}, None, []
    for linea in guion.splitlines():
        if re.match(r"#{2,4} ", linea):
            if actual:
                bloques[actual] = "\n".join(lineas)
            hallado = re.match(rf"#{{3,4}} .*?({ID})", linea)
            actual, lineas = (hallado.group(1) if hallado else None), []
        elif actual:
            lineas.append(linea)
    if actual:
        bloques[actual] = "\n".join(lineas)
    return bloques


def mensajes(guion):
    cuerpo = guion.split("## Las preguntas", 1)[1].split("## Cómo se anotan", 1)[0]
    lista, actual = [], []
    for linea in cuerpo.splitlines():
        if linea.startswith(">"):
            actual.append(linea[1:].removeprefix(" "))
        elif actual:
            lista.append("\n".join(actual).strip())
            actual = []
    if actual:
        lista.append("\n".join(actual).strip())
    return lista


def comprobar(ruta_guion, ruta_catalogo):
    guion = Path(ruta_guion).read_text(encoding="utf-8")
    catalogo = Path(ruta_catalogo).read_text(encoding="utf-8")
    fallos = []

    v_cat, v_guion = version_catalogo(catalogo), version_en_guion(guion)
    if not v_cat or v_cat != v_guion:
        fallos.append(f"Versión: el catálogo es v{v_cat} y el guion dice v{v_guion}")

    ids_cat, opciones_cat = ids_y_opciones_catalogo(tanda_a(catalogo))
    bloques = bloques_guion(guion)
    for ident in sorted(ids_cat - bloques.keys()):
        fallos.append(f"Falta en el guion: {ident}")
    for ident in sorted(bloques.keys() - ids_cat):
        fallos.append(f"Sobra en el guion (no está en el catálogo): {ident}")

    for ident, esperadas in sorted(opciones_cat.items()):
        if ident not in bloques:
            continue
        en_guion = len(re.findall(rf"^> \d+{TECLA}", bloques[ident], re.M))
        if en_guion != esperadas:
            fallos.append(f"{ident}: el catálogo tiene {esperadas} opciones y el guion {en_guion}")

    lista = mensajes(guion)
    for texto in lista:
        limite = LIMITE_CON_OPCIONES if TECLA in texto else LIMITE
        if len(texto) > limite:
            fallos.append(f"Mensaje de {len(texto)} caracteres (límite {limite}): «{texto[:50]}…»")

    for numero, linea in enumerate(guion.splitlines(), 1):
        if re.search(r"(?i)\bsi (?:dice|=|marca|elige|no marca)\s*\d", linea):
            fallos.append(f"Línea {numero}: condición por número de opción: «{linea.strip()[:70]}»")

    print(f"Catálogo v{v_cat} · guion para v{v_guion}")
    print(f"ID: {len(ids_cat)} en el catálogo, {len(bloques)} en el guion · "
          f"{len(opciones_cat)} preguntas con opciones · {len(lista)} mensajes")
    if lista:
        print(f"Mensaje más largo: {max(len(t) for t in lista)} caracteres")
    for fallo in fallos:
        print(f"✘ {fallo}")
    print("✔ Todo en orden" if not fallos else f"✘ {len(fallos)} fallo(s)")
    return not fallos


if __name__ == "__main__":
    argumentos = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    argumentos.add_argument("--guion", default=AQUI / "guion-tanda-a.md")
    argumentos.add_argument("--catalogo",
                            default=AQUI.parent / "cuestionario-cliente" / "preguntas.md")
    opciones = argumentos.parse_args()
    sys.exit(0 if comprobar(opciones.guion, opciones.catalogo) else 1)
