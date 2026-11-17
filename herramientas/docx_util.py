"""Piezas reutilizables para los Word que enviamos a los clientes.

Pensado para un cliente que no sabe de tecnología: casillas que se marcan con
un clic, recuadros de color donde escribir y avisos visuales. Si mañana es una
skill, esto es lo que se reutiliza; el contenido va en cada expediente.

Para guardar, mejor `guardar(doc, ruta)` que `doc.save(ruta)`: no machaca un
documento que alguien tenga abierto.
"""
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

TINTA = RGBColor(0x1E, 0x2A, 0x3A)
ACENTO = RGBColor(0xB5, 0x5A, 0x1E)
GRIS = RGBColor(0x5F, 0x6B, 0x7A)
FONDO_RESPUESTA = "FFF4E0"   # donde escribe el cliente
FONDO_SABEMOS = "EEF2F6"     # lo que ya hemos encontrado
FONDO_PROPUESTA = "EAF5EC"   # textos que proponemos nosotros
FONDO_AVISO = "FDECEC"


def nuevo_documento(fuente="Calibri", titulo="", autor="", idioma="es-ES"):
    doc = Document()
    _propiedades(doc, titulo, autor, idioma)
    seccion = doc.sections[0]
    seccion.page_height, seccion.page_width = Cm(29.7), Cm(21)
    for margen in ("left_margin", "right_margin"):
        setattr(seccion, margen, Cm(2.2))
    seccion.top_margin, seccion.bottom_margin = Cm(2), Cm(2)
    estilos = doc.styles
    normal = estilos["Normal"]
    normal.font.name, normal.font.size, normal.font.color.rgb = fuente, Pt(10.5), TINTA
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), fuente)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.15
    for nivel, tam in ((1, 18), (2, 13), (3, 11)):
        e = estilos[f"Heading {nivel}"]
        e.font.name, e.font.size, e.font.bold = fuente, Pt(tam), True
        e.font.color.rgb = ACENTO if nivel == 1 else TINTA
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


def casilla(parrafo, marcada=False):
    """Casilla de Word de verdad (control de contenido): se marca con un clic."""
    sdt = OxmlElement("w:sdt")
    sdtPr = OxmlElement("w:sdtPr")
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


def opciones(doc, textos, por_fila=1, marcadas=()):
    """Lista de casillas; con por_fila>1 se reparten en columnas."""
    if por_fila == 1:
        for texto in textos:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.3)
            p.paragraph_format.space_after = Pt(2)
            casilla(p, texto in marcadas)
            p.add_run(texto)
        return
    filas = -(-len(textos) // por_fila)
    tabla = doc.add_table(rows=filas, cols=por_fila)
    for i, texto in enumerate(textos):
        celda = tabla.cell(i % filas, i // filas)
        p = celda.paragraphs[0]
        p.paragraph_format.space_after = Pt(1)
        casilla(p, texto in marcadas)
        p.add_run(texto)
    _anchos(tabla, [16.6 / por_fila] * por_fila)
    # Sin este párrafo, Word y LibreOffice funden la tabla con la siguiente.
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def hueco(doc, etiqueta=None, lineas=2, ayuda=None, valor=None):
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
    for _ in range(max(0, lineas - 1)):
        celda.add_paragraph("")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return q


def tabla_respuestas(doc, cabecera, filas, anchos, columnas_respuesta=(), fondo_fila=None):
    """Tabla con cabecera oscura; las columnas de respuesta salen en color."""
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
            if valor == "[ ]":
                casilla(p)
            elif valor:
                r = p.add_run(str(valor))
                r.font.size = Pt(9.5)
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


def propuesta_texto(doc, titulo, texto):
    """Texto que hemos redactado nosotros para que el cliente lo apruebe o cambie."""
    c = recuadro(doc, "✍️  " + titulo + "  ·  propuesta nuestra", texto, FONDO_PROPUESTA, "A9D3B0")
    p = c.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    casilla(p)
    p.add_run("Me gusta así    ")
    casilla(p)
    p.add_run("Cambiadlo así:")
    c.add_paragraph("")
    return c


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
