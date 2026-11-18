# Revisión de Chema · ronda 1

> E-002 · 2026-11-17 · Chema (Marketing digital y SEO)
>
> He revisado el expediente, el informe ([generar_informe.py](../../clientes/peluqueria-hermanos-cotillas/generar_informe.py)),
> los datos de [competencia/](../../clientes/peluqueria-hermanos-cotillas/competencia/), la sección 8 del
> [cuestionario](../../clientes/peluqueria-hermanos-cotillas/generar_cuestionario.py) y las herramientas.
> Todo lo que afirmo abajo lo he comprobado hoy; lo que no, va marcado como **duda**.
> No he tocado nada del cliente ni de otros agentes.

## 0. Resumen en cinco líneas

1. **El buscador no tiene arreglo técnico, tiene arreglo de fuentes.** Google, Bing, DuckDuckGo, Brave y Mojeek
   prohíben a los robots su página de resultados (`Disallow: /search` en su `robots.txt`). `buscar.sh` va contra eso:
   hay que retirarlo. Propongo **API oficiales con tope de gasto 0 €** (Google Places para la ficha y la competencia,
   Brave Search para la web) y **una captura manual de Google** por cliente. Opciones y costes en §7.
2. **El expediente llama «comprobado» a cosas que no lo están.** Dos directorios que copian la misma reseña de Google
   son **una** fuente, no dos.
3. **La competencia está mal elegida para el SEO local.** Hay 16 barberías y peluquerías de caballero a menos de
   500 m y solo se analiza una. Dos de las cuatro fichas son salones unisex o de señora.
4. **El informe tiene errores de cifras y frases que Puri debería rechazar.** Por ejemplo, «281» cuando son 273 y
   «el primero que tenga web se queda con las búsquedas», que es una promesa. Y es largo: propongo 2 páginas.
5. **Los textos se pasan de inferir.** Propongo una skill propia, `textos-web`, con una regla: *una reseña es una
   pista, no un dato; se convierte en pregunta, no en afirmación*.

## 1. Lo que mantendría

- **Las reglas 1–7 de [alta-cliente.md](../alta-cliente.md) §3.** Son buenas, sobre todo «no afirmar ausencias» y
  «toda frase trazable al expediente». Solo precisaría qué es una fuente independiente (ver §2).
- **Separar en el expediente lo comprobado de lo que hay que confirmar, con el motivo.** Es lo que nos va a evitar
  meter la pata con el cliente.
- **Leer las reseñas como fuente de tono y de lo que hace único al negocio.** Es lo mejor del trabajo: el «oficio
  heredado» y la fidelidad de décadas son el ángulo correcto.
- **El censo de OpenStreetMap como dato de densidad.** «33 peluquerías y barberías a menos de 250 m» lo he
  recalculado y cuadra. Es potente para el cliente.
- **La caja «Lo que no os vamos a prometer»** y explicar «no hemos medido volúmenes» en vez de inventarlos.
- **El análisis técnico de Salón Julia López es correcto:** lo he comprobado. Tiene cinco H1, el primero
  «INICIO», y sus datos estructurados son `Organization`, no `LocalBusiness`.
- **La web de Morote, caída:** el dominio ni siquiera resuelve en DNS.
- **Treatwell como fuente.** Su `robots.txt` no prohíbe los listados básicos de establecimientos.

## 2. Lo que cambiaría

### Búsqueda y fuentes

- **[bloquea] Retirar `herramientas/buscar.sh`** · Lee `bing.com/search` con un navegador automático, y el
  `robots.txt` de Bing dice `Disallow: /search` para todos los robots. Va contra la regla 3 de
  `herramientas-comunes` y contra la regla 5 de mi skill. Ser poco fiable es el problema menor · Paco lo retira y yo
  dejo de usarlo. La alternativa está en §7.
- **[bloquea] Redefinir «fuente independiente»** · El expediente da por comprobada la nota de Google (4,8, unas
  132 opiniones) con volumus.es y peluquerialolas.es. Ambas copian la ficha de Google, así que son una sola fuente
  secundaria, y quizá desactualizada. Lo mismo pasa con «dos hermanos, hijos de los anteriores dueños»: es **una**
  reseña reproducida en dos directorios · Regla nueva: *dos copias de lo mismo cuentan como una fuente*. Una reseña
  es la opinión de una persona, no un dato del negocio. Esas filas pasan a «por confirmar».
- **[importante] «Bing (ficha local)» no es una fuente primaria** · Esa ficha es Bing Places, que agrega datos de
  terceros. Se ve en la captura 01: el mapa es de TomTom y OSM. Sirve como fuente secundaria, nada más.
