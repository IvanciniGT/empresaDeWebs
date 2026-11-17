---
name: guia-estilos-previa
description: "Prepara la dirección de arte provisional e interna de un cliente nuevo antes de que contrate (concepto, paleta con contrastes WCAG comprobados también en lo que no es texto, tipografías, iconos, esquema de la primera pantalla del móvil y lista de fotos que harán falta) y la convierte en guía definitiva cuando llegan sus fotos. No se envía al cliente. Úsala cuando el expediente tiene la información pública recopilada, y otra vez cuando el cliente contrata y manda material."
---

# guia-estilos-previa

> **BORRADOR v0.2 · revisado por Lola** · Dueña: Lola · En revisión (ronda 1)
>
> Cambios respecto a la v0.1 y su porqué: [revision-lola.md](../../ronda-1/revision-lola.md) §4.

## Para qué sirve (y para qué no)

Es una **hipótesis de diseño hecha sin haber visto el local**. Sirve para tres cosas:

1. **Que Reme presupueste bien:** cuántas secciones, qué componentes, qué falta (fotos, logotipo).
2. **Que Menchu sepa qué material pedir:** la lista de fotos, con tamaños.
3. **Ganar días cuando el cliente contrate:** la definitiva parte de aquí.

**No es** el diseño de la web, ni un logotipo, ni los textos. No se envía al
cliente: «no le regalamos el diseño» (Iván). Cuanto más se parezca a una web
terminada, más trabajo tiramos si el local no se parece a lo que imaginábamos.

## Cuándo

| Momento | Qué se hace | Salida |
|---|---|---|
| Expediente con lo público, en paralelo con el cuestionario B1 | **Previa** | PDF interno de 3–4 páginas |
| El cliente acepta el presupuesto y manda fotos (fachada, rótulo, interior) o logotipo | **Definitiva** (ver abajo) | Guía de estilos del proyecto, para Paco |

## Entrada

- Expediente: §1 datos comprobados, §2 a confirmar, §3 reseñas literales.
- Capturas de su presencia actual y de la competencia (para **no** parecerse).
- Previo de precio de Reme: el plan que encaja (una página o varias).

## Contenido de la previa

Un PDF de **3 o 4 páginas**, sin portada a página completa y sin saltos de
página forzados por sección.

| # | Bloque | Qué lleva | Qué **no** lleva |
|---|---|---|---|
| 1 | **Lo que sabemos y lo que no** | Qué decisiones salen del expediente y cuáles son a ciegas: «sin ver fachada, rótulo, interior ni logotipo». | Afirmaciones sobre la competencia que no estén en el expediente o en el informe. |
| 2 | **Concepto** | Dos o tres palabras, tres rasgos que transmitir y tres que evitar, cada uno con su porqué y su fuente (normalmente las reseñas). | — |
| 3 | **Paleta provisional** | 4–6 colores con **papel**: texto, fondo, superficie, acción (botones), secundario, detalle. Código y uso. **Tabla de contrastes** completa (abajo). | Colores «por si acaso» que no tienen papel. |
| 4 | **Tipografías** | Máximo dos familias con licencia libre, muestra y la tabla de tamaños (abajo). | Frases de ejemplo inventadas: se usa una reseña literal o un texto neutro («Horario · Servicios · Cómo llegar»). |
| 5 | **Iconos** | El juego (Lucide, licencia ISC) y la **lista** de los que hacen falta. | Iconos dibujados a mano. |
| 6 | **Primera pantalla en el móvil** | Esquema en grises, a baja fidelidad, con etiquetas de función: `[Frase principal · Chema]`, `[Foto: fachada]`. Cumple la regla de los tres segundos (abajo). | Textos, precios o servicios. Nada que parezca terminado. |
| 7 | **Estructura de secciones** | Lista ordenada y una línea por sección. Tiene que cuadrar con el plan del previo de precio. | Secciones que dependen de una respuesta del cliente sin marcarlas como «si…». |
| 8 | **Fotos que harán falta** | Lista de tomas con su uso y su tamaño mínimo (abajo). La usa Menchu en B2. | Fotos de Google o de directorios, ni siquiera «de muestra». |
| 9 | **Riesgos y preguntas** | Lo que cambiaría la propuesta si el cliente dice X («si el rótulo es verde, cambia el acento»). Las preguntas para el cuestionario van a Reme, a través de Federico. | — |

**Fuera de la previa**, y por qué:

