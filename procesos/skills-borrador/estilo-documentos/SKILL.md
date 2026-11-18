---
name: estilo-documentos
description: "Define y revisa el aspecto de todo lo que la empresa manda a los clientes: el informe de venta (PDF A5, 2 páginas más anexo), la imagen de su primera página para WhatsApp, la tanda A y la B en Word y los documentos internos. Paleta con contraste comprobado, tipografía, componentes con su nombre en CSS y en Python, lectura en el móvil y accesibilidad. Úsala al maquetar o revisar un documento para un cliente, y cuando Paco cambie las herramientas de documentos."
---

# estilo-documentos

> **BORRADOR v0.3 · Lola** · Dueña: Lola · Lo implementa Paco en `herramientas/`
> Aprobado por Iván: **A-006** (estilo común provisional) y **A-005** (informe
> de 2 páginas más un anexo, en A5). Historia: [revision-lola.md](../../ronda-1/revision-lola.md) §3, §4 y §8.

## Principio

**Nuestros documentos llevan nuestra identidad; la del cliente va en su web.**
Paleta, letra, componentes y estructura son los mismos en el informe, en el
Word y en lo que venga. Si un cliente recibe tres documentos, tienen que
parecer de la misma empresa.

Mientras no haya nombre (§15), la identidad es **provisional y neutra**:
- Nada de logotipo inventado.
- **Nada de «[Nombre de la empresa]» en un documento que sale:** si no hay
  nombre, la línea de marca se quita.
- Cuando llegue el nombre, solo cambia la cabecera.

## Qué cubre

| Documento | Formato | Canal | Prototipo |
|---|---|---|---|
| Informe de venta | **PDF A5 vertical**: página 1, página 2 y anexo | WhatsApp y copia por correo | [`muestra-informe.html`](prototipo/muestra-informe.html) |
| Primera página del informe como imagen | **PNG de 1080 px de ancho** | WhatsApp, antes del PDF | Se saca del PDF (abajo) |
| Tanda A en Word | **A4, una columna**. Es la copia «para el ordenador»: en el móvil, las preguntas van por el chat (A-003) | Correo | [`bloques_docx.py`](prototipo/bloques_docx.py) |
| Tanda B en Word | Igual que la A | Correo | Igual |
| Internos (guía previa, previo de precio) | El mismo estilo, con sello INTERNO. A4 o A5 | No salen | `.interno` en [`estilo.css`](prototipo/estilo.css) |

## Paleta

Los nombres son los mismos en CSS (`--acento`) y en Python (`ACENTO`).

| Nombre | Color | Uso |
|---|---|---|
| `tinta` | `#1E2A3A` | Texto, cabeceras de tabla (con texto blanco), barra de «Cómo contestar» |
| `acento` | `#9C4A14` | Títulos, cifras, números de pregunta, recuadro de captura, barra de «Escribid aquí» |
| `gris` | `#56606D` | Notas, pies, ayudas, número de opción; barra de «Lo que hemos encontrado» |
| `fondo` | `#F4F6F9` | Cajas, cifras, «Cómo contestar» |
| `acento-suave` | `#F6E3D3` | Caja de conclusión |
| `bien` / `bien-suave` | `#24693F` / `#E3F3E8` | Estado «Sí»; barra de «Nuestra propuesta» |
| `atencion` / `atencion-suave` | `#8A5A00` / `#FBF0D9` | Estado «A medias» |
| `mal` / `mal-suave` | `#B3261E` / `#FBE4E2` | Estado «No», «Importante», sello INTERNO |
| `linea` | `#D0D7DE` | Solo separadores, nunca información |
| Fondos de los recuadros del Word | `#EEF2F6` · `#FFF4E0` · `#EAF5EC` | Lo que hemos encontrado · Escribid aquí · Nuestra propuesta |

Cada par que se usa, comprobado con
[`contraste.py`](../guia-estilos-previa/contraste.py). Pasan de 4,5 : 1, así
que valen para texto de cualquier tamaño:

| Delante | Fondo | Contraste |
|---|---|---|
| tinta | blanco · fondo | 14,50 · 13,40 |
| blanco | tinta · acento | 14,50 · 6,17 |
| acento | blanco · fondo · acento-suave · `#FFF4E0` | 6,17 · 5,69 · 4,95 · 5,66 |
| gris | blanco · fondo · acento-suave · `#EEF2F6` · `#FFF4E0` | 6,38 · 5,89 · 5,12 · 5,67 · 5,85 |
| bien | bien-suave · `#EAF5EC` | 5,76 · 5,92 |
| atencion | blanco · atencion-suave | 5,92 · 5,24 |
| mal | blanco · mal-suave | 6,53 · 5,38 |

