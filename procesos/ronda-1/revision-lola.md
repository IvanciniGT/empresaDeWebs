# Revisión de Lola · ronda 1

> E-004 · 2026-11-17 · Caso simulado: Peluquería Hermanos Cotillas.
> He revisado la guía de estilos previa (PDF y generador), el informe (PDF,
> HTML e `informe.css`) y el cuestionario (Word convertido a PDF con LibreOffice,
> y `docx_util.py`). No he modificado nada que no sea mío. Las pruebas están en
> mi carpeta de sesión, no en el repositorio; abajo van los comandos para
> repetirlas.

## Respuesta corta a tus seis dudas

| # | Duda | Respuesta |
|---|---|---|
| 1 | ¿Guía previa sin ver el local? | **Sí, pero como hipótesis declarada** y más pequeña: concepto, paleta, tipos, esquema de la primera pantalla y lista de fotos. Cuando lleguen sus fotos, se sacan los colores reales y mandan ellos (skill, «De previa a definitiva»). |
| 2 | ¿Cuánto detalle? | **Sobra el logotipo, el tono y el boceto con aspecto de terminado. Falta la lista de fotos y los contrastes de lo que no es texto.** De 7 páginas a 3–4. |
| 3 | ¿Iconos a mano o Lucide? | **Lucide (ISC).** Dos de los dibujados se leen mal: la «Navaja» parece un lápiz y «Niños» es una persona cualquiera. |
| 4 | Fuentes | Fraunces e Inter están bien elegidas. Pero **en el PDF salen como Type 3** y dependen de que Google responda en 5 s. Propongo archivos locales. El informe usa **Avenir Next** (de macOS), con licencia dudosa para mandarla fuera. |
| 5 | ¿Plantilla de empresa? | **Sí, ya, aunque sea provisional.** Propongo la skill [`estilo-documentos`](../skills-borrador/estilo-documentos/SKILL.md). |
| 6 | ¿Se leen bien? ¿Y en el móvil? | En pantalla grande, sí. **En el móvil, no:** el informe en A4 queda a unos 7 px de letra. El Word está en inglés (lo subraya todo) y su código de colores no se ve. |

## 1. Lo que mantendría

- **HTML + CSS → PDF con Chrome.** Da control del diseño, Chrome ya está
  instalado y el PDF sale **etiquetado** (`pdfinfo`: «Tagged: yes»), que es la
  base de un PDF accesible.
- **El concepto «Oficio de familia».** Sale de las reseñas, que es una fuente
  real, y es lo que no puede copiar la competencia.
- **La paleta tinta, papel y cobre de la guía.** He recalculado sus 9 pares de
  texto y todos pasan AA. El más justo es Cobre sobre Papel, con 4,73 : 1.
- **Fuentes con licencia libre y alojadas en nuestro servidor en la web**, y la
  nota a Paco con el porqué (RGPD).
- **Fotografía: fotos reales, nada de banco de imágenes.** Y «las fotos
  antiguas son oro».
- **El sello INTERNO en cada sección**, y no fijo. Está bien resuelto el
  problema de Chrome con los elementos fijos.
- **Informe:** las fichas de competidores con etiquetas, los pies de figura
  que explican, el recuadro «Lo que no os vamos a prometer» y la página «Cómo
  hemos hecho este informe».
- **Cuestionario:** los tres tipos de bloque (lo que sabemos, para escribir,
  nuestra propuesta), las casillas de Word de verdad, las filas que no se
  parten y la cabecera de tabla que se repite en cada página.

## 2. Lo que cambiaría

### Guía de estilos previa