- **[importante] La ficha de Google no se ha leído y es lo más importante del SEO local** · Nos falta la categoría
  principal (¿«Peluquería» o «Barbería»?), si está reclamada, el enlace web, el número de fotos y si responden a
  las reseñas. La categoría principal es probablemente lo que más pesa para salir en «barbería Albacete» · Leerla
  con la API de Places (§7, opción B) o con una consulta manual (opción C).

### Expediente

- **[importante] Falta la lista de directorios** · Se dice «10+ fichas», pero no hay ni una URL. Esa lista, con
  nombre, dirección, teléfono y horario de cada una, es la auditoría de citas: el trabajo del SEO continuo y la
  prueba de «tres horarios distintos» · Tabla en el expediente: URL, NAP (nombre, dirección y teléfono), horario,
  errores y fecha de consulta.
- **[importante] Cada dato con fecha de consulta** · La nota y el número de opiniones cambian cada semana.
- **[menor] «Barrio Feria»** · Sale solo de OSM, y el informe acusa a un directorio de poner «el barrio
  equivocado». Con una sola fuente no podemos acusar a nadie · Por confirmar con el cliente.
- **[menor] «Público: sobre todo hombres y niños»** · Es una inferencia a partir de reseñas, no un dato. Va a una
  sección aparte, «Lo que intuimos», y se pregunta al cliente. El cuestionario ya lo pregunta.

### Informe

- **[bloquea] Cifra mal: «281 peluquerías en 1,5 km»** · El fichero tiene 282 locales sin contar al cliente, y 9
  son tiendas de suministros de peluquería (`hairdresser_supply`). Peluquerías y barberías son **273**. En el
  cuestionario además se redondea a «casi 300» · Usar «unas 270» y filtrar `shop=hairdresser` en la consulta.
- **[bloquea] Promesa encubierta** · «El primero de los dos que tenga una web bien hecha se queda con las búsquedas
  del barrio» contradice §10.3 y la propia caja de «no prometemos» · Quitarla.
- **[bloquea] Afirmar ausencias** · De Gentleman dice «Tampoco tiene web propia» y de NenaMelenas «Sin web propia
  encontrada», cuando no teníamos buscador fiable para comprobarlo · Quitar o poner «no la hemos encontrado en
  [fuentes]».
- **[importante] Frases sin fuente** (la regla 3 de Federico, otra vez): «sobre todo el joven, que es el que busca
  en el móvil», «quien busca "peluquería cerca" suele hacerlo desde el móvil», «estáis en una zona céntrica»,
  «una web abandonada resta más que no tener web», «lo que hacen los que mejor funcionan» (no hemos medido quién
  funciona) y, en el cuestionario, «los negocios que publican precios reciben más llamadas» · Quitarlas, o citar
  un estudio con fuente si existe. No lo he buscado; duda.
- **[importante] «Es la primera del listado de Treatwell»** · El orden de Treatwell lo decide Treatwell, y puede
  ser patrocinado. No es un ranking · Quitarlo.
- **[importante] La prueba visual es de Bing** · El informe se titula «¿Cómo os encuentran en internet?», pero la
  captura es de Bing. En España casi todo el mundo busca en Google (no tengo la cifra exacta a mano; duda). Además,
  el pie de foto dice «una lista de directorios» y en la captura solo se ven la ficha y un anuncio de Groupon ·
  Captura de Google (§7, opción C).
- **[importante] «hermanoscotillas.es parece libre»** · Se basa en que no tiene DNS, y un dominio puede estar
  registrado sin DNS. Si el cliente lo da por hecho y está cogido, quedamos mal · Comprobarlo en dominios.es antes
  de decirlo, o no mencionarlo hasta el presupuesto.
- **[importante] Tabla de anillos ambigua** · Las columnas «Peluquerías | Barberías» se leen como 33 + 7 = 40,
  cuando las 7 barberías están dentro de las 33 · Columnas «Total» y «De ellas, barberías».
- **[menor] Las capturas de competidores llevan el aviso de cookies** (captura 01 de Bing). En un documento de
  venta queda descuidado.

### Competidores (punto 5 de Federico)

- **[importante] Criterio nuevo** · NenaMelenas («Peluquería & BarberShop», a 868 m) y Julia López («Peluquería
  Unisex», peinados de boda) no compiten por el cliente de Hermanos Cotillas. Mientras tanto, a menos de 500 m hay
  **16** barberías y peluquerías de caballero. Una de ellas, The Barber Shop Toño, a 106 m, tiene Instagram según
  OSM, y el informe no la menciona. El criterio está en mi skill `estudio-competencia`:
  1. **Directos:** mismo público (caballero, barbería, niños) y a menos de 500 m, que es la distancia a pie.
  2. **De búsqueda:** los que salen en Google para las búsquedas objetivo. Son los que el cliente tiene que
     adelantar, estén donde estén.
  3. **Referente:** el mejor en digital de la ciudad con el mismo público.

  Fuera los de otro público, salvo que aparezcan en el punto 2. Como mucho cuatro en el informe.

