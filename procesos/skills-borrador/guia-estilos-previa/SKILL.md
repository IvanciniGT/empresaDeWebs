---
name: guia-estilos-previa
description: "Prepara la dirección de arte provisional e interna de un cliente nuevo antes de que contrate: lo que sabemos y lo que no, concepto, paleta con contrastes comprobados por papel, tipografías, iconos, esquema en grises de la primera pantalla del móvil, estructura y lista de fotos. Se genera con una plantilla a partir de un JSON y se convierte en guía definitiva cuando llegan las fotos del cliente. No se envía al cliente. Úsala cuando el expediente tiene la información pública y el previo de precio, y otra vez si llega la foto de la fachada o cuando contrata."
---

# guia-estilos-previa

> **BORRADOR v0.3 · Lola** · Dueña: Lola · Aprobado el alcance por Iván: **A-006**
> (3–4 páginas, como hipótesis). Historia: [revision-lola.md](../../ronda-1/revision-lola.md) §4 y §8.

## Para qué sirve (y para qué no)

Es una **hipótesis de diseño hecha sin haber visto el local**. Sirve para tres cosas:

1. **Que Reme presupueste bien:** cuántas secciones, qué componentes, qué falta (fotos, logotipo).
2. **Que Menchu sepa qué fotos pedir en la tanda B,** con tamaños.
3. **Ganar días cuando el cliente contrate:** la definitiva parte de aquí.

**No es** el diseño de la web, ni un logotipo, ni los textos, ni el tono.

- Los textos y el **tono de comunicación son de Chema** (`textos-web`).
- La guía no se envía al cliente: «no le regalamos el diseño» (Iván).

## Cuándo

| Momento | Qué se hace |
|---|---|
| Expediente con lo público **y previo de precio hecho**, en paralelo con la tanda A | **Previa a ciegas** |
| Llega la foto de la fachada (pregunta opcional **A 5.6**, choque 3) | **Previa con fachada:** se rehace la paleta con sus colores (abajo) |
| El cliente acepta el presupuesto y llegan las fotos de la tanda B | **Definitiva** (al final de esta skill) |

## Entrada

- Expediente: §1 datos comprobados, §2 a confirmar, §3 reseñas literales.
- Informe y capturas de la competencia, para **no** parecerse.
- Previo de precio de Reme: el plan que encaja (una página o varias).
- Si ha llegado: la foto de la fachada, en `privado/fotos/`. La guarda Menchu
  y Federico me avisa.

## Dónde van los ficheros

El repositorio es **público** (A-013) y `interno/` **sí entra en git**, así que
la guía previa y el previo de precio que hay hoy en el caso de ejemplo se pueden
descargar desde GitHub. Lo he elevado (revisión, §8).

Mientras no se decida:
- el JSON y el PDF del cliente van en `clientes/<negocio>/privado/guia/`, que ya está fuera de git;
- en el repositorio solo la plantilla, que es genérica, y el ejemplo ficticio.

## Contenido: 3 páginas A4

Lo genera [`generar_guia.py`](generar_guia.py) a partir de un JSON. Ejemplo:
[`ejemplo/datos-ejemplo.json`](ejemplo/datos-ejemplo.json). Usa el estilo común
(`estilo-documentos`) con el sello INTERNO en cada sección.

| Bloque | Qué lleva | Qué **no** lleva |
|---|---|---|
| **Cabecera** | Negocio, fecha, autora, plan que encaja. Caja: «propuesta a ciegas» o «con foto de la fachada», y que es una hipótesis | Portada a página completa |
| **Lo que sabemos / lo que no** | Cada dato con su fuente (expediente §1, §3). Lo que no sabemos, dicho | Afirmaciones sobre la competencia que no estén en el informe |
| **Concepto** | Nombre en dos o tres palabras. Tres rasgos que transmitir, con su porqué **y su fuente**, y tres que evitar | — |
| **Tipografías** | Máximo dos familias con licencia libre. Muestra con texto **neutro** («Horario · Servicios · Cómo llegar»). Tabla de tamaños (regla 7) | Frases de venta inventadas |
| **Paleta** | Un color por **papel**: `texto`, `fondo`, `superficie`, `accion`, `texto_accion`, `secundario` y `detalle`. Tabla de contrastes **calculada** para cada uso | Colores «por si acaso» |
| **Iconos** | La lista de Lucide (ISC) que hace falta, por nombre (`phone`, `clock`, `map-pin`…) | Iconos dibujados a mano |
| **Primera pantalla del móvil** | Esquema **en grises**, con etiquetas de función (`[Frase principal · Chema · 40–45 caracteres]`, `[Foto: fachada]`) y la línea de «fin de la primera pantalla» | Textos, precios, servicios sin comprobar, colores del cliente: nada que parezca terminado |
| **Secciones** | Lista ordenada, una línea por sección; las que dependen de una respuesta, con «solo si…» | — |
| **Fotos para la tanda B** | Toma, para qué y tamaño mínimo (abajo) | Fotos de Google o de directorios, ni de muestra |
| **Riesgos y preguntas** | Qué cambiaría si el cliente dice X. Las preguntas para el cuestionario, a Reme a través de Federico | — |

