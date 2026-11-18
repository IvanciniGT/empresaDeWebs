# Expediente · Peluquería Hermanos Cotillas (ronda 2)

> ⚠️ **CLIENTE SIMULADO · RONDA 2.** Es un negocio real, pero **no es cliente
> nuestro y nadie le ha contactado**. Los mensajes de este expediente **no se han
> enviado**. Solo usamos información pública. Reglas:
> [procesos/ronda-2/arranque.md](../../procesos/ronda-2/arranque.md).
>
> **Repositorio público (A-013):** aquí no va ningún dato personal. Lo personal,
> en `privado/`, que está fuera de git.

| | |
|---|---|
| **Estado** | Primer contacto hecho · **sin respuesta** del cliente |
| **Abierto** | 2026-11-18, miércoles, 18:10 · Menchu (fase 0, encargo E-017) |
| **Canal** | WhatsApp (simulado) |
| **Petición literal** | «Hola, somos la Peluquería Hermanos Cotillas, de Albacete. Queremos una web.» |
| **Encaje con §5** | Sí, en principio: negocio local de servicios en España. Tamaño sin confirmar («somos» y «Hermanos»: probablemente pocas personas) |
| **Trato** | Vosotros (escriben en plural y no dicen cómo prefieren que se les trate; §9.2, tuteo por defecto) |
| **Próximo contacto** | 2026-11-19, jueves, por la mañana · mensaje de cierre si siguen sin contestar |
| **Primer envío prometido** | 2026-11-25, miércoles (5 días laborables, `primer-contacto`) · se promete en el mensaje del jueves |
| **Datos personales y conversación** | `privado/contacto.md` y `privado/contactos.md` |

## 0. Primer contacto (Menchu)

Skill: [primer-contacto](../../procesos/skills-borrador/primer-contacto/SKILL.md) **v0.4**.

### Lo que sabemos y lo que no

| Pregunta mínima | Respuesta | De dónde |
|---|---|---|
| 1 · Negocio y ciudad | Peluquería Hermanos Cotillas · Albacete. Calle: no la dijo | Petición literal |
| 2 · Web, redes, ficha de Google | **No lo sabemos.** Preguntado, sin respuesta | — |
| 3 · Con quién hablo | No lo sabemos | — |
| 4 · Cuándo escribirles, y si usan correo | No lo sabemos | — |
| 5 · Qué quieren conseguir | Solo «Queremos una web» | Petición literal |

**Para la fase 1 (Chema):** tenemos el nombre del negocio y la ciudad, que bastan
para empezar a investigar. **No sabemos si tienen web o redes**: que no se dé
por hecho que no las tienen (alta-cliente, regla 3).

### Mensajes

Ninguno se ha enviado: es una simulación. En un caso real, Iván los copiaría
desde `privado/mensajes/` (A-003). Ninguno lleva datos personales.

**Día 0 · miércoles 18 · 18:10 · dos mensajes seguidos**

> **1 · Presentación** (plantilla 1)
>
> ¡Hola! Soy Menchu, de [Empresa]. Soy una asistente de inteligencia
> artificial: os atiendo yo, y lo importante (presupuestos, publicar vuestra
> web) lo revisa y aprueba Iván, el responsable. Si en algún momento preferís
> hablar con él, decídmelo.
>
> Gracias por escribirnos. Para empezar solo necesito saber un par de cosas;
> del resto nos encargamos nosotros.

> **2 · Enlaces** (plantilla 3)
>
> ¿Tenéis ya web, Instagram, Facebook o ficha en Google Maps? Si es así,
> mandadme los enlaces. Así no os preguntamos lo que ya está publicado.

La plantilla 2 («¿cómo se llama vuestro negocio y en qué ciudad está?») no se
manda: ya nos lo dijeron. Las preguntas 3 a 5 esperan a que contesten, porque la
skill pide una pregunta cada vez.

**Resultado: sin respuesta** (simulación: nadie contesta).

**Día +1 · jueves 19 · por la mañana · si siguen sin contestar** (redactado; no
enviado)

> Hola de nuevo. Con lo que nos contasteis ya podemos empezar: vamos a mirar
> lo que hay publicado sobre la Peluquería Hermanos Cotillas. El miércoles 25
> os mando un pequeño informe, gratis y sin compromiso, y unas preguntas
> cortas para el presupuesto; la mayoría se contestan eligiendo una opción.
>
> Lo de los enlaces, si os acordáis, me lo podéis mandar cuando queráis. Si
> mientras tanto os surge algo, aquí estoy.

Es la plantilla 6 (cierre), adaptada a que no han contestado: sin su nombre, y con
un recordatorio de la pregunta de los enlaces. **La skill no dice qué hacer si no
contestan en el primer contacto**, así que esta adaptación no sale de una
plantilla aprobada. En real, necesitaría el sí de Iván a través de Federico.
Lo propongo para la skill (ver el historial).

