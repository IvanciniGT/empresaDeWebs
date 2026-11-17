# Revisión · Primer envío · Peluquería Hermanos Cotillas

> Revisado por **Puri** (Calidad) · 2026-11-17 · skill `revisar-entregable` v0.2
> ⚠️ Cliente simulado: nada de esto se envía. Se ha revisado como si saliera mañana.

```
VEREDICTO: RECHAZADO
```

**9 bloquean · 33 importantes · 21 menores.**

Lo más grave no es la forma, son los datos:

- la cifra de la portada del informe está inflada;
- el «vecino más cercano» no lo es;
- el informe promete resultados en Google;
- el cuestionario pide datos personales sin cláusula de privacidad;
- hay más de veinte afirmaciones que no salen del expediente.

Federico quitó seis frases inventadas, y quedan más del mismo tipo (R10–R27).

**Para aprobar:**

- ningún error que bloquee;
- ningún importante sin arreglar, salvo que Iván acepte uno por escrito y sabiendo lo que acepta;
- el Word probado en Microsoft Word.

## Qué he revisado

| Entregable | Versión revisada (fecha · sha256) |
|---|---|
| `Informe de mercado y SEO local - Peluquería Hermanos Cotillas.pdf` (9 págs.) | 17/11 18:53 · `04d6999a6787` |
| `Cuestionario - Peluquería Hermanos Cotillas.docx` (10 págs. en LibreOffice) | 17/11 19:01 · `04745e0a460c` |
| `email-borrador.md` | 17/11 19:01 · `dd07394a0e19` |

Contra: [expediente](../expediente.md), capturas de `recopilado/` y `competencia/`, datos de
OpenStreetMap guardados (`competencia/*.json`), [AGENTS.md](../../../AGENTS.md) y
[alta-cliente.md](../../../procesos/alta-cliente.md).

Las páginas del cuestionario son las de LibreOffice. En Word pueden cambiar.

## Cómo lo he revisado

1. Texto completo extraído (`pdftotext`, `soffice` → PDF) y leído entero.
2. Cada página, renderizada (`pdftoppm`) y mirada.
3. **Cada cifra y cada afirmación**, buscadas en el expediente y en las capturas.
4. El censo de competidores, **recalculado** desde `competidores-osm-1500m.json`.
5. Dos dominios, comprobados por DNS (`dig`): no se contacta con nadie.
6. El Word, abierto por dentro: casillas, idioma, metadatos, imágenes y tipografías.

**Lo que NO he podido comprobar** (no cuenta como aprobado):

- El Word en Microsoft Word: casillas, maquetación y huecos (ver R09).
- Cómo se ven los dos adjuntos en el móvil, en la vista previa de Gmail, Outlook y WhatsApp.
- Lo que muestra Google, porque bloquea las consultas automáticas.
- Cinco de las nueve citas de reseñas: no hay captura del original (R30).

## Escala de gravedad

- **bloquea**: no puede salir así. Puede ser algo falso o inventado presentado como hecho, un incumplimiento de AGENTS.md o de la ley, algo roto o algo que no podemos cumplir.
- **importante**: hay que arreglarlo antes de enviar. Solo Iván puede aceptarlo tal cual, por escrito.
- **menor**: conviene arreglarlo, pero no impide el envío.

Formato de cada línea: `ID [gravedad] Dónde · Qué pasa · Qué debería pasar`.

## Bloquean