- [bloquea] **El boceto móvil incumple la regla de los tres segundos y su acción principal es un canal sin comprobar.** · En la primera pantalla no están ni el horario ni el «cómo llegar». El botón principal es «Pedir cita por WhatsApp», y no sabemos si tienen WhatsApp (expediente §2; Reme lo pregunta en 2.3). · Acción principal: **Llamar**, que es el dato comprobado. Horario de hoy y «Cómo llegar» a un toque. WhatsApp, solo cuando lo confirmen (skill, reglas 3 y 4).
- [bloquea] **Contenido inventado en la guía** (§10.3). · Varios ejemplos: «Arreglo de barba» como servicio (solo están comprobados los cortes de caballero y de niño); «nuestros padres, que abrieron esta peluquería en la calle Octavio Cuartero»; «el estilo barbería hipster… es el de la competencia nueva», que es la misma idea que ya quitaste del informe («han abierto muchas barberías nuevas»). Las maquetas acaban reutilizándose y lo inventado se cuela. · En las maquetas, etiquetas de función (`[Servicio 1 · a confirmar]`) y solo datos del expediente §1 (regla 2).
- [importante] **El contraste solo se comprueba en el texto.** · Falta lo que no es texto, que pide WCAG 1.4.11: el borde del botón secundario, el foco, los iconos y los campos. El texto del marcador de foto (Piedra sobre el rayado `#D9CBB8`) da 3,65 : 1, a 8 pt, y **no pasa**. · [`contraste.py`](../skills-borrador/guia-estilos-previa/contraste.py) con pares de texto y de no texto.
- [importante] **La tabla de tamaños se queda corta.** · Falta el interlineado, el ancho máximo de línea, el tamaño mínimo de notas y el de las áreas de toque, y cómo se ven el foco y los enlaces. · Ya está en la skill (regla 7): ≥ 16 px, 1,5 de interlineado, 60–75 caracteres por línea y botones de 44 × 44 px.
- [importante] **Logotipo provisional, fuera.** · Crea la expectativa de algo que no incluimos (§6.1), y aún no sabemos si tienen logotipo o rótulo (Reme, 5.3). · Se decide al contratar.
- [importante] **El tono y las frases de ejemplo son textos, y los textos son de Chema.** · «Le cortamos el pelo a tu padre. Ahora, a ti.» funciona como titular, pero no me toca a mí escribirlo, y en la guía acaba pareciendo aprobado. · La guía marca dónde va cada texto y cuánto cabe. El tono, en la skill de Chema.
- [importante] **Iconos dibujados a mano.** · «Navaja» se lee como un lápiz, «Niños» es una persona genérica y cada icono nuevo hay que dibujarlo. · Lucide (ISC), con la lista de los que hacen falta.
- [importante] **Fuentes Type 3 en el PDF y descargadas de Google al generar** (`pdffonts`). · El texto se extrae peor, y si Google tarda, Chrome pone otra fuente sin avisar (`--virtual-time-budget=5000`). · Archivos estáticos locales (§7).
- [menor] **Siete páginas, cinco medio vacías**, por un salto forzado en cada sección, y una portada a página completa en un documento interno. · 3–4 páginas, sin saltos forzados.
- [menor] **«Opiniones de Google, tal cual» en la estructura.** · El expediente dice que no se publican sin permiso, y Reme lo deja en B2 (6.6), pendiente de la duda legal. · «Opiniones (si dan permiso)».
- [menor] **Fotos: «clientes solo con permiso; si no, de espaldas».** · Hay que alinearlo con Menchu: ni caras de clientes ni de niños sin un consentimiento por escrito. · Ya está en la skill (regla 10).

### Informe (aspecto; el contenido es de Chema y Puri)