### Avisos para el resto del alta

- **Plazo:** la fecha del miércoles 25 sale de los 5 días laborables, que siguen
  pendientes de Iván (Puri, R02). Puri admite usarlos en la ronda 2. Por dentro,
  el objetivo es el lunes 23. Si el miércoles 25 a las 12:00 no está confirmado
  el envío, aviso al cliente con una fecha nueva (`primer-contacto`).
- **Festivos:** entre el 19 y el 25 de noviembre no hay festivos nacionales.
  Los locales de Albacete no los he comprobado.
- **Privacidad:** el primer mensaje no lleva la línea de privacidad (Puri, R01;
  pendiente de A-010). En la simulación no hay datos de nadie. Con un cliente
  real, no se manda sin resolver antes A-010.
- **Huecos:** `[Empresa]` y el número de WhatsApp de la empresa siguen sin
  existir (§15).

## Secciones de la investigación

Las secciones 1 a 7 las abre Chema en la fase 1, con su skill `investigar-cliente`.

> **Fase 1 · Chema · E-018 · 2026-11-18.** Skill
> [investigar-cliente](../../procesos/skills-borrador/investigar-cliente/SKILL.md)
> **v0.3**. Todo se ha consultado de nuevo en esta ronda: no se ha reutilizado nada
> de `clientes/peluqueria-hermanos-cotillas/`.
>
> **Estado: parcial.** Las secciones 4 y 5, y parte de la 6 y la 7, dependen de las
> capturas de Google que hace Iván con el
> [guion](privado/capturas-google/guion.html) (en `privado/`, fuera de git).
> Hasta que lleguen, **la ficha de Google no se ha visto**: nada de este expediente
> sale de ella.

### Guion de captura para Iván

| | |
|---|---|
| **Fichero** | `privado/capturas-google/guion.html` · generado el 2026-11-18 a las 18:25 con `enlaces_captura.py` · 9 capturas |
| **Centro del mapa** | 38.9925046, -1.8616289 (nodo de OSM del cliente, ver §1) |
| **Búsqueda principal** | «peluquería caballero Albacete» |
| **Otras búsquedas** | «barbería Albacete» · «peluquería Albacete» (de control: la genérica) |
| **Cómo se eligieron** | Paso 4 de `estudio-competencia`: OSM marca el local como `male=yes` (público masculino), de ahí «caballero» y «barbería». **Falta el criterio 1** (las palabras de las reseñas) y el 2 (la categoría de Google): ninguno se puede usar antes de las capturas. Si las reseñas usan otras palabras, se dice en la fase 2 y no se repiten capturas |
| **Avisado** | Federico, 2026-11-18 18:28, para que se lo pase a Iván |

## 1. Datos comprobados

Ninguno todavía. Un dato comprobado pide una fuente primaria o dos secundarias
independientes (regla 1), y hasta ahora solo tenemos una secundaria
(OpenStreetMap). La ficha de Google (primaria) llega con las capturas de Iván.

| Dato | Valor | Fuente(s) y nivel | Consultado |
|---|---|---|---|
| Nombre comercial y ciudad | Peluquería Hermanos Cotillas · Albacete | El cliente, en su mensaje (primaria) | 2026-11-18 18:10 |

## 2. Datos a confirmar con el cliente