- **Logotipo**, ni siquiera provisional. No está incluido (§6.1) y crea una
  expectativa. Si al contratar no tienen, se propone uno tipográfico sencillo
  en la definitiva.
- **Tono de comunicación y textos.** Son de Chema. La guía solo dice dónde va
  cada texto y cuánto cabe («frase principal: unos 40–45 caracteres, a
  comprobar con el texto real»).
- **Maqueta en alta fidelidad.** Se hace al contratar.

## Reglas

1. **La identidad es del cliente.** Si tiene rótulo, logotipo o colores, mandan. La previa lo dice en la primera página: «propuesta a ciegas».
2. **Nada sin comprobar en una maqueta.** Ningún servicio, horario, canal ni
   año que no esté en el expediente §1. Lo de §2 va marcado `[a confirmar]`.
   Las maquetas acaban reutilizándose y lo inventado se cuela (§10.3).
3. **La acción principal es un canal comprobado.** Si solo sabemos el
   teléfono, el botón principal es «Llamar». WhatsApp o la reserva, solo
   cuando el cliente confirme que los tiene. Que sepamos su teléfono fijo no
   dice nada de si tienen WhatsApp: se pregunta, no se supone.
4. **Regla de los tres segundos.** En la primera pantalla del móvil, sin
   desplazar, están el **teléfono** (un toque para llamar), el **horario de
   hoy** y **cómo llegar** (un toque para abrir el mapa).
5. **Contraste comprobado, también en lo que no es texto** (WCAG 2.2 AA,
   §11), con [`contraste.py`](contraste.py):
   - Texto normal: **4,5 : 1**. Texto grande (≥ 24 px, o ≥ 18,66 px en negrita): 3 : 1.
     Los botones a 17 px en negrita **no** son texto grande: necesitan 4,5.
   - Bordes de campos y botones secundarios, iconos sin texto e indicador de foco: **3 : 1** con lo que tienen al lado (criterio 1.4.11).
   - Texto sobre foto o sobre un marcador de posición rayado: se mide contra el tono **más claro** del fondo.
   - Un par que no llega **solo** puede ser decoración.
6. **No depender del color.** Enlaces subrayados. Errores con texto e icono, no solo en rojo.
7. **Tamaños mínimos**, en la tabla de tipografías:

   | | Móvil | Ordenador |
   |---|---|---|
   | Texto | ≥ 16 px (proponemos 17), interlineado 1,5 | 18 px, interlineado 1,5 |
   | Notas y pies | ≥ 14 px | ≥ 14 px |
   | Ancho de línea | — | 60–75 caracteres como máximo |
   | Áreas de toque | **≥ 44 × 44 px** (WCAG pide 24 × 24; nosotros, más) | — |

8. **Solo recursos con licencia** (§10.3), anotada al lado de cada uno.
   Fuentes y licencias habituales: Google Fonts (SIL OFL), Lucide (ISC).
9. **Fuentes en archivo, no desde Google.** En la web, por el RGPD (la IP del
   visitante). En el PDF, porque si Google tarda en responder Chrome usa otra
   fuente **sin avisar**, y porque las de Google salieron como Type 3 en el
   PDF (probablemente por ser variables), con el texto peor extraíble. Mientras no haya fuentes en `herramientas/`, se acepta
   Google en la previa (es interna), pero hay que comprobar con `pdffonts`
   que salió la fuente buena.
10. **Fotos de personas:** nada de caras de clientes ni de niños sin un
    consentimiento por escrito con el modelo que apruebe Iván (pendiente, §15).
    Mientras tanto: el equipo, el local y los detalles del oficio.

## Pasos

1. Leer el expediente y el previo. Apuntar qué sabemos del aspecto real del
   local y qué no.
2. Mirar la competencia del informe para **no parecerse**.
3. Escribir el concepto con su porqué y su fuente.
4. Elegir la paleta y comprobarla: todos los pares de texto **y** los de no
   texto que se usan en el esquema.
   ```
   python3 procesos/skills-borrador/guia-estilos-previa/contraste.py \
     "#1F2A37:#F6F0E6" "#FFFFFF:#9A5B2E" "#9A5B2E:#F6F0E6" --minimo 3
   ```
   La tabla en Markdown que devuelve va tal cual a la guía.
5. Tipografías, tabla de tamaños y lista de iconos.
6. Esquema de la primera pantalla y lista de secciones. Repasarlo contra las
   reglas 2, 3 y 4.
