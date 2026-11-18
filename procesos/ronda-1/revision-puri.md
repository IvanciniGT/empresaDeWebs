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

## 8. Ronda 1b

> Puri · 2026-11-18 · Encargo E-012

### 8.1 Lo que he cambiado

| Qué | Cambio | Comprobado así |
|---|---|---|
| [`revisar-entregable`](../skills-borrador/revisar-entregable/SKILL.md) v0.2 → **v0.3** | Decisiones A-001 a A-015, lo que piden Chema, Lola y Menchu (tabla 8.2), apartado J nuevo (mensajes y plantillas de WhatsApp), categoría A–J en cada error, marcas de regresión y de exclusión, y sección «Comparar dos versiones» | Lectura contra [ronda-1b.md](ronda-1b.md), la consolidación y la bandeja |
| [`comprobar.py`](../skills-borrador/revisar-entregable/comprobar.py) | **El Word lo revisa `revisar_docx.py` de Paco** (he quitado mis comprobaciones repetidas) y **la ortografía, `ortografia.py` de Paco**. Lee la **lista de frases de Chema** de sus skills. Añade datos personales en lo que entra en git, letra en el móvil a 390 px con imágenes de cada página (también del Word), formato A4/A5, tipografías fuera de estilo, versión de plantilla del pie y una tabla de cifras por documento. Lo que no puede comprobar lo dice | 7 pruebas, abajo |
| [`comparar.py`](../skills-borrador/revisar-entregable/comparar.py) (nuevo) | Cuenta dos veredictos con las mismas reglas: gravedad, categoría, regresiones y exclusiones | 4 pruebas, abajo |
| [Veredicto base](../../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md) | Categoría en cada error; **re-revisión con la v0.3: R64–R66** (Word fuera de esquema, móvil a 6,9 px y contraste 4,38:1); ortografía pasada por la base, sin errores nuevos; **sin los nombres de autores de reseñas** que puse en R30 (A-013) | `comparar.py` sobre la base da 10/35/21 |

**Pruebas de `comprobar.py`.** Todas en `/tmp`, con datos inventados, y cada una con un
caso que tiene que fallar:

1. **Datos personales sin git:** marca el móvil, el correo, el DNI y el NIE del expediente.
   No marca lo mismo en `privado/`, ni el fijo del local, ni `wght@9..144` (un falso
   positivo real de la primera versión), ni un correo `noreply`.
2. **Datos personales con git:** las carpetas excluidas (`privado/`, `maquetas/`) dan 0; un
   fichero normal con esos datos da los 4.
3. **Faltan herramientas:** sin `revisar_docx.py`, sin `ortografia.py` y sin las skills de
   Chema, sale `[no comprobado]` para cada una. Nunca un aprobado en silencio.
4. **Un Word limpio hecho con `docx_util.py`:** ningún aviso del Word, y lee «Tanda A v0.3»
   del pie.
5. **Ortografía:** caza «Prefierís». **Esta prueba me pilló un fallo:** la primera versión
   quitaba las palabras en mayúscula y dejaba pasar la errata, porque iba a principio de frase.
   Ahora las palabras buenas son las del expediente.
6. **Expediente:** una palabra inventada sale si no está en el expediente y no sale si está.
7. **El envío de Federico:** salen los avisos esperados (64 errores de estructura, el idioma
   y las propiedades del Word, las tipografías, 7,2 px en el móvil, «281» frente a «300
   peluquerías»).

**Pruebas de `comparar.py`.**

- La base contra sí misma da 10/35/21 y «no es mejor».
- Una ronda 2 inventada con 0/2/1 da «mejor» en lo contable.
- Una con «(= R05)» da una regresión de un error que bloqueaba y «no es mejor», y avisa del error sin categoría.
- Un error excluido en los dos lados resta en los dos.

### 8.2 Lo que me pedían y dónde está

| Quién | Qué | Dónde |
|---|---|---|
| Chema | «Dos copias = una fuente», «nada de ausencias», «ninguna generalización sin fuente», «cifras con fecha» | Skill: paso 3 y lista A |
| Chema | Su lista de frases | `comprobar.py` la lee de `estudio-competencia` y `textos-web`: no la copio |
| Lola | Lectura en el móvil (`pdftoppm -scale-to-x 390`) | Paso 1 (imágenes y px) y lista F |
| Lola | `contraste.py` con los colores del documento | Paso 2 y lista G |
| Lola | `alt` en todas las imágenes; idioma del Word | Lista G; `revisar_docx.py` |
| Lola | Ninguna maqueta con datos sin comprobar | Lista A |
| Menchu | Promesas de lo que no hacemos (llamadas, fotos, plazos) | Lista B |
| Menchu | Ausencias; textos que afirman lo que el envío pregunta | Listas A y D |
| Menchu | Revisar **una vez** sus plantillas y el guion | «Cuándo» y lista J. **Lo hago cuando Federico me lo encargue**: el guion aún no tiene preguntas |
| Menchu | Medir cuánto tarda cada fase en la ronda 2 | Método, S3 |
| Paco | Usar `revisar_docx.py` en lugar de duplicarlo | Hecho; también uso `ortografia.py` |
| Reme | ¿Me sirve «se comprueba así»? | 8.4 |

