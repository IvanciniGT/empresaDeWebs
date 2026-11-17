# Catálogo de preguntas · cuestionario-cliente

> **BORRADOR v0.2 · revisado por Reme.** Es la fuente única de las preguntas.
> El cuestionario (Word, teléfono o, en el futuro, formulario) se monta **desde
> aquí** y conserva los ID, para que cada respuesta pueda trazarse hasta su
> requisito.

## Cómo se lee

- **ID:** estable. No se reutiliza aunque la pregunta se quite.
- **★:** sin esta respuesta **no se puede hacer el presupuesto**. En B2, sin
  ella no se puede empezar el trabajo.
- **Destino:** adónde va la respuesta. Una pregunta sin destino se quita.

| Destino | Va a | Lo usa |
|---|---|---|
| `PRECIO` | Previo de precio y borrador de presupuesto | Reme |
| `REQ` | `requisitos.md` (requisito con criterio de aceptación) | Reme → Lola, Paco, Puri |
| `CONT` | `requisitos.md` §4 (contenido) | Chema |
| `DIS` | `requisitos.md` §4 (contenido) | Lola |
| `DATO` | `expediente.md` §1, con fuente «cliente» | Todos |
| `CONTACTO` | `expediente.md` | Menchu |
| `LEGAL` | Contrato, factura y aviso legal | Iván / quien redacte |

**Regla de batería:** si la respuesta puede cambiar el **plan, el precio o el
plazo**, va en B1. Si solo cambia el contenido, va en B2.

---

## B1 · Conoceros (antes del presupuesto)

Objetivo: **4 páginas como máximo** y unos 15 minutos para rellenarlo.

### Bloque 1 · Lo que ya sabemos (validar)

Una sola tabla: «Lo que hemos encontrado · ¿Correcto? · Si no, ¿cuál es el bueno?».
Las filas salen **solo** del expediente (§1 comprobados, §2 a confirmar).

| ID | Fila | ★ | Para qué | Destino |
|---|---|---|---|---|
| 1.1 | Nombre del negocio | | Identidad, dominio, ficha de Google | DATO |
| 1.2 | Dirección | | Mapa, datos estructurados, ficha de Google | DATO, REQ |
| 1.3 | Teléfono | | Botón de llamada (§6.1) | DATO, REQ |
| 1.4 | Horario | ★ | Va siempre en la web (§6.1) y es el dato que más mienten los directorios | DATO, REQ |
| 1.5 | Quiénes sois (una frase) | | Textos | DATO, CONT |
| 1.6 | Vuestra clientela (lo que dicen las reseñas) | | Textos y diseño: a quién habla la web | DATO, CONT, DIS |
| 1.7 | Web, dominio, correo propio o redes: «no hemos encontrado ninguna; si tenéis, poned el enlace» | ★ | Si ya hay web o dominio, hay que trasladarlos: cambia el trabajo y el plazo | PRECIO, REQ |

No se incluye nada que el cliente no pueda corregir (por ejemplo, su nota en
Google). Las ausencias se escriben como «no hemos encontrado», nunca como «no
tenéis».

### Bloque 2 · Contacto

| ID | Pregunta | ★ | Para qué | Destino |
|---|---|---|---|---|
| 2.1 | ¿Con quién hablamos? (nombre) | ★ | Saber a quién dirigirnos | CONTACTO |
| 2.2 | ¿Quién da el visto bueno a la web? Si sois varios, ¿basta con uno? | ★ | Quién aprueba el presupuesto, los textos y las 2 rondas de cambios | CONTACTO, REQ |
| 2.3 | Móvil, y si tiene WhatsApp | ★ | Canal principal (§9.1) | CONTACTO |
| 2.4 | Correo electrónico | ★ | El presupuesto se envía por correo (§9.1) | CONTACTO |
| 2.5 | Mejor momento para llamaros | | Llamar cuando puedan atender | CONTACTO |

### Bloque 3 · Vuestro negocio

