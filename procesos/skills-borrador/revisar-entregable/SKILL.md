---
name: revisar-entregable
description: "Revisa todo documento o mensaje antes de que llegue a Iván o al cliente (informe PDF, cuestionario Word, email, mensajes de WhatsApp, presupuesto, guía): rastrea cada cifra y cada afirmación hasta su fuente, recalcula los datos, busca promesas, ausencias no probadas y huecos sin rellenar, comprueba datos personales, coherencia entre documentos, tono, ortografía, accesibilidad mínima, licencias y que el archivo funcione donde lo abrirá el cliente. Da veredicto APROBADO o RECHAZADO con cada error, su gravedad y su arreglo. Úsala con cada entregable antes de cualquier envío, y otra vez con cada versión corregida."
---

# revisar-entregable

> **BORRADOR v0.2 · revisado por Puri** · 2026-11-17 · **Dueña: Puri**
> Sobre la v0.1 de Federico. Sale de revisar el primer envío de la Peluquería
> Hermanos Cotillas: [veredicto](../../../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md),
> 63 errores en tres documentos.

## Cuándo

- Antes de que **cualquier** cosa salga hacia el cliente o hacia Iván para aprobarla:
  documentos, emails y mensajes de WhatsApp.
- Otra vez con **cada versión corregida**. Un arreglo se cierra cuando lo he
  comprobado, no cuando el autor lo da por hecho.
- Las webs tienen su propia lista (§11 y skill aparte). Esta es para documentos.

## Reglas

1. **Nadie revisa lo suyo.** Si el autor soy yo, otro agente lo revisa (lo asigna Federico).
2. **Yo no arreglo.** Describo el error y su arreglo; Federico se lo encarga a quien corresponda.
3. **Lo que no he podido comprobar no está aprobado.** Va en el veredicto, en «No comprobado».
4. **Reviso la versión exacta que se enviaría.** Anoto fecha y huella (`shasum -a 256`).
   Si cambia un byte, es otra versión.
5. **No rebajo la vara por el plazo.** Si hay prisa, se lo digo a Federico.

## Entrada

- Los entregables, en la carpeta `entregables/`, tal cual se adjuntarían.
- La **fuente de verdad**: el expediente **y** lo que lo respalda (capturas, datos
  guardados como el censo de OSM, la fuente de cada cita).
- AGENTS.md, la ficha del proceso y los criterios de aceptación de Reme, si los hay.

## Pasos

### 1. Comprobación automática

```
python3 procesos/skills-borrador/revisar-entregable/comprobar.py \
        clientes/<negocio>/entregables clientes/<negocio>/expediente.md
```

Saca:

- **Huecos sin rellenar** (`[Empresa]`…).
- **Cifras que no aparecen en el expediente.**
- **Frases con palabras de alarma** («todo», «nunca», «nadie», «suele», «se queda con», «os llamamos»…).
- **Idioma, propiedades, miniatura y texto alternativo del Word.**
- **Páginas, etiquetado y tipografías del PDF.**
- **Ficheros de bloqueo** (`~$…`) y **documentos internos** colados.

Es un punto de partida: señala dónde mirar, no lo que está bien.

### 2. Leerlo todo y verlo todo

- Texto entero: `pdftotext -layout`. El Word, convertido con
  `soffice --headless --convert-to pdf`.
- **Cada página como imagen** (`pdftoppm -r 60 -png`), mirada una a una: huecos,
  cortes, capturas ilegibles, colores que no se distinguen.

### 3. Rastrear cada afirmación

Para **cada cifra, dato, comparación y frase general**, busco la fuente. Las frases
generales son las que empiezan con «nadie», «el cliente nuevo…» o «lo que más…».

| Si la fuente es… | Hago |
|---|---|
| El expediente | Compruebo que el expediente la respalda con una captura o un dato guardado |
| Datos guardados (OSM, JSON) | **Recalculo la cifra** desde los datos. Nunca me fío de la cifra tecleada |
| Una captura | Abro la captura y leo la frase literal |
| Nada | Error: «afirmación sin fuente» |

Fallos que ya han salido y hay que buscar siempre:

- **Cifras infladas por un filtro mal hecho.** Ejemplo: tiendas de productos
  contadas como peluquerías.
- **«El más cercano», «el primero», «el único»** sin comprobar con los datos.
- **Ausencias afirmadas.** «No tenéis web», «0 páginas que controléis».
- **Opiniones nuestras presentadas como hechos.** «Es lo que más convence»,
  «una web abandonada resta más que no tener web».
- **Cosas que el documento pregunta y a la vez da por hechas.** Ejemplo: el año de
  apertura en la pregunta y «abrieron en…» en el texto propuesto.