### 8.3 Cómo compararemos la ronda 2 con la versión de Federico

**Qué se compara:** **todo lo que recibiría el cliente en el primer envío**, en las dos
versiones. Son los mensajes de WhatsApp tal como Iván los copiaría, el correo, los
adjuntos y las preguntas de la tanda A.

**Qué no se compara:** lo interno (guía previa, previo de precio y requisitos), porque la
versión de Federico no se revisó.

**La base** es el [veredicto de Federico](../../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md)
**re-revisado con la v0.3**. Los archivos están congelados en el commit `e38b879`, con
huellas `04d6999a6787`, `04745e0a460c` y `dd07394a0e19`.

#### Lo que decide (primarias)

| # | Métrica | Cómo se mide | Base (Federico) |
|---|---|---|---|
| **P1** | Errores por gravedad en la **primera entrega** a Puri | Veredicto con la v0.3 → `comparar.py` | **10 · 35 · 21** (con la v0.2 eran 9 · 33 · 21) |
| **P2** | Afirmaciones falsas o sin fuente (errores de la categoría A) | Ídem | **36** |
| **P3** | Regresiones: errores de la base que vuelven, aunque sea con otras palabras | Marcados «(= Rxx)» en el veredicto | — |
| **P4** | Llega a **APROBADO**, y en cuántas vueltas | Historial de veredictos | **No llegó** (RECHAZADO, sin corrección) |
| **P5** | Cubre los **mensajes clave** K1–K8 (tabla de abajo) | A mano, mensaje por mensaje | **7 de 8** (falta K8) |

**P5 existe para que no se pueda mejorar callando:** un envío vacío tendría cero errores.
Los mensajes clave salen de AGENTS.md y de lo que hacía bien la versión de Federico:

| # | El cliente tiene que recibir… | Federico |
|---|---|---|
| K1 | Quién le escribe, que es asistente de IA (§9.3) y quién es el responsable | ✓ |
| K2 | Lo bueno que ya tiene, con prueba (nota, reseñas, oficio) | ✓ |
| K3 | Lo que le falta (sin web propia encontrada, directorios con datos que no controla) | ✓ |
| K4 | Su competencia cercana, con una cifra correcta y fechada, y algún competidor concreto | ✓ (con R03 y R05) |
| K5 | Qué le proponemos, sin precios [PROPUESTA] y diciendo que no prometemos posiciones | ✓ |
| K6 | El siguiente paso: qué pasa después, cuándo y que es «gratis y sin compromiso» (A-005) | ✓ |
| K7 | Las preguntas que hacen falta para el presupuesto | ✓ (69, demasiadas) |
| K8 | Cómo contactar: un canal y un dato reales | ✗ (huecos, R01) |

Un mensaje cuenta como cubierto si está, aunque tenga errores: esos ya cuentan en P1.

#### Lo que se mide y no decide (informativas)

| # | Métrica | Cómo | Base (Federico) |
|---|---|---|---|
| S1 | **Esfuerzo del cliente:** páginas, palabras, preguntas totales y obligatorias, adjuntos y mensajes | `comprobar.py` (métricas) y recuento de preguntas con la regla de abajo | Informe: 9 págs. A4, 1.720 palabras · Cuestionario: 10 págs., 1.726 palabras, **69 preguntas (32 con ★)** · Correo: 284 palabras · 2 adjuntos · 1 mensaje |
| S2 | **Letra en el móvil**, en px en una pantalla de 390 px | `comprobar.py` (estimada, ±10 %) y el CSS | **6,9 px** (7,2 estimada) |
| S3 | **Tiempo por fase** y **minutos de Iván** (lo pide Menchu para el plazo interno) | Hora de inicio y fin de cada encargo en `encargos.md`; minutos de Iván anotados por Federico | **No medido.** Los ficheros van de las 18:28 a las 19:02, sin revisión ni aprobación |
| S4 | **Fugas de Puri:** errores que Federico (por muestreo) o Iván encuentran después de mi APROBADO | Muestreo de Federico | — |

**Regla de recuento de preguntas.** Cuenta una cada cosa que el cliente contesta por
separado: una fila que validar, un hueco de texto, un grupo de casillas o un mensaje de
WhatsApp que espera respuesta. Las condicionales cuentan aparte: «N obligatorias +
M condicionales».

