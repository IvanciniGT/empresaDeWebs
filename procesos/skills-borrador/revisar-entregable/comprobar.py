"""Comprobaciones mecánicas de un envío antes de la revisión a mano de Puri.

No da el veredicto: señala lo que hay que mirar. Lo que no salga aquí no
está aprobado; solo significa que la máquina no sabe verlo. Lo que no puede
comprobar lo dice como [no comprobado], nunca lo calla.

Uso (Python del sistema; usa pdftotext, pdfinfo, pdffonts y pdftoppm):
    python3 comprobar.py <carpeta del envío> <expediente.md> [más fuentes .md/.json]

El Word lo revisa herramientas/pruebas/revisar_docx.py (de Paco) con el Python
de .venv: aquí solo se llama, para no mantener dos comprobaciones de lo mismo.
"""
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
REVISAR_DOCX = RAIZ / "herramientas" / "pruebas" / "revisar_docx.py"
PYTHON_VENV = RAIZ / ".venv" / "bin" / "python"
# Las listas de frases de los autores se leen de sus skills: si Chema cambia
# la suya, la comprobación cambia con ella sin copiarla aquí.
LISTAS_DE_AUTORES = [
    RAIZ / "procesos" / "skills-borrador" / "estudio-competencia" / "SKILL.md",
    RAIZ / "procesos" / "skills-borrador" / "textos-web" / "SKILL.md",
]
SECCION_LISTA = "Frases que se revisan antes de entregar"