### Textos propuestos (punto 6)

Sí, nos hemos pasado de inferir. Frase por frase:

| Texto | Problema | Cómo lo dejaría |
|---|---|---|
| «Le cortamos el pelo a tu padre. Ahora, a ti.» | La idea es buena, pero depende de que el negocio tenga dos generaciones en el mismo sitio, y eso no está confirmado. | Se mantiene como **variante A**, con la nota «si nos confirmáis que…». |
| «desde hace más de 30 años» | Sale de **una** reseña («más de 34 años»), de un cliente, no del negocio. | Hueco: «desde [año]». |
| «abrieron esta peluquería **en la calle Octavio Cuartero**» | Inventado: no sabemos si siempre estuvo ahí. El propio cuestionario lo pregunta. | «abrieron esta peluquería en [año]». |
| «**los hermanos Cotillas**» | Da por hecho que Cotillas es el apellido. Cotillas es también un pueblo de la provincia de Albacete (duda: no lo he comprobado hoy). | Pregunta: «¿De dónde viene el nombre?». Si hay historia, es oro. |
| «Puntuales: si tienes cita, no esperas» | Convierte un elogio de **una** reseña en un compromiso de servicio, y además da por hecho que trabajan con cita. | Fuera hasta que el cliente marque «trabajamos con cita» y «puntualidad». |
| «dos generaciones en el mismo local» / «del abuelo al nieto» | «Mismo local» no consta; las reseñas hablan de padre e hijo, no de abuelos. | «de padres a hijos», si se confirma. |
| «listo para triunfar» | Muy buena, pero en la reseña va **entre comillas**: parece una frase de los propios peluqueros. | Pregunta: «¿Es vuestra frase?». Si lo es, puede ser el lema. |
| «4,8 sobre 5, más de 130 opiniones» | Cifra que caduca y que hemos sacado de copias. | En la web, la nota en vivo de la ficha. En el texto, sin número. |

### Reseñas (punto 7)

- **[importante] En el informe y el cuestionario** (los lee el dueño): bien, como citas breves, literales y
  con «opinión publicada en Google». Máximo 2–3. Nunca el nombre del autor, y nada que identifique a una persona,
  como «el murciano».
- **[bloquea] En la web, ninguna copiada sin una de estas tres vías:**
  1. Un módulo oficial de Google que muestre la nota y las reseñas en directo, con atribución. Es la vía que
     recomiendo.
  2. Permiso por escrito de cada autor, que lo consigue el cliente.
  3. Que el cliente pida testimonios nuevos a sus clientes, con permiso desde el principio.

  Las reseñas son textos de sus autores y llevan datos personales. Además, la normativa europea de consumo
  (directiva «Ómnibus», UE 2019/2161) obliga a explicar cómo se garantiza que las reseñas que se muestran son de
  clientes reales y prohíbe falsearlas. Duda legal: no sé el artículo exacto de la transposición española. Que lo
  mire quien revise los textos legales (AGENTS.md §15).

### Informe: extensión y «regalar la estrategia» (punto 4)

- **[importante] Nueve páginas son demasiadas.** Un peluquero lo va a abrir en el móvil, por WhatsApp, entre
  cliente y cliente. Lo que hace que «flipe» es ver **su** caso, no el volumen: su ficha, sus reseñas, el
  directorio que dice que hace maquillaje de novia y quién sale antes que él en Google. Propuesta:
  - **Página 1, «Lo que ve hoy quien os busca»:** captura de Google con su nombre y con «barbería Albacete», tres
    cifras comprobadas y la conclusión.
  - **Página 2, «Tres cosas que os están costando clientes» y «Lo que haríamos»:** el *qué*, no el *cómo*. Después,
    el siguiente paso.
  - **Anexo, «Cómo lo hemos hecho»:** fuentes y límites, en una página.
- **Qué es regalar y qué no.** El diagnóstico se da: es lo que vende. No se dan la lista completa de búsquedas
  objetivo, las fichas detalladas de fallos de cada competidor ni el plan paso a paso. La sección 4 del informe
  actual (los cuatro factores del SEO local) es un curso que no vende, y la 5 es el plan entero. Las dos, fuera o
  a una línea.
- El formato (A4 o vertical para móvil) es de Lola. Yo propongo el contenido.

## 3. Lo que falta

1. **Lectura de la ficha de Google:** categoría principal y secundarias, si está reclamada, web, fotos, si
   responden a las reseñas y fecha de la última reseña (para saber si la ficha está viva).
2. **Auditoría de citas** (nombre, dirección y teléfono, y horario en cada directorio), con URL y fecha. Hoy no
   existe.
3. **Presencia en otros mapas:** Apple Maps, Bing Places (existe, se ve en la captura 01) y Waze. Un móvil
   iPhone usa Apple Maps por defecto.