**S3 no decide** porque la versión de Federico no pasó por revisión ni por Iván: la ronda 2
tardará más **a propósito**. S4 cuenta contra mí, no contra el equipo.

#### Cómo se hace

0. **La vara se fija antes de ver la ronda 2** (hecho hoy): la skill v0.3, `comprobar.py`
   y `comparar.py` quedan como están. Si durante la revisión aparece una comprobación
   nueva, **se aplica a las dos versiones o a ninguna**, y lo anoto en los dos veredictos.
1. La ronda 2 entrega **todo el envío** en su carpeta nueva, con la **tabla de trazas**
   (afirmación → prueba) de Chema y el texto exacto de los mensajes.
2. **Primera revisión** con la v0.3 → veredicto 1. **Este es el que cuenta para P1, P2,
   P3 y P5.**
3. Correcciones y re-revisiones con los mismos ID **hasta APROBADO** → P4.
4. **Muestreo de Federico, en las dos versiones por igual:**
   - 10 errores al azar de cada veredicto: ¿existe el error? ¿es correcta la gravedad?
   - Una página o un mensaje al azar de cada versión, buscando lo que se me haya escapado.

   Si no estamos de acuerdo, decide Iván (choque 5).
5. `python3 comparar.py <base> <ronda 2>` y la tabla completa en
   `procesos/ronda-2/comparacion.md`, o donde diga Federico.

**Reglas para que sea justo:**

- **Un error es un defecto** que se arregla con un cambio, aunque salga en varios sitios.
- **La gravedad, con la tabla de la skill y sus ejemplos.** En caso de duda, la del caso
  parecido de la base.
- **Si Iván acepta un error en las dos versiones,** se excluye en las dos. Lo previsible es
  el nombre de la empresa, si §15 sigue sin decidir. Sin eso, R01 bloquearía las dos para
  siempre y la ronda 2 no podría llegar a APROBADO.
- **Que la ronda 2 sea más corta es mérito suyo,** no un truco: lo pidió Iván (A-005).
  P5 impide que se acorte quitando lo necesario.

#### La regla de «mejor» (propuesta; el bono lo decide Iván)

**Mínimo (si no se cumple, no ha salido mejor):** se cumplen las cinco.

- P4: llega a APROBADO.
- P1: menos errores que la base **en cada gravedad**.
- P2: menos afirmaciones falsas o sin fuente.
- P3: **ningún error de la base que bloqueaba vuelve**.
- P5: cubre todo lo que cubría la base (7 de 8), y K8 si ya hay nombre de empresa.

**Objetivo (lo que yo llamaría «ha salido bien»):** se cumplen las seis.

- Primera entrega con **0 errores que bloqueen**.
- **5 importantes como máximo.**
- **P2 = 0**: ni una afirmación sin fuente.
- **P3 = 0**: ninguna regresión, de ninguna gravedad.
- **APROBADO en 2 vueltas como máximo.**
- **P5 = 8 de 8**, o 7 de 8 si el nombre está excluido.

Lo de «5 importantes» y «2 vueltas» es mi propuesta, sin más base que la ronda 1: que lo
valide Iván.

### 8.4 A Reme: la columna «se comprueba así» de `requisitos.md`

**Sí me sirve, y es la que más voy a usar.** Tu regla provisional (dónde se mira y qué
tiene que verse, sin «bien», «claro» ni «rápido») va en la buena dirección. Propongo
cerrarla así:

1. **Tres partes fijas:** **Dónde** (aparato y página) · **Qué hago** (abrir, tocar,
   desplazarme) · **Qué tiene que pasar** (algo que se ve y es sí o no). Si un criterio
   no se puede contestar con sí o no, no se puede comprobar.
2. **Los aparatos, una vez, en la cabecera** del fichero, y no en cada fila. Propongo:
   - **móvil:** 390 × 844 y 360 × 800, Chrome sin ventana;
   - **ordenador:** 1366 × 768;
   - **móvil real:** solo lo que el emulador no prueba, como que se abra el marcador. Lo hace Iván o va a «No comprobado».
3. **Palabras que no valen** en un criterio: bien, claro, rápido, fácil, adecuado,
   correcto, intuitivo, moderno, atractivo, suficiente y «visible» sin precisar.
   - En R-01, «se ve desde la página principal» puede querer decir sin desplazarse o
     desplazándose; hay que elegir.
   - En R-02, «visible en todas las páginas» puede ser siempre en pantalla o en algún sitio de la página.

   Decir cuál no es decir «cómo» (tu regla 4): es el resultado que el cliente necesita.