| ID | Pregunta | ★ | Para qué | Destino |
|---|---|---|---|---|
| 3.1 | ¿Desde qué año existe el negocio? (aproximado vale) | | Experiencia (mínimo de Iván); textos | CONT |
| 3.2 | ¿Qué os define? Casillas del **bloque de sector** + «Otra: ___» | | Puntos fuertes, valores y posicionamiento (mínimo de Iván) | CONT, DIS |
| 3.3 | ¿Qué hacéis? Casillas del **bloque de sector** + filas en blanco. Columna «precio, si queréis publicarlo» | ★ | Productos y precios (mínimo de Iván); tamaño de la sección de servicios | REQ, CONT |
| 3.4 | ¿Vendéis productos? ¿Queréis venderlos **por internet**? | ★ | Una tienda online está fuera de catálogo (§5, §6): pasa a Federico | PRECIO |
| 3.5 | ¿Cómo dais las citas hoy? Sin cita · teléfono · WhatsApp · con una aplicación (¿cuál?) | ★ | Herramientas y procesos (mínimo de Iván). Integrar un programa de terceros no está incluido (§6.1) | PRECIO, REQ |
| 3.6 | ¿Algo que deba saber quien viene? (aparcamiento, acceso en silla de ruedas, cómo llegar) | | Datos del local (mínimo de Iván); textos y ficha de Google | CONT |

### Bloque 4 · La web que queréis

| ID | Pregunta | ★ | Para qué | Destino |
|---|---|---|---|---|
| 4.1 | ¿Para qué queréis la web? Casillas: que nos encuentren clientes nuevos · ver horario, precios y cómo llegar sin llamar · pedir cita más fácil · **reservar desde la web a cualquier hora** · imagen más profesional / que nos conozcan · llegar a otro tipo de cliente (¿cuál?) · vender por internet · buscar personal · otra | ★ | Elegir el plan y lo que entra. «Reservar desde la web» lleva a Negocio; «vender por internet» queda fuera de catálogo | PRECIO, REQ |
| 4.2 | Si solo pudierais quedaros con una, ¿cuál? (una línea) | ★ | Prioridad. Si hay que recortar, se protege esta | REQ |
| 4.3 | ¿En qué idiomas? ¿Tenéis quien traduzca? | | Las traducciones no están incluidas (§6.1) | PRECIO |
| 4.4 | ¿Cada cuánto cambiaríais algo (horario, precios, promociones)? Casi nunca · 1–2 veces al mes · cada semana | | Mantenimiento Básico o Plus (§8.2) | PRECIO |
| 4.5 | ¿Para cuándo la queréis? (fecha o «sin prisa») | | Plazo y prioridad | PRECIO |

### Bloque 5 · Lo que tenéis

| ID | Pregunta | ★ | Para qué | Destino |
|---|---|---|---|---|
| 5.1 | ¿Tenéis fotos o vídeos del local y vuestros que podamos usar? Varias · alguna · ninguna | ★ | Mínimo de Iván. La fotografía no está incluida (§6.1). Sin fotos se alarga el plazo | PRECIO |
| 5.2 | Si faltan: ¿las haríais vosotros con el móvil y nuestra guía, o preferís un fotógrafo? | | Extra de fotografía | PRECIO |
| 5.3 | Logotipo: lo tenemos en archivo · solo el rótulo · no tenemos · queremos uno nuevo | | El logotipo no está incluido (§6.1) | PRECIO, DIS |
| 5.4 | Ficha de Google: la gestionamos nosotros · la creó otra persona · no sabíamos que existía · no lo sabemos | | Alta o revisión de la ficha (§6.1). Si no la controlan, recuperarla lleva tiempo | REQ |

Además, en B1 van siempre, sin ser preguntas: cómo rellenarlo, el código de
colores, el aviso de **no mandar contraseñas**, la alternativa por teléfono,
la cláusula de protección de datos y el «¿y ahora qué?».

---

## B2 · Al contratar (tras aceptar el presupuesto)

