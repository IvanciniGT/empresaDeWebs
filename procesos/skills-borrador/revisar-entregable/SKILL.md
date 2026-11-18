---
name: revisar-entregable
description: "Revisa todo lo que va a salir hacia el cliente o hacia Iván (informe PDF, preguntas en Word, mensajes de WhatsApp, emails, plantillas de mensajes, presupuesto, guía): rastrea cada cifra y cada afirmación hasta su prueba, recalcula los datos, busca promesas, ausencias no probadas, huecos y datos personales en git, cruza los documentos del envío, comprueba tono, ortografía, lectura en el móvil, accesibilidad, licencias y que el archivo funcione donde lo abrirá el cliente. Da veredicto APROBADO o RECHAZADO con cada error, su gravedad, su categoría y su arreglo, y compara versiones. Úsala con cada envío antes de que salga, con cada versión corregida y con cada versión de una plantilla."
---

# revisar-entregable

> **BORRADOR v0.3 · revisado por Puri** · 2026-11-18 · **Dueña: Puri**
> v0.2: lista para documentos, después del primer envío de Federico
> ([veredicto](../../../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md)).
> v0.3: las decisiones de Iván A-001 a A-015, lo que me piden Chema, Lola, Menchu y Reme,
> el Word con `revisar_docx.py` de Paco y la comparación de versiones.

## Cuándo

- Antes de que **cualquier** cosa salga hacia el cliente o hacia Iván para aprobarla:
  documentos, mensajes de WhatsApp tal como Iván los va a copiar (A-003) y emails.
- Otra vez con **cada versión corregida**, hasta APROBADO. Un arreglo se cierra cuando
  lo he comprobado yo, no cuando el autor lo da por hecho.
- **Una vez por versión** de cada plantilla: mensajes de Menchu, recordatorios (A-012),
  guion de la tanda A y plantillas de Word (A-007). Si la plantilla cambia, se revisa
  otra vez; si solo cambian los datos del cliente, se revisa el envío.
- Las webs tienen su propia lista (§11, skill aparte). Esta es para documentos y mensajes.

## Reglas

1. **Nadie revisa lo suyo.** Lo que escribo yo lo revisa Federico, por muestreo (choque 5).
2. **Yo no arreglo.** Describo el error y su arreglo, y Federico se lo encarga a quien corresponda.
3. **Lo que no he podido comprobar no está aprobado.** Va al veredicto, en «No comprobado».
4. **Reviso la versión exacta que se enviaría.** Anoto la fecha y la huella (`shasum -a 256`).
   Si cambia un byte, es otra versión.
5. **No rebajo la vara por el plazo.** Si hay prisa, se lo digo a Federico.
6. **Un error es un defecto que se arregla con un cambio.** Si aparece en varios sitios,
   se ponen todos los sitios, pero cuenta uno.
7. **El repositorio es público (A-013).** En mis veredictos no van nombres de personas
   ni datos personales del cliente: se cita el sitio («la reseña de la p. 7»), no a la persona.

## Entrada

- El envío entero, como lo recibirá el cliente: en `entregables/`, más el texto de los
  mensajes de WhatsApp.
- **La fuente de verdad:**
  - el expediente;
  - lo que lo respalda: capturas, la captura de Google que hace Iván (A-001), la consulta y la respuesta de Overpass (A-015) y la prueba de cada cita;
  - la **tabla de trazas** del autor, si la hay.
- AGENTS.md, las decisiones de Iván ([aprobaciones](../../../operacion/aprobaciones.md)),
  la ficha del proceso y los requisitos (`requisitos.md`), si los hay.

## Pasos

### 1. Comprobación automática

```
python3 procesos/skills-borrador/revisar-entregable/comprobar.py \
        clientes/<negocio>/entregables clientes/<negocio>/expediente.md [otras fuentes]
```