**Fuera de la previa:** logotipo (§6.1), tono y textos (Chema) y maqueta en alta fidelidad.

## Reglas

1. **La identidad es del cliente.** Si tiene rótulo, logotipo o colores, mandan.
   Sin foto de la fachada, la guía lo dice en la primera caja: «propuesta a ciegas».
2. **Nada sin comprobar en una maqueta.** Ningún servicio, horario, canal ni
   año que no esté en el expediente §1. Lo de §2 va como `[a confirmar]`.
3. **La acción principal es un canal comprobado.** Si solo sabemos el teléfono,
   es «Llamar». WhatsApp o la reserva, cuando el cliente lo confirme (A 3.5).
   *El generador no deja sacar la guía si `accion_principal.comprobado` es falso.*
4. **Regla de los tres segundos.** En la primera pantalla del móvil, sin
   desplazar: **llamar** (un toque), el **horario de hoy** y **cómo llegar**
   (un toque al mapa).
5. **Contraste por papel, también en lo que no es texto** (WCAG 2.2 AA, §11).
   - Texto: **4,5 : 1**, en cada uno de sus usos: texto sobre fondo y sobre
     tarjetas, el texto del botón, los enlaces y las notas.
   - Bordes de botones y campos, foco e iconos: **3 : 1**.
   - Un botón de 17 px en negrita **no** es texto grande.
   - El color de `detalle` solo puede decorar.
   - *El generador calcula los nueve pares y no saca la guía si alguno no llega.*
6. **No depender del color.** Enlaces subrayados; errores con texto e icono.
7. **Tamaños mínimos** (la tabla va en la guía):

   | | Móvil | Ordenador |
   |---|---|---|
   | Texto | 17 px (mínimo 16), interlineado 1,5 | 18 px, interlineado 1,5 |
   | Notas y pies | ≥ 14 px | ≥ 14 px |
   | Áreas de toque | **≥ 44 × 44 px** | — |
   | Ancho de línea | — | 60–75 caracteres |

8. **Solo recursos con licencia** (§10.3), anotada al lado de cada uno.
   Instalados por Paco (A-008):
   - fuentes en `herramientas/fuentes/inter/` y `herramientas/fuentes/fraunces/`, con su `OFL.txt`;
   - iconos en `herramientas/iconos/`.
9. **Fuentes en archivo.**
   - En la web, por el RGPD.
   - En el PDF, para que salga la fuente buena y no Type 3.
   - El generador usa `herramientas/fuentes/` si la familia está. Si no, Google
     (solo en esta guía interna) y lo avisa. Se comprueba con `pdffonts`.
10. **Fotos de personas:** ni caras de clientes ni de niños sin un
    consentimiento por escrito con el modelo que apruebe Iván (A-010).

## Pasos

1. Leer el expediente, el informe y el previo. Apuntar qué sabemos del aspecto
   real del local y qué no.
2. Copiar `ejemplo/datos-ejemplo.json` a `clientes/<negocio>/privado/guia/datos.json` y rellenarlo:
   - cada dato de «sabemos», con su fuente;
   - el concepto, con su porqué;
   - un color por papel;
   - las tipografías, con `prefijo` si hay varios cortes, por ejemplo
     `Fraunces72pt` para titulares;
   - la acción principal y si está comprobada;
   - las secciones, los riesgos y las preguntas.
3. Probar colores sueltos mientras se elige:
   `python3 procesos/skills-borrador/guia-estilos-previa/contraste.py "#5E6670:#F6F0E6"`.
4. Generar:
   ```
   .venv/bin/python procesos/skills-borrador/guia-estilos-previa/generar_guia.py \
     clientes/<negocio>/privado/guia/datos.json \
     "clientes/<negocio>/privado/guia/Guía de estilos previa - INTERNO - <negocio>.pdf"
   ```
   Si se niega, dice qué par o qué regla falla: se cambia el color, no la regla.
5. Comprobar (abajo) y pasarla a Federico.

## Fotos: tomas y tamaños (para la tanda B)

Medido en píxeles del lado largo del archivo **tal como nos llega**:

