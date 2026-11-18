"""Lee el cuestionario que devuelve el cliente y saca las respuestas por ID.

Las respuestas se leen de los controles de contenido que pone docx_util.py
cuando se le da `id` (etiqueta «ID» o «ID|parte»): casillas marcadas, texto de
los huecos y celdas de respuesta.

Uso:
  python3 herramientas/leer_cuestionario.py RESPUESTA.docx [-o SALIDA.md]
         [--catalogo preguntas.md] [--original ENVIADO.docx] [--permitir-en-git]

  --catalogo   añade el texto de cada pregunta, sacado del catálogo de Reme
               (preguntas.md: ID con la tanda, «A 4.1», «B 6.3»).
  --original   el Word tal como se envió: así se ve también lo que el cliente
               haya escrito FUERA de los recuadros (pasa más de lo que parece).
  -o           sin -o, se escribe en pantalla. Las respuestas son datos
               personales: si SALIDA.md iría a git (el repositorio es público),
               no se escribe. Lo normal: clientes/<negocio>/privado/.

Solo usa la biblioteca estándar: vale el python3 del sistema.
Sale con 1 si el documento no tiene controles con ID (se han perdido al guardarlo
con otro programa, o no se generó con ID): entonces hay que leerlo a mano.
"""
import re
import subprocess
import sys
import zipfile
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from xml.etree import ElementTree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
W14 = "{http://schemas.microsoft.com/office/word/2010/wordml}"
MARCADAS = {"☒", "☑", "✓", "✔", "✗", "✘", "x", "X"}


def _raiz(ruta):
    with zipfile.ZipFile(ruta) as z:
        return ElementTree.fromstring(z.read("word/document.xml"))


def _texto(elemento):
    """Texto de un elemento, un párrafo por línea, sin el de los controles anidados."""
    lineas = []
    for p in elemento.iter(f"{W}p"):
        trozos = []
        for nodo in p.iter():
            if nodo.tag == f"{W}t" and nodo.text:
                trozos.append(nodo.text)
            elif nodo.tag in (f"{W}tab",):
                trozos.append("\t")
            elif nodo.tag in (f"{W}br", f"{W}cr"):
                trozos.append("\n")
        lineas.append("".join(trozos))
    return "\n".join(lineas).strip()


def _texto_en_linea(contenido):
    """Texto de un control: en línea (runs sueltos) o de bloque (párrafos)."""
    if contenido.find(f"{W}p") is not None:
        return _texto(contenido)
    trozos = []
    for nodo in contenido.iter():
        if nodo.tag == f"{W}t" and nodo.text:
            trozos.append(nodo.text)
        elif nodo.tag in (f"{W}br", f"{W}cr"):
            trozos.append("\n")
        elif nodo.tag == f"{W}tab":
            trozos.append("\t")
    return "".join(trozos).strip()


def _padres(raiz):
    return {hijo: padre for padre in raiz.iter() for hijo in padre}


def _etiqueta_de_casilla(sdt, padres):
    """El texto que acompaña a la casilla: lo que va detrás en su mismo párrafo."""
    parrafo = padres.get(sdt)
    if parrafo is None or parrafo.tag != f"{W}p":
        return ""
    hermanos = list(parrafo)
    trozos = []
    for nodo in hermanos[hermanos.index(sdt) + 1:]:
        if nodo.tag == f"{W}sdt":
            break  # empieza la casilla siguiente (dos en el mismo párrafo)
        trozos += [t.text for t in nodo.iter(f"{W}t") if t.text]
    # Sin el número de opción que se ve delante («2  Por teléfono»): ya va en el ID.
    return re.sub(r"^\d+\s+", "", "".join(trozos).strip())