# Lo que ha salido en las revisiones y no está en las listas de los autores.
ALARMAS_PROPIAS = [
    "todo", "toda", "todos", "todas", "nadie", "ningún", "ninguna", "lo que más", "seguro",
    "seguramente", "muchos", "pocas", "pocos", "fiable", "comprobado", "llamamos", "llamaros",
    "no tenéis", "no existe", "prometemos", "os ayudamos a hacer", "revisa todo",
]
UNIDADES = r"%|€|km|m\b|metros|años|minutos|opiniones|reseñas|valoraciones|peluquerías|barberías|negocios|directorios|páginas|competidores|preguntas"
CIFRA = re.compile(r"(?<![\w/§.,])(\d{1,4}(?:[.,]\d{1,3})?)\s*(" + UNIDADES + r")?", re.I)
HUECO = re.compile(r"\[(?!x\]|\s\])[^\]\n]{2,60}\](?!\()")
# Datos personales que no pueden estar en git (A-009, A-013). Los fijos de
# negocio (9xx) no salen: son públicos.
PERSONALES = {
    "móvil": re.compile(r"(?<!\d)(?:\+34[\s.]?)?[67]\d{2}[\s.]?\d{2,3}[\s.]?\d{2}[\s.]?\d{2,3}(?!\d)"),
    "correo": re.compile(r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b"),
    "DNI/NIE": re.compile(r"(?<![\w])(?:\d{8}|[XYZ]\d{7})[-\s]?[A-Z](?![\w])"),
    "IBAN": re.compile(r"\bES\d{2}(?:\s?\d{4}){5}\b"),
}
CORREOS_PERMITIDOS = re.compile(r"noreply|example\.|users\.noreply\.github")
TEXTO_GIT = {".md", ".txt", ".json", ".csv", ".html", ".py", ".yaml", ".yml"}
FACTOR_ALTURA = 1.3  # altura de la caja de una palabra / cuerpo de letra (±10 % según la fuente)


def texto_pdf(ruta):
    return subprocess.run(["pdftotext", "-layout", str(ruta), "-"], capture_output=True, text=True).stdout


def texto_docx(ruta):
    with zipfile.ZipFile(ruta) as z:
        partes = [z.read("word/document.xml").decode("utf8")]
        partes += [z.read(n).decode("utf8") for n in z.namelist() if re.match(r"word/footer\d*\.xml", n)]
    return "\n".join(re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", x)) for x in partes)


def frases(texto):
    plano = re.sub(r"\s+", " ", texto)
    return [f.strip() for f in re.split(r"(?<=[.!?»])\s+", plano) if f.strip()]


def lista_negra(avisos):
    frases_lista, origen = set(ALARMAS_PROPIAS), []
    for skill in LISTAS_DE_AUTORES:
        if not skill.exists():
            avisos.append(("no comprobado", skill.parent.name, "no encuentro la skill: su lista de frases no se ha usado"))
            continue
        bloque = re.search(rf"## {SECCION_LISTA}\n(.*?)(?=\n## |\Z)", skill.read_text(encoding="utf8"), re.S)
        if not bloque:
            avisos.append(("no comprobado", skill.parent.name, f"la skill no tiene la sección «{SECCION_LISTA}»"))
            continue
        nuevas = {f.lower() for f in re.findall(r"«([^»]+)»", bloque.group(1))}
        frases_lista |= nuevas
        origen.append(f"{skill.parent.name} ({len(nuevas)})")
    patrones = []
    for f in sorted(frases_lista):
        # «garantiz» y «céntric» son raíces: casan con cualquier final.
        fin = r"\w*" if f.endswith(("iz", "ic", "garantiz", "céntric")) else r"\b"
        patrones.append(re.compile(r"(?<!\w)" + re.escape(f) + fin, re.I))
    return patrones, origen


def revisar_docx(ruta, avisos):
    if not (PYTHON_VENV.exists() and REVISAR_DOCX.exists()):
        avisos.append(("no comprobado", ruta.name, f"falta {REVISAR_DOCX.relative_to(RAIZ)} o .venv: el Word no se ha revisado"))
        return
    r = subprocess.run([str(PYTHON_VENV), str(REVISAR_DOCX), str(ruta)], capture_output=True, text=True)
    if r.returncode not in (0, 1):
        avisos.append(("no comprobado", ruta.name, f"revisar_docx.py ha fallado: {r.stderr.strip()[-200:]}"))
        return
    estructura, total = [], re.search(r"^(\d+) problemas", r.stdout, re.M)
    for linea in r.stdout.splitlines():
        if not linea.startswith("✗"):
            continue
        if re.search(r"repetido|fuera de orden|Ignorable", linea):
            estructura.append(linea[1:].strip())
        else:
            avisos.append(("importante", ruta.name, "revisar_docx: " + linea[1:].strip()))
    if estructura:
        # revisar_docx enseña solo los 20 primeros: el resto se deduce del total.
        otros = sum(1 for a in avisos if a[1] == ruta.name and a[2].startswith("revisar_docx"))
        n = int(total.group(1)) - otros if total else len(estructura)
        # Fuera de esquema: Word puede negarse a abrirlo o ofrecer «repararlo».
        avisos.append(("bloquea", ruta.name, f"revisar_docx: {n} errores de estructura, p. ej. «{estructura[0]}». "
                       f"Detalle: .venv/bin/python herramientas/pruebas/revisar_docx.py <docx>"))
    with zipfile.ZipFile(ruta) as z:
        doc = z.read("word/document.xml").decode("utf8")
    pie = re.search(r"(?:Tanda\s+[AB]|\bB[12])\s*v\d+(?:\.\d+)?", texto_docx(ruta))
    avisos.append(("info", ruta.name, f"{doc.count('<w14:checkbox>')} casillas · versión de plantilla en el pie: "
                   f"{pie.group(0) if pie else 'NINGUNA'} → ¿la ha probado Iván en Word? (A-007)"))


def revisar_pdf(ruta, avisos, carpeta_movil):
    info = subprocess.run(["pdfinfo", str(ruta)], capture_output=True, text=True).stdout
    paginas = re.search(r"Pages:\s+(\d+)", info)
    tam = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info)
    formato = "?"
    if tam:
        ancho, alto = float(tam.group(1)), float(tam.group(2))
        formato = "A4" if abs(ancho - 595) < 3 else "A5" if abs(ancho - 420) < 3 else f"{ancho:.0f}×{alto:.0f} pt"
    avisos.append(("info", ruta.name, f"{paginas.group(1) if paginas else '?'} páginas · {formato}"))
    if "Tagged:          yes" not in info:
        avisos.append(("menor", ruta.name, "PDF sin etiquetar (accesibilidad)"))
    fuentes = subprocess.run(["pdffonts", str(ruta)], capture_output=True, text=True).stdout
    familias = sorted({re.sub(r"^[A-Z]{6}\+", "", l.split()[0]).split("-")[0] for l in fuentes.splitlines()[2:] if l.strip()})
    ajenas = [f for f in familias if not re.match(r"Inter|Fraunces", f)]
    if ajenas:
        avisos.append(("importante", ruta.name, f"tipografías fuera de estilo-documentos (A-006, A-008): {', '.join(ajenas)}"))
    # Legibilidad en el móvil: altura más frecuente de las palabras, llevada a 390 px de ancho.
    bbox = subprocess.run(["pdftotext", "-bbox", str(ruta), "-"], capture_output=True, text=True).stdout
    alturas, ancho_pt = [], None
    for w, cuerpo in re.findall(r'<page width="([\d.]+)" height="[\d.]+">(.*?)</page>', bbox, re.S):
        ancho_pt = ancho_pt or float(w)
        alturas += [round(float(b) - float(a), 1) for a, b in re.findall(r'yMin="([\d.]+)" xMax="[\d.]+" yMax="([\d.]+)"', cuerpo)]
    if alturas and ancho_pt:
        letra_px = statistics.mode(alturas) / FACTOR_ALTURA * 390 / ancho_pt
        avisos.append(("info", ruta.name, f"letra del cuerpo en un móvil de 390 px: ≈ {letra_px:.1f} px "
                       "(estimada, ±10 %). Mirar las imágenes de móvil"))
    salida = carpeta_movil / ruta.stem[:40]
    subprocess.run(["pdftoppm", "-scale-to-x", "390", "-scale-to-y", "-1", "-png", str(ruta), str(salida)], capture_output=True)
    return int(paginas.group(1)) if paginas else None


def paginas_docx(ruta, avisos, carpeta_movil):
    # Son las páginas de LibreOffice; en Word pueden cambiar (lo mira Iván, A-007).
    soffice = shutil.which("soffice")
    if not soffice:
        avisos.append(("no comprobado", ruta.name, "sin LibreOffice: ni páginas ni imágenes de móvil del Word"))
        return None
    with tempfile.TemporaryDirectory() as tmp:
        copia = Path(tmp) / "documento.docx"
        shutil.copy(ruta, copia)
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", tmp, str(copia)], capture_output=True)
        pdf = Path(tmp) / "documento.pdf"
        if not pdf.exists():
            avisos.append(("bloquea", ruta.name, "LibreOffice no lo ha podido convertir a PDF"))
            return None
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        subprocess.run(["pdftoppm", "-scale-to-x", "390", "-scale-to-y", "-1", "-png", str(pdf),
                        str(carpeta_movil / ruta.stem[:40])], capture_output=True)
    n = re.search(r"Pages:\s+(\d+)", info)
    return f"{n.group(1)} (LibreOffice)" if n else None


def ortografia(textos, fuentes, avisos):
    # Usa herramientas/ortografia.py de Paco (hunspell + diccionario es_ES + palabras
    # de la empresa). Las palabras del expediente cuentan como buenas: así salen los
    # nombres propios del cliente y no las erratas, vayan o no en mayúscula.
    sys.path.insert(0, str(RAIZ / "herramientas"))
    # Sin caché .pyc: la carpeta herramientas/ es de Paco, no escribo en ella.
    sys.dont_write_bytecode = True
    try:
        import ortografia as corrector
    except ImportError:
        avisos.append(("no comprobado", "ortografía", "falta herramientas/ortografia.py: leer palabra por palabra"))
        return {}
    buenas = set(re.findall(r"[^\W\d_]+", fuentes))
    dudosas = {}
    for nombre, texto in textos.items():
        try:
            dudosas[nombre] = sorted(corrector.palabras_dudosas(texto, extra=sorted(buenas)))
        except SystemExit as e:
            avisos.append(("no comprobado", "ortografía", f"{e} (A-008): leer palabra por palabra"))
            return {}
    return dudosas


def ficheros_que_entran_en_git(carpeta):
    r = subprocess.run(["git", "-C", str(carpeta), "ls-files", "--cached", "--others", "--exclude-standard", "-z", "."],
                       capture_output=True, text=True)
    if r.returncode == 0:
        return [carpeta / n for n in r.stdout.split("\0") if n]
    # Sin git, lo prudente es mirarlo todo menos privado/.
    return [f for f in carpeta.rglob("*") if f.is_file() and "privado" not in f.relative_to(carpeta).parts]


def datos_personales(carpeta_cliente, textos, avisos):
    fuentes = dict(textos)
    for f in ficheros_que_entran_en_git(carpeta_cliente):
        if f.is_file() and f.suffix in TEXTO_GIT:
            fuentes[str(f.relative_to(carpeta_cliente))] = f.read_text(encoding="utf8", errors="ignore")
    for nombre, texto in fuentes.items():
        for tipo, patron in PERSONALES.items():
            for m in sorted(set(patron.findall(texto))):
                if tipo == "correo" and CORREOS_PERMITIDOS.search(m):
                    continue
                avisos.append(("bloquea", nombre, f"posible {tipo} en un fichero que entra en git: {m} (A-009, A-013)"))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    carpeta, expediente = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    fuentes = expediente.read_text(encoding="utf8")
    for extra in sys.argv[3:]:
        fuentes += Path(extra).read_text(encoding="utf8", errors="ignore")
    avisos, textos, paginas = [], {}, {}
    patrones, origen_lista = lista_negra(avisos)
    carpeta_movil = Path(tempfile.mkdtemp(prefix="puri-movil-"))

    for f in sorted(carpeta.iterdir()):
        if f.name.startswith("~$"):
            avisos.append(("menor", f.name, "fichero de bloqueo de Word: alguien tiene el documento abierto. No adjuntar"))
            continue
        if f.name.startswith(".") or f.is_dir():
            continue
        if re.search(r"interno|previo|gu[ií]a de estilos", f.name, re.I):
            avisos.append(("bloquea", f.name, "parece un documento interno dentro del envío"))
        if f.suffix == ".pdf":
            textos[f.name] = texto_pdf(f)
            paginas[f.name] = revisar_pdf(f, avisos, carpeta_movil)
        elif f.suffix == ".docx":
            textos[f.name] = texto_docx(f)
            revisar_docx(f, avisos)
            paginas[f.name] = paginas_docx(f, avisos, carpeta_movil)
        elif f.suffix in (".md", ".txt"):
            textos[f.name] = f.read_text(encoding="utf8")

    datos_personales(expediente.parent, textos, avisos)
    dudosas = ortografia(textos, fuentes, avisos)

    print(f"# Comprobación automática · {carpeta.name}\n")
    print(f"Lista de frases: propias + {', '.join(origen_lista) or 'ninguna de los autores'}.")
    print(f"Imágenes como en un móvil de 390 px: {carpeta_movil}\n")
    print("## Avisos\n")
    for gravedad, donde, que in avisos:
        print(f"- [{gravedad}] {donde} · {que}")

    cifras_por_doc = defaultdict(set)
    metricas = []
    for nombre, texto in textos.items():
        print(f"\n## {nombre}\n")
        huecos = sorted(set(HUECO.findall(texto)))
        if huecos:
            print("**Huecos sin rellenar** (bloquean salvo que Iván los acepte):")
            for h in huecos:
                print(f"- {h}")
        print("\n**Cifras que no aparecen tal cual en las fuentes** (rastrear una a una):")
        vistas, sin_fuente = set(), 0
        for fr in frases(texto):
            for num, unidad in CIFRA.findall(fr):
                if unidad:
                    cifras_por_doc[f"{num} {unidad.lower()}"].add(nombre)
                if (num, unidad) in vistas or num in fuentes:
                    continue
                vistas.add((num, unidad))
                sin_fuente += 1
                print(f"- {num}{(' ' + unidad) if unidad else ''} · «{fr[:140]}»")
        print("\n**Frases de la lista** (¿tienen fuente?, ¿prometen algo?, ¿afirman una ausencia?):")
        alarmas = 0
        for fr in frases(texto):
            if any(p.search(fr) for p in patrones):
                alarmas += 1
                print(f"- «{fr[:160]}»")
        if nombre in dudosas and dudosas[nombre]:
            print("\n**Ortografía** (palabras que hunspell no conoce):", ", ".join(dudosas[nombre]))
        metricas.append((nombre, paginas.get(nombre, "—"), len(texto.split()), sin_fuente, alarmas, len(huecos)))

    print("\n## Cifras con unidad, por documento\n")
    print("Mismo dato en varios documentos: comprobar que vale lo mismo en todos (paso 4).\n")
    for cifra in sorted(cifras_por_doc, key=lambda c: (c.split()[1], c)):
        print(f"- {cifra}: {', '.join(sorted(cifras_por_doc[cifra]))}")

    print("\n## Métricas (informativas, para comparar versiones)\n")
    print("| Documento | Páginas | Palabras | Cifras sin fuente | Frases de la lista | Huecos |")
    print("|---|---|---|---|---|---|")
    for fila in metricas:
        print("| " + " | ".join(str(x) for x in fila) + " |")

    print("\n## Lo que esta comprobación NO mira\n")
    print("La verdad de cada frase, el tono, las citas contra su prueba, la maquetación, el Word "
          "en Microsoft Word, el contraste (contraste.py con los colores del documento), los nombres "
          "de personas y si una cifra igual vale lo mismo. Eso es la revisión a mano.")


if __name__ == "__main__":
    main()
