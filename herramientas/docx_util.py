"""Piezas reutilizables para los Word que enviamos a los clientes.

Pensado para un cliente que no sabe de tecnología: casillas que se marcan con
un clic, recuadros de color donde escribir y avisos visuales. Si mañana es una
skill, esto es lo que se reutiliza; el contenido va en cada expediente.

Para guardar, mejor `guardar(doc, ruta)` que `doc.save(ruta)`: no machaca un
documento que alguien tenga abierto.

Respuestas con ID (para leerlas después con leer_cuestionario.py): las piezas
donde contesta el cliente aceptan `id`, el del catálogo de preguntas (por
ejemplo «A 4.1»). Se guarda como etiqueta del control de contenido (`w:tag`):
  - casilla y opciones → «ID|n», n = número de opción, empezando en 1;
  - hueco → «ID»: lo que se escribe va dentro de un control de texto en línea;
  - tabla_respuestas(ids=[…]) → «ID|título de la columna», en cada celda de respuesta;
  - propuesta_texto → «ID|Me gusta así», «ID|Cambiadlo así» y «ID|cambio».
Sin `id`, todo sale como antes.
"""
import itertools
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# Paleta de estilo-documentos v0.3 (Lola). Mismos nombres que en estilo.css;
# los contrastes están comprobados en esa skill: si cambia uno, se repite.
VERSION_ESTILO = "estilo v0.3"
FUENTE = "Arial"   # la tiene cualquier aparato que abra un Word; el Word no incrusta fuentes
ANCHO_CM = 16.6    # A4 con márgenes de 2,2 cm
TINTA = RGBColor.from_string("1E2A3A")
ACENTO = RGBColor.from_string("9C4A14")
GRIS = RGBColor.from_string("56606D")
BIEN = RGBColor.from_string("24693F")
ATENCION = RGBColor.from_string("8A5A00")
MAL = RGBColor.from_string("B3261E")
FONDO_RESPUESTA = "FFF4E0"   # donde escribe el cliente
FONDO_SABEMOS = "EEF2F6"     # lo que ya hemos encontrado
FONDO_PROPUESTA = "EAF5EC"   # textos que proponemos nosotros
FONDO_AVISO = "FBE4E2"

# tipo: (etiqueta, fondo, color de la barra y de la etiqueta). Informa la
# etiqueta; el color solo ayuda (se tiene que entender en blanco y negro).
BLOQUES = {
    "como":      ("CÓMO CONTESTAR", "F4F6F9", "1E2A3A"),
    "sabemos":   ("LO QUE HEMOS ENCONTRADO", FONDO_SABEMOS, "56606D"),
    "escribid":  ("ESCRIBID AQUÍ", FONDO_RESPUESTA, "9C4A14"),
    "propuesta": ("NUESTRA PROPUESTA", FONDO_PROPUESTA, "24693F"),
    "aviso":     ("IMPORTANTE", FONDO_AVISO, "B3261E"),
}
ESTADOS = {"si": ("Sí", BIEN), "medias": ("A medias", ATENCION), "no": ("No", MAL)}


def nuevo_documento(fuente=FUENTE, titulo="", autor="", idioma="es-ES"):
    doc = Document()
    _propiedades(doc, titulo, autor, idioma)
    seccion = doc.sections[0]
    seccion.page_height, seccion.page_width = Cm(29.7), Cm(21)
    for margen in ("left_margin", "right_margin"):
        setattr(seccion, margen, Cm(2.2))
    seccion.top_margin, seccion.bottom_margin = Cm(2), Cm(2)
    estilos = doc.styles
    normal = estilos["Normal"]
    normal.font.name, normal.font.size, normal.font.color.rgb = fuente, Pt(11), TINTA
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), fuente)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.15
    for nivel, tam, color in ((1, 20, ACENTO), (2, 14, ACENTO), (3, 12, TINTA)):
        e = estilos[f"Heading {nivel}"]
        e.font.name, e.font.size, e.font.bold = fuente, Pt(tam), True
        e.font.color.rgb = color
        # Los títulos usan la fuente del tema (Calibri Light); se quita para que manden los nuestros.
        rfonts = e.element.rPr.rFonts
        for atributo in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if rfonts.get(qn(atributo)) is not None:
                del rfonts.attrib[qn(atributo)]
        e.paragraph_format.space_before = Pt(16 if nivel == 1 else 10)
        e.paragraph_format.space_after = Pt(6)
        e.paragraph_format.keep_with_next = True
    return doc