| Uso | Mínimo | Por qué |
|---|---|---|
| Foto principal, a todo el ancho (normalmente la fachada) | **2000 px**, horizontal y con aire alrededor | En el ordenador ocupa unos 1440 px de pantalla, y en móviles de alta densidad unos 1200. El aire deja recortarla en vertical para el móvil |
| Secciones y galería | **1200 px** | Se ven a la mitad del ancho como mucho |
| Retrato del equipo | **1000 px** | Se ve en tarjeta |

Tomas habituales:
- fachada de día con el rótulo;
- interior entero;
- el equipo, junto;
- cada uno trabajando;
- detalles del oficio;
- fotos antiguas del negocio, escaneadas o de frente y sin reflejos.

**WhatsApp:** aún no sabemos qué tamaño llega con la opción normal y con la HD
(está pendiente que Iván lo mida). Mientras tanto:
- la foto principal, por correo o como documento;
- el resto, por WhatsApp con HD.

Para la foto de la fachada de la A 5.6 vale cualquiera: en la previa solo se
mira, no se publica.

## Comprobación antes de entregar

- [ ] El generador terminó sin negarse: contrastes y acción principal, bien.
- [ ] Cada dato del cliente está en el expediente §1 con su fuente, o va como `[a confirmar]`.
- [ ] La primera pantalla del esquema tiene llamar, el horario de hoy y cómo llegar.
- [ ] `pdfinfo`: 3–4 páginas. `pdffonts`: solo las fuentes elegidas (sin Type 3 ni fuentes del sistema).
- [ ] Licencia anotada en fuentes e iconos.
- [ ] Ni logotipo, ni textos de Chema, ni fotos de terceros.
- [ ] El JSON y el PDF, fuera de git.

## Con la foto de la fachada (previa) o al contratar (definitiva)

1. **Sacar los colores reales** con [`colores_foto.py`](colores_foto.py):
   ```
   .venv/bin/python procesos/skills-borrador/guia-estilos-previa/colores_foto.py \
     clientes/<negocio>/privado/fotos/fachada.jpg --zona 20,10,60,20 -n 5
   ```
   - `--zona` recorta en % (izquierda, arriba, ancho, alto), por ejemplo solo el rótulo.
   - Devuelve cada color con su proporción y su contraste con blanco y con negro.
   - La luz engaña: mejor dos fotos o dos zonas del mismo elemento.
   - Si hay logotipo en archivo, sus colores mandan.
2. **Llevarlos al JSON**:
   - el color del cliente pasa a ser `accion` o `detalle`;
   - se pone `foto_fachada` con la ruta;
   - se regenera.
3. **Si su color no da contraste para texto,** se usa en superficies grandes y
   detalles, y se oscurece **solo** su versión para texto y botones. Se anota en
   `uso` como «variante accesible de su color».
4. **Anotar qué cambió** respecto a la previa y por qué (en `riesgos`, o en el expediente).
5. **Definitiva, al contratar:** la guía del proyecto para Paco. Lleva:
   - componentes con todos sus estados (normal, foco visible, pulsado, desactivado y error);
   - formulario con etiquetas visibles;
   - aviso de cookies con «Rechazar» igual de visible que «Aceptar» (§11);
   - maquetas para móvil, tableta y ordenador;
   - espaciado en múltiplos de 8 px;
   - colores y tamaños como variables CSS;
   - fuentes e iconos con su licencia;
   - fotos optimizadas.

   El formato está por cerrar con Paco.

## Herramientas (en esta skill)

| Herramienta | Qué hace | Probado |
|---|---|---|
| [`contraste.py`](contraste.py) | Contraste WCAG con veredicto para texto, texto grande y no texto. `--minimo` sale con error | Con valores de referencia: 21; 4,54 frente a 4,47 |
| [`generar_guia.py`](generar_guia.py) | La guía desde el JSON. Se niega si falla un contraste o la acción principal | El ejemplo, en 3 páginas. Con un gris claro se niega por 2 pares, y con WhatsApp sin comprobar también. Si se quita la comprobación, genera: la prueba detecta que falta |
| [`colores_foto.py`](colores_foto.py) | Colores dominantes de una foto o zona, con su contraste | Imágenes de colores conocidos (2 y 3 colores): salen exactos. Sin el refinado por k-medias, la prueba falla |

Comunes (de Paco): `herramientas/html_a_pdf.mjs`, fuentes e iconos. Paco decide
si alguna de las mías pasa a `herramientas/` (choque 4).

## Dudas abiertas

- **¿`interno/` fuera de git?** Lo decide Iván (revisión, §8).
- **Formato de la guía definitiva para Paco:** ¿PDF, HTML con variables CSS o las dos cosas?
- **Ver la fachada sin preguntar** (fotos de calle con licencia abierta): sigue
  sin comprobar. Con la pregunta A 5.6 pierde urgencia.
