"""Prototipo de las piezas del Word según estilo-documentos v0.3 (Lola).

No es una herramienta: es la referencia para que Paco lo lleve a
herramientas/docx_util.py. Se apoya en lo que ya hay allí (nuevo_documento,
guardar, casilla, _colocar...) y solo añade el aspecto.

Genera una muestra con datos ficticios (el repositorio es público):
    .venv/bin/python procesos/skills-borrador/estilo-documentos/prototipo/bloques_docx.py /tmp/muestra.docx
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / "herramientas"))

from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.shared import Cm, Pt, RGBColor  # noqa: E402

import docx_util as du  # noqa: E402

VERSION_ESTILO = "estilo v0.3"
FUENTE = "Arial"
ANCHO_CM = 16.6   # A4 con márgenes de 2,2 cm

# Paleta de estilo-documentos (contrastes en SKILL.md).
TINTA = RGBColor.from_string("1E2A3A")
ACENTO = RGBColor.from_string("9C4A14")
GRIS = RGBColor.from_string("56606D")
BIEN = RGBColor.from_string("24693F")
ATENCION = RGBColor.from_string("8A5A00")
MAL = RGBColor.from_string("B3261E")

# tipo: (etiqueta, fondo, color de la barra y de la etiqueta)
# La etiqueta es la que informa; el color solo ayuda (no depender del color).
BLOQUES = {
    "como":      ("CÓMO CONTESTAR", "F4F6F9", "1E2A3A"),
    "sabemos":   ("LO QUE HEMOS ENCONTRADO", "EEF2F6", "56606D"),
    "escribid":  ("ESCRIBID AQUÍ", "FFF4E0", "9C4A14"),
    "propuesta": ("NUESTRA PROPUESTA", "EAF5EC", "24693F"),
    "aviso":     ("IMPORTANTE", "FBE4E2", "B3261E"),
}
ESTADOS = {"si": ("Sí", BIEN), "medias": ("A medias", ATENCION), "no": ("No", MAL)}


def documento(titulo, autor):
    """Documento A4 con el estilo común: Arial 11, títulos en acento, español."""
    doc = du.nuevo_documento(FUENTE, titulo=titulo, autor=autor)
    normal = doc.styles["Normal"]
    normal.font.size, normal.font.color.rgb = Pt(11), TINTA
    for nivel, tam, color in ((1, 20, ACENTO), (2, 14, ACENTO), (3, 12, TINTA)):
        estilo = doc.styles[f"Heading {nivel}"]
        estilo.font.size, estilo.font.color.rgb = Pt(tam), color
    return doc


def _barra(tabla, color):
    """Borde fino alrededor y barra gruesa a la izquierda: se ve en blanco y negro."""
    bordes = OxmlElement("w:tblBorders")
    for lado, grosor in (("top", 4), ("left", 36), ("bottom", 4), ("right", 4)):
        b = OxmlElement(f"w:{lado}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), str(grosor))   # octavos de punto: 36 = 4,5 pt
        b.set(qn("w:color"), color)
        bordes.append(b)
    du._colocar(tabla._tbl.tblPr, bordes)


def bloque(doc, tipo, lineas=(), alto=0):
    """Recuadro con etiqueta en mayúsculas. `alto`: líneas vacías para escribir."""
    etiqueta, fondo, color = BLOQUES[tipo]
    tabla = doc.add_table(rows=1, cols=1)
    du._anchos(tabla, [ANCHO_CM])
    du._margen_celdas(tabla, 0.25)
    _barra(tabla, color)
    du._fila_entera(tabla.rows[0])
    celda = tabla.cell(0, 0)
    du._sombrear(celda, fondo)
    r = celda.paragraphs[0].add_run(etiqueta)
    r.bold, r.font.size, r.font.color.rgb = True, Pt(9), RGBColor.from_string(color)
    for linea in lineas:
        celda.add_paragraph(linea)
    for _ in range(alto):
        celda.add_paragraph("")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return celda


def pregunta(doc, id_, texto, ayuda=None, imprescindible=False):
    """Número a la vista (el ID del catálogo de Reme) para poder contestar por
    WhatsApp citándolo. «Imprescindible» con palabra, no con ★."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(f"{id_}   ")
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


def _etiquetar_ultima_casilla(parrafo, tag):
    """w:tag en la casilla para que un script lea la respuesta por ID. Va antes
    de w14:checkbox: en sdtPr los elementos de w: van delante de las extensiones."""
    sdtPr = parrafo._p.findall(f"{qn('w:sdt')}/{qn('w:sdtPr')}")[-1]
    etiqueta = OxmlElement("w:tag")
    etiqueta.set(qn("w:val"), tag)
    sdtPr.insert(0, etiqueta)


def opciones(doc, id_, textos):
    """Una casilla por línea, a todo el ancho (nada de columnas: en el móvil se
    cortan). El número de la opción, a la vista: es el mismo que se usa por
    WhatsApp («A 3.5: 2 y 3»)."""
    for n, texto in enumerate(textos, start=1):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = n < len(textos)
        du.casilla(p)
        _etiquetar_ultima_casilla(p, f"{id_}.{n}")
        r = p.add_run(f"{n}  ")
        r.font.color.rgb = GRIS
        p.add_run(texto)