def _propiedades(doc, titulo, autor, idioma):
    """Quita lo que deja la plantilla de python-docx: autor «python-docx», fecha de
    2013, idioma inglés (Word marcaría todo el texto como faltas) y una miniatura
    en blanco que es lo que enseña el Finder o el correo como vista previa."""
    ahora = datetime.now(timezone.utc).replace(microsecond=0, tzinfo=None)
    p = doc.core_properties
    p.title, p.author, p.last_modified_by = titulo, autor, autor
    p.comments, p.language, p.revision = "", idioma, 1
    p.created = p.modified = ahora
    lang = doc.styles.element.find(f"{qn('w:docDefaults')}/{qn('w:rPrDefault')}/{qn('w:rPr')}/{qn('w:lang')}")
    if lang is not None:
        lang.set(qn("w:val"), idioma)
        lang.set(qn("w:eastAsia"), idioma)
    tema = doc.settings.element.find(qn("w:themeFontLang"))
    if tema is not None:
        tema.set(qn("w:val"), idioma)
    paquete = doc.part.package
    for rid, rel in list(paquete.rels.items()):
        if rel.reltype == RT.THUMBNAIL:
            paquete.rels.pop(rid)


def documento_abierto(ruta):
    """Fichero de bloqueo si alguien tiene abierto el documento, o None.

    Word crea «~$» + el nombre (con los dos primeros caracteres sustituidos si el
    nombre es largo) y LibreOffice «.~lock.<nombre>#»."""
    ruta = Path(ruta)
    for nombre in (f"~${ruta.name}", f"~${ruta.name[2:]}", f".~lock.{ruta.name}#"):
        if (ruta.parent / nombre).exists():
            return ruta.parent / nombre
    return None


def guardar(doc, ruta):
    """Guarda, salvo que el documento esté abierto en Word o LibreOffice."""
    bloqueo = documento_abierto(ruta)
    if bloqueo:
        raise SystemExit(f"No se guarda {ruta}: está abierto ({bloqueo.name}). Ciérralo y vuelve a generarlo.")
    doc.save(str(ruta))
    return ruta


# Word valida el orden de los hijos de tblPr y tcPr (el esquema los define en
# secuencia) y puede dar el documento por dañado si no cuadra; LibreOffice lo
# perdona. Por eso no se hace append(): se coloca cada pieza en su sitio.
_ORDEN = {
    "tblPr": ("tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
              "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders",
              "shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription"),
    "tcPr": ("cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap",
             "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"),
}


def _colocar(padre, elemento):
    """Pone `elemento` en `padre` respetando el orden del esquema y sin duplicarlo."""
    orden = _ORDEN[padre.tag.split("}")[1]]
    nombre = elemento.tag.split("}")[1]
    for viejo in padre.findall(elemento.tag):
        padre.remove(viejo)
    despues = orden[orden.index(nombre) + 1:]
    for hijo in padre:
        if hijo.tag.split("}")[1] in despues:
            hijo.addprevious(elemento)
            return elemento
    padre.append(elemento)
    return elemento


def _sombrear(celda, color):
    tcPr = celda._tc.get_or_add_tcPr()
    sombra = OxmlElement("w:shd")
    sombra.set(qn("w:val"), "clear")
    sombra.set(qn("w:color"), "auto")
    sombra.set(qn("w:fill"), color)
    _colocar(tcPr, sombra)


