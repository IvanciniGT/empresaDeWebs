# Catálogo de preguntas · cuestionario-cliente

> **BORRADOR v0.3.1 · revisado por Reme · 2026-11-18 · tanda A CERRADA.**
> v0.3.1: las cinco notas de Menchu (A 4.1 y A 4.6, A 5.7 en dos, A 3.4, A 1.3).
> Es la fuente única de las preguntas. El guion de WhatsApp de Menchu, el Word
> y cualquier formato futuro salen de aquí y **conservan los ID**, para que cada
> respuesta llegue hasta su requisito.

## Cómo se lee

- **ID:** el número (4.1). Es estable: no cambia de significado ni se
  reutiliza, aunque la pregunta se retire. Se escribe con la tanda delante:
  **A 4.1**, **B 6.3**. En v0.2 las tandas se llamaban B1 y B2.
- **Obligatoria:** la respuesta hace falta siempre. Si el cliente ya la dio
  (en el primer contacto o en otra respuesta), **no se vuelve a preguntar**: se
  anota de dónde sale.
- **Condicional:** solo se pregunta si se cumple su condición. El cliente no
  ve las que no le tocan.
- **★:** sin esta respuesta **no se puede cerrar el presupuesto**. Si no llega,
  Menchu la repite en el recordatorio.
- **Destino:** adónde va la respuesta. Una pregunta sin destino se quita.
- **Las condiciones nombran la opción, no su número** («A 4.1 marca *vender por
  internet*»), para que reordenar las opciones no rompa el guion.

| Destino | Va a | Lo usa |
|---|---|---|
| `PRECIO` | Previo de precio y borrador de presupuesto | Reme |
| `PLAZO` | Plazo del presupuesto y prioridad | Reme |
| `REQ` | `requisitos.md` (requisito con criterio de aceptación) | Reme → Lola, Paco, Puri |
| `CONT` | `requisitos.md` §4 (contenido) | Chema |
| `DIS` | `requisitos.md` §4 (contenido) | Lola |
| `DATO` | `expediente.md` §1, con fuente «cliente, A x.y, fecha». **Solo datos del negocio que ya son públicos o que el negocio quiere publicar.** `expediente.md` está en git, que es público: un dato de una persona (un móvil personal, el nombre de un autónomo que no figura en el rótulo) va a `PRIVADO` | Todos |
| `PRIVADO` | `privado/` (datos personales, A-009) | Quien lo necesite |

**La regla de la tanda A:** solo entra lo que puede cambiar **el plan, el
precio o el plazo**. Lo que solo cambia el contenido va en la tanda B, después
de aceptar el presupuesto.

---

## Tanda A · para el presupuesto

**8 obligatorias** (5 con ★), **10 condicionales** y **1 opcional**.

Por WhatsApp, una pregunta por mensaje (Menchu, `guion-tanda-a.md`). Las cuatro
filas de A 1.1–1.4 se confirman **en un solo mensaje** y cuentan como **una**
pregunta: el cliente contesta «sí» o corrige lo que esté mal.

Orden propuesto: empezar por lo fácil (confirmar) y terminar con la foto. El
cómo se dice y el orden final son de Menchu.

### Obligatorias