- **R01** [bloquea] Informe (portada y pie), cuestionario (portada y los diez pies) y email (firma) · Quedan sin rellenar `[Nombre de nuestra empresa]`, `[Teléfono / WhatsApp]` y `[correo]` · Que no salga nada con huecos. Depende de §15 (nombre de la empresa): lo decide Iván.
- **R02** [bloquea] Informe p. 6, Barber Shop Gentleman · «el primero de los dos que tenga una web bien hecha **se queda con las búsquedas del barrio**» es una promesa de resultados (§4.1, §10.3), y contradice el recuadro «Lo que no os vamos a prometer» de la p. 7 · Quitarla. Basta con describir: «tampoco tiene web propia».
- **R03** [bloquea] Informe pp. 2 y 4 (cifra de portada, tabla, «48 de esos negocios») y email · La cifra está inflada: **«281» incluye 9 tiendas de productos de peluquería** (`shop=hairdresser_supply`: Mas K Pelo, Procosmética, Cebrián, Cecos, Rimar, Nux, Arenadel, Del Rey, Cosmybell). Además, el fichero da 282 y no 281: las cifras están tecleadas a mano en la maqueta, no calculadas · Solo peluquerías: **33 / 85 / 206 / 273** (250 m / 500 m / 1 km / 1,5 km). Que la cifra salga del cálculo, no de la maqueta.
- **R04** [bloquea] Cuestionario p. 4 · «las **casi 300** peluquerías y barberías»: es una tercera versión de la misma cifra (281 en el informe y el email), redondeada hacia arriba · La misma cifra en los tres documentos, la corregida de R03.
- **R05** [bloquea] Informe p. 6 · «Barber Shop Gentleman · **Vuestro vecino más cercano** · a 80 m» es falso. Según nuestros datos de OSM hay tres más cerca: **Actuall (41 m), My Bell (46 m) y MG Peluqueros (51 m)**. Gentleman es la *barbería* más cercana. El cliente conoce su calle mejor que nadie y lo verá en el acto · «La barbería más cercana». Distancias sacadas de los datos.
- **R06** [bloquea] Informe p. 2 · «**0** páginas en internet que controléis vosotros» afirma una ausencia que no podemos probar. Contradice la p. 3 («no sabemos si la estáis gestionando», sobre la ficha de Google) y la regla 4 de `alta-cliente.md` · Quitar esa cifra o cambiarla por algo comprobado: «No hemos encontrado una web vuestra».
- **R07** [bloquea] Email («os llamamos y lo rellenamos juntos por teléfono») y cuestionario: p. 2 («Tres consejos»), p. 3 («Mejor momento para llamaros») y p. 10 · Prometemos una llamada que hoy nadie puede hacer: §9.1 no tiene canal de teléfono y los agentes no llaman · Quitarlo, o que Iván decida quién llama y cuándo. Hasta entonces, no se ofrece.
- **R08** [bloquea] Cuestionario p. 3, datos de contacto y datos legales · Pide nombre, móvil, correo, **NIF**, razón social y domicilio fiscal **sin cláusula informativa de protección de datos** (art. 13 RGPD: responsable, finalidad, base, derechos). Además, los datos legales llevan ★ «imprescindible para empezar» antes de haber presupuesto, en contra de §12 («solo los datos que hacen falta para el trabajo») · Cláusula de privacidad, que depende de R01 porque falta el responsable. Los datos legales, a la tanda B (después de aceptar el presupuesto).
- **R09** [bloquea] Cuestionario, todo · **No se ha probado en Microsoft Word.** «Las casillas se marcan con un clic» es una promesa al cliente sin comprobar. La estructura interna es la correcta (100 casillas `w14:checkbox`, la que usa Word), pero eso no prueba cómo se comporta · Prueba en Word con la lista «Probar un Word» de la [skill](../../../procesos/skills-borrador/revisar-entregable/SKILL.md) antes de enviar. Opciones en el §7 de la [revisión de Puri](../../../procesos/ronda-1/revision-puri.md).

## Importantes

**Afirmaciones sin fuente** (del mismo tipo que las seis que quitó Federico):