def _bordes(tabla, color="D0D7DE", grosor=4):
    tblPr = tabla._tbl.tblPr
    bordes = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b = OxmlElement(f"w:{lado}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), str(grosor))
        b.set(qn("w:color"), color)
        bordes.append(b)
    _colocar(tblPr, bordes)


def _margen_celdas(tabla, cm=0.2):
    tblPr = tabla._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for lado in ("top", "left", "bottom", "right"):
        m = OxmlElement(f"w:{lado}")
        m.set(qn("w:w"), str(int(cm * 567)))
        m.set(qn("w:type"), "dxa")
        mar.append(m)
    _colocar(tblPr, mar)


def _fila_entera(fila, cabecera=False):
    """La fila no se parte entre páginas; si es cabecera, se repite en cada página."""
    trPr = fila._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    if cabecera:
        trPr.append(OxmlElement("w:tblHeader"))


def _anchos(tabla, anchos_cm):
    # Word mira el ancho de las celdas; LibreOffice, la rejilla (tblGrid) y el
    # layout fijo, que ya pone python-docx al quitar el autofit.
    tabla.autofit = False
    for col, ancho in zip(tabla._tbl.tblGrid.findall(qn("w:gridCol")), anchos_cm):
        col.set(qn("w:w"), str(int(ancho * 567)))
    for fila in tabla.rows:
        for celda, ancho in zip(fila.cells, anchos_cm):
            celda.width = Cm(ancho)


_ids_control = itertools.count(1001)


def _identificar(sdtPr, etiqueta):
    """Etiqueta (w:tag) y número único (w:id) del control. Van antes del tipo de control."""
    if etiqueta is None:
        return
    tag = OxmlElement("w:tag")
    tag.set(qn("w:val"), str(etiqueta))
    sdtPr.append(tag)
    numero = OxmlElement("w:id")
    numero.set(qn("w:val"), str(next(_ids_control)))
    sdtPr.append(numero)


def _control_de_texto(parrafo, etiqueta, ayuda="Escribid aquí"):
    """Convierte lo que haya en el párrafo en un control de texto EN LÍNEA con
    etiqueta. En línea y no de bloque: LibreOffice saca el texto de los de bloque
    al guardar (comprobado), y estos los conserva con su etiqueta.
    Si el párrafo está vacío, muestra `ayuda` en gris, que desaparece al escribir."""
    if etiqueta is None:
        return
    p = parrafo._p
    runs = p.findall(qn("w:r"))
    sdt = OxmlElement("w:sdt")
    sdtPr = OxmlElement("w:sdtPr")
    _identificar(sdtPr, etiqueta)
    if not runs:
        sdtPr.append(OxmlElement("w:showingPlcHdr"))
    texto = OxmlElement("w:text")
    texto.set(qn("w:multiLine"), "1")
    sdtPr.append(texto)
    sdt.append(sdtPr)
    contenido = OxmlElement("w:sdtContent")
    sdt.append(contenido)
    if runs:
        for r in runs:
            contenido.append(r)
    else:
        r = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        rPr.append(OxmlElement("w:i"))
        color = OxmlElement("w:color")
        color.set(qn("w:val"), "8A94A3")
        rPr.append(color)
        r.append(rPr)
        t = OxmlElement("w:t")
        t.text = ayuda
        r.append(t)
        contenido.append(r)
    p.append(sdt)


def casilla(parrafo, marcada=False, id=None):
    """Casilla de Word de verdad (control de contenido): se marca con un clic."""
    sdt = OxmlElement("w:sdt")
    sdtPr = OxmlElement("w:sdtPr")
    _identificar(sdtPr, id)
    cb = OxmlElement("w14:checkbox")
    chk = OxmlElement("w14:checked")
    chk.set(qn("w14:val"), "1" if marcada else "0")
    cb.append(chk)
    for etiqueta, simbolo in (("w14:checkedState", "2612"), ("w14:uncheckedState", "2610")):
        estado = OxmlElement(etiqueta)
        estado.set(qn("w14:val"), simbolo)
        estado.set(qn("w14:font"), "MS Gothic")
        cb.append(estado)
    sdtPr.append(cb)
    sdt.append(sdtPr)
    contenido = OxmlElement("w:sdtContent")
    r = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    fuentes = OxmlElement("w:rFonts")
    fuentes.set(qn("w:ascii"), "MS Gothic")
    fuentes.set(qn("w:hAnsi"), "MS Gothic")
    rPr.append(fuentes)
    r.append(rPr)
    t = OxmlElement("w:t")
    t.text = "☒" if marcada else "☐"
    r.append(t)
    contenido.append(r)
    sdt.append(contenido)
    parrafo._p.append(sdt)
    parrafo.add_run(" ")
    return parrafo


def opciones(doc, textos, por_fila=1, marcadas=(), id=None, numeros=None):
    """Lista de casillas. Con `id`, el número de cada opción sale a la vista (es
    el que se usa por WhatsApp: «A 3.5: 2 y 3»). Con por_fila>1 se reparten en
    columnas, pero estilo-documentos v0.3 las quita: en el móvil se cortan."""
    etiqueta = (lambda n: None) if id is None else (lambda n: f"{id}|{n}")
    numeros = id is not None if numeros is None else numeros
    if por_fila == 1:
        for n, texto in enumerate(textos, start=1):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.3)
            p.paragraph_format.space_after = Pt(3 if numeros else 2)
            p.paragraph_format.keep_with_next = numeros and n < len(textos)
            casilla(p, texto in marcadas, etiqueta(n))
            if numeros:
                p.add_run(f"{n}  ").font.color.rgb = GRIS
            p.add_run(texto)
        return
    filas = -(-len(textos) // por_fila)
    tabla = doc.add_table(rows=filas, cols=por_fila)
    for i, texto in enumerate(textos):
        celda = tabla.cell(i % filas, i // filas)
        p = celda.paragraphs[0]
        p.paragraph_format.space_after = Pt(1)
        casilla(p, texto in marcadas, etiqueta(i + 1))
        p.add_run(texto)
    _anchos(tabla, [16.6 / por_fila] * por_fila)
    # Sin este párrafo, Word y LibreOffice funden la tabla con la siguiente.
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def hueco(doc, etiqueta=None, lineas=2, ayuda=None, valor=None, id=None):
    """Recuadro de color para que escriba el cliente."""
    tabla = doc.add_table(rows=1, cols=1)
    _anchos(tabla, [16.6])
    _bordes(tabla, "E8C9A0")
    _margen_celdas(tabla, 0.25)
    _fila_entera(tabla.rows[0])
    celda = tabla.cell(0, 0)
    _sombrear(celda, FONDO_RESPUESTA)
    p = celda.paragraphs[0]
    if etiqueta:
        r = p.add_run(etiqueta)
        r.bold, r.font.size = True, Pt(9.5)
    if ayuda:
        r = p.add_run(("  " if etiqueta else "") + ayuda)
        r.italic, r.font.size, r.font.color.rgb = True, Pt(8.5), GRIS
    q = celda.add_paragraph(valor or "")
    if id is None:
        for _ in range(max(0, lineas - 1)):
            celda.add_paragraph("")
    else:
        # Un solo párrafo con el control, y el alto con el espaciado: sin líneas
        # vacías fuera del control donde el cliente pueda escribir sin querer.
        q.paragraph_format.space_after = Pt(15 * max(0, lineas - 1))
        _control_de_texto(q, id)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return q


def tabla_respuestas(doc, cabecera, filas, anchos, columnas_respuesta=(), fondo_fila=None, ids=None):
    """Tabla con cabecera oscura; las columnas de respuesta salen en color.
    `ids`: un ID por fila (o None en las filas sin respuesta)."""
    tabla = doc.add_table(rows=1 + len(filas), cols=len(cabecera))
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    _bordes(tabla)
    _margen_celdas(tabla, 0.15)
    for n, fila in enumerate(tabla.rows):
        _fila_entera(fila, cabecera=(n == 0))
    for i, titulo in enumerate(cabecera):
        c = tabla.cell(0, i)
        _sombrear(c, "1E2A3A")
        r = c.paragraphs[0].add_run(titulo)
        r.bold, r.font.size, r.font.color.rgb = True, Pt(9), RGBColor(0xFF, 0xFF, 0xFF)
    for f, fila in enumerate(filas, start=1):
        for i, valor in enumerate(fila):
            c = tabla.cell(f, i)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            if i in columnas_respuesta:
                _sombrear(c, FONDO_RESPUESTA)
            elif fondo_fila:
                _sombrear(c, fondo_fila)
            id_fila = ids[f - 1] if ids else None
            etiqueta = f"{id_fila}|{cabecera[i]}" if id_fila is not None else None
            if valor == "[ ]":
                casilla(p, id=etiqueta)
            elif valor:
                r = p.add_run(str(valor))
                r.font.size = Pt(9.5)
            if i in columnas_respuesta and valor != "[ ]":
                _control_de_texto(p, etiqueta, ayuda="Escribid")
    _anchos(tabla, anchos)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return tabla


def recuadro(doc, titulo, texto, fondo=FONDO_SABEMOS, borde="C5D0DB"):
    tabla = doc.add_table(rows=1, cols=1)
    _anchos(tabla, [16.6])
    _bordes(tabla, borde, 6)
    _margen_celdas(tabla, 0.3)
    _fila_entera(tabla.rows[0])
    c = tabla.cell(0, 0)
    _sombrear(c, fondo)
    p = c.paragraphs[0]
    r = p.add_run(titulo)
    r.bold = True
    for linea in texto if isinstance(texto, list) else [texto]:
        q = c.add_paragraph(linea)
        q.paragraph_format.space_after = Pt(2)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return c


def propuesta_texto(doc, titulo, texto, id=None):
    """Texto que hemos redactado nosotros para que el cliente lo apruebe o cambie."""
    c = recuadro(doc, "✍️  " + titulo + "  ·  propuesta nuestra", texto, FONDO_PROPUESTA, "A9D3B0")
    p = c.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    casilla(p, id=None if id is None else f"{id}|Me gusta así")
    p.add_run("Me gusta así    ")
    casilla(p, id=None if id is None else f"{id}|Cambiadlo así")
    p.add_run("Cambiadlo así:")
    _control_de_texto(c.add_paragraph(""), None if id is None else f"{id}|cambio", ayuda="Escribid aquí cómo lo queréis")
    return c


# ───────────── Piezas de estilo-documentos v0.3 (prototipo de Lola: bloques_docx.py)


def _barra(tabla, color):
    """Borde fino alrededor y barra gruesa a la izquierda: se ve en blanco y negro."""
    bordes = OxmlElement("w:tblBorders")
    for lado, grosor in (("top", 4), ("left", 36), ("bottom", 4), ("right", 4)):
        b = OxmlElement(f"w:{lado}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), str(grosor))   # octavos de punto: 36 = 4,5 pt
        b.set(qn("w:color"), color)
        bordes.append(b)
    _colocar(tabla._tbl.tblPr, bordes)


def bloque(doc, tipo, lineas=(), alto=0, id=None):
    """Recuadro con etiqueta en mayúsculas (tipos en BLOQUES).
    `alto`: líneas para escribir. Con `id` (para «escribid»), lo que se escriba
    va en un control con esa etiqueta y lo lee leer_cuestionario.py."""
    etiqueta, fondo, color = BLOQUES[tipo]
    tabla = doc.add_table(rows=1, cols=1)
    _anchos(tabla, [ANCHO_CM])
    _margen_celdas(tabla, 0.25)
    _barra(tabla, color)
    _fila_entera(tabla.rows[0])
    celda = tabla.cell(0, 0)
    _sombrear(celda, fondo)
    r = celda.paragraphs[0].add_run(etiqueta)
    r.bold, r.font.size, r.font.color.rgb = True, Pt(9), RGBColor.from_string(color)
    for linea in lineas:
        celda.add_paragraph(linea)
    if id is not None:
        q = celda.add_paragraph("")
        q.paragraph_format.space_after = Pt(15 * max(0, alto - 1))
        _control_de_texto(q, id)
    else:
        for _ in range(alto):
            celda.add_paragraph("")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return celda


def pregunta(doc, id, texto, ayuda=None, imprescindible=False):
    """El ID del catálogo de Reme a la vista, para poder contestar por WhatsApp
    citándolo. «Imprescindible» con palabra, no con ★ (Arial no lo trae)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(f"{id}   ")
    r.bold, r.font.color.rgb = True, ACENTO
    p.add_run(texto).bold = True
    if imprescindible:
        r = p.add_run("  · imprescindible")
        r.font.size, r.font.color.rgb = Pt(10), GRIS
    if ayuda:
        q = doc.add_paragraph()
        q.paragraph_format.keep_with_next = True
        r = q.add_run(ayuda)
        r.font.size, r.font.color.rgb = Pt(10), GRIS
    return p


def validar_dato(doc, id, que, valor, imprescindible=False):
    """Lo que hemos encontrado + «1 Está bien / 2 Hay algo mal» + hueco. Nunca una
    casilla sola: sin marcar no se sabe si es «no» o «no lo he mirado»."""
    pregunta(doc, id, que, imprescindible=imprescindible)
    bloque(doc, "sabemos", valor if isinstance(valor, list) else [valor])
    opciones(doc, ["Está bien", "Hay algo mal: escribid el bueno debajo"], id=id)
    bloque(doc, "escribid", alto=1, id=f"{id}|bueno")


def estado(parrafo, tipo):
    """«Sí», «A medias» o «No», en negrita y en su color. Sin símbolos: Arial no trae ✓."""
    palabra, color = ESTADOS[tipo]
    r = parrafo.add_run(palabra)
    r.bold, r.font.color.rgb = True, color
    return r


def como_contestar(doc, minutos, preguntas, tipos=("sabemos", "escribid", "propuesta")):
    """Primera página, antes de cualquier pregunta. `tipos`: solo los recuadros que
    salen en ESE documento (la leyenda no explica lo que no hay)."""
    bloque(doc, "como", [
        f"Son {preguntas} preguntas y se tarda unos {minutos} minutos.",
        "Podéis contestar aquí, en el Word, o por WhatsApp citando el número de la "
        "pregunta y de la opción: «A 3.5: 2 y 3».",
        "Lo que no sepáis, dejadlo en blanco.",
    ])
    explicaciones = {"sabemos": "lo que hemos encontrado: decidnos si está bien.",
                     "escribid": "el sitio para vuestra respuesta.",
                     "propuesta": "un texto nuestro: aprobadlo o cambiadlo.",
                     "aviso": "algo que tenéis que saber."}
    t = doc.add_paragraph()
    r = t.add_run("Qué significa cada recuadro")
    r.bold, r.font.size = True, Pt(10)
    for tipo in tipos:
        etiqueta, _, color = BLOQUES[tipo]
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(etiqueta)
        r.bold, r.font.size, r.font.color.rgb = True, Pt(9), RGBColor.from_string(color)
        p.add_run(f"  {explicaciones[tipo]}").font.size = Pt(10)


def pie(doc, nombre_documento):
    """Pie para el cliente: el documento y la página. La versión del estilo va en
    las propiedades (cp:version), que es donde la busca Iván al probar (A-007)."""
    pie_de_pagina(doc, nombre_documento)
    for r in doc.sections[0].footer.paragraphs[0].runs:
        r.font.size, r.font.name = Pt(9), FUENTE
    doc.core_properties.version = VERSION_ESTILO


def imagen(doc, ruta, ancho_cm, pie=None, descripcion=None):
    """Imagen centrada. `descripcion` es el texto alternativo (lo que lee un
    lector de pantalla); si no se da, se usa el pie."""
    doc.add_picture(str(ruta), width=Cm(ancho_cm))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    alternativo = descripcion or pie
    if alternativo:
        for docpr in doc.paragraphs[-1]._p.iter(qn("wp:docPr")):
            docpr.set("descr", alternativo)
    if pie:
        p = doc.add_paragraph(pie)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.italic, r.font.size, r.font.color.rgb = True, Pt(8.5), GRIS


def salto_pagina(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def pie_de_pagina(doc, texto):
    pie = doc.sections[0].footer.paragraphs[0]
    pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = pie.add_run(texto + "  ·  página ")
    r.font.size, r.font.color.rgb = Pt(8), GRIS
    # Campo PAGE: Word pone el número al abrir el documento.
    for tipo, texto_campo in (("begin", None), (None, "PAGE"), ("end", None)):
        run = pie.add_run()
        run.font.size, run.font.color.rgb = Pt(8), GRIS
        if tipo:
            fld = OxmlElement("w:fldChar")
            fld.set(qn("w:fldCharType"), tipo)
            run._r.append(fld)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = texto_campo
            run._r.append(instr)