Si cambia un color, se repite la comprobación:
`contraste.py --minimo 4.5` con los pares de texto y `--minimo 3` con los de
no texto (barras, bordes, marcas del mapa).

## Tipografía

| Documento | Fuente | Por qué |
|---|---|---|
| PDF | **Inter** 4.1 (SIL OFL) 400, 400 cursiva, 600 y 700, **estáticas**, ya instaladas por Paco en `herramientas/fuentes/inter/` (`Inter-Regular.ttf`, `Inter-Italic.ttf`, `Inter-SemiBold.ttf`, `Inter-Bold.ttf`) | Se puede incrustar (OFL). Sale igual en cualquier máquina. Comprobado: la muestra sale solo con Inter, incrustada como TrueType (CID), sin Type 3. |
| Word | **Arial** | La tiene cualquier ordenador o móvil que abra un Word, y no hay que mandarla: el Word no incrusta nada. |

**Por qué no Inter también en el Word** (R62 de Puri). Lo común es la paleta,
los componentes y la estructura, no necesariamente la fuente:

- Un Word no puede contar con Inter en el aparato del cliente.
- Incrustarla en el `.docx` funciona en Word de escritorio, pero no sé si
  funciona en el móvil ni en el visor del correo, y lo hace más pesado.
- La duda de Puri era sobre la licencia de una fuente de Apple incrustada en un
  PDF. Con Arial en el Word no se incrusta nada; con Inter en el PDF, la
  licencia es libre.

**Fraunces** (OFL) no es nuestra: solo se usa en la guía previa, como propuesta
para la web del cliente.

### Tamaños

| | PDF A5 | Word A4 |
|---|---|---|
| Texto | 12 pt, interlineado 1,45 | 11 pt, interlineado 1,15 |
| Notas, pies, ayudas | 10 pt (pie de página: 8 pt) | 10 pt (pie: 9 pt) |
| Título de documento | 21 pt | 20 pt, acento |
| Título de sección | 15 pt, acento | 14 pt, acento |
| Subtítulo | 12,5 pt | 12 pt |
| Cifras | 24 pt, acento | — |
| Ancho de línea | ~60 caracteres (128 mm de caja) | ~90 caracteres |

Espaciado, en múltiplos de **4 mm** en el PDF.

## Informe de venta: A5, 2 páginas más el anexo (A-005)

Márgenes de 12 × 10 × 14 mm. El contenido es de Chema (`estudio-competencia`);
la colocación, mía.

| Página | Lleva, por este orden |
|---|---|
| **1 · Lo que ve hoy quien os busca** | Cabecera: marca, «Informe gratuito y sin compromiso» y la fecha; título; «Para \<negocio\> · \<dirección\>» · captura recortada con su recuadro y su pie · **tres cifras** en fila · caja de conclusión, de dos frases |
| **2 · Tres cosas que os están costando clientes · Lo que haríamos** | Tres hallazgos numerados, cada uno con su estado · «Lo que haríamos» con marcas · una cita literal como mucho · caja **Siguiente paso**, con el contacto |
| **Anexo · Cómo lo hemos hecho** | Etiqueta ANEXO · tabla de fuentes con fecha · límites · atribución de OSM · «Preparado con ayuda de asistentes de IA y revisado por Iván, el responsable» (A-004) |

Reglas:
1. **Saltos de página solo al empezar la página 2 y el anexo** (`.nueva-pagina`).
   Dentro de cada parte, nada de saltos forzados.
2. **Cada parte cabe en su página.** Si no cabe, se recorta el texto (lo hace
   Chema). Nunca se baja la letra ni se estrechan los márgenes. Comprobación:
   `pdfinfo` dice 3 páginas (o 2 más las del anexo).
3. **La página 1 se entiende sola.** Es la que se manda como imagen.
4. **La parte principal termina en «Siguiente paso»**, con el contacto. El
   anexo es lo último del PDF, pero no lo último que «se lee».
5. **Pie de página:** «Informe · \<negocio\>» a la izquierda y «página X de Y» a la
   derecha, con las cajas de margen de `@page`. Probado con Chrome 157 en
   `html_a_pdf.mjs`.

**Imagen para WhatsApp:**

```
pdftoppm -f 1 -l 1 -scale-to-x 1080 -scale-to-y -1 -png informe.pdf informe-pagina-1
```

Sale un PNG de 1080 × 1530 px y unos 130 KB con la muestra. Se ve entera en el
chat, sin abrir nada.