- **R10** [importante] Informe p. 2 · «Quien busca "peluquería" sin conoceros **encuentra antes a otros**». No hemos podido consultar Google (lo dice la p. 9) · Quitarla, o decir lo que sí sabemos: «no tenéis web que pueda salir en esas búsquedas».
- **R11** [importante] Informe p. 2 · «✔ **Todo** lo publicado sobre vosotros» contradice los «Límites» de la p. 9 (sin Google, sin búsqueda fiable en redes) · «Lo que hemos encontrado publicado sobre vosotros».
- **R12** [importante] Informe p. 3 · Directorios: «**No los podéis corregir**» es falso según nuestra propia captura: mispelus tiene «¿Es tu negocio o ves un error? **Sugerir una corrección**» (`recopilado/capturas/02-mispelus.png`) · «Algunos permiten pedir correcciones, pero son muchos y no los controláis».
- **R13** [importante] Informe p. 3 · Reservas online: «**Vuestros competidores más activos sí**». En la captura de Treatwell hay **5 centros** en todo Albacete, y dos son de estética o bronceado. De Booksy no hay ninguna prueba guardada · «En Treatwell aparecen pocas peluquerías de Albacete (5 cuando lo miramos)».
- **R14** [importante] Informe p. 4 · «nadie elige peluquería por ser la más cercana… Se elige por confianza… y por comodidad» se presenta como hecho sin fuente · Presentarlo como opinión nuestra, o quitarlo.
- **R15** [importante] Informe p. 4 · «sobre todo, por el joven, que es el que busca en el móvil» no tiene fuente · Quitarlo.
- **R16** [importante] Informe p. 5 · Julia López, «**Una de las pocas** peluquerías de la zona con web propia». Solo sabemos que OSM registra web en 2 de 282, y OSM casi nunca guarda la web (lo dice `alta-cliente.md`) · «Tiene web propia».
- **R17** [importante] Informe p. 5 · Julia López, «**algún** precio orientativo (peinados de boda desde 40 €)». Su web publica varios precios, entre ellos **Corte Caballero desde 11 €**, que es justo el dato que le importa a una peluquería de caballero (`julia-lopez-ordenador.png`) · Describirlo bien y dar ese precio.
- **R18** [importante] Informe p. 6, tabla · «Una historia que contar… **Ningún competidor la cuenta**». Julia López pone en portada «Más de 30 años de experiencia» · Quitarlo, o algo que se pueda defender con lo que hemos visto.
- **R19** [importante] Informe p. 6, tabla · «El cliente nuevo no llama para preguntar: compara y elige», «**Es lo que más convence** a quien no os conoce» y «Quien busca "peluquería cerca" suele hacerlo desde el móvil, en la calle» no tienen fuente · Quitarlas o presentarlas como opinión.
- **R20** [importante] Informe p. 6, tabla · «Cita sin llamar · Vosotros hoy: **No**». No sabemos cómo dan cita: el expediente dice «Cita previa: desconocido» · «No lo sabemos» o quitar la fila.
- **R21** [importante] Informe p. 6 · Morote: «Una web abandonada **resta más que no tener web**» se da como hecho · Quitarlo. Dejar el dato: el enlace de OSM lleva a un dominio que no funciona (comprobado hoy por DNS).
- **R22** [importante] Informe p. 6 · Gentleman, «con un **público parecido**»: no tenemos ese dato · Quitarlo.
- **R23** [importante] Informe p. 7 · «Estáis en una **zona céntrica** de Albacete» y que la cercanía «juega a favor»: lo primero no está en el expediente (barrio Feria) y la cercanía depende de dónde está quien busca · Quitarlo.
- **R24** [importante] Informe p. 7 («barba») y búsquedas («barbería Albacete / arreglo de barba») · Usamos la **barba** como servicio suyo, y el expediente solo da por seguros el corte de caballero y el de niño · Quitarla hasta que lo confirmen.
- **R25** [importante] Cuestionario p. 5 · «Los negocios que publican precios **reciben más llamadas**». No tiene fuente y **contradice el informe** («el cliente nuevo no llama para preguntar») · Quitarla. «Es decisión vuestra» basta.
- **R26** [importante] Cuestionario pp. 7 y 8, textos propuestos · Dan por hechas cosas que el propio cuestionario pregunta en la p. 4:
  - que los padres «**abrieron** esta peluquería en la calle Octavio Cuartero»;
  - «dos generaciones… **en el mismo local**»;
  - «Aprendimos el oficio de nuestros padres».

  Además, «**Muchos** de nuestros clientes vienen desde hace más de 30 años» sale de una sola reseña · Que los textos solo afirmen lo que está en el expediente. Lo demás, como hueco [así].
- **R27** [importante] Cuestionario p. 8 · «Puntuales: **si tienes cita, no esperas**» es una promesa que les ponemos en la boca sin saber si dan cita, y «el **sillón antiguo**» está inventado: no aparece en ninguna fuente · Quitar las dos.

**Coherencia, tono y uso:**