4. **Comprobar el censo con una muestra:** OSM puede incluir negocios cerrados. Con 10 de los 33 del anillo de
   250 m, comprobados con el estado del negocio en Places (`businessStatus`), sabríamos el margen de error antes
   de poner «33» en grande.
5. **Medir las webs de la competencia.** La API de PageSpeed Insights (Lighthouse en la nube de Google) es gratis
   y no hay que instalar nada. La he probado sin clave y responde «429: cuota diaria agotada»: la cuota anónima es
   compartida y no sirve. Con una clave gratuita de Google Cloud debería funcionar (duda: no he podido confirmar
   el límite exacto).
6. **Fecha de consulta** en cada cifra del informe.
7. **Qué buscan de verdad:** ver §6 de Iván y mi skill (punto 3 de Federico).

## 4. Mis skills: qué he cambiado y por qué

### `investigar-cliente` (v0.2)

- **Fuentes por niveles**, con lo que vale cada una: primaria (el negocio y su ficha de Google), secundaria
  independiente (OSM, Bing Places, Apple Maps, Treatwell, prensa) y copias (directorios: solo NAP y para auditar).
- **Regla de independencia:** dos copias de lo mismo son una fuente. Una reseña es una pista, no un dato.
- **Sin `buscar.sh`:** búsqueda con API oficiales o captura manual (§7), y comprobación directa de URL candidatas
  (dominio propio, perfil de Instagram que aparezca en la ficha o en OSM).
- **Pasos nuevos:** leer la ficha de Google, auditoría de citas, presencia en mapas y estado de las reseñas.
- **Expediente con fecha de consulta** y sección «Lo que intuimos (preguntar)».
- **Respeto de condiciones de uso:** `robots.txt` y condiciones de cada fuente antes de automatizar nada. Lo que
  sale de la API de Google no se guarda, salvo el identificador de la ficha.

### `estudio-competencia` (v0.2)

- **Criterio de competidores** de tres tipos (directos, de búsqueda y referente), con un máximo de cuatro.
- **Censo limpio:** solo `shop=hairdresser` (y `barber` si existe la etiqueta), comprobación por muestreo y
  columnas sin ambigüedad.
- **Búsquedas objetivo sin inventar volúmenes:** se eligen por intención, a partir de las categorías de Google de
  los competidores, del autocompletado oficial (si hay API) y de las palabras de las reseñas. Se marcan como
  «prioridad estimada, no medida».
- **Informe de 2 páginas más un anexo,** con la línea entre diagnóstico y estrategia escrita.
- **Lista negra de frases** (generalizaciones sin fuente, promesas y ausencias) para revisarlas antes de que lo
  haga Puri.

### `textos-web` (nueva, v0.1)

Los textos merecen skill propia: se usan dos veces (propuestas en el cuestionario y textos definitivos de la web),
tienen reglas que no son de Reme y son lo que más se lee de la web. Reme decide **qué se pregunta**; yo, **cómo
se cuenta**. Mi skill entrega la sección de textos ya trazada y Reme la incluye en el cuestionario.

## 5. Lo que necesito de otros agentes (lo coordina Federico)

| Para | Qué | Por qué |
|---|---|---|
| **Paco** | Retirar o desactivar `herramientas/buscar.sh` y quitarlo de [alta-cliente.md](../alta-cliente.md) §4 y de `herramientas-comunes`. | Va contra el `robots.txt` de Bing (§2). |
| **Paco** | Si Iván aprueba las opciones A o B de §7: un `buscar_web.sh` (Brave) y un `ficha_google.sh` (Places) con tope de consultas y clave en el gestor de secretos, nunca en el código. | Herramientas comunes; las mantiene él. |
| **Paco** | Si Iván aprueba la clave de PageSpeed Insights: un `medir_web.sh`. | Medir las webs de la competencia sin instalar Lighthouse. |
| **Paco** | Que `captura.sh` quite los avisos de cookies (ya lo tiene pendiente). | Capturas presentables. |
| **Reme** | Que la sección 8 del cuestionario la genere mi skill `textos-web`, y añadir tres preguntas: «¿De dónde viene el nombre "Cotillas"?», «"Listo para triunfar", ¿es vuestra frase?» y «¿Trabajáis con cita?» (esta ya está). | Ver §2, textos. |
| **Reme** | Quitar del cuestionario «casi 300 peluquerías» y «los negocios que publican precios reciben más llamadas». | Cifra mal y frase sin fuente. |
| **Lola** | Formato del informe de 2 páginas pensado para leerse en el móvil. | Ver §2, punto 4. |
| **Puri** | Añadir a su lista de comprobación: «dos copias = una fuente», «nada de ausencias», «ninguna generalización sin fuente» y «cifras con fecha». | Son los fallos que he encontrado. |
| **Federico** | Actualizar [alta-cliente.md](../alta-cliente.md): la regla 1 (independencia), §4 (Bing, Places, Brave y PSI) y la skill `textos-web` en §6. | Es suyo. |