def validar_dato(doc, id_, que, valor, imprescindible=False):
    """Lo que hemos encontrado + «Está bien / Hay algo mal» + hueco. Nunca una
    casilla sola: sin marcar no se sabe si es «no» o «no lo he mirado»."""
    pregunta(doc, id_, que, imprescindible=imprescindible)
    bloque(doc, "sabemos", valor if isinstance(valor, list) else [valor])
    opciones(doc, id_, ["Está bien", "Hay algo mal: escribid el bueno debajo"])
    bloque(doc, "escribid", alto=1)


def estado(parrafo, tipo):
    """Estado con palabra y color, en negrita. Sin símbolos: Arial no trae ✓."""
    palabra, color = ESTADOS[tipo]
    r = parrafo.add_run(palabra)
    r.bold, r.font.color.rgb = True, color
    return r


def como_contestar(doc, minutos, preguntas):
    """Va en la primera página, antes de cualquier pregunta."""
    bloque(doc, "como", [
        f"Son {preguntas} preguntas y se tarda unos {minutos} minutos.",
        "Podéis contestar aquí, en el Word, o por WhatsApp citando el número de la "
        "pregunta y de la opción: «A 3.5: 2 y 3».",
        "Lo que no sepáis, dejadlo en blanco.",
    ])
    t = doc.add_paragraph()
    r = t.add_run("Qué significa cada recuadro")
    r.bold, r.font.size = True, Pt(10)
    for tipo, explicacion in (("sabemos", "lo que hemos encontrado: decidnos si está bien."),
                              ("escribid", "el sitio para vuestra respuesta."),
                              ("propuesta", "un texto nuestro: aprobadlo o cambiadlo.")):
        etiqueta, _, color = BLOQUES[tipo]
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(etiqueta)
        r.bold, r.font.size, r.font.color.rgb = True, Pt(9), RGBColor.from_string(color)
        p.add_run(f"  {explicacion}").font.size = Pt(10)


def pie(doc, nombre_documento):
    """El pie lo lee el cliente: solo el documento y la página. La versión del
    estilo va en las propiedades, que es donde Iván la busca al probar (A-007)."""
    du.pie_de_pagina(doc, nombre_documento)
    for r in doc.sections[0].footer.paragraphs[0].runs:
        r.font.size, r.font.name = Pt(9), FUENTE
    doc.core_properties.version = VERSION_ESTILO


def muestra(ruta):
    doc = documento("Tanda A · Negocio de Ejemplo (MUESTRA)", "Muestra de estilo-documentos")
    doc.add_heading("Unas preguntas para prepararos el presupuesto", 1)
    p = doc.add_paragraph()
    r = p.add_run("Negocio de Ejemplo · MUESTRA CON DATOS FICTICIOS")
    r.font.color.rgb = GRIS
    como_contestar(doc, minutos=10, preguntas=8)

    doc.add_heading("1. Lo que ya sabemos de vosotros", 2)
    validar_dato(doc, "A 1.4", "Horario", ["Lunes a viernes: 9:00–14:00 y 16:30–20:30",
                                           "Sábado: 9:00–14:00 · Domingo: cerrado"], imprescindible=True)
    validar_dato(doc, "A 1.3", "Teléfono", "600 00 00 00")

    doc.add_heading("2. Vuestro negocio", 2)
    pregunta(doc, "A 3.5", "¿Cómo dais las citas ahora?", "Marcad todas las que uséis.", imprescindible=True)
    opciones(doc, "A 3.5", ["Sin cita, por orden de llegada", "Por teléfono", "Por WhatsApp",
                            "Con una aplicación (escribid cuál debajo)"])
    bloque(doc, "escribid", alto=1)

    pregunta(doc, "A 5.6", "Si tenéis a mano una foto de la fachada con el rótulo, mandádnosla por WhatsApp.",
             "De día y sin gente delante. Si no la tenéis, no pasa nada.")

    # Desde aquí, componentes que no van en la tanda A: se enseñan para la B.
    doc.add_heading("Componentes de la tanda B (solo en esta muestra)", 2)
    bloque(doc, "propuesta", ["[Frase principal: la escribe Chema]"])
    opciones(doc, "B 8.1", ["Me gusta así", "Cambiadlo: escribid cómo debajo"])
    bloque(doc, "escribid", alto=1)

    p = doc.add_paragraph("Ejemplo de estado: ficha de Google ")
    estado(p, "si")
    p.add_run(" · horario en internet ")
    estado(p, "no")
    p.add_run(" · fotos ")
    estado(p, "medias")

    bloque(doc, "aviso", ["Nunca nos mandéis contraseñas. Si hace falta entrar en alguna cuenta, "
                          "os explicamos cómo darnos acceso con nuestro propio usuario."])
    pie(doc, "Tanda A · Negocio de Ejemplo")
    return du.guardar(doc, ruta)


if __name__ == "__main__":
    print(muestra(sys.argv[1] if len(sys.argv) > 1 else "/tmp/lola-muestra-tanda-a.docx"))