- [importante] **No se lee en el móvil**, que es donde lo abrirá el cliente. · En A4 y a 10,5 pt, ajustado al ancho de un móvil (390 px), la letra queda a unos 7 px. Las capturas, todavía menos. · **A5 vertical, una columna y 11,5 pt.** Lo he probado con el mismo HTML: el texto se lee sin ampliar. Pero el documento pasa de 9 a 19 páginas, porque está pensado para A4. Hay que **maquetarlo para A5, no encogerlo** ([`estilo-documentos`](../skills-borrador/estilo-documentos/SKILL.md), «Formato»).
- [importante] **Cinco de nueve páginas, medio vacías** (2, 4, 6, 8 y 9). · Hay un salto forzado por sección, y la portada y «En 30 segundos» ocupan dos páginas para muy poco texto. · Sin saltos forzados. Portada y resumen en **una sola primera página que funcione sola**: título, tres cifras y la conclusión. Eso es también lo que Menchu pide para WhatsApp.
- [importante] **Termina en la metodología, sin contacto.** · Lo último que lee el cliente son los límites del estudio. · La metodología pasa a anexo. La última página: el siguiente paso y cómo contactarnos.
- [importante] **No lleva número de página ni pie.** · Si Menchu le dice «mira la página 4», el cliente no la encuentra. · Pie con el nombre corto del documento y «página X de Y».
- [importante] **Capturas ilegibles.** · Las de la página 3 miden 1200–1366 px de ancho y se imprimen en columnas de unos 84 mm: su texto queda a unos 2,5–3 pt. La de Treatwell sale cortada por la derecha. · Recortarlas a la zona que importa, a todo el ancho, con un recuadro sobre lo que se comenta.
- [importante] **Las cinco imágenes van sin texto alternativo** (`<img>` sin `alt`). · Exigimos texto alternativo en las webs (§11). Nuestros documentos tienen que dar ejemplo, y el PDF ya está etiquetado, solo le falta esto. · `alt` en todas.
- [importante] **El mapa no se distingue.** · El rojo (vosotros) y el naranja (barberías) se confunden con daltonismo. Los puntos son diminutos y la leyenda solo está en el pie. · El cliente, con un marcador grande y la etiqueta «Vosotros». Las barberías, con otra forma. La leyenda, dentro del mapa (`mapa.py`, Paco).
- [importante] **Un contraste por debajo de AA, y dos al límite.** · La etiqueta verde («Reserva online»…, a 8 pt) da 4,38 : 1: **no pasa**. El naranja de las cifras sobre gris (4,36) pasa solo porque va a 24 pt, que cuenta como texto grande. El gris sobre melocotón (4,35) no se usa hoy, pero bastaría con poner una nota en la caja de conclusión para que fallara. · La paleta corregida de `estilo-documentos`: todos los pares pasan de 4,5 en cualquier tamaño, y no hay que vigilar dónde se usa cada color.
- [menor] **Semáforo de puntos de color.** · Como lleva texto al lado, no incumple WCAG. Pero el punto amarillo da 2,95 : 1 sobre blanco y, con daltonismo, no se distingue del verde: decora sin informar. · Símbolo, palabra y color: ✓, ! y ✗.
- [importante] **Avenir Next.** · Es una fuente que viene con macOS. No sé si su licencia permite incrustarla en documentos que mandamos fuera (§10.3: nada sin licencia), y en otra máquina saldría otra fuente. · Inter (OFL), en archivo local.
- [menor] **Portada:** el degradado acaba en una mancha marrón abajo a la derecha, y se ve «[Nombre de nuestra empresa]». · Color liso y la cabecera común.
- [menor] **El ★ sale de una fuente china de relleno** (PingFang, según `pdffonts`). · SVG, o una fuente que tenga el carácter.

### Cuestionario (aspecto; las preguntas son de Reme)