| Saca | Cómo |
|---|---|
| Huecos sin rellenar (`[Empresa]`…) | Búsqueda en el texto |
| Cifras que no aparecen en las fuentes, y cada cifra con unidad por documento | Ídem, para el paso 4 |
| Frases de la lista: las mías **más las de Chema**, leídas de `estudio-competencia` y `textos-web` | Si Chema cambia su lista, cambia aquí solo |
| **El Word**: estructura, idioma, propiedades, miniatura, texto alternativo | Llama a `herramientas/pruebas/revisar_docx.py` de Paco (no lo duplico). Además: casillas y **versión de la plantilla en el pie** |
| **El PDF**: páginas, formato (A4/A5), etiquetado y tipografías fuera de `estilo-documentos` | `pdfinfo`, `pdffonts` |
| **El móvil**: letra del cuerpo en px a 390 px de ancho, e imágenes de cada página, también del Word | `pdftotext -bbox`, `pdftoppm -scale-to-x 390` |
| **Datos personales en git**: móviles, correos, DNI/NIE e IBAN en todo lo que entra en git, sin contar `privado/` (A-009) | `git ls-files` |
| **Ortografía**: palabras desconocidas que no están en el expediente | `hunspell` (A-008). Si no está, lo dice |
| Ficheros de bloqueo `~$…` y documentos internos colados | Nombre del fichero |
| Métricas: páginas, palabras, cifras sin fuente, frases de la lista y huecos | Para comparar versiones |

Es un punto de partida: señala dónde mirar, no lo que está bien. Lo que no puede
comprobar sale como `[no comprobado]`, nunca en silencio.

### 2. Leerlo todo y verlo todo

- Texto entero, palabra por palabra. La ortografía automática no sustituye a la lectura.
- **Cada página como imagen de móvil** (las genera el paso 1), a tamaño real y sin
  ampliar: huecos, cortes, capturas ilegibles, colores que no se distinguen.
- **Contraste:** `python3 procesos/skills-borrador/guia-estilos-previa/contraste.py`
  con cada par de colores del documento que **no esté** en la paleta de `estilo-documentos`.
  Si solo usa la paleta, basta con comprobar que no hay colores sueltos.

### 3. Rastrear cada afirmación

Para **cada cifra, dato, comparación y frase general**, busco su prueba.

| Si la fuente es… | Hago |
|---|---|
| El expediente | Compruebo que el expediente la respalda con una prueba guardada y una fecha |
| Datos guardados (Overpass, JSON) | **Recalculo la cifra** con el script del autor y la consulta guardada (A-015). Nunca me fío de la cifra escrita |
| Una captura (también la de Google de Iván, A-001) | Abro la captura y leo el dato literal y la fecha |
| Una reseña | Es una **pista, no un dato**: puede ser una pregunta para el cliente, nunca una afirmación sobre el negocio |
| Dos directorios que dicen lo mismo | Son **una sola fuente** si copian la misma ficha (normalmente, la de Google) |
| Nada | Error «afirmación sin fuente» |

Fallos que ya han salido y hay que buscar siempre:

- Cifras infladas por un filtro mal hecho, como contar tiendas como peluquerías.
- «El más cercano», «el primero», «el único», «pocas», sin comprobarlo con los datos.
- Ausencias afirmadas: «no tenéis web», «0 páginas que controléis».
- Opiniones nuestras presentadas como hechos: «es lo que más convence».
- Cifras **sin fecha**: notas, número de opiniones, precios de competidores. Caducan.
- Lo que el envío pregunta y a la vez da por hecho, por ejemplo el año de apertura.
- Detalles de color inventados («el sillón antiguo») y datos sin comprobar en una
  maqueta o un boceto.
- Citas retocadas, o la misma cita distinta en cada documento.

### 4. Cruzar los documentos del envío

Con la lista «Cifras con unidad, por documento» del paso 1 y los mensajes de WhatsApp:
**un dato, un valor, en todos.** Las cifras de los mensajes se copian del informe
aprobado, nunca se escriben de memoria. Si un documento dice «reciben más llamadas» y
otro «no llama para preguntar», es un error.

### 5. Pasar la lista de comprobación (abajo)

### 6. Probar el archivo donde lo abrirá el cliente

Ver «Probar un Word» y «Probar un PDF». Lo que no se haya podido probar va a «No comprobado».

### 7. Veredicto