- **R28** [importante] Informe p. 7 · «Google se fija sobre todo en **tres** cosas:» y vienen **cuatro** recuadros · Corregir.
- **R29** [importante] Informe p. 8 y cuestionario p. 7 · Prometemos mostrar las opiniones «**tal cual**… sin retocar», y las citas de los dos documentos están retocadas: cortadas, con mayúscula inicial nueva y sin marcar el corte en el informe. La misma reseña aparece de tres formas distintas · Citas literales, con […] donde se corta, y la misma versión en todos los documentos.
- **R30** [importante] Email, informe y cuestionario · La cifra que más usamos, «**más de 34 años**», sale de una reseña de la que **no hay captura**. Tampoco la hay de otras cuatro citas («Llevo casi toda mi vida…», «Han podido domar…», «Un trato muy amable…», «Me parecen muy profesionales…»). Las capturas solo muestran las de Juan Ortega, Ana Cid, José Mª Navarro y, a medias, Luis Santamaría · Guardar la prueba (captura o texto con URL y fecha) de cada cita que se use.
- **R31** [importante] Cuestionario pp. 6 y 7 · Pedimos permiso para mostrar las opiniones solo al negocio. El expediente dice «no se publican sin permiso del negocio **y del autor**» · Que el expediente y el cuestionario digan lo mismo. Lo decide Iván.
- **R32** [importante] Cuestionario p. 4 · «¿Cómo **se llamaban** o cómo los conocía el barrio?». Los padres están **jubilados**, no muertos, y el pasado puede doler · «¿Cómo se llaman…?».
- **R33** [importante] Cuestionario p. 2 · «Web propia: **No tenéis**» afirma una ausencia · «No hemos encontrado ninguna».
- **R34** [importante] Cuestionario p. 8 · Fotos con clientes: «Si no quiere, **que salga de espaldas**». Si no quiere, no sale: de espaldas también se le puede reconocer. Con niños (son clientela habitual) hace falta el consentimiento de los padres · «Solo con permiso por escrito. Si no, que no salga».
- **R35** [importante] Cuestionario p. 8 · La columna «¿Nos ayudáis a hacerla?» está al revés (quiere decir «¿queréis que os ayudemos?») y ofrece algo que no damos: la fotografía queda fuera de §6.1 · Quitar la columna.
- **R36** [importante] Cuestionario p. 6 · «Si tuvierais que quedaros con una, **rodeadla**». En un Word no se puede rodear nada · «…escribidla aquí:» y un hueco.
- **R37** [importante] Cuestionario p. 2 · La leyenda de colores es casi invisible: tres tonos pastel muy parecidos, y si se imprime en blanco y negro se pierde. El significado va **solo en el color** · Rótulo o icono además del color, y más contraste.
- **R38** [importante] Cuestionario, todo · Son **10 páginas antes del presupuesto**. La skill de Reme v0.2 pone 4 como máximo para la tanda B1 · Dejar en B1 solo lo que cambia plan, precio o plazo.
- **R39** [importante] Cuestionario, archivo · El idioma del documento es **inglés (en-US)**. En Word, el cliente verá todo el texto subrayado en rojo, y la autocorrección en inglés le cambiará lo que escriba · Idioma es-ES en estilos y texto.
- **R40** [importante] Cuestionario, propiedades del archivo · Autor «**python-docx**», descripción «generated by python-docx», creado y modificado el **23/12/2013** y sin título. Se ve en Archivo › Propiedades · Autor: la empresa. Título, fecha real y sin la descripción.
- **R41** [importante] Informe p. 5 · NenaMelenas: «barba **desde 16 €**» no se ve en ninguna captura (la de Treatwell corta los precios de la barba). «Cita **en dos clics**» y «opiniones **verificadas**» tampoco están comprobados · Solo lo que muestran las capturas: corte hombre 16 €, corte niño 14 €.
- **R42** [importante] Email · «Iván… revisa y aprueba **todo** lo que os enviamos»: con respuestas por WhatsApp en 2 horas (§9.1) no será verdad · Lo que Iván decida que puede cumplir. Por ejemplo: «supervisa nuestro trabajo y aprueba presupuestos y publicaciones».

## Menores