7. Lista de fotos con tamaños.
8. Maquetar en HTML y pasar a PDF con `herramientas/html_a_pdf.sh`. Sello
   «INTERNO · NO ENVIAR AL CLIENTE» en cada página.
9. Comprobar antes de entregar (abajo) y pasarla a Federico.

## Fotos: lista de tomas y tamaños

Tamaño medido en píxeles del lado largo del archivo **tal como nos llega**:

| Uso | Mínimo | Por qué |
|---|---|---|
| Foto principal, a todo el ancho | **2000 px**, horizontal y con aire alrededor del motivo | En el ordenador ocupa unos 1440 px de pantalla, y en móviles de alta densidad, unos 1200. El aire permite recortarla en vertical para el móvil. |
| Fotos de secciones y galería | **1200 px** | Se ven a la mitad del ancho como mucho. |
| Retrato del equipo | **1000 px** | Se ve en tarjeta. |

Tomas habituales: fachada de día con el rótulo · interior entero · el equipo
junto · cada uno trabajando · detalles del oficio · fotos antiguas del negocio
(escaneadas o fotografiadas de frente, sin reflejos).

**WhatsApp:** no sabemos todavía qué tamaño llega con la opción normal y con
la HD. Hasta medirlo (ver la revisión, §7), la foto principal se pide por
correo o como documento, y el resto, por WhatsApp con HD.

## Comprobación antes de entregar

- [ ] Cada dato del cliente que aparece está en el expediente §1, o va marcado `[a confirmar]`.
- [ ] La acción principal del esquema es un canal comprobado (regla 3).
- [ ] Teléfono, horario de hoy y cómo llegar, en la primera pantalla (regla 4).
- [ ] Tabla de contrastes generada con `contraste.py`, con pares de texto **y** de no texto.
- [ ] Licencia anotada en cada fuente, icono e imagen.
- [ ] Ni logotipo, ni textos de Chema, ni fotos de terceros.
- [ ] `pdffonts` muestra las fuentes elegidas, no otras de relleno.
- [ ] 3–4 páginas, sello INTERNO en todas.

## De previa a definitiva (al contratar)

1. Con las fotos de la fachada, el rótulo y el interior, **sacar los colores
   reales** con un cuentagotas sobre la foto. Usar varias muestras, porque la
   luz engaña. Si hay logotipo en archivo, sus colores mandan.
2. Comparar con la previa. Si el color del cliente no da contraste para
   texto, se usa en superficies grandes y detalles, y se oscurece **solo** su
   versión para texto y botones. Se anota como «variante accesible de su color».
3. Rehacer la tabla de contrastes.
4. Anotar en la guía qué cambió respecto de la previa y por qué.
5. Completar la guía del proyecto para Paco:
   - componentes con todos sus estados: normal, foco visible, pulsado, desactivado, error;
   - formulario con etiquetas visibles;
   - aviso de cookies con «Rechazar» igual de visible que «Aceptar» (§11);
   - maquetas móvil → tableta → ordenador;
   - espaciado en múltiplos de 8 px;
   - colores y tamaños como variables CSS;
   - archivos de fuentes e iconos con su licencia;
   - fotos optimizadas.

## Salida

- `interno/Guía de estilos previa - INTERNO - <negocio>.pdf`, y su HTML en `maquetas/`.
- Al contratar: la guía definitiva del proyecto (formato a cerrar con Paco).

## Herramientas

- [`contraste.py`](contraste.py): contraste WCAG con el veredicto de texto,
  texto grande y no texto. Sin dependencias. `--minimo` sale con error si
  algún par no llega.
- `herramientas/html_a_pdf.sh`: de HTML a PDF con Chrome sin ventana.
- `pdffonts` (ya instalado): comprobar qué fuentes salieron en el PDF.

## Dudas abiertas

- ¿Podemos ver la fachada antes de contratar sin pedir nada al cliente?
  Mapillary tiene fotos de calle con licencia abierta. Falta comprobar la
  licencia exacta, si hay fotos de esa calle y si su uso automático lo permite.
  Solo serían para mirar, nunca para publicar.
- Formato de la guía definitiva para Paco: ¿PDF, HTML con variables CSS o las dos cosas?
- Plantilla de la guía (diseño fijo y datos de cada cliente aparte) para no copiar
  300 líneas de Python por cliente: la propongo a Paco en la revisión.