| ID | Pregunta | ★ | Para qué | Destino |
|---|---|---|---|---|
| 6.1 | Titular, forma jurídica (autónomo, S.L., C.B.…), NIF y domicilio fiscal | ★ | Contrato, factura y aviso legal (LSSI) | LEGAL |
| 6.2 | Vuestros nombres y si queréis que salgan en la web | ★ | Textos | CONT |
| 6.3 | La historia: cómo empezó, desde cuándo la lleváis vosotros, si siempre ha estado en el mismo sitio, quién más trabaja, alguna anécdota | | Textos. **Mejor por teléfono**: se cuenta más fácil de lo que se escribe | CONT |
| 6.4 | Servicios: descripción corta y precio definitivo de cada uno | ★ | Sección de servicios | CONT |
| 6.5 | Formas de pago | | Información práctica | CONT |
| 6.6 | Permiso para mostrar vuestras opiniones de Google | | Contenido. **Pendiente de la duda legal** (revisión, §6) | CONT, LEGAL |
| 6.7 | Fotos: lista de fotos que hacen falta, con la guía para hacerlas | ★ | Contenido | CONT, DIS |
| 6.8 | Logotipo en archivo, si lo tienen | | Diseño | DIS |
| 6.9 | Webs que os gustan y que no; colores que os representan | | Diseño (**solo si Lola lo necesita**) | DIS |
| 6.10 | Dominio elegido | ★ | Registro, a nombre del cliente | REQ |
| 6.11 | Número de WhatsApp para clientes y correo al que llegan los mensajes del formulario | ★ | El botón de WhatsApp y el formulario van siempre (§6.1); falta saber a dónde | REQ |
| 6.12 | Accesos: ficha de Google y dominio, con usuario propio o acceso delegado | ★ | Trabajo de ficha y dominio. **Nunca contraseñas** (§12) | REQ |

La aprobación de los textos **no es una pregunta del cuestionario**: es la
fase 4 de §13.5, con sus 2 rondas.

### B2 · Bloques según el tipo de web

Solo si las respuestas de B1 lo piden:

| Si en B1… | Bloque | Qué se pregunta |
|---|---|---|
| 4.1 marca «reservar desde la web» | Reservas | Servicios que se reservan y duración de cada uno, quién atiende, antelación, cancelaciones, cómo se entera el negocio |
| 4.3 pide otro idioma | Idiomas | Qué partes se traducen, quién traduce y quién revisa |
| 4.1 marca «buscar personal» | Empleo | Qué puestos, cómo quieren recibir candidaturas (datos personales: ojo al RGPD) |

Vender por internet **no tiene bloque**: está fuera de catálogo y lo decide
Iván.

---

## Bloques de sector

Cambian solo las **casillas** de 3.2 y 3.3 y la lista de fotos de 6.7. El
resto del cuestionario es igual para todos.

**Solo existen los sectores con los que ya hemos trabajado.** Con el primer
cliente de un sector nuevo se usa el bloque genérico (filas en blanco) y, al
terminar, se escribe su bloque con lo que de verdad hayan respondido. No se
inventan opciones.

### Peluquería / barbería

Origen: caso Hermanos Cotillas (ronda 1).

- **3.2 Qué os define:** negocio familiar de toda la vida · cortes clásicos ·
  especialistas en niños · trato cercano, de confianza · puntualidad: con cita
  no se espera · precios ajustados · rapidez · asesoramos al cliente · cuidamos
  la barba.
- **3.3 Servicios:** corte de caballero · corte de niño · corte + lavado ·
  arreglo de barba · afeitado a navaja · degradado · corte de señora · color /
  tinte · cejas · tratamientos capilares · venta de productos.
- **6.7 Fotos:** fachada de día · interior entero · el equipo junto · cada uno
  trabajando · cortes terminados (de espaldas o de perfil si el cliente lo
  prefiere) · detalles del oficio · fotos antiguas del negocio.

### Genérico

- **3.2:** solo «Contadnos en una línea qué os hace distintos».
- **3.3:** tabla en blanco de 8 filas: servicio o producto, precio si queréis
  publicarlo.
- **6.7:** fachada, interior, equipo y producto o trabajo terminado.