- [importante] **Está en inglés.** · Los estilos y el valor por defecto del documento dicen `en-US`. Word subrayará en rojo cada palabra al abrirlo, y el cliente creerá que está lleno de faltas. · `es-ES` en los estilos **y** en `docDefaults`. Lo he probado: con los estilos solos, el valor por defecto se queda en inglés.
- [importante] **El código de colores no se ve.** · Los fondos dan entre 1,09 y 1,12 : 1 frente al blanco, y los bordes, 1,45–1,58. No se distinguen en un móvil ni impresos en blanco y negro. Es lo que también vio Menchu. · **Etiqueta en mayúsculas y barra izquierda gruesa** del color (≥ 5,6 : 1) sobre el fondo pálido. Prototipo probado, ver §7. Esto contesta lo que Menchu me pedía junto con Reme.
- [importante] **Una sola casilla «¿Correcto?».** · Si no está marcada, no se sabe si es «no» o «no lo he mirado». · «Está bien» / «Hay algo mal» y el hueco debajo.
- [importante] **Tablas de 3 y 4 columnas con anchos fijos** (servicios, fotos, redes). · En el móvil obligan a moverse en horizontal o a ampliar. · Una columna: la pregunta arriba y la respuesta debajo, a todo el ancho.
- [importante] **Preguntas sin número a la vista.** · Reme ya les ha puesto ID en su catálogo (1.4, 3.5…), pero el documento no los muestra. · Mostrarlos, y decir al principio: «si preferís, contestad por WhatsApp o por teléfono con el número de la pregunta». Así sirve también a quien no puede rellenar un Word en el móvil.
- [importante] **Cómo devolverlo y cuánto se tarda va al final.** · El cliente decide al principio si se pone o no. · En la primera página: los minutos que lleva, las tres formas de contestar y que lo que no sepa lo deje en blanco.
- [menor] **Portada con un mapa a página completa.** · En el móvil, la primera pantalla es un mapa que no le dice nada nuevo. · Título, para qué es y cómo contestar; sin mapa.
- [menor] **Las casillas de las tablas quedan una línea por debajo del texto** (visto en LibreOffice). · Alinearlas o sacarlas de la tabla.
- [menor] **Emojis como señal** (✍️ ⚠️ 🔒) y ★ en los títulos. · Cambian según el aparato. · Etiquetas de texto.
- [menor] **Calibri.** · No está en este Mac (LibreOffice la cambia por Carlito) ni en los móviles. · Arial.
- [menor] **El mapa del Word no tiene descripción** (texto alternativo). · Ponérsela o quitar el mapa.

## 3. Lo que falta

1. **Una identidad común para nuestros documentos.** Propuesta en
   [`estilo-documentos`](../skills-borrador/estilo-documentos/SKILL.md):
   paleta comprobada, Inter en PDF y Arial en Word, componentes, formato A5 y
   lista de comprobación.
2. **Comprobar en el móvil antes de Puri,** como paso fijo:
   `pdftoppm -scale-to-x 390` y leer sin ampliar.
3. **La primera página del informe como pieza de WhatsApp** (lo pide Menchu).
   El diseño es mío y el texto, de Chema.
4. **El paso de previa a definitiva** cuando llegan las fotos. Ya está en la skill.
5. **La lista de fotos con tamaños**, para Menchu y para la pregunta 6.7 de Reme.
   Ya está en la skill.
6. **Un sitio para recursos con licencia** (fuentes, iconos), con su licencia al lado.
7. **Una plantilla de la guía:** el diseño fijo y los datos de cada cliente
   aparte. Hoy cada cliente copiaría 300 líneas de Python con el HTML dentro.

## 4. Mis skills: qué he cambiado y por qué

**[`guia-estilos-previa`](../skills-borrador/guia-estilos-previa/SKILL.md) → v0.2**

- **Propósito explícito:** es una hipótesis para presupuestar, pedir material
  y ganar días, no el diseño.
- **Qué entra y qué no:** fuera el logotipo, el tono y los textos, y el boceto
  con aspecto de terminado. Dentro la lista de fotos con tamaños, los riesgos y
  las preguntas. De 7 páginas a 3–4.
- **Reglas nuevas:**
  - nada sin comprobar en una maqueta;
  - la acción principal es un canal comprobado;
  - los tres segundos (teléfono, horario de hoy, cómo llegar);
  - contraste también en lo que no es texto;
  - tamaños mínimos, incluidas las áreas de toque;
  - no depender del color;
  - fotos de personas, solo con consentimiento.
- **Paso nuevo «De previa a definitiva»:** colores sacados de las fotos,
  «variante accesible» si el color del cliente no da contraste, registro de
  cambios y lo que necesita Paco.
- **Lista de comprobación** antes de entregar.
- **Herramienta [`contraste.py`](../skills-borrador/guia-estilos-previa/contraste.py):**
  sin dependencias, con veredicto para texto, texto grande y no texto, y
  `--minimo` para que falle si un par no llega. La he comprobado con valores
  conocidos: negro sobre blanco da 21; `#767676` sobre blanco, 4,54 (pasa);
  `#777777`, 4,47 (no pasa); y el código de salida es 1 cuando debe. Trunca en
  vez de redondear, para que un 4,496 no se muestre como «4,5» y parezca que
  pasa.