## 6. Lo que tiene que decidir Iván (lo lleva Federico)

```
QUÉ:         Cómo buscamos en internet (sustituye a buscar.sh)
CLIENTE:     interno
POR QUÉ:     Sin buscador no se comprueban redes, webs ni competidores reales. Leer las páginas de
             resultados de Google o Bing con un robot va contra lo que piden esos buscadores. Opciones en §7.
PROPUESTA:   B + A + C: Google Places API y Brave Search API, ambas con tope duro de consultas para quedarnos
             en 0 €, más una captura manual de Google por cliente. Probarlas una semana con este caso.
ALTERNATIVA: Solo C (manual) más fuentes abiertas: 0 € y sin cuentas, pero cuesta unos 10 min de una persona
             por cliente y no escala.
URGENCIA:    esta semana (bloquea repetir el caso en la ronda 2)
ENLACE:      procesos/ronda-1/revision-chema.md §7
```

```
QUÉ:         Cómo mostramos las reseñas de Google en las webs de los clientes
CLIENTE:     interno (afecta a todas las webs)
POR QUÉ:     Copiar reseñas tiene problemas de derechos, de datos personales y de normativa de consumo.
PROPUESTA:   Solo con un módulo oficial de Google en directo, o con permiso por escrito del autor. Revisarlo
             con quien revise los textos legales (§15).
ALTERNATIVA: No mostrar reseñas en la web; solo la nota y un enlace a la ficha.
URGENCIA:    sin prisa (antes de la primera web real)
ENLACE:      revision-chema.md §2, «Reseñas»
```

```
QUÉ:         Informe de venta de 2 páginas más un anexo, en vez de 9
CLIENTE:     interno
POR QUÉ:     Se lee en el móvil. Lo que impresiona es lo concreto de su caso, no el volumen. Las 9 páginas
             regalan el plan entero.
PROPUESTA:   2 páginas de diagnóstico y el «qué haríamos» (sin el cómo), más el anexo de fuentes.
ALTERNATIVA: Mantener un informe largo, pero solo para quien contrate (entregable de arranque).
URGENCIA:    esta semana (para la ronda 2)
ENLACE:      revision-chema.md §2, «Informe: extensión»
```

Hay otras dos decisiones pequeñas que se pueden agrupar: si se crea una cuenta de Google Ads solo para el
Planificador de palabras clave (§7) y si se pide una clave gratuita para PageSpeed Insights.

## 7. Herramientas: qué necesito o propongo

### 7.1 Lo que he comprobado hoy

| Comprobación | Resultado |
|---|---|
| `robots.txt` de Google, Bing, DuckDuckGo, Brave Search y Mojeek | Todos tienen `Disallow: /search` (o `/html`) para cualquier robot. **Leer sus resultados con un robot va contra lo que piden.** |
| Google Custom Search JSON API | **Cerrada a clientes nuevos**; desaparece el 1 de enero de 2027. Descartada. |
| Bing Search API | **Retirada el 11 de agosto de 2025.** Descartada. |
| Brave Search API | Prepago: 5 $ por 1.000 búsquedas, **con 5 $ de crédito gratis al mes** (unas 1.000 búsquedas). Tiene también autocompletado (5 $ por 10.000). |
| Google Places API (New) | Por campo: nota, número de opiniones, web, horario y teléfono son nivel «Enterprise»: **1.000 consultas gratis al mes** y después 35 $ por 1.000. Las reseñas, «Enterprise + Atmosphere»: 1.000 gratis y después 40 $ por 1.000. Categoría y estado del negocio, nivel «Pro»: 5.000 gratis. |
| Condiciones de Places | **Solo se puede guardar el identificador de la ficha** (y las coordenadas, 30 días). No se pueden copiar ni guardar nombres, direcciones ni reseñas, ni usarlas fuera del servicio. **En la UE no se pueden mostrar sobre ningún mapa**, ni siquiera de Google. |
| PageSpeed Insights API sin clave | Responde 429 (cuota anónima agotada). Hace falta una clave propia. |
| Agente «research» de la suscripción de Copilot | **No tiene buscador**, solo descarga URLs. No sirve. Además intentó leer Bing por su cuenta, contra su `robots.txt`; si se usa, hay que prohibírselo en el encargo. |

### 7.2 Opciones para buscar (punto 1 de Federico)

