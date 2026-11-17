"""Genera el cuestionario Word de la Peluquería Hermanos Cotillas (cliente simulado).

Ejecutar desde la raíz del repositorio:
    .venv/bin/python clientes/peluqueria-hermanos-cotillas/generar_cuestionario.py
"""
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "herramientas"))

from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Pt  # noqa: E402

import docx_util as w  # noqa: E402

AQUI = Path(__file__).resolve().parent
EMPRESA = "[Nombre de nuestra empresa]"  # pendiente de decidir (AGENTS.md §15)
NEGOCIO = "Peluquería Hermanos Cotillas"
SALIDA = AQUI / "entregables" / "Cuestionario - Peluquería Hermanos Cotillas.docx"
IMPRESCINDIBLE = "★ "


def portada(doc):
    for _ in range(5):
        doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run("Vamos a hacer vuestra web")
    r.bold, r.font.size, r.font.color.rgb = True, Pt(30), w.TINTA
    p = doc.add_paragraph()
    r = p.add_run(NEGOCIO)
    r.font.size, r.font.color.rgb = Pt(20), w.ACENTO
    p = doc.add_paragraph()
    r = p.add_run("Cuestionario para conoceros · Paso 1 de 2")
    r.font.size, r.font.color.rgb = Pt(13), w.GRIS
    doc.add_paragraph()
    w.imagen(doc, AQUI / "recopilado/capturas/06-mapa-osm.png", 16.5,
             "C/ Octavio Cuartero, 57 · Albacete  ·  Mapa: © colaboradores de OpenStreetMap")
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run(f"Preparado por {EMPRESA} · {date.today():%d/%m/%Y}")
    r.font.size, r.font.color.rgb = Pt(9.5), w.GRIS
    w.salto_pagina(doc)


def como_rellenar(doc):
    doc.add_heading("Antes de empezar: cómo rellenar esto", 1)
    doc.add_paragraph(
        "Para que vuestra web hable de vosotros y no de una peluquería cualquiera, "
        "necesitamos conoceros un poco. Ya hemos hecho los deberes: hemos buscado todo "
        "lo que hay publicado sobre vosotros en internet y lo hemos puesto aquí. "
        "Vosotros solo tenéis que corregir, completar y darnos el visto bueno."
    )
    leyenda = w.tabla_respuestas(doc, ["Color", "Qué significa"], [
        ["", "Lo que ya hemos encontrado. Decidnos si es correcto."],
        ["", "Huecos para que escribáis vosotros."],
        ["", "Textos que hemos redactado para vuestra web. Aprobadlos o cambiadlos."],
        ["★", "Imprescindible para empezar. Lo demás puede esperar."],
    ], [2, 14.6])
    for fila, color in zip(leyenda.rows[1:4], (w.FONDO_SABEMOS, w.FONDO_RESPUESTA, w.FONDO_PROPUESTA)):
        w._sombrear(fila.cells[0], color)
    w.recuadro(doc, "Tres consejos", [
        "• Si no sabéis algo, dejadlo en blanco. No pasa nada.",
        "• Las casillas ☐ se marcan con un clic.",
        "• ¿Os resulta más cómodo hablarlo? Os llamamos y lo rellenamos juntos por teléfono.",
    ])