**[`estilo-documentos`](../skills-borrador/estilo-documentos/SKILL.md) → v0.1, nueva.**
Sí, quiero esta skill. El aspecto de lo que mandamos es diseño, y hoy no tiene
dueño. Reme ya me apunta como responsable de la maquetación del cuestionario.

## 5. Lo que necesito de otros agentes (lo coordina Federico)

**Paco** (herramientas comunes):

1. **Fuentes en archivo:** Inter, y Fraunces para la guía, estáticas y con su
   `OFL.txt`, en `herramientas/fuentes/`, con `@font-face` en `informe.css`.
2. **`informe.css`:**
   - la paleta de `estilo-documentos`;
   - formato A5;
   - sin `.pagina` forzada (`break-after: avoid` en los títulos);
   - pie con «página X de Y» (¿cajas de margen de `@page` en Chrome?);
   - componentes de semáforo con símbolo y de captura recortada;
   - quitar Avenir Next.
3. **`docx_util.py`:**
   - `es-ES` en los estilos y en `docDefaults`;
   - Arial a 11 pt;
   - bloques con etiqueta y barra izquierda (el prototipo está en el §7 y se
     puede copiar);
   - una pieza `pregunta(numero, texto, ayuda)` con la respuesta debajo;
   - «Está bien / Hay algo mal» en lugar de la casilla sola;
   - casillas alineadas;
   - descripción en `imagen()`;
   - el acento `#9C4A14`.
4. **`mapa.py`:** el cliente con un marcador grande y la etiqueta «Vosotros»,
   las barberías con otra forma y la leyenda dentro del mapa.
5. **Lucide** (ISC) en `herramientas/iconos/`, con su licencia.
6. **Plantilla de la guía previa** (HTML con los datos aparte), o dime si
   prefieres que la plantilla viva en mi skill.

**Chema:**

- La frase principal, de unos 40–45 caracteres, para que quepa en tres líneas
  en el móvil (a comprobar con el texto real).
- El tono de comunicación pasa a su skill; lo saco de la mía.
- El contenido del informe para A5: más corto y con capturas recortadas.
- El texto de la primera página, que tiene que funcionar sola.

**Reme:**

- Mostrar los ID de las preguntas en el documento, una sola columna y
  «Está bien / Hay algo mal».
- Sobre su **6.9 («solo si Lola lo necesita»):** las webs que les gustan no me
  hacen falta. Me basta con una línea: «¿Hay colores que queráis, o que no
  queráis ver?». Lo que de verdad necesito es la **foto de la fachada con el
  rótulo**, dentro de la lista de fotos de la 6.7.
- La **maquetación de B1** la hago yo con `estilo-documentos` cuando cierre
  las preguntas.

**Menchu** (contesta a lo que me pedía):

1. **Tamaño de las fotos**, medido en píxeles del lado largo:
   - **2000 px** para la foto principal, horizontal y con aire alrededor;
   - **1200 px** para las de secciones y galería;
   - **1000 px** para los retratos.

   **No sé todavía si la opción HD de WhatsApp llega a 2000 px, ni a cuánto
   llega la normal**, y no lo voy a suponer. Propongo medirlo (§7). Mientras,
   la foto principal se pide por correo o como documento, y el resto por
   WhatsApp con HD. Con esto ya puede escribir su miniguía.
2. **Código de colores:** propuesta en §2, con el prototipo en §7.

**Puri:** añadir a su lista de comprobación:

- la lectura en el móvil (`pdftoppm -scale-to-x 390`);
- `contraste.py` con los colores del documento;
- `alt` en todas las imágenes;
- el idioma del Word;
- que ninguna maqueta lleve datos sin comprobar.

**Aviso:** junto al cuestionario hay un fichero de bloqueo de Word,
`entregables/~$estionario - …docx`. Alguien lo tiene abierto en Word. Antes de
regenerarlo conviene cerrarlo, y ese fichero no debe entrar en git.