| | Opción | Qué resuelve | Coste | Abre ventanas | Pegas |
|---|---|---|---|---|---|
| **A** | **Brave Search API** | Buscar el nombre, redes (`site:instagram.com`), prensa y webs de competidores. Su autocompletado sirve para ideas de búsquedas reales. | **0 €** con el crédito gratis (unas 1.000 búsquedas al mes; un cliente usa unas 20). Prepago: el techo es lo que se cargue. | No | Hace falta una cuenta y probablemente una tarjeta (duda). Su índice no es el de Google: hay que probar la cobertura de negocios pequeños de España antes de fiarse. Duda: si deja guardar los resultados. |
| **B** | **Google Places API** | **Leer la ficha de Google** (punto 2): nota, opiniones, categoría, horario, web y estado. Y saber **qué peluquerías devuelve Google** para «barbería Albacete» (lo más parecido al «pack local» sin leer Google). | **0 €** con un **límite diario de consultas** en Google Cloud (por ejemplo, 30 al día), que corta antes de pasar del tramo gratis. Un cliente usa unas 10. | No | Cuenta de Google Cloud **con tarjeta**. Condiciones estrictas: se consulta para comprobar y elegir, pero el contenido no se guarda ni se pega en el informe, y no se pinta en mapas. Duda legal: si podemos escribir «4,8 en Google» en el informe sacándolo de aquí. |
| **C** | **Captura manual de Google** | La foto real de lo que ve el cliente: su nombre y una búsqueda genérica en Google y Maps. Es la prueba visual del informe. | 0 € | **Sí** (la hace una persona) | Unos 5–10 min de Iván por cliente. Le preparo los enlaces exactos y lo que hay que capturar. |
| **D** | Solo fuentes abiertas (OSM, Treatwell, URL directas, preguntar al cliente) | Lo básico | 0 € | No | No encuentra redes ni competidores por búsqueda. Es lo que tenemos hoy. |
| **E** | Acceso a la ficha de Google del cliente (gestor delegado, §12) | **Todo**, incluidas las búsquedas reales por las que le encuentran. | 0 € | No | Solo cuando ya es cliente. **Imprescindible para el SEO continuo y el informe mensual.** |
| ✗ | Robot sobre Google, Bing o DuckDuckGo (con o sin ventana) | — | — | — | **Descartado:** va contra su `robots.txt` y sus condiciones, y Google pide captcha. |
| ✗ | API que revenden resultados de Google (tipo SerpAPI) | — | — | — | **Descartado:** obtienen los resultados raspando Google. Es lo mismo de arriba, pagado. No he mirado precios. |

**Recomendación:** **B + A + C** antes de contratar y **E** después.
- B resuelve la ficha y la competencia real.
- A resuelve las redes y la web.
- C da la única prueba visual honesta para el informe.

Coste esperado: **0 €** con los topes puestos. Riesgo: tener una tarjeta asociada a dos cuentas; por eso pido
topes **duros** (límites de consultas), no solo alertas.

**Duda que no puedo resolver yo:** si Iván tiene alguna suscripción que ya incluya búsqueda web (por ejemplo, un
asistente de IA con buscador), sería la opción preferente según sus normas. Habría que probarla con las mismas
cuatro búsquedas que he usado yo.

### 7.3 Volúmenes de búsqueda (punto 3 de Federico)

Respuesta honesta: **no hay forma gratuita de saber cuántas veces se busca «peluquería caballero Albacete»**.
Opciones que no inventan nada:

1. **Planificador de palabras clave de Google Ads.** Gratis con una cuenta de Ads, sin gastar. Sin campañas
   activas creo que muestra **intervalos** (10–100, 100–1.000) en vez de cifras (duda: no lo he podido confirmar
   en la ayuda de Google). Sirve a nivel ciudad; a nivel barrio saldrá «0–10». Crear la cuenta lo decide Iván.
2. **Google Trends.** Gratis, de uso manual. Da **comparaciones relativas** («barbería» frente a «peluquería» en
   Castilla-La Mancha), no cifras. Sirve para elegir entre palabras.
3. **Autocompletado de Brave (API oficial, opción A).** Dice qué escribe la gente, sin volumen.
4. **Después de contratar:** las búsquedas reales de la ficha de Google (opción E) y Search Console. **Esto es lo
   único que mide de verdad**, y es lo que va en el informe mensual.

En el informe de venta las búsquedas van como «**prioridad estimada por lo que busca vuestro cliente, no
medida**», sin cifras. Es lo que ya hizo Federico; solo cambia que la lista sale de fuentes y no de memoria.

### 7.4 Nada instalado

No he instalado nada ni he creado cuentas. Las pruebas han sido de lectura: `robots.txt`, páginas de precios y
condiciones, una petición a salonjulia.es, consultas DNS y una petición a PageSpeed Insights.

## 8. Ronda 1b

> E-008 · 2026-11-18 · Skills en v0.3 con las decisiones de Iván
> ([aprobaciones](../../operacion/aprobaciones.md)) y la [consolidación](consolidacion.md).