def lo_que_sabemos(doc):
    doc.add_heading("1. Lo que ya sabemos de vosotros", 1)
    doc.add_paragraph("Esto es lo que hemos encontrado en Google y en otras páginas. Marcad si es correcto.")
    filas = [
        ["Nombre", NEGOCIO, "[ ]", ""],
        ["Dirección", "C/ Octavio Cuartero, 57 · 02004 Albacete (barrio de la Feria)", "[ ]", ""],
        ["Teléfono", "967 23 57 91", "[ ]", ""],
        ["Horario", "Lunes a viernes 9:00–14:00 y 16:30–20:30\nSábados 8:30–14:00 · Domingos cerrado", "[ ]", ""],
        ["Quiénes sois", "Dos hermanos peluqueros que seguís el negocio de vuestros padres", "[ ]", ""],
        ["Opiniones en Google", "4,8 sobre 5, con unas 132 opiniones", "[ ]", ""],
        ["Web propia", "No tenéis", "[ ]", ""],
        ["Redes sociales", "No hemos encontrado ninguna", "[ ]", ""],
    ]
    w.tabla_respuestas(doc, ["Dato", "Lo que hemos encontrado", "¿Correcto?", "Si no, ¿cuál es el bueno?"],
                       filas, [2.8, 7.2, 1.9, 4.7], columnas_respuesta=(3,), fondo_fila=w.FONDO_SABEMOS)
    w.recuadro(doc, "⚠️  Ojo con un detalle", [
        "Hay más de diez páginas de directorios que hablan de vuestra peluquería con textos "
        "escritos por una máquina. Algunas dicen que hacéis maquillaje, alisados o peinados "
        "de novia, y que tenéis una «zona de relax». Vuestra web servirá también para que "
        "quien os busque lea lo que de verdad hacéis, contado por vosotros.",
    ], w.FONDO_AVISO, "F2B8B5")


def contacto(doc):
    doc.add_heading("2. Datos de contacto", 1)
    doc.add_heading(IMPRESCINDIBLE + "¿Con quién hablamos?", 3)
    w.tabla_respuestas(doc, ["", "Respuesta"], [
        ["Nombre de quien nos atiende", ""],
        ["Móvil", ""],
        ["¿Tiene WhatsApp?", "[ ]"],
        ["Correo electrónico", ""],
        ["Mejor momento para llamaros", ""],
    ], [6, 10.6], columnas_respuesta=(1,))
    doc.add_heading("¿Qué contacto ponemos en la web para vuestros clientes?", 3)
    w.opciones(doc, ["Teléfono fijo del local (967 23 57 91)", "Un móvil con WhatsApp",
                     "Correo electrónico", "Formulario de contacto en la web"], por_fila=2)
    w.hueco(doc, "Número de WhatsApp para clientes (si queréis usarlo)", 1)


def legales(doc):
    doc.add_heading("3. " + IMPRESCINDIBLE + "Datos legales", 1)
    doc.add_paragraph(
        "La ley obliga a que toda web de un negocio diga quién es su titular (aviso legal). "
        "Solo los usamos para eso."
    )
    w.tabla_respuestas(doc, ["", "Respuesta"], [
        ["¿Sois autónomos o una sociedad (S.L., C.B.…)?", ""],
        ["Nombre completo o razón social del titular", ""],
        ["NIF / CIF", ""],
        ["Domicilio fiscal (si no es el del local)", ""],
    ], [6, 10.6], columnas_respuesta=(1,))


def quienes_sois(doc):
    doc.add_heading("4. Quiénes sois", 1)
    doc.add_paragraph(
        "Es lo que más os diferencia de las casi 300 peluquerías y barberías que hay a "
        "menos de kilómetro y medio de la vuestra. Merece la pena contarlo bien."
    )
    w.tabla_respuestas(doc, ["", "Respuesta"], [
        [IMPRESCINDIBLE + "Vuestros nombres", ""],
        ["¿En qué año abrieron vuestros padres?", ""],
        ["¿Cómo se llamaban o cómo los conocía el barrio?", ""],
        ["¿Desde cuándo lleváis vosotros el negocio?", ""],
        ["¿Siempre ha estado en la calle Octavio Cuartero?", ""],
        ["¿Trabaja alguien más con vosotros?", ""],
    ], [7.5, 9.1], columnas_respuesta=(1,))
    w.hueco(doc, "Contadnos una anécdota o algo que os haga sentir orgullosos del negocio", 4,
            "(Por ejemplo: el cliente más antiguo, cómo empezó todo, algo que solo pasa en vuestra peluquería)")
    doc.add_heading("¿Qué os define? Marcad las que os representen", 3)
    w.opciones(doc, [
        "Negocio familiar de toda la vida", "Cortes clásicos de caballero", "Cortes modernos (degradados, diseños)",
        "Especialistas en niños", "Trato cercano, de confianza", "Puntualidad: si tienes cita, no esperas",
        "Precios ajustados", "Rapidez", "Asesoramos al cliente", "Cuidamos la barba",
    ], por_fila=2)
    w.hueco(doc, "¿Algo más que os diferencie?", 2)


