---
name: estilo-documentos
description: "Define y revisa el aspecto de los documentos que la empresa manda a los clientes (informe PDF, cuestionario Word y los que vengan): identidad común, paleta con contraste comprobado, tipografía, componentes, lectura en el móvil y accesibilidad. Úsala al maquetar o revisar un documento para un cliente, y cuando Paco cambie informe.css o docx_util.py."
---

# estilo-documentos

> **BORRADOR v0.1 · propuesta de Lola** (no existía) · Dueña: Lola · Lo
> implementa Paco en `herramientas/` · En revisión (ronda 1)
>
> Por qué hace falta: [revision-lola.md](../../ronda-1/revision-lola.md) §3.

## Principio

**Nuestros documentos llevan nuestra identidad; la del cliente va en su web.**
Hoy el informe sale en azul y naranja, la guía en tinta y cobre y el Word en
otra cosa. Un cliente que recibe tres documentos con tres aspectos distintos no
sabe si vienen de la misma empresa.

Mientras no haya nombre (§15), la identidad es **provisional y neutra**: la
misma paleta, la misma tipografía y los mismos componentes. Cuando llegue el
nombre, solo cambia la cabecera. Nada de logotipo inventado.

## Paleta (comprobada con `contraste.py`)

| Papel | Color | Uso |
|---|---|---|
| Tinta | `#1E2A3A` | Texto, cabeceras de tabla (con texto blanco) |
| Acento | `#9C4A14` | Títulos, cifras, números de pregunta, barra «Escribid aquí» |
| Gris | `#56606D` | Notas, pies, ayudas; barra «Lo que hemos encontrado» |
| Fondo | `#F4F6F9` | Cajas y cifras |
| Acento suave | `#F6E3D3` | Caja de conclusión |
| Bien | `#24693F` | Etiquetas «sí»; barra «Nuestra propuesta» |
| Atención | `#8A5A00` | Etiquetas «a medias» |
| Mal | `#B3261E` | Etiquetas «no» |

Sustituye a `#B55A1E`, `#5F6B7A`, `#2E7D4F` y `#C98A12`. El verde no llegaba
a AA en las etiquetas (4,38 : 1 a 8 pt). El naranja sobre gris (4,36) y el gris
sobre melocotón (4,35) solo valían según dónde se usaran. Con la paleta nueva,
cualquier par vale para texto de cualquier tamaño y no hay que vigilarlo.

Pares que se usan, todos ≥ 4,5 : 1 (texto) o ≥ 3 : 1 (barras y marcas):

| Delante | Fondo | Contraste |
|---|---|---|
| Tinta | blanco | 14,50 |
| Acento | blanco · fondo · acento suave | 6,17 · 5,69 · 4,95 |
| Blanco | acento | 6,17 |
| Gris | blanco · fondo · acento suave · `#FFF4E0` | 6,38 · 5,89 · 5,12 · 5,85 |
| Bien | `#E3F3E8` | 5,76 |
| Mal | `#FBE4E2` | 5,38 |
| Atención | blanco | 5,92 |
| Barra gris | `#EEF2F6` | 5,67 |
| Barra acento | `#FFF4E0` | 5,66 |
| Barra verde | `#EAF5EC` | 5,92 |

Si se cambia un color, se vuelve a pasar `contraste.py --minimo 4.5` con todos
los pares de texto y `--minimo 3` con los de no texto.

## Tipografía

| Documento | Fuente | Por qué |
|---|---|---|
| PDF | **Inter** (SIL OFL), archivos estáticos en `herramientas/fuentes/` | Con licencia para incrustar, igual en cualquier máquina y sin depender de Google al generar |
| Word | **Arial** | Está en Windows, Mac e iPhone. Calibri no está en este Mac (LibreOffice la cambia por Carlito) ni en los móviles. Un Word no puede fiarse de fuentes incrustadas. |

Hoy el informe usa Avenir Next, una fuente que viene con macOS. No sabemos si
su licencia permite incrustarla en documentos que mandamos fuera (§10.3), y
solo existe en Mac. Se deja de usar.

Tamaños:

| | PDF A5 | Word A4 |
|---|---|---|
| Texto | 11,5 pt, interlineado 1,5 | 11 pt, interlineado 1,15 |
| Notas, pies, ayudas | ≥ 9,5 pt | ≥ 10 pt |
| Títulos de sección | 17 pt | 14 pt |

## Formato

- **PDF para el cliente: A5 vertical, una columna.** El A4 a 10,5 pt, en un
  móvil ajustado al ancho, deja el texto a unos 7 px: no se lee sin ampliar.
  El A5 a 11,5 pt se lee. Además, se imprime bien en A4 a dos caras o a
  tamaño real. **Se maqueta para A5, no se encoge:** encoger el informe
  actual lo llevó de 9 a 19 páginas.