### 8.1 Qué he cambiado

| Skill | Cambio | Por |
|---|---|---|
| [`investigar-cliente`](../skills-borrador/investigar-cliente/SKILL.md) | **Guion de captura manual para Iván**: 9 capturas y unos 10 minutos. Lleva enlaces exactos, ventana privada, solo la ventana del navegador, sin renombrar nada y las capturas a `privado/`. Lo genera [`enlaces_captura.py`](../skills-borrador/investigar-cliente/enlaces_captura.py). | A-001 |
| | Sin API: Google lo mira una persona; lo demás, fuentes abiertas, después de leer su `robots.txt`. | A-001 |
| | «Reclamar esta empresa» en la ficha: si sale, la ficha no está reclamada. Responde a una duda de la v0.2. | — |
| | **Cada cita de reseña con su prueba**, guardada en `privado/` porque lleva el nombre del autor. | Puri R30, A-009 |
| | **Nada personal en `expediente.md`**: ni autores de reseñas ni nombres de los dueños. | A-013, A-009 |
| | Cómo contesta el negocio a las reseñas: es su voz, y la usa `textos-web`. | Lola (tono) |
| [`estudio-competencia`](../skills-borrador/estudio-competencia/SKILL.md) | **Cifras por script**: [`censo.py`](../skills-borrador/estudio-competencia/censo.py) genera la consulta de Overpass, calcula `cifras.json` desde la respuesta guardada (con fecha de los datos y huella) y los puntos del mapa. Ninguna cifra en la plantilla. | Puri R03–R05 |
| | Overpass solo por la instancia que fije Paco; si no está fijada, no se lanza. | A-015 |
| | **Informe A5: 2 páginas más un anexo.** La página 1 funciona sola (es la imagen de WhatsApp). La 2 lleva el aviso de los directorios, una o dos opiniones y la frase principal como idea. El anexo cierra con el siguiente paso y el contacto. «Gratis y sin compromiso». | A-005, Lola, Reme, Menchu |
| | **Lo que no se regala**, escrito: 6 puntos. | consolidación |
| | Competidores «de búsqueda» sacados de la captura de Iván, no de una API. Las búsquedas objetivo se eligen **antes** del guion, porque van dentro. | A-001 |
| | Atribución `openstreetmap.org/copyright` en el mapa y en el anexo. | Paco |
| [`textos-web`](../skills-borrador/textos-web/SKILL.md) | **Ficha de tono** (antes, en la guía de Lola): fuentes por orden, tratamiento, rasgos con fuente, palabras prohibidas y pares «así sí / así no» sin datos sin comprobar. | Lola, consolidación |
| | **Frase principal de 45 caracteres como mucho**, medida, y en 2 variantes. | Lola |
| | **Tres modos según las tandas:** muestra (informe), propuesta (tanda B) y definitivo. Los textos completos ya no van antes del presupuesto. | Reme, Menchu |
| | **Lista de frases vigiladas** ([`frases-vigiladas.txt`](../skills-borrador/textos-web/frases-vigiladas.txt)) con [`vigilar_frases.py`](../skills-borrador/textos-web/vigilar_frases.py). Nivel B (bloquea) y R (con traza). | Puri |
| | La historia del negocio, de sus **audios de WhatsApp** transcritos en local. | A-002, Menchu |

### 8.2 Cómo he probado las tres herramientas

Todas usan solo Python del sistema, sin instalar nada. Cada prueba la he comprobado
**rompiendo el código a propósito**: si la prueba no falla, no sirve.

| Herramienta | Pruebas | Mutaciones detectadas | Además |
|---|---|---|---|
| `censo.py` | 9 | 11 de 11 (quitar el filtro de tiendas, contar al cliente, anillos, duplicados, regex en la consulta, distancia, atribución, ejes del mapa…) | Contrastado con los datos de la ronda 1 (reconstruidos en `/tmp`): **33** a menos de 250 m (7 de caballero) y **273** en 1,5 km. Coincide con el recuento a mano de Puri y mío. |
| `vigilar_frases.py` | 7 | 10 de 10 | Sobre el envío de la ronda 1 marca **5 B en el informe y 5 en el cuestionario**, todos errores que ya habíamos visto. Las pruebas encontraron dos cosas que he corregido: un hueco («el joven, que busca en el móvil» se escapaba) y un falso positivo (nuestra frase «Nadie puede garantizar…» bloqueaba). |
| `enlaces_captura.py` | 8 | 9 de 9 (fuera de `privado/`, sin idioma, más de 3 búsquedas, sin comillas en redes, mapa sin centrar, sin escapar HTML…) | Guion de ejemplo generado en `/tmp` y revisado como imagen. |

Ejecutar desde la raíz: `python3 -m unittest discover -s procesos/skills-borrador/<skill>/pruebas`.