def leer_controles(ruta):
    """{id: [{"parte", "tipo", "valor", "etiqueta"}]} en el orden del documento."""
    raiz = _raiz(ruta)
    padres = _padres(raiz)
    respuestas = {}
    for sdt in raiz.iter(f"{W}sdt"):
        pr = sdt.find(f"{W}sdtPr")
        tag = pr.find(f"{W}tag") if pr is not None else None
        if tag is None or not tag.get(f"{W}val"):
            continue
        valor_tag = tag.get(f"{W}val")
        ident, _, parte = valor_tag.partition("|")
        contenido = sdt.find(f"{W}sdtContent")
        casilla = pr.find(f"{W14}checkbox")
        if casilla is not None:
            estado = casilla.find(f"{W14}checked")
            simbolo = _texto(contenido) if contenido is not None else ""
            # Word cambia los dos; algún programa solo cambia el símbolo.
            if estado is not None and estado.get(f"{W14}val") is not None:
                marcada = estado.get(f"{W14}val") in ("1", "true", "on")
            else:
                marcada = any(c in MARCADAS for c in simbolo)
            respuestas.setdefault(ident, []).append({"parte": parte, "tipo": "casilla", "valor": marcada, "etiqueta": _etiqueta_de_casilla(sdt, padres)})
        else:
            # Con la marca de «texto de ayuda», lo que hay es nuestro «Escribid aquí»: no ha contestado.
            ayuda = pr.find(f"{W}showingPlcHdr") is not None
            texto = "" if ayuda or contenido is None else _texto_en_linea(contenido)
            respuestas.setdefault(ident, []).append({"parte": parte, "tipo": "texto", "valor": texto, "etiqueta": ""})
    return respuestas


def fuera_de_controles(enviado, recibido):
    """Párrafos que el cliente ha añadido o cambiado fuera de los controles."""
    def parrafos(ruta):
        raiz = _raiz(ruta)
        padres = _padres(raiz)
        resultado = []
        for p in raiz.iter(f"{W}p"):
            nodo, dentro = p, False
            while nodo in padres:
                nodo = padres[nodo]
                if nodo.tag == f"{W}sdtContent":
                    dentro = True
                    break
            if not dentro:
                # Las casillas van en el mismo párrafo que su texto: se quitan sus símbolos.
                texto = "".join(t.text or "" for t in p.iter(f"{W}t") if not _en_control(t, padres)).strip()
                resultado.append(texto)
        return resultado

    antes, despues = parrafos(enviado), parrafos(recibido)
    cambios = []
    for operacion, _, _, j1, j2 in SequenceMatcher(a=antes, b=despues, autojunk=False).get_opcodes():
        if operacion in ("insert", "replace"):
            cambios += [t for t in despues[j1:j2] if t]
    return cambios


def _en_control(t, padres):
    """¿Está este texto dentro de un control con etiqueta (casilla o respuesta)?"""
    nodo = t
    while nodo in padres:
        nodo = padres[nodo]
        if nodo.tag == f"{W}sdt":
            return nodo.find(f"{W}sdtPr/{W}tag") is not None
    return False