- **Detalles de color inventados.** Ejemplo: «el sillón antiguo».
- **Citas retocadas.** Mayúscula nueva, cortes sin […] o la misma cita distinta en
  cada documento.

### 4. Cruzar los documentos del envío

Una tabla con cada dato que aparece en más de un documento: cifras, nombres,
número de opiniones, número de directorios, citas y promesas. **Un dato, un valor,
en todos.** Si un documento dice «reciben más llamadas» y otro «no llama para
preguntar», es un error.

### 5. Pasar la lista de comprobación (abajo)

### 6. Probar el archivo donde lo abrirá el cliente

Ver «Probar un Word» y «Probar un PDF». Lo que no pueda probar, a «No comprobado».

### 7. Veredicto

En `clientes/<negocio>/revisiones/<fecha>-<envío>.md`, con el formato de abajo.
Después, a Federico con ESTADO / RESULTADO / PENDIENTE.

## Lista de comprobación de documentos

### A. Verdad y trazabilidad
- [ ] Cada cifra se puede señalar en el expediente o recalcular desde los datos guardados.
- [ ] Cada cita de una reseña tiene su prueba (captura o texto con URL y fecha) y es literal; los cortes, con […].
- [ ] Ninguna frase general sin fuente («nadie…», «el cliente…», «lo que más…», «suele…»).
- [ ] Ninguna ausencia afirmada: «no hemos encontrado», nunca «no tenéis».
- [ ] Ningún superlativo sin comprobar: el más cercano, el primero, el único, pocos, muchos.
- [ ] Lo que no se ha podido medir se dice («no hemos podido consultar Google»), y el resto del documento no lo contradice.

### B. Promesas y política (AGENTS.md)
- [ ] Ninguna promesa de posiciones ni de resultados (§4.1, §10.3), tampoco disfrazada («se queda con las búsquedas»).
- [ ] Nada [PROPUESTA] comunicado como definitivo: precios, plazos, canales (§8.2, §9.1, §9.4).
- [ ] Todo lo que ofrecemos lo podemos hacer hoy: llamadas, visitas, fotos, «Iván revisa todo».
- [ ] Ningún servicio fuera de catálogo (§6). Ejemplo: fotografía.
- [ ] Identificación como asistente de IA si el texto le habla al cliente (§9.3).
- [ ] Nunca se piden contraseñas (§12).
- [ ] Nada interno en el envío: ni previo de precio ni guía de estilos.
- [ ] Ni descuentos ni gratis sin aprobación de Iván (§8.1).

### C. Datos personales y legal
- [ ] Si se piden datos personales, lleva **cláusula informativa** (responsable, finalidad, base, derechos).
- [ ] Solo se pide lo que hace falta **en ese momento** (§12). Los datos legales, después de aceptar el presupuesto.
- [ ] Fotos de personas: solo con permiso por escrito; con menores, el de sus padres.
- [ ] Publicar reseñas: con el permiso que diga el expediente.
- [ ] Terceros nombrados (competidores): solo hechos comprobables, sin valoraciones que puedan perjudicarles, salvo que Iván lo haya aceptado.

### D. Coherencia
- [ ] Un dato, un valor, en todos los documentos del envío (paso 4).
- [ ] Los datos del negocio (nombre, dirección, teléfono, horario) son idénticos al expediente, y lo «a confirmar» se presenta como tal.
- [ ] Lo que se anuncia se cumple en el propio documento: «tres cosas» son tres; «sin retocar» quiere decir sin retocar.

### E. Lenguaje y tono (§9.2)
- [ ] Ortografía y erratas: leído entero, palabra por palabra.
- [ ] Tipografía española: comillas «», cifras con coma decimal, «€» detrás.
- [ ] Trato coherente (tú/vosotros, usted) y género correcto («la asistente»).
- [ ] Sin jerga sin explicar.
- [ ] Nada que pueda doler: tiempos verbales sobre personas («se llamaban»), suposiciones sobre la familia.
- [ ] Las instrucciones se pueden seguir **en el formato del archivo**: en un Word no se puede «rodear».

### F. Forma y legibilidad
- [ ] Sin huecos `[así]` salvo los intencionados, que se explican al cliente.
- [ ] Nada cortado; capturas legibles al tamaño real y recortadas a lo que se comenta.
- [ ] Sin medias páginas vacías sin motivo; páginas numeradas si son más de 3.
- [ ] Extensión razonable para leerlo **en el móvil**. Cuestionario B1: 4 páginas como máximo (skill de Reme).

### G. Accesibilidad mínima
- [ ] Idioma del documento: español (en un Word, `es-ES` en los estilos).
- [ ] Imágenes con texto alternativo.
- [ ] El significado no va solo en el color; los colores tienen contraste suficiente.
- [ ] PDF etiquetado (`pdfinfo` → «Tagged: yes»).

