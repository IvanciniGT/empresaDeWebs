"""Compara dos veredictos de Puri: la base (versión de Federico) y la ronda 2.

Cuenta los errores por gravedad y por categoría con las mismas reglas en los dos,
y busca las regresiones (errores de la base que vuelven). No decide el bono: da
los números de la regla mínima del método y dice qué falta mirar a mano.

Formato de cada error en el veredicto (skill revisar-entregable v0.3):
    - **R07** [bloquea · B] Dónde · Qué pasa · Qué debería pasar
En la ronda 2, un error que repite uno de la base lleva «(= R05)».
Un error que Iván acepta para las dos versiones lleva «(excluido de la comparación: motivo)»
en los dos veredictos.

Uso: python3 comparar.py <veredicto base.md> <veredicto ronda 2.md>
"""
import re
import sys
from collections import Counter
from pathlib import Path

ERROR = re.compile(r"^- \*\*([RE]\d+)\*\* \[(bloquea|importante|menor)(?: · ([A-I]))?\]", re.M)
REGRESION = re.compile(r"\(= (R\d+)\)")
EXCLUIDO = "excluido de la comparación"
GRAVEDADES = ("bloquea", "importante", "menor")
CATEGORIAS = "ABCDEFGHI"


def leer(ruta):
    texto = Path(ruta).read_text(encoding="utf8")
    errores, avisos = {}, []
    for linea in texto.splitlines():
        m = ERROR.match(linea)
        if not m:
            continue
        ident, gravedad, categoria = m.groups()
        if ident in errores:
            avisos.append(f"{ident} aparece dos veces en {Path(ruta).name}: cuenta una")
            continue
        if not categoria:
            avisos.append(f"{ident} no tiene categoría en {Path(ruta).name}")
        errores[ident] = {
            "gravedad": gravedad,
            "categoria": categoria or "?",
            "excluido": EXCLUIDO in linea,
            "repite": REGRESION.findall(linea),
        }
    return errores, avisos


def contar(errores):
    vivos = [e for e in errores.values() if not e["excluido"]]
    return Counter(e["gravedad"] for e in vivos), Counter(e["categoria"] for e in vivos), len(errores) - len(vivos)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    base, avisos_b = leer(sys.argv[1])
    nueva, avisos_n = leer(sys.argv[2])
    if not base or not nueva:
        sys.exit("No encuentro errores con el formato de la v0.3 en alguno de los dos veredictos.")
    g_b, c_b, x_b = contar(base)
    g_n, c_n, x_n = contar(nueva)

    print("# Comparación de veredictos\n")
    print(f"- Base: `{sys.argv[1]}` ({len(base)} errores, {x_b} excluidos)")
    print(f"- Ronda 2: `{sys.argv[2]}` ({len(nueva)} errores, {x_n} excluidos)\n")
    for aviso in avisos_b + avisos_n:
        print(f"⚠️ {aviso}")

    print("\n## P1 · Errores por gravedad (primera entrega a Puri)\n")
    print("| Gravedad | Base | Ronda 2 | ¿Menos? |\n|---|---|---|---|")
    menos_en_todas = True
    for g in GRAVEDADES:
        menos = g_n[g] < g_b[g] or g_b[g] == g_n[g] == 0
        menos_en_todas &= menos
        print(f"| {g} | {g_b[g]} | {g_n[g]} | {'sí' if menos else 'NO'} |")

    print("\n## P2 · Por categoría (A = afirmaciones falsas o sin fuente)\n")
    print("| | " + " | ".join(CATEGORIAS) + " |\n|---|" + "---|" * len(CATEGORIAS))
    print("| Base | " + " | ".join(str(c_b[c]) for c in CATEGORIAS) + " |")
    print("| Ronda 2 | " + " | ".join(str(c_n[c]) for c in CATEGORIAS) + " |")
    menos_a = c_n["A"] < c_b["A"] or c_b["A"] == c_n["A"] == 0

    print("\n## P3 · Regresiones (errores de la base que vuelven)\n")
    regresiones = [(i, r) for i, e in nueva.items() for r in e["repite"]]
    graves = []
    for ident, repetido in regresiones:
        origen = base.get(repetido)
        if not origen:
            print(f"- {ident} dice repetir {repetido}, que no está en la base ⚠️")
            continue
        print(f"- {ident} repite {repetido} ({origen['gravedad']})")
        if origen["gravedad"] == "bloquea":
            graves.append(ident)
    if not regresiones:
        print("Ninguna.")

    print("\n## Regla mínima de «mejor» (lo contable)\n")
    filas = [
        ("Menos errores en cada gravedad (P1)", menos_en_todas),
        ("Menos afirmaciones falsas o sin fuente (P2, categoría A)", menos_a),
        ("Ningún error de la base que bloqueaba vuelve (P3)", not graves),
    ]
    for texto, ok in filas:
        print(f"- [{'x' if ok else ' '}] {texto}")
    print("- [ ] Llega a APROBADO, y en cuántas vueltas (P4): a mano, del historial de veredictos")
    print("- [ ] Cubre los mensajes clave K1–K8 (P5): a mano, con la tabla del método")
    print("\nEl bono lo decide Iván. Esto solo son los números.")


if __name__ == "__main__":
    main()