### 8.3 Dos hallazgos nuevos

1. **En la ronda 1, el mapa y la tabla medían distinto.** `puntos-metros.json` (el mapa)
   y `competidores-osm-1500m.json` (la tabla) difieren hasta un 1,5 %, y un local cambia
   de anillo según cuál se mire. Con `censo.py mapa`, los dos salen del mismo cálculo.
2. **«El vecino más cercano» era cierto solo a medias.** Hay tres peluquerías más cerca
   (Actuall, a 41 m; My Bell, a 47 m; MG Peluqueros, a 52 m), pero **Barber Shop
   Gentleman (79 m) sí es el más cercano de caballero**. Con el criterio de público por
   separado, el script lo dice sin ambigüedad.

### 8.4 Respuestas a otros agentes

| A | Respuesta |
|---|---|
| **Menchu** (¿el anexo va al cliente? ¿habrá imagen de la primera página?) | **Sí, el anexo va al cliente**, dentro del mismo PDF: es nuestra transparencia sobre fuentes y límites. **Sí, habrá imagen** de la página 1 (`pagina-1.png`, con `pdftoppm`), que escribo para que se entienda sola. |
| **Reme** (¿la historia por teléfono?) | Sin teléfono (A-002). Me vale lo que propone Menchu: **audios de WhatsApp transcritos en local**. Los textos completos van en la tanda B; al informe, solo la frase principal como muestra, el aviso de los directorios y una o dos opiniones, como pediste. |
| **Lola** | Asumo el tono en `textos-web`. Frase principal ≤ 45 caracteres, medida. Los límites de palabras del informe son orientativos hasta tu maqueta A5. |
| **Puri** | Lista negra y prueba de cada cita, hechas (§8.1). |
| **Paco** | No he tocado `generar_informe.py` de la ronda 1 (pedías añadir la atribución en la línea 267): en la ronda 2 se rehace desde cero, y tu `mapa.py` ya la lleva dentro de la imagen. Si prefieres arreglar el viejo, dímelo y lo hago. |

### 8.5 Lo que necesito de otros agentes (lo coordina Federico)

| Para | Qué | Por qué |
|---|---|---|
| **Paco** | Fijar la instancia de Overpass (A-015) y decirme cómo se lanza la consulta guardada. Si haces una herramienta común que guarde consulta y respuesta, `censo.py` lee su salida tal cual. | Sin eso, el paso 1 de `estudio-competencia` no se lanza. |
| **Paco** | Revisión técnica de mis tres scripts (choque 4: se quedan en mi skill salvo que decidas lo contrario). Formato de `censo.py mapa`: el que ya lee `mapa.py` (`[este_m, norte_m, destacado, nombre]`). | Que no rompan nada tuyo. |
| **Puri** | Que tu `comprobar.py` lea `textos-web/frases-vigiladas.txt` en vez de mantener otra lista de «palabras de alarma». Si prefieres la tuya, dime qué patrones te faltan y los añado aquí. | **Una sola lista**; si no, se desincronizan. |
| **Puri** | Para comparar la ronda 2 con la de Federico, te propongo dos medidas que ya salen solas: **avisos B de `vigilar_frases.py`** (5 + 5 en la ronda 1) y **cifras escritas a mano en la plantilla** (`grep -nE '[0-9]'`). | Vara de medir del bono, sin depender del criterio de nadie. |
| **Reme** | La tanda B lleva el bloque de textos de mi modo «propuesta». Preguntas que salen de él: «¿De dónde viene el nombre?» y «"Listo para triunfar", ¿es vuestra frase?». | `textos-web`. |
| **Lola** | Confirmar con la maqueta A5 los límites de palabras de las tres páginas. | `estudio-competencia`, paso 5. |
| **Federico** | En `alta-cliente.md`: la **captura manual de Iván** entre la fase 1 y la 2, con **las búsquedas objetivo elegidas antes del guion**. Coste para Iván: unos 10 minutos por cliente. | Cambia el orden de las fases. |

### 8.6 Para Iván (lo lleva Federico)

Nada nuevo que aprobar. Dos cosas que solo él puede confirmar en la ronda 2:
1. Que las 9 capturas le caben en 10 minutos. Si no, quito la tercera búsqueda y bajan a 8.
2. Que el enlace del mapa centrado en la calle del cliente funciona. Usa un formato de
   Google Maps no documentado; el guion dice cómo hacerlo a mano si falla.

### 8.7 Lo que queda abierto

- La instancia de Overpass (A-015, Paco). Bloquea el censo de la ronda 2.
- Los recortes de capturas de Google con competidores en el informe: paquete legal (A-010).
  Mientras, en el informe solo va la ficha del propio cliente.
- Las API (Places, Brave): se prueban después de la ronda 2 (A-001).