En `clientes/<negocio>/revisiones/<fecha>-<envío>.md`, con el formato de abajo.
Después, a Federico con ESTADO / RESULTADO / PENDIENTE.

## Lista de comprobación

Cada error del veredicto lleva la letra de su apartado.

### A. Verdad y trazabilidad
- [ ] Cada cifra se puede señalar en su prueba o recalcular desde los datos guardados.
- [ ] Las cifras del censo salen de un script, con la consulta y la respuesta de Overpass guardadas (A-015).
- [ ] Cada cifra que caduca lleva fecha: notas, opiniones, precios, recuentos.
- [ ] Dos copias de lo mismo son una sola fuente; una reseña es una pista, no un dato.
- [ ] Cada cita tiene su prueba (captura o texto con URL y fecha) y es literal, con […] en los cortes.
- [ ] Ninguna frase general sin fuente («nadie…», «el cliente…», «lo que más…», «suele…»).
- [ ] Ninguna ausencia afirmada: «no hemos encontrado», nunca «no tenéis».
- [ ] Ningún superlativo sin contar: el más cercano, el primero, el único, pocos o muchos.
- [ ] Ninguna maqueta ni boceto lleva datos sin comprobar presentados como reales.

### B. Promesas y política
- [ ] **Ninguna llamada**, ni ofrecida ni insinuada («mejor momento para llamaros») (A-002).
- [ ] Nada que no hagamos: visitas, sesiones de fotos, servicios fuera de §6, plazos que no dependen de nosotros.
- [ ] Ninguna promesa de posiciones ni de resultados (§4.1, §10.3), tampoco disfrazada («se queda con las búsquedas»).
- [ ] Nada [PROPUESTA] como definitivo: precios, plazos, canales (§8.2, §9.1, §9.4). Hoy solo está decidido el dominio dentro de la cuota (A-011).
- [ ] El informe se ofrece como **«gratis y sin compromiso»** (A-005).
- [ ] Sobre Iván, lo aprobado: «lo importante (presupuestos, publicar vuestra web) lo revisa y aprueba Iván, el responsable» (A-004). Nada de «revisa todo».
- [ ] Identificación como asistente de IA en el primer mensaje al cliente (§9.3).
- [ ] Nunca se piden contraseñas (§12). Nada interno en el envío. Ni descuentos ni gratis sin aprobación (§8.1).

### C. Datos personales y legal
- [ ] **Ningún dato personal en lo que entra en git** (A-009, A-013): el paso 1 busca móviles, correos y documentos de identidad; los **nombres de personas** se miran a mano. Van en `privado/`.
- [ ] Si se piden datos personales, lleva cláusula informativa (responsable, finalidad, base y derechos).
- [ ] Solo se pide lo que hace falta **en ese momento** (§12). Los datos legales, las fotos y la aprobación de textos van en la tanda B.
- [ ] Fotos de personas: solo con permiso por escrito, y con menores, el de sus padres.
- [ ] Reseñas publicadas y competidores con nombre: según la regla provisional del expediente, hasta que responda el profesional (A-010).

### D. Coherencia
- [ ] Un dato, un valor, en todo el envío, mensajes incluidos (paso 4).
- [ ] Los datos del negocio son idénticos al expediente, y lo «a confirmar» se presenta como tal.
- [ ] **Nada que el envío pregunte se da por hecho** en otra parte del envío.
- [ ] Lo que se anuncia se cumple en el propio documento: «tres cosas» son tres; «sin retocar» es sin retocar.

### E. Lenguaje y tono (§9.2)
- [ ] Ortografía: `hunspell` (paso 1) **y** lectura entera. Una errata para el cliente es, como mínimo, importante.
- [ ] Tipografía española: comillas «», coma decimal, «€» detrás.
- [ ] Trato coherente (tú/vosotros, usted) y género correcto («la asistente»).
- [ ] Sin jerga sin explicar. Nada que pueda doler, como «se llamaban» o suposiciones sobre la familia.
- [ ] Las instrucciones se pueden seguir **en el formato**: en un Word no se puede «rodear»; en WhatsApp, una pregunta se contesta con un mensaje.