def leer_catalogo(ruta):
    """{«A 4.1»: «¿Para qué queréis la web?…», …} a partir de las tablas del catálogo.

    Entiende el formato de la v0.3 (el ID lleva la tanda: «**A 4.1**», «B 6.1»,
    y rangos como «A 1.1–1.4») y el de la v0.2 (número suelto bajo «## B1 …»)."""
    preguntas, bateria = {}, ""
    id_con_tanda = re.compile(r"^\**\s*([AB]\d?)\s+(\d+)\.(\d+)(?:\s*[–-]\s*(?:\d+\.)?(\d+))?\s*\**$")
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        cabecera = re.match(r"^##\s+(B\d+)\b", linea)
        if cabecera:
            bateria = cabecera.group(1)
            continue
        if re.match(r"^##\s", linea):
            bateria = ""
        if not linea.startswith("|"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        for n, celda in enumerate(celdas[:-1]):
            m = id_con_tanda.match(celda)
            if m:
                tanda, bloque, desde, hasta = m.group(1), m.group(2), int(m.group(3)), m.group(4)
                texto = re.sub(r"\*\*", "", celdas[n + 1])
                for numero in range(desde, int(hasta or desde) + 1):
                    preguntas.setdefault(f"{tanda} {bloque}.{numero}", texto)
                break
        else:
            fila = re.match(r"^\|\s*(\d+\.\d+[a-z]?)\s*\|\s*([^|]+?)\s*\|", linea)
            if fila and bateria:
                preguntas[f"{bateria} {fila.group(1)}"] = fila.group(2)
    return preguntas


def _orden(ident):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", ident)]


def a_markdown(fichero, respuestas, catalogo=None, fuera=None):
    celda = lambda s: str(s).replace("|", "\\|").replace("\n", " ⏎ ")
    lineas = [
        f"# Respuestas · {Path(fichero).name}",
        "",
        f"> Leído con leer_cuestionario.py el {date.today().isoformat()}. Las respuestas son del cliente, literales.",
        "> Datos personales: este fichero va en `privado/`.",
        "",
        "| ID | Pregunta | Respuesta |",
        "|---|---|---|",
    ]
    for ident in sorted(respuestas, key=_orden):
        partes = respuestas[ident]
        trozos = []
        casillas = [p for p in partes if p["tipo"] == "casilla" and p["parte"].isdigit()]
        sueltas = [p for p in partes if p not in casillas]
        if casillas:
            marcadas = [p["etiqueta"] or f"opción {p['parte']}" for p in casillas if p["valor"]]
            trozos.append(", ".join(marcadas) if marcadas else "(ninguna marcada)")
        for p in sueltas:
            nombre = f"{p['parte']}: " if p["parte"] else ""
            if p["tipo"] == "casilla":
                trozos.append(f"{nombre}{'☒' if p['valor'] else '☐'}")
            else:
                trozos.append(f"{nombre}{p['valor'] or '(vacío)'}")
        pregunta = (catalogo or {}).get(ident, "")
        lineas.append(f"| {ident} | {celda(pregunta)} | {celda(' · '.join(trozos))} |")
    if catalogo:
        sin_respuesta = [i for i in sorted(catalogo, key=_orden) if i not in respuestas and i.split()[0] in {r.split()[0] for r in respuestas}]
        if sin_respuesta:
            lineas += ["", f"Preguntas del catálogo que no estaban en este documento: {', '.join(sin_respuesta)}."]
    if fuera is not None:
        lineas += ["", "## Escrito fuera de los recuadros", ""]
        lineas += [f"- {t}" for t in fuera] if fuera else ["_Nada._"]
    return "\n".join(lineas) + "\n"


def iria_a_git(ruta):
    ruta = Path(ruta).resolve()
    carpeta = ruta.parent
    while not carpeta.exists():
        carpeta = carpeta.parent
    dentro = subprocess.run(["git", "-C", str(carpeta), "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
    if dentro.returncode != 0:
        return False
    ignorado = subprocess.run(["git", "-C", str(carpeta), "check-ignore", "-q", str(ruta)])
    return ignorado.returncode != 0


def main(argumentos):
    opciones = {"-o": None, "--catalogo": None, "--original": None}
    permitir, libres, i = False, [], 0
    while i < len(argumentos):
        a = argumentos[i]
        if a in opciones:
            opciones[a], i = argumentos[i + 1], i + 2
        elif a == "--permitir-en-git":
            permitir, i = True, i + 1
        else:
            libres.append(a)
            i += 1
    if len(libres) != 1:
        print(__doc__.split("\n\n")[2])
        return 2
    fichero = libres[0]
    respuestas = leer_controles(fichero)
    if not respuestas:
        print(f"✗ {fichero} no tiene controles con ID: o se ha guardado con un programa que los quita, o no se generó con ID. Hay que leerlo a mano.", file=sys.stderr)
        return 1
    catalogo = leer_catalogo(opciones["--catalogo"]) if opciones["--catalogo"] else None
    fuera = fuera_de_controles(opciones["--original"], fichero) if opciones["--original"] else None
    texto = a_markdown(fichero, respuestas, catalogo, fuera)
    if opciones["-o"]:
        if not permitir and iria_a_git(opciones["-o"]):
            print(f"✗ {opciones['-o']} entraría en git y el repositorio es público. Escríbelo en clientes/<negocio>/privado/.", file=sys.stderr)
            return 3
        Path(opciones["-o"]).parent.mkdir(parents=True, exist_ok=True)
        Path(opciones["-o"]).write_text(texto, encoding="utf-8")
        print(f"✓ {opciones['-o']}: {len(respuestas)} preguntas")
    else:
        print(texto, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