def servicios(doc):
    doc.add_heading("5. " + IMPRESCINDIBLE + "Servicios y precios", 1)
    doc.add_paragraph(
        "Marcad lo que hacéis y poned el precio si queréis que salga en la web. "
        "Los negocios que publican precios reciben más llamadas, porque el cliente ya sabe "
        "a qué atenerse. Pero es decisión vuestra."
    )
    filas = [[s, "[ ]", "", ""] for s in [
        "Corte de caballero", "Corte de niño", "Corte + lavado", "Arreglo de barba",
        "Afeitado a navaja", "Degradado / fade", "Corte de señora", "Color / tinte",
        "Cejas", "Tratamientos capilares", "Venta de productos",
    ]] + [["", "[ ]", "", ""]] * 3
    w.tabla_respuestas(doc, ["Servicio", "¿Lo hacéis?", "Precio (€)", "Duración aprox."],
                       filas, [7, 2.4, 3.2, 4], columnas_respuesta=(2, 3))
    doc.add_heading("Citas", 3)
    w.opciones(doc, [
        "Trabajamos con cita previa", "Atendemos sin cita, por orden de llegada",
        "Las dos cosas", "Nos gustaría que los clientes pudieran pedir cita desde la web",
    ])
    w.hueco(doc, "¿Cómo dais las citas ahora? (teléfono, WhatsApp, libreta, alguna aplicación…)", 2)
    doc.add_heading("Formas de pago", 3)
    w.opciones(doc, ["Efectivo", "Tarjeta", "Bizum", "Bonos o tarjetas regalo"], por_fila=4)


def objetivos(doc):
    doc.add_heading("6. " + IMPRESCINDIBLE + "¿Para qué queréis la web?", 1)
    doc.add_paragraph("Marcad todas las que queráis. Si tuvierais que quedaros con una, rodeadla.")
    w.opciones(doc, [
        "Que nos encuentre gente nueva del barrio cuando busque «peluquería» en Google",
        "Que los clientes vean horario, precios y cómo llegar sin tener que llamar",
        "Que nos pidan cita más fácilmente",
        "Que la gente joven nos conozca",
        "Dar una imagen más profesional",
        "Controlar lo que se dice de nosotros en internet",
        "Vender productos",
        "Buscar personal",
    ])
    doc.add_heading("¿Quién es vuestro cliente típico?", 3)
    w.opciones(doc, ["Hombres adultos", "Hombres mayores", "Jóvenes", "Niños", "Mujeres",
                     "Gente del barrio", "Gente que viene de fuera del barrio"], por_fila=2)
    w.hueco(doc, "¿Qué tipo de cliente os gustaría tener más?", 2)
    doc.add_heading("Idiomas", 3)
    w.opciones(doc, ["Solo en español", "También en otro idioma (¿cuál?): ______________"])


def opiniones(doc):
    doc.add_heading("7. Lo que dicen vuestros clientes", 1)
    doc.add_paragraph(
        "Hemos leído vuestras opiniones de Google. Hablan solas, y son lo mejor que tenéis "
        "para convencer a alguien nuevo. Estas son algunas:"
    )
    w.recuadro(doc, "Opiniones reales de Google", [
        "«Peluquería muy profesional regentada por dos peluqueros, hijos de los anteriores "
        "dueños ya jubilados, que te cortan el pelo a tu gusto […] dejándote "
        "\"listo para triunfar\".»",
        "«Llevo más de 34 años cortándome el pelo allí y nunca he tenido ningún problema.»",
        "«Primero con sus padres y ahora con sus hijos…»",
        "«Un trato muy amable y atento. Siempre puntuales. Grandes profesionales.»",
        "«Han podido domar el pelo de mi hijo, y el de los hombres de mi familia.»",
    ])
    w.opciones(doc, [
        "Sí, queremos mostrar nuestras opiniones de Google en la web",
        "Preferimos que no",
    ])
    w.recuadro(doc, "¿Por qué os lo preguntamos?",
               "Las opiniones son de vuestros clientes. Las mostraríamos tal cual salen en Google, "
               "con su enlace, sin elegir solo las buenas ni retocarlas.")