| # | ID | Pregunta | Opciones | ★ | Qué cambia según la respuesta | Destino |
|---|---|---|---|---|---|---|
| 1 | **A 1.1–1.4** | Confirmar lo que hemos visto: nombre del negocio (1.1), dirección (1.2), teléfono (1.3) y horario (1.4) | «Está bien» / lo que haya que corregir | | Si algo no cuadra, el informe y el previo se hicieron con datos equivocados y hay que revisarlos antes del presupuesto. El horario es el dato en el que más fallan los directorios | DATO, REQ. **A 1.3:** si nos dan otro número y es un móvil personal, PRIVADO; en el expediente queda «teléfono confirmado por el cliente, en `privado/contacto.md`» |
| 2 | **A 4.1** | ¿Para qué queréis la web? Podéis marcar varias | 1 que nos encuentre gente nueva · 2 que vean horario, servicios y cómo llegar sin llamar · 3 que puedan pedir o reservar cita desde la web · 4 vender productos por internet · 5 que se pueda leer en otro idioma · 6 buscar personal · 7 otra cosa | ★ | *Pedir o reservar cita* → A 4.6, que decide Esencial o Negocio. *Vender* → **fuera de catálogo** (A 3.4). *Otro idioma* → traducciones, **aparte** (§6.1). *Gente nueva* → anotar para ofrecer el SEO continuo más adelante, con datos. Si el primer contacto ya lo dijo, se cita y se pregunta solo «¿algo más de esto?» | PRECIO, REQ |
| 3 | **A 3.3** | ¿Qué servicios hacéis? Como os salga, o una foto de la lista de precios si la tenéis a mano | Ejemplos del bloque de sector | ★ | Una lista corta cabe en **Esencial**. Una carta o un catálogo largo, en **Negocio** | PRECIO, REQ, CONT |
| 4 | **A 3.5** | ¿Cómo dais las citas ahora? | 1 sin cita, por orden de llegada · 2 por teléfono · 3 por WhatsApp · 4 con una aplicación o web de reservas · 5 otra | ★ | 4 → integrarla **no está incluido** (§6.1): ver A 3.7. 3 → el botón principal de la web puede ser WhatsApp; si no, **Llamar** (Lola) | PRECIO, REQ, DIS |
| 5 | **A 5.5** | ¿Qué tenéis ya? Marcad lo que tengáis | 1 dominio (una dirección www…), ¿cuál? · 2 logotipo en archivo · 3 fotos del local o de vuestro trabajo que podamos usar · 4 vídeos · 5 nada de esto | ★ | Sin fotos → plazo más largo o fotógrafo (**aparte**, §6.1): A 5.2. Sin logotipo → A 5.3. Dominio propio → se traslada y su renovación entra en la cuota (A-011) | PRECIO, PLAZO, DIS |
| 6 | **A 5.4** | La ficha de Google Maps (la que sale con vuestras opiniones): ¿quién la lleva? | 1 nosotros · 2 otra persona · 3 no sabíamos que existía · 4 no lo sé | | Su alta o revisión entra en la creación (§6.1). 2–4 → recuperarla depende de un tercero o de Google y **alarga el plazo** | PLAZO, REQ |
| 7 | **A 4.4** | Cuando la web esté hecha, ¿cada cuánto cambiaríais algo (horario, precios, una promoción)? | 1 una vez al mes o menos · 2 de dos a cuatro veces al mes · 3 más a menudo | ★ | 1 → Mantenimiento **Básico** · 2 → **Plus** · 3 → Plus y horas fuera de plan (§8.2) | PRECIO |
| 8 | **A 4.5** | ¿Para cuándo os gustaría tenerla? | Una fecha o «sin prisa» | | Plazo del presupuesto y prioridad. **No se promete nada al contestar** | PLAZO |

Las 8 cubren los mínimos de Iván que cambian precio o plazo: herramientas y
procesos (A 3.5), para qué y otros idiomas (A 4.1, A 4.3), fotos, vídeos y
logotipo (A 5.5), datos del local (A 1.1–1.4) y productos (A 3.3). Los datos de
contacto los recoge `primer-contacto`. Lo que no cambia el precio
(experiencia, puntos fuertes, valores, posicionamiento) pasa a la tanda B: ver
«Lo que ha salido de la tanda A».

### Condicionales

| ID | Solo si… | Pregunta | Qué cambia | Destino |
|---|---|---|---|---|
| **A 4.6** | A 4.1 marca *pedir o reservar cita* | ¿Queréis que el cliente elija día y hora él solo en la web, o que os pida cita y la confirméis vosotros? | Elegir él solo = agenda = **Negocio**. Pedir y confirmar = botón de WhatsApp o formulario, incluido en **Esencial** | PRECIO, REQ |
| **A 3.4** | A 4.1 marca *vender productos por internet* | ¿Qué productos queréis vender por internet, y cuántos más o menos? | Fuera de catálogo (§5, §6). **Menchu avisa a Federico en el momento y sigue con el resto de preguntas**, salvo que Federico diga que pare. Lo decide Iván, y **el presupuesto no se cierra hasta que decida** | PRECIO |
| **A 4.3** | A 4.1 marca *otro idioma* | ¿En qué idioma? ¿Tenéis quien lo traduzca? | Las traducciones no están incluidas (§6.1) | PRECIO |
| **A 4.7** | A 4.1 marca *buscar personal* | ¿Os basta con un aviso («buscamos peluquero, escribidnos») o queréis recibir currículums desde la web? | Recibir currículums es tratar datos personales de terceros: más trabajo legal (A-010) | PRECIO, REQ |
| **A 3.7** | A 3.5 marca *aplicación o web de reservas* | ¿Qué aplicación es? ¿Os basta con un botón en la web que lleve a ella? | El botón, incluido. Integrarla dentro de la web, **aparte** (§6.1) | PRECIO, REQ |
| **A 5.7** | Dijo en el primer contacto que tiene web | ¿Quién os lleva la web ahora, y la seguís pagando? | Si hay un proveedor con contrato, trasladarla depende de él: **plazo** | PLAZO |
| **A 5.8** | Ídem | ¿Hay algo de la web actual que queráis conservar (textos, fotos, la dirección)? | Aprovechar o rehacer cambia el trabajo (skill `extraer-web-existente`) | PRECIO |
| **A 5.2** | A 5.5 no marca *fotos* | ¿Las fotos las haríais vosotros con el móvil, con unos consejos nuestros, o preferís un fotógrafo? | Fotógrafo: **aparte**, sin tarifa (lo decide Iván). Móvil: más plazo | PRECIO, PLAZO |
| **A 5.3** | A 5.5 no marca *logotipo* | ¿Queréis un logotipo nuevo, o seguís con el nombre tal cual (como en el rótulo)? | Logotipo nuevo: **no incluido** (§6.1); a Federico | PRECIO |
| **A 2.2** | En el primer contacto salió que sois varios | ¿Quién da el visto bueno a la web? ¿Basta con uno de vosotros? | Quién acepta el presupuesto y las 2 rondas de cambios. Si tienen que estar todos de acuerdo, **más plazo** | PLAZO, PRIVADO |