## Word: tanda A y tanda B

A4, márgenes de 2,2 cm y **una sola columna**: nada de tablas de 3 o 4
columnas para contestar.

| Pieza (en [`bloques_docx.py`](prototipo/bloques_docx.py)) | Cómo es |
|---|---|
| `documento(titulo, autor)` | Sobre el `nuevo_documento` de Paco: Arial 11, títulos en acento, `es-ES` |
| `como_contestar(doc, minutos, preguntas)` | **Primera página, antes de cualquier pregunta.** Cuántas son y los minutos; que se puede contestar por WhatsApp con «A 3.5: 2 y 3»; que lo que no se sepa se deja en blanco. Debajo, la leyenda **solo de los recuadros que salen** en ese documento |
| `bloque(doc, tipo, lineas, alto)` | Fondo pálido, **barra izquierda de 4,5 pt** y **etiqueta en mayúsculas**: CÓMO CONTESTAR, LO QUE HEMOS ENCONTRADO, ESCRIBID AQUÍ, NUESTRA PROPUESTA, IMPORTANTE. Se entiende impreso en blanco y negro |
| `pregunta(doc, id, texto, ayuda, imprescindible)` | El **ID del catálogo de Reme** a la vista («A 3.5») en acento, el texto en negrita y «· imprescindible» con palabras, nunca con ★. La ayuda, debajo y en gris |
| `opciones(doc, id, textos)` | Una casilla por línea, con su **número de opción** a la vista y un `w:tag` = `<id>.<n>` para leerla con un script |
| `validar_dato(doc, id, que, valor)` | Lo que hemos encontrado + «1 Está bien / 2 Hay algo mal» + hueco. **Nunca una casilla sola** |
| `estado(parrafo, tipo)` | «Sí», «A medias» o «No», en negrita y en su color. Sin símbolos, porque Arial no trae ✓ |
| `pie(doc, nombre)` | «\<documento\> · página N». **La versión del estilo va en las propiedades** (`cp:version`), no en el pie: el cliente no tiene por qué leerla, e Iván prueba una vez por versión (A-007) |

**Fuera:** emojis como señal (✍️ ⚠️ 🔒), ★, portadas y mapas a página completa,
y las casillas en columnas.

## Componentes del PDF

En [`estilo.css`](prototipo/estilo.css), y probados en la muestra:

| Componente | Clase | Regla |
|---|---|---|
| Cabecera | `.cabecera` | No hay portada: el título va en la primera página, con el contenido |
| Cifra | `.cifras > .cifra` | Tres en fila. Número en acento y qué significa en una línea. **Calculada por script** (acuerdo de la ronda 1) |
| Caja | `.caja`, `.caja.conclusion` | Fondo, sin borde |
| Captura | `figure > .recorte > img` + `.marca-captura` | **Recortada a lo que importa** y a todo el ancho, con recuadro en acento sobre lo que se comenta (posición en %). Pie con la fecha. `alt` obligatorio |
| Hallazgo | `.hallazgo` | Número en círculo, título y una o dos líneas |
| Estado | `.estado.si` / `.medias` / `.no` | **Símbolo + palabra + color**: ✓, –, ✗ (trazos de Lucide `check`, `minus` y `x`) |
| Lista de lo que haríamos | `ul.haremos` | Marca `check` en `bien` |
| Cita | `blockquote` + `cite` | Literal, con la fuente debajo |
| Siguiente paso | `.siguiente` | Borde en acento. Cierra la parte principal |
| Tabla | `table` | Cabecera en tinta; texto a 10 pt; las filas no se parten |
| Anexo | `.anexo.nueva-pagina` | Etiqueta ANEXO |
| Sello interno | `.interno` | En cada sección de un documento interno |

**Iconos:** solo Lucide (ISC), ya en `herramientas/iconos/<nombre>.svg`. En la
muestra, los trazos de `check`, `minus` y `x` van copiados en línea: el
generador real los tiene que leer de ahí.

## Mapa (para `mapa.py`)

- **Vosotros:** el marcador más grande, en acento, con borde blanco y la etiqueta
  **«Vosotros»** en una caja blanca.
- **Los demás:** se distinguen **por la forma**, no solo por el color:
  peluquerías en círculos y barberías en cuadrados, las dos en tinta.
- **Leyenda dentro del mapa:** caja blanca arriba a la izquierda, con las tres
  formas y su nombre.
- **Anillos** con su distancia escrita.
- **Contraste:** las marcas tienen que llegar a 3 : 1 contra el mapa aclarado.
  El acento y la tinta sobre un gris claro pasan de sobra.