### H. Licencias
- [ ] Imágenes, iconos y tipografías con licencia para uso comercial. Mejor una tipografía libre (OFL) que una del sistema.
- [ ] Atribución «© colaboradores de OpenStreetMap» en cada mapa.
- [ ] Capturas de terceros: solo las necesarias para comentarlas, y lo que haya decidido Iván.

### I. El archivo
- [ ] Nombre claro, con el del negocio.
- [ ] Propiedades limpias: autor, título y fecha reales; nada de «python-docx».
- [ ] Sin miniatura en blanco, sin comentarios ni control de cambios olvidados.
- [ ] Sin ficheros de bloqueo `~$…` ni `.DS_Store` en lo que se adjunta.
- [ ] Tamaño total adecuado para correo y WhatsApp.

## Probar un Word

Sin Microsoft Word solo se puede comprobar la estructura (paso 1). La prueba de
verdad la hace una persona en Word.

**Lista para Iván** (unos 10 minutos, en su Mac):

1. Abrir el .docx **adjunto a un correo**, como lo recibiría el cliente.
2. **Casillas:** marcar y desmarcar 3 de páginas distintas, una dentro de tabla.
   Guardar, cerrar y abrir: ¿siguen marcadas?
3. **Huecos:** escribir dos líneas en un recuadro grande y en una celda pequeña.
   ¿Crece la celda sin romper la página?
4. **Ortografía:** ¿sale el texto subrayado en rojo? Si sale, el idioma está mal.
5. **Aspecto:** ¿cuántas páginas tiene? ¿Algo descolocado respecto al PDF de LibreOffice?
6. Archivo › Propiedades: autor, título y fechas.
7. Guardar como PDF desde Word y pasárselo a Puri, para comparar con lo que vemos nosotros.

**Además, en el móvil:** abrirlo desde la app de correo y desde WhatsApp en un
iPhone o un Android. ¿Se lee? ¿Se puede rellenar? Si no, el cuestionario no va
por Word: va por WhatsApp, pregunta a pregunta (skill `primer-envio` de Menchu).

## Probar un PDF

- Verlo a tamaño real en el móvil: ¿se lee sin hacer zoom en cada página?
- `pdfinfo`: páginas, etiquetado y tamaño. `pdffonts`: tipografías incrustadas.
- Que los enlaces, si los hay, funcionen.

## Escala de gravedad

| Gravedad | Cuándo | Ejemplos reales |
|---|---|---|
| **bloquea** | No puede salir así: falso, inventado como hecho, incumple AGENTS.md o la ley, roto, o promete lo que no podemos hacer | Cifra de portada inflada; «vecino más cercano» falso; promesa de búsquedas; datos personales sin cláusula; hueco `[Empresa]`; Word sin probar |
| **importante** | Hay que arreglarlo antes de enviar. Solo Iván puede aceptarlo tal cual, por escrito | Frase general sin fuente; contradicción entre documentos; idioma del Word en inglés; «se llamaban» |
| **menor** | Conviene arreglarlo, pero no impide el envío | Medias páginas en blanco; «el asistente» por «la asistente»; un dato redondeado |

Una errata en un documento para el cliente es, como mínimo, **importante**.

## Salida

```
# Revisión · <envío> · <negocio>
VEREDICTO: APROBADO / RECHAZADO
Resumen: N bloquean · N importantes · N menores, y qué hace falta para aprobar.
Qué he revisado: archivo · fecha · huella
Cómo lo he revisado · Lo que NO he podido comprobar
R01 [bloquea|importante|menor] Dónde · Qué pasa (con la prueba) · Qué debería pasar
Decisiones que necesita Iván
```

- **APROBADO**: cero errores que bloqueen, cero importantes sin aceptar por Iván, y nada esencial en «No comprobado».
- Los ID (R01…) se mantienen entre versiones. En la re-revisión, cada uno queda **cerrado** (con prueba), **abierto** o **reabierto**.

## Lo que aprendí en la ronda 1

- Los errores no estaban en la forma, sino en **los datos y en las frases generales**.
  Hay que rastrearlas una a una; leer «por encima» no las encuentra.
- **Las cifras tecleadas a mano se desvían de los datos.** Se recalculan siempre.
- **La herramienta no sabe lo que mide:** el filtro de OSM contó tiendas como peluquerías.
- Lo que «se puede hacer en Word» no se sabe hasta probarlo en Word.

## Dudas abiertas

- ¿Quién revisa lo que escribo yo (veredictos y skills)? Propuesta: Federico.
- ¿Puedo usar el Word instalado en el Mac de Iván para las pruebas? Lo decide Iván.