- **Sin saltos de página forzados por sección.** Se usa `break-inside: avoid`
  en bloques y figuras, y `break-after: avoid` en títulos. Las medias páginas
  vacías parecen documentos sin terminar.
- **La primera página funciona sola:** título, a quién va, tres cifras y la
  conclusión. Es la que se ve como vista previa en WhatsApp y en el correo.
- **La última página es el siguiente paso y el contacto.** La metodología y las
  fuentes van antes, como anexo.
- **Pie en cada página:** nombre corto del documento y «página X de Y».

## Componentes

| Componente | Cómo es | Regla |
|---|---|---|
| Bloques del cuestionario | Fondo pálido + **barra izquierda gruesa** del color + **etiqueta en mayúsculas**: «LO QUE HEMOS ENCONTRADO», «ESCRIBID AQUÍ», «NUESTRA PROPUESTA» | El color ayuda; la etiqueta es la que informa. Se tiene que entender impreso en blanco y negro. |
| Pregunta | Número (el ID de Reme, p. ej. `1.4`) en acento + texto en negrita; ayuda debajo en gris; respuesta **debajo**, a todo el ancho | Una columna. Así se puede contestar por WhatsApp o por teléfono citando el número. |
| Validar un dato | «Está bien» / «Hay algo mal» + hueco | Nunca una casilla sola: sin marcar no se sabe si es «no» o «no lo he mirado». |
| Estado (semáforo) | Símbolo + palabra + color: ✓ Sí · ! A medias · ✗ No | Nunca solo un punto de color. |
| Cifra | Número grande en acento + qué significa en una línea | En A5, 2 × 2. |
| Captura | **Recortada a la zona que importa**, a todo el ancho, con un recuadro en lo que se comenta y su pie | Si el texto de la captura no se lee a tamaño real, no sirve: se recorta más o se describe. |
| Mapa | El cliente con un marcador grande y la etiqueta «Vosotros»; las categorías se distinguen por **forma**, no solo por color, con la leyenda dentro del mapa | Rojo y naranja no se distinguen con daltonismo. |
| Cita | Comillas latinas y raya izquierda en acento; la fuente debajo | Literal, sin retocar. |
| Iconos y símbolos | SVG (Lucide, ISC) o un carácter que la fuente tenga | Nada de emojis como señal (cambian según el aparato). Nada de ★ si la fuente no lo trae: salió de una fuente china de relleno. |

## Accesibilidad (mínimos)

- Idioma español: `lang="es"` en el HTML; en el Word, `es-ES` en los estilos
  **y** en `docDefaults`. Hoy el Word va en inglés y lo subraya todo como faltas.
- Texto alternativo en **todas** las imágenes: `alt` en el HTML y descripción en
  el Word. Si una imagen es decorativa, `alt=""`.
- Títulos de verdad (`h1`–`h3`, estilos «Título 1–3») para poder navegar.
- PDF etiquetado (Chrome ya lo hace; se comprueba con `pdfinfo`: «Tagged: yes»).
- Contraste: la paleta de arriba, sin colores sueltos.

## Comprobación antes de pasarlo a Puri

```
pdfinfo  doc.pdf | grep -E "Pages|Tagged"   # páginas y etiquetado
pdffonts doc.pdf                            # solo nuestras fuentes, sin rellenos
pdftoppm -scale-to-x 390 -scale-to-y -1 -png doc.pdf movil   # como en un móvil
```

- [ ] Las páginas de `movil-*.png` se leen **sin ampliar**.
- [ ] Ninguna página a medias salvo la última.
- [ ] La primera página se entiende sola. La última dice qué pasa ahora y cómo contactarnos.
- [ ] Imágenes con texto alternativo; idioma español.
- [ ] Paleta y fuentes de esta skill, sin colores ni fuentes sueltas.
- [ ] El Word se convierte a PDF con LibreOffice y se revisa igual. Pendiente: probarlo en Word para móvil.

## Herramientas

- `herramientas/informe.css` y `herramientas/docx_util.py`: los mantiene Paco.
  Esta skill dice **cómo deben verse**; los cambios se le piden a través de Federico.
- [`contraste.py`](../guia-estilos-previa/contraste.py).

## Dudas abiertas

- ¿Cómo se ve y se rellena el Word en el móvil (Word para iPhone y Android, y
  la vista previa del correo y de WhatsApp)? No lo he podido probar sin un
  móvil. Las casillas son controles de contenido de Word y no sé si funcionan ahí.
- Pie con «página X de Y» en el PDF: creo que Chrome admite las cajas de margen
  de `@page` desde hace poco, pero no lo he comprobado. Si no, otra solución (Paco).
- Identidad definitiva: cuando haya nombre, ¿logotipo propio o solo tipográfico?
