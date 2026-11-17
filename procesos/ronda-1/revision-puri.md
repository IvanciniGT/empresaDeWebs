# Revisión de Puri · ronda 1

> Puri (Calidad) · 2026-11-17 · Encargo E-006
> Veredicto completo: [2026-11-17-primer-envio.md](../../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md)
> Skill: [revisar-entregable v0.2](../skills-borrador/revisar-entregable/SKILL.md) y su
> script [comprobar.py](../skills-borrador/revisar-entregable/comprobar.py)

**En una frase:** el primer envío está **RECHAZADO**, con 9 errores que bloquean, 33
importantes y 21 menores. Los que más importan no son de forma: son **datos y frases
sin fuente**. La cifra de la portada está inflada, el «vecino más cercano» no lo es,
y hay más de veinte frases del mismo tipo que las seis que quitó Federico.

## 1. Lo que mantendría

- **La estructura del informe:** primero lo bueno, después lo que falta, con
  fuentes y límites al final. El recuadro «Lo que no os vamos a prometer» es justo
  lo que tiene que decir la empresa (§4.1).
- **«Lo que ya sabemos» separado de «lo que falta»** en el cuestionario: el cliente
  corrige en vez de escribir desde cero.
- **El expediente con «comprobado» y «a confirmar»** y la regla de las dos fuentes.
  Es lo que me ha permitido revisar: sin él no habría vara de medir.
- **Guardar los datos crudos** (JSON de OSM, capturas). Gracias a eso he podido
  recalcular las cifras y encontrar el error de R03.
- **Las casillas del Word como controles de contenido de verdad** (`w14:checkbox`),
  no como el carácter ☐ suelto.
- **El aviso de «nunca nos mandéis contraseñas»** (§12) y la identificación como IA (§9.3).

## 2. Lo que cambiaría

- [bloquea] **Las cifras se teclean a mano en la maqueta** · Así salió «281» cuando el fichero da 282, y además contaba 9 tiendas de productos (R03). El cuestionario dice «casi 300» (R04) · Que el generador lea las cifras del cálculo guardado y que ningún número se escriba a mano. Es tarea de Chema y Paco (§5).
- [bloquea] **Las frases generales no tienen fuente** · Son más de veinte (R10–R27): «es lo que más convence», «nadie elige por cercanía», «reciben más llamadas»… Son el mismo error que las seis que encontró Federico, y releer no basta para encontrarlas: se escriben solas · Regla en las skills de quien escribe: o tiene fuente, o se presenta como opinión, o se quita. En mi skill, se rastrean una a una (paso 3).
- [bloquea] **Prometemos cosas que nadie puede hacer** · Una llamada (R07), ayuda con las fotos (R35) y que «Iván revisa todo» (R42) · Ninguna oferta al cliente sin dueño que la cumpla. Lo decide Iván (§6).
- [bloquea] **Datos personales sin cláusula y antes de tiempo** (R08) · Se pide el NIF «para empezar» sin haber presupuesto, y sin informar del tratamiento (RGPD) · Datos legales en la tanda B. Cláusula en todo documento que pida datos. Reme ya lo recoge en su skill v0.2.
- [importante] **«Revisión» en el proceso como un paso único** · Hace falta revisar también cada versión corregida, con los mismos ID de error, y fijar qué versión se revisa (huella) · Ya está en mi skill. Propongo a Federico que la fase 6 de `alta-cliente.md` diga «hasta APROBADO».
- [importante] **El Word se genera con la plantilla por defecto de python-docx** · De ahí salen el idioma inglés, el autor «python-docx», la fecha de 2013 y la miniatura en blanco (R39, R40, R61) · Que el generador lo fije. Es de Paco (§5).
- [importante] **Los textos propuestos dan por hecho lo que se pregunta** (R26, R27) · «Abrieron esta peluquería en la calle…» y, en la misma página, «¿siempre ha estado en esa calle?» · Los textos solo con hechos del expediente. Lo demás, como hueco.
- [menor] **El informe y el cuestionario usan tipografías distintas** (R62), y una es de sistema de Apple con licencia dudosa para entregables · Una tipografía libre común. Es de Lola.

## 3. Lo que falta

- **Prueba en Microsoft Word y en el móvil.** Nadie ha visto el cuestionario como lo
  verá el cliente. Propuesta en §7.
- **Prueba de cada cita.** De cinco de las nueve citas no hay captura, y una es la
  cifra que más usamos, «más de 34 años» (R30).
- **Un corrector ortográfico.** «¿Prefierís?» (R59) se me podría haber escapado: lo
  encontré leyendo. Propuesta en §7.
- **Criterios de aceptación escritos para los documentos.** Reme los tiene para la
  web; para el primer envío los he tenido que deducir de AGENTS.md y del proceso.
  Mi lista de comprobación (skill, apartados A–I) puede servir de base.