- **Atribución:** la de Paco, abajo a la derecha, con `openstreetmap.org/copyright`.
- Si el mapa va en el informe A5, a todo el ancho y con las etiquetas a ≥ 9 pt
  una vez impreso. Con 1100 px a 128 mm, son unos **27 px**. Las de hoy, a
  18 px, quedarían a unos 6 pt.

## Accesibilidad (mínimos)

- **Idioma:**
  - en el HTML, `lang="es"`;
  - en el Word, `es-ES` en `docDefaults`, en los estilos y en las
    propiedades (ya lo hace `nuevo_documento`).
- **Texto alternativo en todas las imágenes:**
  - en el HTML, `alt`, que dice lo que se ve **y** lo que importa;
  - en el Word, `descripcion` en `imagen()`;
  - si una imagen es decorativa, `alt=""`.
- **Títulos de verdad** (`h1`–`h3` y «Título 1–3») y PDF **etiquetado**
  (`pdfinfo`: «Tagged: yes»).
- **Nada solo con color:** recuadros con etiqueta, estados con palabra, mapa
  con formas.
- **Enlaces subrayados.**

## Comprobación antes de pasarlo a Puri

```
node herramientas/html_a_pdf.mjs informe.html informe.pdf --estricto   # falla si no cargó Inter o una imagen (la muestra pasa)
pdfinfo  informe.pdf | grep -E "Pages|Tagged|Page size"                 # 3 páginas, Tagged: yes, 420 x 595 pt (A5)
pdffonts informe.pdf                                                    # solo Inter, sin fuentes de relleno
pdftoppm -scale-to-x 390 -scale-to-y -1 -png informe.pdf movil          # leerlo como en un móvil
.venv/bin/python herramientas/pruebas/revisar_docx.py tanda-a.docx      # el Word, sin errores de estructura
soffice --headless --convert-to pdf tanda-a.docx                        # y verlo
```

- [ ] Las páginas de `movil-*.png` se leen **sin ampliar**.
- [ ] Cada parte del informe cabe en su página, y ninguna página queda a medias salvo el anexo.
- [ ] Ningún «[Nombre de…]» ni marcador a la vista.
- [ ] Paleta y fuentes de esta skill, sin colores ni fuentes sueltas.
- [ ] Imágenes con texto alternativo; idioma español.
- [ ] La leyenda del Word solo explica los recuadros que salen.
- [ ] El Word, probado por Iván en Microsoft Word una vez por versión de plantilla (A-007).

## Para Paco: cómo llevarlo a `herramientas/`

1. **Fuentes:** hechas (`herramientas/fuentes/inter/` y `fraunces/`, con su `OFL.txt`).
2. **CSS:** [`estilo.css`](prototipo/estilo.css), a `herramientas/`. En el
   prototipo, el `@font-face` apunta a `../../../../herramientas/fuentes/inter/`
   para que se pueda probar donde está. En `herramientas/` queda en
   `fuentes/inter/…`. Propongo un fichero nuevo y dejar `informe.css` para los
   generadores antiguos, por su regla de compatibilidad. Lo decide él.
3. **`docx_util.py`:**
   - la paleta;
   - Arial 11 por defecto;
   - las piezas de [`bloques_docx.py`](prototipo/bloques_docx.py), que ya usan
     `_colocar` y pasan `revisar_docx.py`.

   El formato del `w:tag` (`<id>.<n>`, por ejemplo `A 3.5.2`) es una
   propuesta: lo cierra con Reme para `leer_cuestionario.py`. Los huecos de
   «Escribid aquí» también necesitarían su `id` (petición de Reme).
4. **`mapa.py`:** lo de «Mapa», arriba. Hoy usa Avenir Next para las
   etiquetas: mejor Inter, desde `herramientas/fuentes/inter/`.
5. **Iconos:** Lucide ya está. Que el generador del informe meta en línea
   `herramientas/iconos/<nombre>.svg` en vez de los trazos copiados.

## Dudas abiertas

- **El Word en el móvil:** cómo se ve y si se pueden marcar las casillas en
  Word para iPhone o Android. Ahora pesa menos, porque en el móvil se contesta
  por el chat (A-003). Lo cubre la prueba de Iván (A-007).
- **Incrustar Inter en el Word:** no sé si se ve en el móvil ni en el visor del
  correo. Mientras no se pruebe, Arial.
- **Identidad definitiva:** cuando haya nombre, ¿logotipo propio o solo tipográfico?