### Opcional (choque 3)

| ID | Pregunta | Para qué | Destino |
|---|---|---|---|
| **A 5.6** | Si tenéis a mano una foto de la fachada con el rótulo, de día y sin gente delante, mandádnosla. Si no, no pasa nada | La guía de estilos previa de Lola. No es material para la web. **Siempre la última** | DIS |

**Ninguna foto más hasta que acepten el presupuesto.** La lista de precios
de A 3.3 no cuenta como foto: es una forma de contestar.

### Lo que ha salido de la tanda A (y por qué)

| ID v0.2 | Qué era | Ahora | Por qué |
|---|---|---|---|
| 1.5 | Quiénes sois (una frase) | **B 6.3** | Contenido |
| 1.6 | Vuestra clientela | **B 6.3** | Contenido. Lo dicen ya las reseñas |
| 1.7 | Web y redes | **Retirada** | Lo pregunta `primer-contacto` (enlaces). El dominio, en A 5.5 |
| 2.1, 2.3, 2.4, 2.5 | Nombre, móvil, correo, cuándo escribir | **Retiradas** | Lo recoge `primer-contacto` y va a `privado/contacto.md` |
| 3.1 | Desde qué año existe | **B 6.3** | Experiencia: contenido, no precio |
| 3.2 | Qué os define | **B 6.3** | Puntos fuertes y valores: contenido |
| 3.6 | Aparcamiento, accesibilidad, cómo llegar | **B 6.13** | Contenido |
| 4.2 | Si os quedáis con una | **Retirada** | Lo da el «qué queréis conseguir» literal de `primer-contacto` |
| 5.1 | ¿Tenéis fotos? | **Dentro de A 5.5** | Una pregunta en vez de tres |

**De la propuesta de Menchu** (revisión, §5), entran 1 (A 1.1–1.4), 3 (A 3.3),
4 (A 3.5 y A 4.6), 5 (A 4.1), 6 (A 5.5) y 7 (A 5.4). Quedan fuera:
- **2, nombres y año:** el nombre de quien habla ya lo tiene `primer-contacto`;
  los de los demás y el año son contenido → B 6.2 y B 6.3;
- **8, redes:** ya se preguntan en `primer-contacto` (enlaces).

Las que añado: **A 4.4** (decide Básico o Plus) y **A 4.5** (plazo). Menchu
tenía la fecha como opcional del primer contacto; aquí es obligatoria, pero
**no se pregunta si ya la dio**.

---

## Tanda B · al aceptar el presupuesto