### F. Forma y legibilidad
- [ ] Sin huecos `[así]` salvo los intencionados, explicados al cliente, o los que Iván acepte por escrito.
- [ ] **Se lee en el móvil sin ampliar** (imágenes de 390 px, paso 1). La letra del cuerpo, igual o mayor que el mínimo de `estilo-documentos`.
- [ ] Informe: **2 páginas más un anexo, en A5** (A-005). La primera página funciona sola; la última es el siguiente paso.
- [ ] Nada cortado; capturas recortadas a lo que se comenta y legibles a tamaño real.
- [ ] Sin medias páginas vacías, salvo la última; páginas numeradas.
- [ ] Tanda A: **10 preguntas obligatorias como máximo**; el resto, condicionales y con su condición clara (choque 1).

### G. Accesibilidad mínima
- [ ] Idioma español (en el Word, `revisar_docx.py` sin avisos de idioma).
- [ ] Texto alternativo en todas las imágenes.
- [ ] Contraste: solo la paleta de `estilo-documentos`; los colores sueltos, con `contraste.py` (4,5 para texto y 3 para lo que no es texto).
- [ ] El significado no va solo en el color: rótulo o símbolo además del color.
- [ ] PDF etiquetado.

### H. Licencias
- [ ] Solo las tipografías e iconos aprobados (Inter, Fraunces y Lucide, A-008) o con licencia comprobada. Nada de fuentes de relleno del sistema.
- [ ] Atribución «© colaboradores de OpenStreetMap» con `openstreetmap.org/copyright` en cada mapa.
- [ ] Capturas de terceros: solo las necesarias para comentarlas.

### I. El archivo
- [ ] Word: `revisar_docx.py` sin problemas (estructura, propiedades, idioma, miniatura y texto alternativo).
- [ ] Word: la **versión de plantilla del pie la ha probado Iván en Word** (A-007), con su fecha en el registro de pruebas.
- [ ] Nombre claro; sin comentarios ni control de cambios; sin `~$…` ni `.DS_Store` en lo que se adjunta.
- [ ] Tamaño adecuado para WhatsApp y correo.

### J. Mensajes y plantillas de WhatsApp
- [ ] Se revisa el **texto exacto** que Iván va a copiar, mensaje a mensaje (A-003).
- [ ] Primer mensaje: quién escribe, que es asistente de IA y de dónde viene el contacto.
- [ ] Una idea por mensaje; cada pregunta, con su ID del catálogo de Reme.
- [ ] Cifras copiadas del informe aprobado (paso 4).
- [ ] Recordatorios a los 3 y a los 8 días laborables, sin presión ni promesas (A-012).
- [ ] Plantillas: los huecos `[nombre]`, `[día]` y similares, marcados y explicados para quien rellena.

## Probar un Word

**La parte automática** la hace `revisar_docx.py` en el paso 1. **La prueba de verdad la
hace Iván en Microsoft Word, una vez por versión de plantilla** (A-007), con esta lista:

1. Abrir el .docx **adjunto a un correo**, como lo recibiría el cliente. ¿Sale algún
   aviso de «reparar» o de contenido ilegible?
2. **Casillas:** marcar y desmarcar 3, de páginas distintas, una dentro de tabla.
   Guardar, cerrar y abrir: ¿siguen marcadas?
3. **Huecos:** escribir dos líneas en un recuadro grande y en una celda pequeña.
   ¿Crece la celda sin romper la página?
4. **Ortografía:** ¿sale el texto subrayado en rojo? Si sale, el idioma está mal.
5. **Aspecto:** ¿cuántas páginas tiene? ¿Hay algo descolocado respecto al PDF de LibreOffice?
6. Archivo › Propiedades: autor, título y fechas.
7. Guardar como PDF desde Word y pasármelo para compararlo.
8. En el móvil, si lo tiene a mano: abrirlo desde la app de correo. ¿Se lee?

Iván lo anota en el **registro de pruebas de Word**: versión de la plantilla, fecha,
resultado de cada punto y el PDF del punto 7. Sin esa línea, el punto I.2 no está
comprobado y el Word no sale.

