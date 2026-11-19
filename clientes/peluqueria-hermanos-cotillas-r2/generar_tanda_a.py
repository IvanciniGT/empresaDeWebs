"""Genera el Word de la tanda A (preguntas para el presupuesto) de la Peluquería
Hermanos Cotillas, ronda 2 (cliente simulado).

Ejecutar desde la raíz del repositorio:
    .venv/bin/python clientes/peluqueria-hermanos-cotillas-r2/generar_tanda_a.py

Preguntas: catálogo de Reme v0.3.1 (procesos/skills-borrador/cuestionario-cliente/preguntas.md).
Solo datos del negocio: este fichero y el Word van a git, que es público (A-013).
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "herramientas"))

import docx_util as w  # noqa: E402

AQUI = Path(__file__).resolve().parent
NEGOCIO = "Peluquería Hermanos Cotillas"
NOMBRE = f"Preguntas para el presupuesto - {NEGOCIO}"
SALIDA = AQUI / "entregables" / f"{NOMBRE}.docx"
CATALOGO = "catálogo v0.3.1"


def solo_si(texto):
    return f"Solo si {texto}. Si no, pasad a la siguiente."


def inicio(doc):
    doc.add_heading("Unas preguntas para preparar vuestro presupuesto", 1)
    doc.add_paragraph(
        f"Con esto os preparamos un presupuesto cerrado para la web de {NEGOCIO}, "
        "por escrito y sin compromiso. Casi todas se contestan marcando una opción."
    )
    w.bloque(doc, "como", [
        "Son 8 preguntas, y alguna más solo si os toca (lo pone en cada una).",
        "Podéis contestar aquí, en el Word, o por WhatsApp citando el número de la "
        "pregunta y de la opción: «A 3.5: 2 y 3».",
        "Lo que no sepáis, dejadlo en blanco.",
    ])
    t = doc.add_paragraph()
    t.add_run("Qué significa cada recuadro").bold = True
    for tipo, explicacion in (("sabemos", "lo que hemos encontrado: decidnos si está bien."),
                              ("escribid", "el sitio para vuestra respuesta.")):
        etiqueta, _, color = w.BLOQUES[tipo]
        p = doc.add_paragraph()
        r = p.add_run(etiqueta)
        r.bold, r.font.color.rgb = True, w.RGBColor.from_string(color)
        p.add_run(f"  {explicacion}")


def lo_que_sabemos(doc):
    doc.add_heading("1. Lo que hemos encontrado", 2)
    doc.add_paragraph("Lo hemos visto en OpenStreetMap, un mapa abierto. Decidnos si está bien.")
    w.validar_dato(doc, "A 1.1", "Nombre del negocio", NEGOCIO)
    w.validar_dato(doc, "A 1.2", "Dirección", "Calle Octavio Cuartero, 57 · Albacete")
    w.pregunta(doc, "A 1.3", "¿Qué teléfono queréis que salga en la web?",
               "No lo hemos encontrado. Si es un móvil personal, decídnoslo.")
    w.bloque(doc, "escribid", alto=1, id="A 1.3")
    w.validar_dato(doc, "A 1.4", "Horario", [
        "Lunes a viernes: de 9:00 a 13:45 y de 16:30 a 20:45",
        "Sábados: de 8:30 a 14:00",
    ])


def vuestro_negocio(doc):
    doc.add_heading("2. Vuestro negocio", 2)
    w.pregunta(doc, "A 3.3", "¿Qué servicios hacéis?",
               "Como os salga. Por ejemplo: corte de caballero, de niño, barba, afeitado a "
               "navaja, degradado, color. Si tenéis una lista de precios colgada, "
               "nos vale una foto por WhatsApp.", imprescindible=True)
    w.bloque(doc, "escribid", alto=3, id="A 3.3")

    w.pregunta(doc, "A 3.5", "¿Cómo dais las citas ahora? Podéis marcar varias.", imprescindible=True)
    w.opciones(doc, ["Sin cita, por orden de llegada", "Por teléfono", "Por WhatsApp",
                     "Con una aplicación o web de reservas", "Otra"], id="A 3.5")
    w.pregunta(doc, "A 3.7", "¿Qué aplicación es? ¿Os basta con un botón en la web que lleve a ella?",
               solo_si("en A 3.5 habéis marcado «Con una aplicación o web de reservas»"))
    w.bloque(doc, "escribid", alto=1, id="A 3.7")


def la_web(doc):
    doc.add_heading("3. La web que queréis", 2)
    w.pregunta(doc, "A 4.1", "¿Para qué queréis la web? Podéis marcar varias.", imprescindible=True)
    w.opciones(doc, [
        "Que nos encuentre gente nueva",
        "Que vean el horario, los servicios y cómo llegar sin tener que llamar",
        "Que puedan pedir o reservar cita desde la web",
        "Vender productos por internet",
        "Que se pueda leer en otro idioma",
        "Buscar personal",
        "Otra cosa (escribidla debajo)",
    ], id="A 4.1")
    w.bloque(doc, "escribid", alto=1, id="A 4.1|otra")

    w.pregunta(doc, "A 4.6", "¿Queréis que el cliente elija día y hora él solo en la web, "
               "o que os pida cita y la confirméis vosotros?",
               solo_si("en A 4.1 habéis marcado «Que puedan pedir o reservar cita»"))
    w.opciones(doc, ["Que elija día y hora él solo", "Que nos la pida y la confirmamos nosotros"],
               id="A 4.6")
    w.pregunta(doc, "A 3.4", "¿Qué productos queréis vender por internet, y cuántos más o menos?",
               solo_si("en A 4.1 habéis marcado «Vender productos por internet»"))
    w.bloque(doc, "escribid", alto=1, id="A 3.4")
    w.pregunta(doc, "A 4.3", "¿En qué idioma? ¿Tenéis quien lo traduzca?",
               solo_si("en A 4.1 habéis marcado «Que se pueda leer en otro idioma»"))
    w.bloque(doc, "escribid", alto=1, id="A 4.3")
    w.pregunta(doc, "A 4.7", "¿Os basta con un aviso en la web («buscamos peluquero, escribidnos») "
               "o queréis recibir currículums desde la web?",
               solo_si("en A 4.1 habéis marcado «Buscar personal»"))
    w.opciones(doc, ["Nos basta con un aviso", "Queremos recibir currículums desde la web"], id="A 4.7")

    w.pregunta(doc, "A 4.4", "Cuando la web esté hecha, ¿cada cuánto cambiaríais algo "
               "(el horario, un precio, una promoción)?", imprescindible=True)
    w.opciones(doc, ["Una vez al mes o menos", "De dos a cuatro veces al mes", "Más a menudo"], id="A 4.4")

    w.pregunta(doc, "A 4.5", "¿Para cuándo os gustaría tenerla?", "Una fecha, o «sin prisa».")
    w.bloque(doc, "escribid", alto=1, id="A 4.5")


def lo_que_teneis(doc):
    doc.add_heading("4. Lo que ya tenéis", 2)
    w.pregunta(doc, "A 5.5", "¿Qué tenéis ya? Marcad lo que tengáis.", imprescindible=True)
    w.opciones(doc, [
        "Una dirección de web (dominio), como www.algo.es: escribidla debajo",
        "Logotipo en archivo",
        "Fotos del local o de vuestro trabajo que podamos usar",
        "Vídeos",
        "Nada de esto",
    ], id="A 5.5")
    w.bloque(doc, "escribid", alto=1, id="A 5.5|dominio")
    w.pregunta(doc, "A 5.2", "¿Las fotos las haríais vosotros con el móvil, con unos consejos "
               "nuestros, o preferís un fotógrafo?",
               solo_si("en A 5.5 no habéis marcado las fotos"))
    w.opciones(doc, ["Las hacemos nosotros con el móvil", "Preferimos un fotógrafo"], id="A 5.2")
    w.pregunta(doc, "A 5.3", "¿Queréis un logotipo nuevo, o seguís con el nombre tal cual, como en el rótulo?",
               solo_si("en A 5.5 no habéis marcado el logotipo"))
    w.opciones(doc, ["Queremos un logotipo nuevo", "Seguimos con el nombre tal cual"], id="A 5.3")

    w.pregunta(doc, "A 5.7", "¿Quién os lleva la web ahora, y la seguís pagando?",
               solo_si("tenéis ya una web"))
    w.bloque(doc, "escribid", alto=1, id="A 5.7")
    w.pregunta(doc, "A 5.8", "¿Hay algo de la web actual que queráis conservar (textos, fotos, la dirección)?",
               solo_si("tenéis ya una web"))
    w.bloque(doc, "escribid", alto=1, id="A 5.8")

    w.pregunta(doc, "A 5.4", "La ficha de Google Maps (la que sale con vuestras opiniones): ¿quién la lleva?")
    w.opciones(doc, ["Nosotros", "Otra persona", "No sabíamos que existía", "No lo sé"], id="A 5.4")

    w.pregunta(doc, "A 2.2", "¿Quién da el visto bueno a la web? ¿Basta con uno de vosotros?",
               solo_si("sois varios en el negocio"))
    w.bloque(doc, "escribid", alto=1, id="A 2.2")


def final(doc):
    doc.add_heading("5. Para terminar (si queréis)", 2)
    w.pregunta(doc, "A 5.6", "Si tenéis a mano una foto de la fachada con el rótulo, de día y sin "
               "gente delante, mandádnosla por WhatsApp. Si no, no pasa nada.")
    w.bloque(doc, "aviso", ["Nunca nos mandéis contraseñas. Si algún día hace falta entrar en una "
                            "cuenta vuestra, os explicaremos cómo darnos acceso sin ella."])
    doc.add_paragraph(
        "Con vuestras respuestas os preparamos el presupuesto: cerrado, por escrito y sin compromiso. "
        "Lo importante lo revisa y aprueba Iván, el responsable."
    )
    doc.add_paragraph("[Línea de privacidad: pendiente de A-010]")


def main():
    doc = w.nuevo_documento(titulo=f"Preguntas para el presupuesto · {NEGOCIO}", autor="[Empresa]")
    w.pie(doc, f"{NEGOCIO} · Preguntas para el presupuesto · {CATALOGO}")
    inicio(doc)
    lo_que_sabemos(doc)
    vuestro_negocio(doc)
    la_web(doc)
    lo_que_teneis(doc)
    final(doc)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    print(w.guardar(doc, SALIDA))


if __name__ == "__main__":
    main()