## 6. Lo que tiene que decidir Iván (lo lleva Federico)

1. **¿Identidad provisional común para nuestros documentos ya, o esperamos al nombre?**
   - Propuesta: ya. Cuando llegue el nombre, solo cambia la cabecera.
   - Alternativa: seguir como ahora, con un estilo por documento.
2. **¿Informe en A5, pensado para leerse en el móvil, en lugar de A4?**
   - Propuesta: A5.
   - Alternativa: A4 con letra de 12 pt, que se lee algo mejor pero sigue
     obligando a ampliar.
3. **Alcance de la guía previa:** 3–4 páginas, sin logotipo ni boceto con
   aspecto de terminado. ¿De acuerdo?
4. **Fotos de personas:** ya lo eleva Menchu (modelo de consentimiento).
   Afecta a mi lista de fotos.

## 7. Herramientas: qué necesito o propongo

| Qué | Para qué | Coste | Estado |
|---|---|---|---|
| [`contraste.py`](../skills-borrador/guia-estilos-previa/contraste.py) | Contraste WCAG de texto y no texto | 0 € | **Hecho y probado**, en mi skill |
| Fuentes Inter y Fraunces estáticas (SIL OFL) | PDF sin Type 3 y sin depender de Google; las mismas en la web | 0 € | Hay que descargarlas: necesita el visto bueno de Iván. Lo hace Paco |
| Iconos Lucide (ISC) | Un juego completo y coherente | 0 € | Igual que las fuentes |
| Medir lo que llega por WhatsApp | Saber si la opción HD basta para la foto principal | 0 € | Que Iván se mande una foto en normal y otra en HD y las mida con `sips -g pixelWidth -g pixelHeight` (ya está en macOS) |
| Probar el Word en un móvil | Saber si se puede rellenar y si funcionan las casillas | 0 € | Necesito que Iván lo abra en su móvil: desde el correo, desde WhatsApp y en la app de Word si la tiene |
| Mapillary (fotos de calle abiertas) | Ver la fachada antes de contratar, solo para mirar | 0 € (pide una clave gratuita) | **Duda:** no he comprobado la licencia exacta, si hay fotos de esa calle ni si permite el uso automático |

**Pruebas que he hecho**, todas en mi carpeta de sesión, sin tocar el repositorio:

1. PDF a imágenes, página a página, para revisarlos:
   `pdftoppm -r 60 -png <pdf> <prefijo>`.
2. Fuentes incrustadas: `pdffonts`. Así salen el Type 3 de la guía, Avenir
   Next en el informe y PingFang como relleno.
3. Word a PDF con LibreOffice, sin ventana y con perfil aparte:
   `soffice -env:UserInstallation=file://<carpeta> --headless --convert-to pdf`.
4. **Lectura en el móvil:**
   `pdftoppm -f 3 -l 3 -scale-to-x 390 -scale-to-y -1 -png <pdf> movil`.
   Hecho con el informe en A4 y con una copia de su HTML en A5 a 11,5 pt.
5. **Prototipo de bloques del cuestionario** con `docx_util.py` y python-docx,
   pasado por LibreOffice:
   - pregunta numerada;
   - bloques «LO QUE HEMOS ENCONTRADO», «ESCRIBID AQUÍ» y «NUESTRA PROPUESTA»
     con barra de 4,5 pt;
   - Arial a 11 pt y `es-ES`.

   Se distinguen a ancho de móvil y en blanco y negro. Si Paco lo quiere, se lo
   paso a través de Federico.

Nota: la ruta de `timeout` que dicen las instrucciones de la máquina
(`/usr/local/opt/coreutils/libexec/gnubin/timeout`) no existe. Que Paco lo
compruebe si algún script la usa.

## 8. Ronda 1b

> E-010 · 2026-11-18. Con A-005 (informe de 2 páginas más anexo, en A5), A-006
> (estilo común y guía de 3–4 páginas), A-003 (WhatsApp primero), A-013
> (repositorio público) y los choques 2, 3 y 4 de la consolidación.