| Dato | Lo que hemos visto | Por qué no nos fiamos |
|---|---|---|
| Dirección | Calle Octavio Cuartero, 57 · Albacete | Una sola fuente secundaria: OSM, nodo [13516520881](https://www.openstreetmap.org/node/13516520881), versión 6, editado el 2026-09-23. Se confirma con la ficha de Google |
| Código postal | 02004 | Etiqueta ausente en el nodo: lo **deduce Nominatim** por la zona. Es una inferencia, no un dato |
| Barrio | Feria (Distrito 2) | Solo Nominatim, por los límites de OSM. La skill lo deja en «por confirmar» |
| Horario | L-V 9:00-13:45 y 16:30-20:45 · S 8:30-14:00 | OSM, comprobado por quien lo editó el 2026-04-12 (`check_date:opening_hours`). Hace 7 meses y una sola fuente: se contrasta con la ficha de Google |
| Público | Masculino (`male=yes`) | OSM. Que también atiendan a mujeres o niños no lo dice: se pregunta |
| Accesibilidad | Silla de ruedas: «limitada» (`wheelchair=limited`) | OSM. No dice por qué (¿un escalón?) |
| Actividad | Peluquería (`shop=hairdresser`), no barbería (`shop=barber`) | Es la etiqueta de OSM, no lo que dice el negocio |

## 3. Lo que intuimos (preguntar, no afirmar)

| Intuición | De dónde sale | Pregunta para el cliente |
|---|---|---|
| Es un negocio familiar, de hermanos | Solo el nombre («Hermanos») y el «somos» del mensaje | ¿Quiénes estáis en la peluquería? ¿Queréis salir en la web? |
| Es una peluquería de caballero | `male=yes` en OSM, una sola fuente | ¿Atendéis solo a hombres? ¿Y a niños? |
| Puede que no haya web propia | Los 7 dominios probados no existen (§6) y OSM no enlaza web | ¿Tenéis o habéis tenido web? ¿Algún dominio a vuestro nombre? |

## 4. Ficha de Google (captura manual de Iván, AAAA-MM-DD HH:MM, desde <ciudad>)

**Pendiente de las capturas de Iván.** Cuando lleguen anoto la categoría principal,
si sale «Reclamar esta empresa», la nota y el número de opiniones, la fecha de la
última reseña, si el negocio responde y si la ficha enlaza alguna web.

## 5. Lo que dicen los clientes

**Pendiente de las capturas de Iván** (capturas 2 y 3). Sin capturas no hay citas:
cada cita va con su prueba en `privado/` (regla 7).

## 6. Presencia en internet

«No encontrado» quiere decir que no apareció en esas fuentes en esa fecha, **no que
no exista** (regla 5).

| Dónde | Estado | Fuente y fecha |
|---|---|---|
| OpenStreetMap | **Está**: nodo 13516520881, `shop=hairdresser`, con dirección, horario, público y accesibilidad. No enlaza web, teléfono ni redes | API de OSM, 2026-11-18 18:24 |
| Web propia | **No encontrada.** Ninguno de estos 7 dominios tiene DNS: hermanoscotillas.com/.es/.net, peluqueriahermanoscotillas.com/.es, peluqueriacotillas.com/.es. `cotillas.es` existe, pero es el **Ayuntamiento de Cotillas** (un pueblo de la provincia de Albacete), no el negocio | `dig` y `curl`, 2026-11-18 18:36 |
| Instagram, Facebook | **Sin consultar todavía.** Su `robots.txt` prohíbe leer los perfiles; lo dirán las capturas `site:` de Iván (7 y 8) | `robots.mjs`, 2026-11-18 18:31 |
| Booksy | **No encontrado** entre las 15 374 fichas de España de su sitemap (84 de Albacete). El sitemap se actualizó por última vez el 2026-06-25: un alta posterior no saldría | sitemap de booksy.com, 2026-11-18 18:40 |
| Treatwell | **No se pudo leer:** su sitemap de establecimientos devuelve un 202 vacío, seguramente una protección contra robots. No se insiste (regla 10) | treatwell.es, 2026-11-18 18:41 |
| Bing Maps | **Sin consultar.** Su `robots.txt` lo permite, pero no he podido leer las condiciones de uso de Microsoft (microsoft.com da 403 a `curl`). Sin leerlas, no se usa | 2026-11-18 18:33 |
| Apple Maps | **Sin consultar:** su `robots.txt` prohíbe la URL de búsqueda | `robots.mjs`, 2026-11-18 18:31 |

## 7. Auditoría de citas

**Pendiente.** Sin buscadores no hay forma limpia de encontrar los directorios
automáticos: las URL directas probadas dan 404 (mispelus) o 403 (infoisinfo, y
Cylex en su `robots.txt`); Páginas Amarillas no responde a su `robots.txt`, y la RFC
9309 manda tratarlo como prohibido. **La lista de directorios saldrá de la captura 1
de Iván** (Google con el nombre): cada directorio que aparezca se abre por su URL,
después de leer su `robots.txt`, y se captura con `herramientas/captura.sh`.

| Directorio (URL) | Nombre | Dirección | Teléfono | Horario | Errores | Fecha |
|---|---|---|---|---|---|---|
| — | | | | | | |

**Aviso para las búsquedas:** «Cotillas» también es un pueblo de Albacete. Un
resultado con «Cotillas» y «Albacete» puede ser del pueblo y no del negocio: hay que
comprobarlo en cada captura.

## Historial

| Fecha | Quién | Qué |
|---|---|---|
| 2026-11-18 18:10 | Menchu | Fase 0 (E-017). Expediente abierto con la petición literal. Primer contacto simulado: presentación y pregunta por los enlaces; **sin respuesta**. Cierre redactado para el jueves 19, con el primer envío prometido para el miércoles 25. **No se ha enviado nada.** Para la skill v0.5: qué hacer cuando el cliente no contesta en el primer contacto |
| 2026-11-18 18:45 | Chema | Fase 1 (E-018), **parcial**. Guion de captura para Iván en `privado/capturas-google/guion.html` (9 capturas), avisado a Federico a las 18:28. Local ubicado en OSM (nodo 13516520881). Secciones 1 a 7 abiertas: nada está comprobado todavía, todo va a «a confirmar», y la ficha de Google, las reseñas y la auditoría de citas esperan a las capturas. Nada reutilizado de la ronda 1 |