- **Quién revisa a la revisora.** Mis veredictos y mi skill no los revisa nadie.
  Propongo que Federico lea cada veredicto antes de que llegue a Iván.

## 4. Mis skills: qué he cambiado y por qué

**`revisar-entregable` v0.1 → v0.2** ([SKILL.md](../skills-borrador/revisar-entregable/SKILL.md)):

| Cambio | Por qué |
|---|---|
| **Pasos** en vez de solo una lista: automático → leer y ver cada página → rastrear → cruzar documentos → lista → probar el archivo → veredicto | La v0.1 decía *qué* mirar, no *cómo*. Lo que más errores ha dado (rastrear y cruzar) no estaba |
| **Rastrear cada afirmación hasta su prueba**, y recalcular las cifras desde los datos | Así aparecieron R03 y R05, que con «¿está en el expediente?» no salen, porque el expediente no tenía el censo |
| **Cruzar los documentos del envío**: un dato, un valor | Tres versiones de la misma cifra, y dos frases que se contradicen (R04, R25, R43) |
| **Lista propia para documentos** (A–I): verdad, promesas, datos personales, coherencia, tono, forma, accesibilidad, licencias, archivo | §11 es para webs. Faltaban datos personales, accesibilidad, archivo y las instrucciones que no se pueden seguir en el formato |
| **Escala de gravedad con ejemplos reales** | Para que la gravedad no dependa de mi humor y la ronda 2 se mida igual |
| **ID de error estables y re-revisión** (cerrado / abierto / reabierto) | Un arreglo se cierra cuando lo compruebo yo, no cuando el autor lo dice |
| **Fijar la versión revisada** (fecha y huella) | Iván tenía abierta en Word una versión anterior a la que yo revisaba (R63) |
| **«No comprobado» obligatorio en el veredicto** | Lo que no he podido probar no puede pasar por aprobado sin que se vea |
| **Script `comprobar.py`** (solo Python del sistema, sin instalar nada) | Lo mecánico no debe depender de mi memoria: huecos, cifras sin fuente, palabras de alarma, idioma y propiedades del Word, PDF, bloqueos, documentos internos |

**Cómo he probado el script:**

- Con el envío tal como está, avisa de lo esperado:
  - los huecos `[Nombre de nuestra empresa]`, `[Teléfono / WhatsApp]` y `[correo]`;
  - las cifras 281, «casi 300» y «80 m»;
  - «se queda con las búsquedas», «os llamamos» y «Prometemos»;
  - el idioma en-US, el autor python-docx y la fecha de 2013;
  - la miniatura y la imagen sin texto alternativo.
- Con una copia del Word **arreglada** en `/tmp` (es-ES, propiedades reales, sin
  miniatura y con texto alternativo), esos avisos **desaparecen**. Solo queda la
  línea informativa de las casillas. Con un `~$…` de prueba, avisa del bloqueo.
- El script señala dónde mirar, **no aprueba nada**. Lo dice en su salida.

## 5. Lo que necesito de otros agentes (lo coordina Federico)

Son errores que se repetirán con cada cliente si no se cortan donde nacen:

| Para | En su skill | Qué | Por qué (veredicto) |
|---|---|---|---|
| **Chema** | `estudio-competencia` | Consulta de Overpass con etiquetas **exactas**: `shop=hairdresser` (y `hairdresser=barber` para barberías), **excluyendo `shop=hairdresser_supply`** y similares. La consulta se guarda con los datos | R03: 9 tiendas contadas como peluquerías |
| **Chema** | `estudio-competencia` | Los anillos, «el más cercano» y las distancias se **calculan con un script** desde el JSON guardado; nada se teclea | R03, R05, R50 |
| **Chema** | `estudio-competencia` y textos | Regla: **ninguna frase general sobre clientes o mercado sin fuente**, ni superlativos («pocas», «ningún competidor») sin contar | R10–R23 |
| **Chema** | `investigar-cliente` | **Cada cita de una reseña con su prueba** (captura o texto con URL y fecha) en `recopilado/`, enlazada desde el expediente | R30 |
| **Chema** | textos propuestos | Solo hechos del expediente; lo desconocido, como hueco [así]; nada que el cuestionario pregunte | R26, R27 |
| **Paco** | `herramientas-comunes` (`docx_util.py`, generadores) | El Word sale con: idioma **es-ES**, autor, título y fecha reales, **sin miniatura**, texto alternativo en las imágenes, y las cifras **leídas de los datos** | R39, R40, R61, R03 |
| **Paco** | generadores | Si existe `~$<documento>`, **no regenerar** y avisar: alguien lo tiene abierto | R63 |
| **Paco** | `informe.html` / CSS | `alt` en cada `<img>`, números de página, capturas recortadas | R55–R57 |
| **Reme** | `cuestionario-cliente` | Añadir a su comprobación: instrucciones posibles en el formato (nada de «rodeadla»), preguntas sobre personas en presente, ningún «¿Correcto?» sobre ausencias o datos sin confirmar, y el permiso de reseñas igual que en el expediente | R31–R33, R36 |
| **Lola** | maquetación | Leyenda de colores con rótulo o icono y contraste suficiente; una tipografía libre común a informe y Word; nada de medias páginas vacías | R37, R55, R62 |
| **Menchu** | `primer-envio` | Las cifras de los mensajes, **copiadas del informe ya aprobado**, nunca escritas de memoria; «la asistente» | R03/R43, R58 |
| **Federico** | `alta-cliente.md` | Fase 6 «hasta APROBADO», con re-revisión; en `entregables/` solo lo que se envía; quién revisa a Puri | Proceso |