4. **El valor de referencia, por su ID, nunca copiado,** como ya haces («el confirmado en
   A 1.4»). Yo lo leo de `privado/` en local, y en el veredicto, que va a git, solo
   escribo «coincide» o «no coincide».
5. **Marca [auto] o [a mano].** [auto] es lo que comprueba un script: enlace `tel:`,
   datos estructurados, Lighthouse, enlaces rotos. Así Paco lo puede pasar antes de que
   me llegue, y yo lo automatizo.
6. **Marca [tras publicar]** para lo que solo se puede ver en producción: ficha de Google,
   Search Console, dominio y HTTPS. Lo compruebo en el paso 7 del recorrido (§13.5).
7. **Estado con prueba:** «comprobado por Puri · fecha · versión · enlace a la captura», y si
   falla, el ID del error del veredicto.
8. **ID:** mis errores son `R01` y tus requisitos `R-01`; en un mismo veredicto se van a
   cruzar. Propongo que los tuyos pasen a **`REQ-01`**. Si prefieres mantenerlos, cambio
   yo a `E01` en los veredictos nuevos; lo decide Federico.

Tus dos ejemplos, reescritos con esto:

| ID | Se comprueba así |
|---|---|
| REQ-01 | [a mano] **Móvil y ordenador, página principal** · la abro sin tocar el menú y me desplazo hasta el final · aparecen los 7 días, con sus tramos y los días cerrados, y coinciden con A 1.4. |
| REQ-02 | [auto] **Cada página**, código · el botón de llamar es un enlace `tel:` con el número de A 1.3. [a mano] **Móvil 390 px, cada página** · sin desplazarme · el botón está en pantalla. [móvil real, Iván] al tocarlo se abre el marcador con ese número. |

### 8.5 Lo que necesito de otros agentes (lo coordina Federico)

| Para | Qué | Por qué |
|---|---|---|
| **Paco** | Que `revisar_docx.py` compruebe también el **título vacío** en las propiedades | Lo comprobaba yo; lo he quitado para no duplicar |
| **Paco** | Revisar técnicamente `comprobar.py` y `comparar.py` (choque 4) | Usan sus herramientas y llaman a `.venv` y a `git` |
| **Lola** | Un **mínimo de letra en px** en `estilo-documentos`. Si es un número, lo puedo medir | El A5 a 11,5 pt sale a unos 10,7 px en 390 px. ¿Vale? |
| **Chema** | La **tabla de trazas** (afirmación → prueba) con cada entregable de la ronda 2 | Paso 1 del método; me ahorra rehacer el rastreo |
| **Chema** | Mantener el título «Frases que se revisan antes de entregar» en sus dos skills | `comprobar.py` lo busca por ese título; si cambia, avisa, pero deja de usarla |
| **Reme** | Lo de 8.4, y decidir `REQ-` o `R-` | Colisión de ID |
| **Menchu** | Avisarme, por medio de Federico, cuando el guion y las plantillas estén en su versión para Iván | Las reviso una vez por versión (A-012) |
| **Federico** | Hora de inicio y fin de cada encargo de la ronda 2 en `encargos.md`, y los minutos de Iván | S3 |
| **Federico** | El muestreo del paso 4, en las dos versiones | Choque 5; también mide mis fugas (S4) |
| **Federico** | Un **registro de pruebas de Word** en `operacion/`: versión de plantilla, fecha y resultado | A-007: sin registro no puedo comprobar que la versión del pie está probada |

### 8.6 Lo que tiene que decidir Iván (lo lleva Federico)

1. **El nombre de la empresa en la ronda 2.** Si §15 sigue abierto, propongo excluir ese
   hueco en las dos versiones; si no, ninguna de las dos puede aprobarse.
2. **La regla de «mejor» y el objetivo** de 8.3, sobre todo los dos números que son míos:
   5 importantes y 2 vueltas.

### 8.7 Lo que he encontrado al aplicar A-013 (repositorio público)

- [importante] **`recopilado/capturas/04-resserv-resenas.png` está en git desde `e38b879`**,
  y por tanto es público. Lleva el **nombre completo y la foto** de varios autores de
  reseñas. Son personas, no el negocio · Quitarla de lo que va a git, o recortarla a lo
  que nos sirve sin nombres ni caras, y guardar el original en `privado/`. Lo coordina
  Federico; si hay que borrarla también del historial de git, lo decide Iván.
- [importante] **Mi veredicto base tuvo esos mismos nombres** (en R30) y así entró en git
  en `676177e`. Ya los he quitado de la copia de trabajo, pero **siguen en el historial**.
  Mismo arreglo que el punto anterior. A partir de la v0.3 es una regla de la skill.
- `comprobar.py` busca móviles, correos y documentos de identidad, pero **no nombres** ni
  caras en imágenes: esos se miran a mano.