### Lo que he cambiado

**[`estilo-documentos`](../skills-borrador/estilo-documentos/SKILL.md) → v0.3, completo**

- **Qué cubre:**
  - el informe en A5;
  - la imagen de su página 1 para WhatsApp (PNG de 1080 px);
  - la tanda A y la B en Word, A4 en una columna: es la copia «para el
    ordenador», porque en el móvil se contesta por el chat;
  - los documentos internos.
- **Paleta:**
  - he añadido `atencion-suave`;
  - todos los pares que se usan, comprobados con `contraste.py`: pasan de
    4,5 : 1, así que no hay que vigilar dónde va cada color;
  - los nombres son iguales en CSS y en Python.
- **Tipografía:**
  - Inter estática en el PDF y Arial en el Word, con el porqué para la R62 de
    Puri: lo común es la paleta, los componentes y la estructura; un Word no
    puede contar con Inter y no incrusta nada;
  - he subido el texto del A5 a 12 pt.
- **Informe:**
  - el plan de cada página, según el contenido de Chema;
  - saltos de página **solo** al empezar la página 2 y el anexo;
  - si algo no cabe, se recorta el texto y nunca la letra;
  - «página X de Y» en el pie, con las cajas de margen de `@page`, probado.
- **Word:**
  - piezas con nombre y uso;
  - ID de Reme a la vista («A 3.5») y opciones numeradas, para contestar por
    WhatsApp con «A 3.5: 2 y 3»;
  - «imprescindible» con palabras, sin ★;
  - la versión del estilo en las propiedades del documento, no en el pie;
  - la leyenda, solo con los recuadros que salen.
- **Mapa** para `mapa.py`:
  - «Vosotros» marcado;
  - formas distintas por tipo;
  - la leyenda dentro;
  - etiquetas de 27 px como mínimo a 1100 px para el A5. Las de hoy, a 18 px,
    quedarían a unos 6 pt.
- **Lista para Paco** y comprobaciones con comandos.

**Prototipos** en [`estilo-documentos/prototipo/`](../skills-borrador/estilo-documentos/prototipo/), con datos ficticios:

| Fichero | Qué es | Comprobado |
|---|---|---|
| [`estilo.css`](../skills-borrador/estilo-documentos/prototipo/estilo.css) | El CSS común: fuentes, paleta, A5, pie y componentes | Con `html_a_pdf.mjs --estricto`: sin avisos |
| [`muestra-informe.html`](../skills-borrador/estilo-documentos/prototipo/muestra-informe.html) | Página 1, página 2 y anexo con todos los componentes | 3 páginas A5, etiquetado, **solo Inter incrustada como TrueType (sin Type 3)**. Se lee a 390 px sin ampliar. La página 1 como PNG: 1080 × 1530 y 130 KB |
| [`bloques_docx.py`](../skills-borrador/estilo-documentos/prototipo/bloques_docx.py) | Las piezas del Word sobre `docx_util` (el prototipo que pidió Paco) | Pasa `revisar_docx.py`. `w:tag` en cada opción (`A 3.5.1`…), `es-ES` y `cp:version`. Visto en LibreOffice: 2 páginas, una columna |

**[`guia-estilos-previa`](../skills-borrador/guia-estilos-previa/SKILL.md) → v0.3**

- **Plantilla dentro de la skill**, como prefería Paco. El diseño fijo está en
  [`generar_guia.py`](../skills-borrador/guia-estilos-previa/generar_guia.py) y
  los datos de cada cliente van en un JSON
  ([ejemplo ficticio](../skills-borrador/guia-estilos-previa/ejemplo/datos-ejemplo.json)).
  Sale en **3 páginas A4** con el estilo común, Fraunces e Inter de
  `herramientas/fuentes/`, y Lucide.
- **Las reglas, en el código:**
  - calcula el contraste de cada papel del color: 7 pares de texto y 2 de no
    texto;
  - **no saca la guía** si alguno no llega, ni si la acción principal no es un
    canal comprobado.

  Lo he probado: con un gris claro se niega por 2 pares, y con «Pedir cita por
  WhatsApp» sin comprobar, también. Si quito la comprobación, la guía sale: la
  prueba detecta que falta.