| ID | Pregunta | ★ | Para qué | Destino |
|---|---|---|---|---|
| B 6.1 | Titular, forma jurídica (autónomo, S.L., C.B.…), NIF y domicilio fiscal | ★ | Contrato, factura y aviso legal (LSSI) | PRIVADO |
| B 6.2 | Vuestros nombres, y si queréis que salgan en la web | ★ | Textos | CONT, PRIVADO |
| B 6.3 | La historia: desde qué año existe; cómo empezó; desde cuándo lo lleváis vosotros; si siempre ha estado en el mismo sitio; quién más trabaja; qué os define; quién viene. **Y lo que pide Chema:** de dónde viene el nombre del negocio, y si una frase de las reseñas es vuestra (por ejemplo, «listo para triunfar») | | Textos. **Mejor en audios de WhatsApp** (Menchu los transcribe en local, A-008). Preguntas sobre personas, **en presente** | CONT |
| B 6.4 | Cada servicio: una línea de descripción y el precio, si queréis publicarlo | ★ | Sección de servicios | CONT |
| B 6.5 | Formas de pago | | Información práctica | CONT |
| B 6.6 | Permiso para mostrar vuestras opiniones de Google | | Contenido. **Pendiente de A-010** (¿basta el permiso del negocio o hace falta el del autor?). Diga lo que diga, igual que en el expediente (R31) | CONT |
| B 6.7 | Fotos: la lista de Lola, **con la fachada con el rótulo** y los tamaños. Personas, solo con permiso por escrito; niños, con el de sus padres. Si no hay permiso, no salen (tampoco de espaldas) | ★ | Contenido | CONT, DIS, PRIVADO |
| B 6.8 | Logotipo en archivo, si lo tienen | | Diseño | DIS |
| B 6.9 | ¿Hay colores que queráis, o que no queráis ver? (una línea) | | Diseño. Sin «webs que os gustan» (choque 6) | DIS |
| B 6.10 | El dominio elegido | ★ | Registro, a nombre del cliente (A-011) | REQ |
| B 6.11 | El número de WhatsApp para clientes y el correo al que llegan los mensajes del formulario | ★ | El botón y el formulario van siempre (§6.1); falta saber adónde | REQ, PRIVADO |
| B 6.12 | Accesos a la ficha de Google y al dominio, con usuario propio o acceso delegado | ★ | **Nunca contraseñas** (§12) | REQ |
| B 6.13 | ¿Algo que deba saber quien viene? (aparcamiento, acceso en silla de ruedas, cómo llegar) | | Textos y ficha de Google | CONT |

La aprobación de los textos **no es una pregunta**: es la fase de textos
(§13.5, paso 4), con sus 2 rondas.

### Bloques según el tipo de web

| Si en la tanda A… | Bloque | Qué se pregunta |
|---|---|---|
| A 4.6: el cliente elige día y hora | Reservas | Qué servicios se reservan y cuánto dura cada uno, quién atiende, antelación, cancelaciones, cómo se entera el negocio |
| A 4.3: con idioma | Idiomas | Qué partes se traducen, quién traduce y quién lo revisa |
| A 4.7: currículums | Empleo | Qué puestos, cómo quieren recibirlos, cuánto tiempo se guardan (A-010) |

Vender por internet **no tiene bloque**: está fuera de catálogo y lo decide Iván.

---

## Bloques de sector

Cambian **los ejemplos** de A 3.3 y la lista de fotos de B 6.7. El resto es
igual para todos. **Solo hay bloque de los sectores en los que ya hemos
trabajado**: con el primer cliente de un sector nuevo se usa el genérico y, al
terminar, se escribe el suyo con lo que de verdad contestó. No se inventan
opciones.

### Peluquería / barbería (caso Hermanos Cotillas, ronda 1)

- **A 3.3, ejemplos:** corte de caballero, de niño, barba, afeitado a navaja,
  degradado, corte de señora, color.
- **B 6.3, «qué os define» (para marcar):** negocio familiar de toda la vida ·
  cortes clásicos · niños · trato de confianza · puntualidad · asesoramos al
  cliente · barba.
- **B 6.7, fotos:** fachada con el rótulo (de día) · interior entero · el
  equipo junto · cada uno trabajando · cortes terminados (solo con permiso
  escrito del cliente) · detalles del oficio · fotos antiguas del negocio.

### Genérico

- **A 3.3:** «Contadnos qué hacéis o qué vendéis, como os salga».
- **B 6.3:** «Contadnos en una línea qué os hace distintos».
- **B 6.7:** fachada con el rótulo, interior, equipo y trabajo terminado o producto.

---

## Versiones

| Versión | Fecha | Qué cambia |
|---|---|---|
| v0.2 | 2026-11-17 | Primer catálogo con ID, B1 y B2 |
| v0.3 | 2026-11-18 | B1 y B2 pasan a llamarse tanda A y tanda B. Tanda A cerrada: 8 obligatorias, 9 condicionales y 1 opcional. Sale lo que ya recoge `primer-contacto` y lo que no cambia el precio |
| v0.3.1 | 2026-11-18 | Notas de Menchu: A 4.1 con una sola opción de cita (7 opciones) y A 4.6 como única que decide el plan; A 5.7 se parte en A 5.7 y A 5.8 (10 condicionales); A 3.4 no para la conversación; `DATO` solo para datos del negocio; condiciones por nombre de opción |