def textos_propuestos(doc):
    doc.add_heading("8. Textos que hemos preparado para vosotros", 1)
    doc.add_paragraph(
        "Con lo que hemos leído de vosotros, os proponemos estos textos. Los huecos entre "
        "corchetes [así] son datos que no sabemos. Decidnos qué os parecen."
    )
    w.propuesta_texto(doc, "Frase principal de la web", [
        "Le cortamos el pelo a tu padre. Ahora, a ti.",
        "Peluquería familiar en el barrio de la Feria de Albacete, desde hace más de 30 años.",
    ])
    w.propuesta_texto(doc, "Quiénes somos", [
        "Somos [nombre] y [nombre], los hermanos Cotillas. Aprendimos el oficio de nuestros "
        "padres, que abrieron esta peluquería en la calle Octavio Cuartero en [año].",
        "Hoy seguimos haciendo lo que ellos nos enseñaron: escuchar lo que quieres, cortarte "
        "el pelo a tu gusto y que salgas de aquí listo para triunfar.",
        "Muchos de nuestros clientes vienen desde hace más de 30 años. Y ahora traen a sus hijos.",
    ])
    w.propuesta_texto(doc, "Por qué venir", [
        "• Oficio de familia: dos generaciones de peluqueros en el mismo local.",
        "• Puntuales: si tienes cita, no esperas.",
        "• Para toda la familia: del abuelo al nieto.",
        "• 4,8 sobre 5 en Google, con más de 130 opiniones.",
    ])


def fotos(doc):
    doc.add_heading("9. Fotos, vídeos y logotipo", 1)
    doc.add_paragraph(
        "Las fotos son lo que más se mira en una web de peluquería. No hace falta un "
        "fotógrafo: con un móvil reciente y buena luz se consiguen fotos muy dignas."
    )
    doc.add_heading("Fotos que nos vendrían bien", 3)
    w.tabla_respuestas(doc, ["Foto", "¿La tenéis?", "¿Nos ayudáis a hacerla?"], [
        [IMPRESCINDIBLE + "La fachada, de día", "[ ]", "[ ]"],
        [IMPRESCINDIBLE + "El interior: sillones, espejos, el local entero", "[ ]", "[ ]"],
        [IMPRESCINDIBLE + "Vosotros dos, juntos", "[ ]", "[ ]"],
        ["Cada uno trabajando", "[ ]", "[ ]"],
        ["Cortes terminados (de espaldas o de perfil si el cliente lo prefiere)", "[ ]", "[ ]"],
        ["Detalles: tijeras, navaja, el sillón antiguo…", "[ ]", "[ ]"],
        ["Alguna foto antigua del negocio o de vuestros padres", "[ ]", "[ ]"],
        ["Vídeo corto (menos de 1 minuto) del día a día", "[ ]", "[ ]"],
    ], [10.6, 2.8, 3.2])
    w.recuadro(doc, "Consejos para hacer las fotos", [
        "• Mejor por la mañana, con luz natural y las luces del local encendidas.",
        "• Móvil en horizontal, limpiad la lente antes.",
        "• Si sale un cliente, pedidle permiso. Si no quiere, que salga de espaldas.",
        "• Enviádnoslas por WhatsApp como «documento» o por correo, para que no pierdan calidad.",
    ])
    doc.add_heading("Logotipo", 3)
    w.opciones(doc, [
        "Tenemos logotipo y os lo enviamos",
        "Tenemos el rótulo de la fachada, pero no logotipo en archivo",
        "No tenemos logotipo",
    ])