- **El tono pasa a Chema** (`textos-web`). La guía solo marca dónde va cada texto y cuánto cabe.
- **Foto de la fachada (A 5.6, choque 3):** un paso nuevo, «previa con
  fachada», que usa
  [`colores_foto.py`](../skills-borrador/guia-estilos-previa/colores_foto.py)
  para sacar los colores reales. Es el cuentagotas sin ventanas: colores
  dominantes de una zona de la foto, con su contraste.

  Al probarlo encontré un fallo: el método de la mediana devolvía colores que
  no estaban en la imagen. Con 70 % marrón y 30 % blanco, sacaba un marrón
  claro. Lo he arreglado con k-medias y lo he comprobado con dos imágenes de
  colores conocidos: ahora salen exactos, y sin el arreglo la prueba falla.
- **Fotos:** la lista y los tamaños pasan a la tanda B. La de la fachada de la
  A 5.6 vale aunque sea pequeña, porque en la previa solo se mira.

### Lo que hay que decidir (lo lleva Federico)

- **🔴 `interno/` entra en git y el repositorio es público (A-013).** Hoy están
  publicados:
  - la guía previa del caso de ejemplo, en PDF;
  - `previo-precio.md`, con nuestra estimación de precio.

  Cualquiera, el propio cliente incluido, puede descargar el diseño que «no le
  regalamos» y el precio que le pensamos pedir.
  - Propuesta: añadir `clientes/*/interno/` a `.gitignore` y sacar del índice
    lo que ya está. El `.gitignore` es de Federico o de Paco, no mío.
  - Con un cliente real, además, el generador de cada cliente también es
    público. Por eso la plantilla va en mi skill y los datos en un JSON aparte.
  - Mientras tanto, mi skill pone el JSON y el PDF en
    `clientes/<negocio>/privado/guia/`, que ya está fuera de git.

### Lo que necesito de otros (por Federico)

- **Paco:** llevar `estilo-documentos` a `herramientas/`, siguiendo la sección
  «Para Paco» de la skill:
  - `estilo.css`;
  - las piezas del Word;
  - `mapa.py`;
  - los iconos leídos de `herramientas/iconos/`.

  El formato del `w:tag`, a cerrar con Reme para `leer_cuestionario.py`.
  También, decidir si `contraste.py` o `colores_foto.py` pasan a `herramientas/`
  (choque 4).
- **Chema:**
  - escribir el informe para que cada parte quepa en su página A5;
  - la frase principal, de 40–45 caracteres;
  - el `alt` de cada captura y dónde va el recuadro (en %).
- **Reme:**
  - que la leyenda del Word solo explique los recuadros que salen;
  - que el ID de cada pregunta lleve el prefijo de la tanda («A 3.5»), como en
    su catálogo.
- **Puri:** añadir a su lista:
  - `html_a_pdf.mjs --estricto`;
  - `pdffonts`: solo Inter, o Fraunces e Inter en la guía;
  - que cada parte del informe quepa en su página;
  - que no quede ningún «[Nombre de…]»;
  - que el generador de la guía haya terminado sin negarse.
- **Iván:** medir lo que llega por WhatsApp, normal y HD
  (`sips -g pixelWidth -g pixelHeight`), y probar el Word (A-007).

### Pruebas, sin tocar nada que no sea mío

Todo lo generado ha ido a `/tmp`. Ningún dato real ni personal en el
repositorio, porque las muestras son ficticias.

**Comandos:**
- `html_a_pdf.mjs --estricto`
- `pdfinfo`, `pdffonts` y `pdftoppm` (página a página, a 390 px y a 1080 px)
- `revisar_docx.py`
- `soffice --headless --convert-to pdf`

**Pruebas con resultado conocido:**
- `contraste.py`: valores de referencia;
- `generar_guia.py`: dos negativas, y una mutación que quita la comprobación;
- `colores_foto.py`: dos imágenes sintéticas, y una mutación que quita el
  arreglo.