## Probar un PDF

- En el móvil, a tamaño real (paso 1): ¿se lee sin ampliar?
- `pdfinfo`: páginas, formato y etiquetado. `pdffonts`: solo nuestras fuentes.
- Los enlaces, si los hay, funcionan.

## Escala de gravedad

| Gravedad | Cuándo | Ejemplos reales |
|---|---|---|
| **bloquea** | No puede salir así: falso, inventado como hecho, incumple AGENTS.md, una decisión de Iván o la ley, está roto o promete lo que no podemos hacer | Cifra de portada inflada; «vecino más cercano» falso; promesa de búsquedas; llamada ofrecida; datos personales sin cláusula o en git; hueco `[Empresa]`; Word fuera de esquema o sin probar |
| **importante** | Hay que arreglarlo antes de enviar. Solo Iván puede aceptarlo tal cual, por escrito | Frase general sin fuente; contradicción entre documentos; Word en inglés; no se lee en el móvil; contraste insuficiente; errata |
| **menor** | Conviene arreglarlo, pero no impide el envío | Medias páginas en blanco; un dato redondeado; capturas mal recortadas |

## Salida

```
# Revisión · <envío> · <negocio>
VEREDICTO: APROBADO / RECHAZADO
Resumen: N bloquean · N importantes · N menores, y qué hace falta para aprobar.
Qué he revisado: archivo · fecha · huella
Cómo lo he revisado · Lo que NO he podido comprobar
- **R01** [bloquea|importante|menor · A–J] Dónde · Qué pasa (con la prueba) · Qué debería pasar
Decisiones que necesita Iván
```

- **APROBADO**: cero errores que bloqueen, cero importantes sin aceptar por Iván, y nada
  esencial en «No comprobado».
- Los ID se mantienen entre versiones. En la re-revisión, cada uno queda **cerrado** (con
  prueba), **abierto** o **reabierto**.
- Si un error repite uno de una versión anterior que se compara, lleva «(= R05)».
- Si Iván acepta un error para las dos versiones que se comparan, lleva «(excluido de la
  comparación: motivo)» en los dos veredictos.

## Comparar dos versiones

```
python3 procesos/skills-borrador/revisar-entregable/comparar.py <veredicto base> <veredicto nuevo>
```

Cuenta los errores por gravedad y categoría, y las regresiones. El método completo,
con qué se mide y la regla de «mejor», está en el §8 de la
[revisión de Puri](../../ronda-1/revision-puri.md). Lo importante:

- **La vara se fija antes de ver lo medido.** Si aparece una comprobación nueva, se
  aplica a las dos versiones o a ninguna.
- Cuenta la **primera entrega** a Puri, no la versión corregida.
- No se puede mejorar callando: el envío tiene que seguir diciendo lo que tiene que decir
  (mensajes clave K1–K8).

## Lo que aprendí

- Ronda 1: los errores no estaban en la forma, sino **en los datos y en las frases
  generales**, y hay que rastrearlas una a una. Las cifras tecleadas a mano se desvían.
- Ronda 1b: la v0.2 **no vio 64 errores de estructura del Word** porque LibreOffice lo abre
  todo. Una herramienta de otro (`revisar_docx.py`) los vio. Por eso reutilizo sus
  comprobaciones en vez de escribir las mías.
- Ronda 1b: mi filtro de ortografía quitaba las palabras en mayúscula y dejaba pasar
  justo la errata real («Prefierís», a principio de frase). Lo destapó la prueba con un
  caso que tenía que fallar.

## Dudas abiertas

- **Mínimo de letra en el móvil.** El A5 a 11,5 pt sale a unos 10,7 px en una pantalla de
  390 px. ¿Lo da Lola por bueno? Para medirlo hace falta un número en `estilo-documentos`.
- **Colisión de ID:** mis errores son `R01`, y los requisitos de Reme, `R-01`.
  Propongo que los suyos sean `REQ-01`.
- **Registro de pruebas de Word:** ¿dónde lo anota Iván? Propongo una tabla en
  `operacion/` que mantenga Federico.