- **R43** [menor] Email («una docena de páginas»), informe («una docena», «más de 10», «los diez directorios»), cuestionario («más de diez») · El mismo dato aparece de cuatro formas · Una sola: «más de diez».
- **R44** [menor] Informe y cuestionario · «unas **132** opiniones»: las capturas dan 126 (Marios), 137 (resserv) y 289 (otro directorio) · «Más de 130», con fecha.
- **R45** [menor] Informe p. 3 y cuestionario p. 3 · «zona de relax» entre comillas como si fuera literal. El directorio dice «Restroom donde los clientes pueden relajarse». «Peinados **de novia**» no sale en ninguna captura: dicen «para eventos especiales» · Citar literal o parafrasear sin comillas.
- **R46** [menor] Informe p. 2 y cuestionario p. 3 · «textos escritos **por una máquina**»: no lo sabemos · «textos genéricos que no habéis escrito vosotros».
- **R47** [menor] Informe p. 2 · «33 a menos de 250 m: **en vuestra misma manzana y las de al lado**». Un radio de 250 m son varias manzanas en cada dirección · Solo la cifra y el radio.
- **R48** [menor] Informe p. 4 · Las barberías «**se anuncian** como tales». En realidad, 44 llevan la etiqueta de OSM que ponen voluntarios y 4 se cuentan por el nombre · «aparecen como barberías en el mapa».
- **R49** [menor] Informe p. 4, tabla · La columna «Peluquerías» lleva el total (peluquerías + barberías) · «Total» y «De ellas, barberías».
- **R50** [menor] Informe p. 4 · «hay otra a 50 metros»: la más cercana está a 41 m · «a menos de 50 metros».
- **R51** [menor] Informe p. 5 · NenaMelenas no está en el censo de OSM: no sabemos a qué distancia está, y el resto de competidores sí la lleva. «La primera del listado» de Treatwell: de 5, con un orden que no conocemos · Poner la distancia, o decir que está fuera de la zona.
- **R52** [menor] Informe p. 6 · «Peluquería **Jesús** Morote»: en OSM se llama «Morote», y el nombre completo sale del dominio · El nombre de la fuente.
- **R53** [menor] Informe p. 8 y cuestionario p. 9 · «Hemos **comprobado** que **parece** libre» se contradice consigo mismo. El DNS no es definitivo (`alta-cliente.md`) y la comprobación no está anotada en el expediente · «Por lo que hemos podido ver, está libre» y anotarlo con fecha.
- **R54** [menor] Informe p. 9 · «el orden de magnitud **es fiable**»: no lo hemos medido · Quitarlo.
- **R55** [menor] Informe pp. 2, 4, 6, 8 y 9 · Medias páginas en blanco y sin números de página · Reajustar y numerar.
- **R56** [menor] Informe p. 3 · Las capturas de Bing y del directorio no se leen al tamaño impreso, y la de Bing enseña sobre todo un anuncio de Groupon y el aviso de cookies · Recortar a lo que se comenta.
- **R57** [menor] Informe, todo · Las imágenes no tienen texto alternativo (`<img>` sin `alt` en la maqueta). El PDF sí está etiquetado y en español · `alt` en cada imagen.
- **R58** [menor] Email · «Soy Menchu, **el** asistente» · «la asistente».
- **R59** [menor] Cuestionario p. 10 · Errata: «¿**Prefierís** hablarlo?» → «¿Preferís…?». En la escala habitual sería importante. La dejo en menor porque esa frase desaparece con R07.
- **R60** [menor] Cuestionario pp. 1 y 10 · «Paso 1 de 2» en la portada y cuatro pasos en «¿Y ahora qué?». «**Prometemos** que merece la pena» · Cuadrar los pasos y quitar la promesa.
- **R61** [menor] Cuestionario, archivo · La miniatura interna (`docProps/thumbnail.jpeg`) es una página **en blanco**: en la vista previa del Finder o del correo puede verse vacío. Tampoco hay texto alternativo en el mapa de la portada · Quitar la miniatura o regenerarla, y añadir texto alternativo al mapa.
- **R62** [menor] Informe (Avenir Next, del sistema macOS) y cuestionario (Calibri) · Las dos piezas del mismo envío no se parecen. La licencia de Avenir permite incrustarla para ver e imprimir (fsType 4), pero usar una fuente del sistema de Apple en entregables comerciales es dudoso · Una tipografía libre (OFL) común a los dos documentos. Lo decide Lola.
- **R63** [menor] Carpeta `entregables/` · Hubo un fichero de bloqueo de Word (`~$estionario…docx`) desde las 18:46 hasta las 19:30. Iván tuvo abierta **una versión anterior** a la actual (la actual es de las 19:01): lo que vio en Word no es lo que se enviaría. Si hubiera guardado desde Word, habría machacado la nueva · No adjuntar nunca los `~$…`. Avisar a Iván antes de regenerar un documento que tenga abierto. `comprobar.py` lo detecta.

## Fuera del veredicto: necesita decisión de Iván

- Nombrar y criticar a competidores reales, y meter capturas de sus webs, de Treatwell y de Bing en un documento comercial: ¿se acepta?
- Si las opiniones se muestran con permiso del autor o basta el del negocio (R31).

## Para la ronda siguiente

Este veredicto es la vara de medir. El envío de la ronda 2 se revisa con la misma
skill y se compara así:

1. **Ningún R01–R63 reaparece**, ni con otras palabras.
2. **Cero errores que bloqueen y cero importantes** sin aceptación escrita de Iván.
3. **Cada cifra se puede regenerar** desde los datos guardados, y cada cita tiene su prueba.
4. **El Word está probado en Microsoft Word** y en el móvil.
