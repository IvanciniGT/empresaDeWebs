"""Lista las palabras que el corrector no reconoce, con hunspell y el diccionario
es_ES de LibreOffice (A-008), en local.

Uso:
  python3 herramientas/ortografia.py FICHERO… [--palabras LISTA.txt] [--json]
      FICHERO: .md, .txt, .html, .docx o .pdf
      LISTA.txt: palabras buenas de este cliente (nombres, calles…), una por línea.
                 Si tiene nombres de personas, va en clientes/<negocio>/privado/.
  Sale con 1 si hay palabras dudosas, con 0 si no hay ninguna.

Desde Python (solo usa la biblioteca estándar, vale el python3 del sistema):
  sys.path.insert(0, "herramientas"); import ortografia
  ortografia.palabras_dudosas(texto, extra=["Cotillas"])  →  {"herrata": 1, …}

«Dudosa» no es «falta»: nombres propios, marcas y palabras nuevas también salen.
Lo común a todos los clientes (WhatsApp, OpenStreetMap…) va en
herramientas/diccionarios/empresa.txt; las palabras de un cliente, en su lista.
"""
import html
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree

H = Path(__file__).resolve().parent
HUNSPELL = H / "vendor/hunspell/bin/hunspell"
DICCIONARIO = H / "vendor/diccionarios/es_ES"
EMPRESA = H / "diccionarios/empresa.txt"

# Lo que no es texto y el corrector daría por malo: direcciones, correos, código.
_RUIDO = re.compile(r"https?://\S+|www\.\S+|[\w.+-]+@[\w-]+(?:\.[\w-]+)+|`[^`]*`|\{\{[^}]*\}\}|\[[^\]]*\]\([^)]*\)")


def _comprobar_instalacion():
    if not HUNSPELL.exists() or not DICCIONARIO.with_suffix(".dic").exists():
        raise SystemExit("Falta hunspell o el diccionario: herramientas/instalar.sh hunspell")


def palabras_dudosas(texto, extra=()):
    """Palabras que hunspell no reconoce, con cuántas veces salen."""
    _comprobar_instalacion()
    limpio = _RUIDO.sub(" ", texto)
    conocidas = list(extra)
    if EMPRESA.exists():
        conocidas += [l.strip() for l in EMPRESA.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    with tempfile.NamedTemporaryFile("w", suffix=".dic", encoding="utf-8", delete=False) as personal:
        personal.write("\n".join(conocidas) + "\n")
    try:
        salida = subprocess.run(
            [str(HUNSPELL), "-d", str(DICCIONARIO), "-p", personal.name, "-i", "utf-8", "-l"],
            input=limpio, capture_output=True, text=True, check=True,
        ).stdout
    finally:
        Path(personal.name).unlink(missing_ok=True)
    dudosas = [
        p for p in salida.split()
        # Fuera: cifras, letras sueltas (unidades como «m» o «h»), restos de emojis y siglas cortas en mayúsculas.
        if not re.search(r"\d", p) and len(p) > 1 and re.search(r"[^\W\d_]", p) and not re.fullmatch(r"[A-ZÁÉÍÓÚÑ]{2,5}", p)
    ]
    return dict(Counter(dudosas).most_common())


def texto_de(ruta):
    ruta = Path(ruta)
    tipo = ruta.suffix.lower()
    if tipo == ".docx":
        w = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        with zipfile.ZipFile(ruta) as z:
            raiz = ElementTree.fromstring(z.read("word/document.xml"))
        return "\n".join("".join(t.text or "" for t in p.iter(f"{w}t")) for p in raiz.iter(f"{w}p"))
    if tipo == ".pdf":
        return subprocess.run(["pdftotext", "-layout", str(ruta), "-"], capture_output=True, text=True, check=True).stdout
    contenido = ruta.read_text(encoding="utf-8")
    if tipo in (".html", ".htm"):
        contenido = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", contenido)
        contenido = html.unescape(re.sub(r"<[^>]+>", " ", contenido))
    return contenido


def main(argumentos):
    extra, ficheros, como_json = [], [], False
    i = 0
    while i < len(argumentos):
        if argumentos[i] == "--palabras":
            extra += [l.strip() for l in Path(argumentos[i + 1]).read_text(encoding="utf-8").splitlines() if l.strip()]
            i += 2
        elif argumentos[i] == "--json":
            como_json, i = True, i + 1
        else:
            ficheros.append(argumentos[i])
            i += 1
    if not ficheros:
        print(__doc__.split("\n\n")[1])
        return 2
    resultado = {f: palabras_dudosas(texto_de(f), extra) for f in ficheros}
    if como_json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        for fichero, dudosas in resultado.items():
            print(f"{fichero}: {len(dudosas)} palabras dudosas" + (":" if dudosas else ""))
            for palabra, veces in dudosas.items():
                print(f"  {palabra}" + (f"  (×{veces})" if veces > 1 else ""))
    return 1 if any(resultado.values()) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