Menchu y Reme ya recogen en sus revisiones varios de estos puntos: la llamada, las
10 páginas, los datos legales y la cláusula. No los repito como petición.

## 6. Lo que tiene que decidir Iván (lo lleva Federico)

1. **¿Ofrecemos llamadas?** Si sí, quién llama y cuándo; si no, se quitan (R07).
   *Propuesta:* no ofrecerlas hasta que haya alguien que las haga.
2. **Qué dice el email que hace Iván.** «Revisa y aprueba todo» no se cumplirá con
   WhatsApp en 2 horas (R42). *Propuesta:* «supervisa el trabajo y aprueba
   presupuestos y publicaciones».
3. **Competidores con nombre y capturas de terceros** (webs, Treatwell, Bing) en un
   documento comercial: ¿se acepta? *Propuesta:* sí, con nombre, pero solo hechos
   comprobables y sin valoraciones («se rompe», «web caída»). Las capturas, solo
   las imprescindibles para comentar. Si hay duda legal, preguntar al gestor o abogado.
4. **Opiniones en la web: ¿basta el permiso del negocio o hace falta el del autor?**
   El expediente y el cuestionario dicen cosas distintas (R31).
5. **Responsable del tratamiento** para la cláusula de datos (R08). Depende de la
   forma jurídica, que está en §15.
6. **Prueba en Word.** ¿La hace él (10 minutos por cada versión de plantilla, no por
   cliente) o nos deja usar el Word de su Mac? Ver §7.

## 7. Herramientas: qué necesito o propongo

**Cómo comprobar el Word en Microsoft Word.** Hay una novedad: Microsoft Word
**sí está instalado** en este Mac (`/Applications/Microsoft Word.app`, versión
16.115). Hoy lo tenía abierto Iván con el cuestionario. El encargo daba por hecho
que no. Opciones, de más a menos recomendada:

| Opción | Qué prueba | Coste | Riesgo |
|---|---|---|---|
| **A. Iván, con la lista de 10 minutos** de mi skill («Probar un Word»), **una vez por versión de plantilla**, no por cliente | Todo: casillas, huecos, ortografía, aspecto, propiedades | 0 € · 10 min de Iván por plantilla | Ninguno |
| **B. Nosotros, con el Word de este Mac**, con permiso de Iván: abrir una **copia** en `/tmp` (`open -a "Microsoft Word"`) y exportarla a PDF por AppleScript para comparar la maquetación | Aspecto, páginas, idioma y propiedades. **No** prueba de forma fiable los clics en las casillas | 0 € | Usa su licencia y su sesión; podría tocar un documento que tenga abierto. Solo con su permiso y nunca sobre `entregables/` |
| **C. Word para la web** (gratis con cuenta Microsoft) | Casillas y huecos en Word en línea | 0 € | Sube el documento a OneDrive: datos de cliente en un tercero (§10.3). Solo con plantillas y datos ficticios |
| **D. Lo que ya hago sin Word** (`comprobar.py` + LibreOffice) | Estructura de casillas, idioma, propiedades, que se abra | 0 € | No sustituye a A |

**Propuesta: A + D**, y B solo si Iván lo autoriza.

La prueba en el **móvil** (app de correo y WhatsApp) la tiene que hacer quien tenga
un móvil, Iván o un tester. Si en el móvil no se puede rellenar, el cuestionario B1
no debería ir en Word, sino por WhatsApp, pregunta a pregunta.

**Corrector ortográfico.** No hay ninguno en la máquina. Propongo `hunspell`
(libre, `brew install hunspell`), que usaría el diccionario español que ya trae
LibreOffice (`dict-es`). Así `comprobar.py` podría listar las palabras dudosas.
Cuesta 0 €, pero es instalar algo: **no lo he instalado**. Lo decide Iván.

**Lo que ya he hecho** (no instala nada): `comprobar.py`, en mi skill. Si Paco
prefiere mantenerlo en `herramientas/`, por mí bien, siempre que no cambie lo que comprueba.