def internet(doc):
    doc.add_heading("10. Vuestra presencia en internet", 1)
    doc.add_heading("Ficha de Google (la que sale en Google Maps)", 3)
    w.opciones(doc, [
        "La gestionamos nosotros", "La creó otra persona", "No sabíamos que existía", "No lo sabemos",
    ], por_fila=2)
    w.recuadro(doc, "🔒  Importante: nunca nos mandéis contraseñas", [
        "Si necesitamos entrar en vuestra ficha de Google o en otra cuenta, os explicaremos "
        "cómo darnos acceso con nuestro propio usuario. Vuestra contraseña es solo vuestra.",
    ], w.FONDO_AVISO, "F2B8B5")
    doc.add_heading("Redes sociales", 3)
    w.tabla_respuestas(doc, ["Red", "¿Tenéis?", "Nombre de la cuenta o enlace"], [
        ["Instagram", "[ ]", ""], ["Facebook", "[ ]", ""], ["TikTok", "[ ]", ""], ["Otra", "[ ]", ""],
    ], [4, 2.4, 10.2], columnas_respuesta=(2,))
    doc.add_heading("Dirección de la web (dominio)", 3)
    doc.add_paragraph(
        "Hemos comprobado que hermanoscotillas.es parece libre. El dominio se registra "
        "siempre a vuestro nombre: es vuestro, os quedéis con nosotros o no."
    )
    w.opciones(doc, ["Ya tenemos un dominio: ____________________",
                     "Nos gusta hermanoscotillas.es", "Preferimos otro: ____________________"])


def gustos(doc):
    doc.add_heading("11. Webs que os gustan (y que no)", 1)
    doc.add_paragraph("De peluquerías o de cualquier otra cosa. Nos ayuda mucho a acertar con el estilo.")
    w.hueco(doc, "Webs que os gustan y por qué", 3)
    w.hueco(doc, "Webs que no os gustan y por qué", 3)
    w.hueco(doc, "Colores que os representan (o que no queréis ver ni en pintura)", 2)


def cierre(doc):
    doc.add_heading("¿Y ahora qué?", 1)
    w.tabla_respuestas(doc, ["Paso", "Qué pasa"], [
        ["1", "Nos devolvéis este documento, aunque no esté completo. Lo marcado con ★ es lo más importante."],
        ["2", "Nos mandáis las fotos y el logotipo, si lo tenéis."],
        ["3", "Os enviamos un presupuesto cerrado, por escrito y sin letra pequeña."],
        ["4", "Si os encaja, nos ponemos a trabajar. El plazo de entrega irá escrito en el presupuesto."],
    ], [1.6, 15])
    w.recuadro(doc, "Cómo enviárnoslo", [
        "• Este documento: respondiendo al correo con el archivo adjunto.",
        "• Las fotos: por WhatsApp (como «documento») o por correo.",
        "• ¿Prefierís hablarlo? Decidnos cuándo os viene bien y os llamamos.",
    ], w.FONDO_PROPUESTA, "A9D3B0")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Gracias por vuestro tiempo. Prometemos que merece la pena.")
    r.italic, r.font.color.rgb = True, w.GRIS


def main():
    doc = w.nuevo_documento()
    w.pie_de_pagina(doc, f"{NEGOCIO} · Cuestionario · {EMPRESA}")
    portada(doc)
    como_rellenar(doc)
    lo_que_sabemos(doc)
    contacto(doc)
    legales(doc)
    quienes_sois(doc)
    servicios(doc)
    objetivos(doc)
    opiniones(doc)
    textos_propuestos(doc)
    fotos(doc)
    internet(doc)
    gustos(doc)
    cierre(doc)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    doc.save(SALIDA)
    print(SALIDA)


if __name__ == "__main__":
    main()
