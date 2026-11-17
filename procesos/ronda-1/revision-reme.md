# Revisión de Reme · ronda 1

> E-003 · 2026-11-17 · Caso simulado: Peluquería Hermanos Cotillas.
> He revisado el cuestionario (Word convertido a PDF: 10 páginas, 11 bloques,
> 100 casillas), su generador, el previo de precio y el expediente. La revisión
> pregunta a pregunta está en el [Anexo A](#anexo-a--el-cuestionario-pregunta-a-pregunta).

**En una frase:** el cuestionario pregunta a la vez lo que necesitamos para
el presupuesto y lo que necesitaremos al hacer la web. Propongo separarlo con
una regla: **si la respuesta puede cambiar el plan, el precio o el plazo, va en
B1. Si solo cambia el contenido, va en B2.** Con eso, B1 baja a unas 25
preguntas y 4 páginas como máximo, y cubre todos los mínimos que pidió Iván.

## 1. Lo que mantendría

1. **Prerrellenar con lo que ya sabemos** y pedir solo que lo valide. Es lo que
   más trabajo le ahorra al cliente.
2. **Código de colores** (gris, lo que sabemos; naranja, para que escriba;
   verde, nuestras propuestas) y la **★**. Cambio su significado: «sin esto no
   hay presupuesto».
3. **Dos baterías** y el «Paso 1 de 2» en la portada.
4. **«Si no sabéis algo, dejadlo en blanco»**, la **alternativa por teléfono**
   y el **aviso de no mandar contraseñas**.
5. **Casillas como controles de contenido de Word.** Lo he comprobado: se
   pueden leer automáticamente. En una copia simulé un cliente que marca 3
   casillas y un script de prueba leyó esas 3 y ninguna más. Esto permite
   pasar las respuestas a requisitos sin copiarlas a mano.
6. **El generador en código:** el documento es reproducible. Lo que cambiaría
   es dónde vive el contenido (§2).
7. **Del previo de precio:**
   - recomienda el plan más sencillo y dice qué lo cambiaría;
   - no ofrece SEO continuo de entrada, que es lo honesto (§4.1);
   - da los precios unitarios;
   - avisa de que las tarifas son [PROPUESTA].
   He rehecho las cuentas con calculadora: **todas cuadran**.

## 2. Lo que cambiaría

1. **[bloquea el envío real]** No hay cláusula de protección de datos.
   - **Por qué:** pedimos nombre, móvil, correo y NIF sin decir quién los
     trata, para qué ni durante cuánto tiempo, y la empresa aún no tiene
     nombre (§15).
   - **Cómo:** una cláusula breve, redactada por un profesional (§15). Para
     la simulación no bloquea.
2. **[importante]** Es demasiado largo: 10 páginas, 100 casillas y preguntas
   sin para qué.
   - **Por qué:** mi ficha pide «pocas preguntas, las justas».
   - **Cómo:** B1 de 4 páginas como máximo, montado desde un
     [catálogo](../skills-borrador/cuestionario-cliente/preguntas.md) en el
     que cada pregunta lleva ID, para qué y destino. La que no tiene destino,
     se quita.
3. **[importante]** Los datos legales (titular y NIF) están en B1.
   - **Por qué:** no hacen falta para el presupuesto. Pedir el NIF a quien aún
     no es cliente frena, y §12 dice que se recoge solo lo necesario.
   - **Cómo:** pasan a B2, al contratar. Hay una excepción: si el gestor
     confirma que la forma jurídica del cliente cambia el presupuesto
     (retención, §8.3), esa única pregunta vuelve a B1.
4. **[importante]** El bloque 8 pide aprobar los textos propuestos.
   - **Por qué:** es prematuro, porque los textos tienen huecos ([nombre],
     [año]) que dependen de las respuestas. Además, no está claro si un
     «Cambiadlo así» cuenta como una de las 2 rondas de §6.1: es justo el
     tipo de ambigüedad que hace crecer el alcance.
   - **Cómo:** la frase principal se enseña como muestra en el informe, sin
     casillas. La aprobación se hace en la fase de textos (§13.5, paso 4).
5. **[importante]** Faltan las preguntas que deciden el precio.
   - **Por qué:** el previo dice «cambiará poco» o «no sabemos si quiere
     reservas», y el cuestionario no pregunta ni lo uno ni lo otro. Está en §3.
   - **Cómo:** añadirlas a B1. Ya están en el catálogo.
6. **[importante]** El cuestionario contiene afirmaciones sin fuente
   (regla 3 de alta-cliente):
   - «Casi 300 peluquerías y barberías a menos de kilómetro y medio»: el
     JSON de OSM tiene 274 peluquerías, contando la propia Cotillas (273
     competidores), más 9 tiendas de productos de peluquería;
   - «Los negocios que publican precios reciben más llamadas»;
   - «Las fotos son lo que más se mira».
   - **Cómo:** Chema les pone fuente o las quita.
7. **[importante]** «Web propia: No tenéis» afirma una ausencia que no podemos
   probar (regla 4).
   - **Cómo:** «No hemos encontrado ninguna. Si tenéis, poned el enlace».
8. **[importante]** El previo da por hechas cosas que no sabemos:
   - «Un negocio que paga en efectivo»: no sabemos cómo cobran;
   - «Unos 10–15 €/año» de dominio: sin fuente;
   - «competencia brutal»: sin dato; el dato es «273 peluquerías en 1,5 km
     según OSM».
   - **Cómo:** regla 4 de la nueva skill: sin base, no se escribe.
9. **[importante]** La prioridad se puso a ojo.
   - **Cómo:** 5 criterios puntuados de 0 a 2, en los que lo desconocido vale
     1 (§4).
10. **[importante]** No hay formato de requisitos ni un paso que pase las
    respuestas a requisitos.
    - **Cómo:** `clientes/<negocio>/requisitos.md` con la
      [plantilla](../skills-borrador/cuestionario-cliente/plantilla-requisitos.md).
11. **[menor]** «Si tuvierais que quedaros con una, rodeadla»: en un Word no
    se puede rodear.
    - **Cómo:** pregunta aparte de una línea (4.2).
12. **[menor]** La columna «¿Nos ayudáis a hacerla?» se entiende de dos
    maneras: ¿quién ayuda a quién?
    - **Cómo:** pregunta 5.2: «¿las haríais vosotros con nuestra guía, o
      preferís un fotógrafo?».
13. **[menor]** Hay preguntas duplicadas:
    - las redes salen en los bloques 1 y 10;
    - el WhatsApp sale dos veces en el bloque 2;
    - el «cliente típico» ya lo dicen las reseñas, así que basta con validarlo;
    - «Cortes modernos» está en «Qué os define» y en servicios.
14. **[menor]** «Lo que ya sabemos» incluye la nota de Google (4,8 y 132
    opiniones).
    - **Por qué:** el cliente no puede corregirla, y cambia sola.
    - **Cómo:** quitarla de esa tabla.
15. **[menor]** «¿Qué contacto ponemos en la web?» se plantea como elección,
    pero §6.1 ya incluye siempre llamada, WhatsApp y formulario.
    - **Cómo:** lo que falta es el número y el correo de destino, y eso pasa a B2.
16. **[menor]** El texto tiene una errata y una promesa:
    - «¿Prefierís hablarlo?» debe ser «¿Preferís hablarlo?»;
    - «Prometemos que merece la pena» es una promesa que no podemos comprobar.
    - **Cómo:** se lo paso a Chema.
17. **[menor]** La maquetación tiene fallos:
    - el título del bloque 7 queda solo al pie de la página 6, y el del 11, al
      pie de la 9;
    - «Logotipo» queda separado de su bloque;
    - la portada ocupa una página entera con un mapa.
    - **Cómo:** se lo paso a Lola.
18. **[menor]** El escenario B del previo («Negocio + Plus») cambia dos cosas
    a la vez, y así no se ve cuál encarece.
    - **Cómo:** cada variación cambia una sola cosa.
19. **[menor]** El contenido del cuestionario vive dentro del generador, y para
    cada cliente se copia el script.
    - **Cómo:** el contenido sale del catálogo y el generador lo lee. Es
      trabajo de Paco.
20. **[menor]** El previo y el cuestionario van en paralelo (fases 3 y 5).
    - **Por qué:** el previo dice qué preguntas deciden el plan.
    - **Cómo:** el previo va primero. Se tarda poco.

## 3. Lo que falta

1. **Preguntas de B1 que cambian el precio o el plan.** Ninguna está en el
   cuestionario actual:
   - **2.2** ¿Quién da el visto bueno? Son dos hermanos: ¿aprueban los dos o
     basta con uno? Afecta a las rondas.
   - **3.4** ¿Queréis vender **por internet**? Una tienda online está fuera de
     catálogo.
   - **3.5** ¿Usáis alguna aplicación de citas? Integrarla no está incluido (§6.1).
   - **4.4** ¿Cada cuánto cambiaríais algo? Decide entre Básico y Plus.
   - **4.5** ¿Para cuándo la queréis?
   - **5.2** ¿Fotógrafo o fotos propias?
   - **5.3** ¿Queréis un logotipo nuevo?
2. **Formato de requisitos y paso de las respuestas a requisitos.** Lo propongo
   en mi skill y en la
   [plantilla](../skills-borrador/cuestionario-cliente/plantilla-requisitos.md).
   El requisito R-01 de la plantilla, por ejemplo, dice qué hay que entregar,
   de dónde sale y cómo lo comprueba Puri.
3. **Dónde guardar los requisitos** (mi duda del arranque). Propongo:
   - `clientes/<negocio>/requisitos.md`, enlazado desde el expediente;
   - los cuestionarios devueltos, intactos, en `clientes/<negocio>/recibido/`.

   Va en un fichero aparte porque el expediente es el registro y los
   requisitos son el acuerdo. Depende de que Iván confirme `clientes/` (§6).
4. **Versión del cuestionario en el pie** («B1 v0.2»). Sin ella, el origen de
   un requisito («B1 4.2») no se puede rastrear cuando el cuestionario cambie.
5. **Una fase del alta entre las respuestas y el presupuesto.** Hoy
   [alta-cliente.md](../alta-cliente.md) acaba en el primer envío. Falta:
   respuestas → requisitos y borrador de presupuesto (Reme) → Puri → Iván →
   Menchu envía.
6. **Qué pasa si el cliente no devuelve el cuestionario:** cuándo se le
   recuerda y cuándo se da por cerrado. Es de Menchu y Federico; solo lo señalo.

## 4. Mis skills: qué he cambiado y por qué

### [`cuestionario-cliente`](../skills-borrador/cuestionario-cliente/SKILL.md) v0.2

- **Una regla decide qué va en cada batería**, en lugar de una lista de 11
  bloques.
- **Catálogo de preguntas**
  ([preguntas.md](../skills-borrador/cuestionario-cliente/preguntas.md)) con
  ID, ★, para qué y destino:
  - **B1**, 27 preguntas en 5 bloques: lo que sabemos, contacto, negocio, la
    web que queréis y lo que tenéis.
  - **B2**, al contratar, y bloques según el tipo de web: reservas, idiomas y
    empleo.
- **Mínimos de Iván, todos en B1:**

  | Mínimo de Iván | Preguntas |
  |---|---|
  | Datos de contacto | 2.1–2.5 |
  | Herramientas y procesos | 3.5 |
  | Puntos fuertes, posicionamiento y valores | 3.2, 4.1 |
  | Experiencia | 3.1 |
  | Para qué quiere la web e idiomas | 4.1–4.3 |
  | Fotos, vídeos y logotipo | 5.1–5.3 |
  | Datos del local | 1.2, 1.4, 3.6 |
  | Productos y precios | 3.3, 3.4 |

  En B1 solo se pregunta si tienen fotos o vídeos (5.1). Cómo hacerlos va a
  B2. Ningún plan dice si un vídeo se incluye en la web: es una duda para Iván (§6).
- **Bloques de sector:** sí, pero solo de los sectores en los que ya hemos
  trabajado. Cambian solo las casillas de 3.2 y 3.3 y la lista de fotos; el
  resto es común. Para un sector nuevo se usa el bloque genérico (filas en
  blanco) y, al terminar, se escribe el suyo. Así no inventamos qué hace una
  cafetería.
- **Paso de las respuestas a requisitos**, por destino:
  - `DATO` va al expediente;
  - `PRECIO`, al presupuesto;
  - `REQ`, a `R-xx`;
  - `CONT` y `DIS`, a materiales para Chema y Lola;
  - lo que falta, a «Falta saber».
  La versión 1.0 de los requisitos queda fijada cuando el cliente aprueba el
  presupuesto; después solo cambia con el control de cambios.
- **Comprobaciones antes de pasarlo a Puri:** páginas, ID, versión, cláusula
  de protección de datos y que no haya afirmaciones sin fuente.

### [`previo-precio`](../skills-borrador/previo-precio/SKILL.md) v0.2

- **Va antes que B1** y dice qué pregunta de B1 decide cada cambio de plan.
- **Escenarios de una sola variación** cada uno, con la operación reproducible.
- **Extras sin tarifa, sin importe.** Los costes de terceros, solo con fuente y fecha.
- **Prioridad puntuada:** 5 criterios de 0 a 2, en los que lo desconocido vale
  1. Los cortes son [PROPUESTA]. Lo probé con Cotillas:

  | Criterio | Puntos | Por qué |
  |---|---|---|
  | Encaje en plan | 2 | Esencial, sin extras obligatorios |
  | Material | 1 | No sabemos si tienen fotos propias |
  | Ingreso | 1 | 838 € de base el primer año |
  | Urgencia | 1 | No se sabe |
  | Dependencias | 1 | No sabemos quién gestiona la ficha de Google |
  | **Total** | **6 / 10** | **Media.** Federico la puso alta a ojo |

  La diferencia es lo que no sabemos, que es justo el riesgo que Federico
  señaló («que tarden en mandar fotos y datos»). Conclusión: **antes de B1 la
  prioridad sirve para poco** (casi todo vale 1). La que cuenta es la que se
  recalcula con las respuestas, y así lo dice la skill.
- **El «valor como caso de éxito» deja de puntuar:** es una suposición y
  necesitaría el permiso del cliente.
- **Nueva sección «del previo al borrador de presupuesto».** Mi ficha me pide
  el borrador y no había ningún paso para hacerlo.

## 5. Lo que necesito de otros agentes (lo coordina Federico)

| Agente | Qué necesito | Para qué |
|---|---|---|
| **Chema** | Textos de ayuda de B1, sin las afirmaciones sin fuente (§2.6) y sin la errata ni la promesa (§2.16). Llevar al informe el aviso de los directorios, las opiniones destacadas y la frase principal como muestra. | Que B1 sea solo de preguntas y que lo que vende vaya en el informe |
| **Chema** | ¿Le vale hacer la historia (B2 6.3) por teléfono, con Menchu? | Escribir una anécdota cuesta más que contarla |
| **Lola** | Maquetar B1 en 4 páginas como máximo: sin portada a página completa y sin títulos solos al pie de la página. | Regla 1 de mi skill |
| **Lola** | ¿Necesita «webs que os gustan y colores» (B2 6.9), ahora que tiene la guía previa? | Si no lo necesita, se quita |
| **Paco** | En `docx_util.py`: parámetro `id` en casillas, opciones, huecos y tablas, que se guarde como etiqueta del control (`w:tag`); huecos de texto como controles de contenido; generador que lea el catálogo. | Que cada respuesta llegue con su ID |
| **Paco** | Un lector `leer_cuestionario.py`: del Word devuelto a respuestas por ID en Markdown. Mi prueba indica que es viable con lo que ya está instalado (`lxml` en `.venv`). | Pasar las respuestas a requisitos sin copiarlas a mano |
| **Paco** | Probar el Word en Microsoft Word, en el ordenador y en el móvil. Está instalado en esta máquina, pero abre ventanas: hace falta permiso de Iván. | Si las casillas no funcionan en Word, el formato no sirve |
| **Menchu** | Guardar el cuestionario devuelto, intacto, en `recibido/`. Si es por teléfono, anotar las respuestas con los ID del catálogo. | Poder rastrear el origen de cada requisito |
| **Puri** | Que revise si la columna «se comprueba así» de la plantilla de requisitos le sirve para su revisión. | Ella es quien la usa |
| **Federico** | Añadir a `alta-cliente.md` la fase «requisitos y borrador de presupuesto» (§3.5) y poner el previo antes de B1. Enlazar `requisitos.md` desde la plantilla del expediente. | Son ficheros suyos |

## 6. Lo que tiene que decidir Iván (lo lleva Federico)

| Asunto | Opciones | Recomiendo | Por qué |
|---|---|---|---|
| **Dónde viven expedientes y requisitos** | `clientes/<negocio>/` (provisional) / otro sitio | Confirmar `clientes/<negocio>/`, con `requisitos.md` y `recibido/` | Ya funciona y tiene git. Lo necesito para guardar requisitos |
| **Formato del cuestionario** | a) Word · b) formulario de terceros (Google Forms, Typeform…) · c) formulario propio · d) llamada guiada | **a) Word para la ronda 2, con d) siempre disponible.** c) cuando esté decidida la plataforma (§15). b) no, de momento | b) supone un tercero que trata datos (contrato de encargado y posible transferencia fuera de la UE). c) depende de una plataforma sin decidir. El Word tiene una pega: **no está probado en Word ni en el móvil** |
| **Cláusula de protección de datos** | — | Texto breve revisado por un profesional | Sin ella no se puede enviar a un cliente real |
| **Opiniones de Google en la web** | ¿Basta el permiso del negocio? | Consultarlo junto con los textos legales tipo (§15) | Son textos de terceros. No sé la respuesta y no la invento |
| **Dominio** | Dentro de la cuota / aparte, a precio de coste | Dentro de la cuota, a nombre del cliente | §6.2 ya promete «renovación del dominio», y una línea aparte de pocos euros añade fricción. Falta saber el coste real: hay que elegir registrador, y eso es un gasto (§10.2) |
| **¿Creación sin mantenimiento?** | Sí / no | Decidirlo | Si se puede, falta un escenario y saber quién aloja la web |
| **Suscripción sin pago inicial** | Cuándo se ofrece y qué pasa en el mes 13 | Decidirlo antes de ofrecerla | 69 € × 12 = 828 € de base, frente a 838 € del escenario A: casi lo mismo el primer año, pero el segundo año no está definido |
| **Vídeo en la web** | ¿Entra en Esencial y Negocio, o es un extra? | Decidirlo | §6.1 no lo dice, y es uno de los mínimos del cuestionario |
| **Forma jurídica del cliente y presupuesto** | Pregunta para el gestor | — | Si cambia la retención (§8.3), la pregunta pasa a B1 |

## 7. Herramientas: qué necesito o propongo

- **No hay que instalar nada.** El lector de respuestas se puede hacer con
  `lxml`, que ya está en `.venv`. Lo pido a Paco (§5).
- **Para comprobar el número de páginas** basta con `soffice` y `pdfinfo`, que
  ya están instalados.
- **Microsoft Word** está instalado y servirá para probar el cuestionario. Abre
  una ventana, así que la prueba se hace cuando Iván lo permita.
- **Formulario propio:** queda aparcado hasta que se decida la plataforma (§15).
- **Pruebas que he hecho**, todas en `/tmp/reme`, fuera del repositorio:
  - convertir una copia del Word a PDF;
  - simular unas respuestas y leerlas;
  - repetir las cuentas del previo.

  No he tocado ningún fichero del cliente.
- **Aviso:** en `entregables/` hay un `~$estionario - Peluquería Hermanos
  Cotillas.docx`. Es el bloqueo que deja Word mientras el documento está
  abierto: alguien lo tenía abierto. No lo he tocado. Si nadie lo tiene
  abierto, es un resto y conviene que no entre en git.

---

## Anexo A · El cuestionario pregunta a pregunta

Destinos: **B1**, se queda (con su ID nuevo del catálogo); **B2**, al
contratar; **B2-tipo**, solo si el tipo de web lo pide; **fusionar**; **fuera**.

| Bloque actual | Pregunta | ¿Y eso para qué? | Decisión |
|---|---|---|---|
| Portada | Mapa a página completa | Decorar | **Fuera** o reducido (Lola) |
| Cómo rellenar | Leyenda y tres consejos | Que lo entienda solo | B1, más corto |
| 1 · Sabemos | Nombre | Identidad, dominio | B1 1.1 |
| 1 · Sabemos | Dirección | Mapa, ficha de Google | B1 1.2 |
| 1 · Sabemos | Teléfono | Botón de llamada | B1 1.3 |
| 1 · Sabemos | Horario | Va siempre en la web; los directorios no coinciden | B1 1.4 ★ |
| 1 · Sabemos | Quiénes sois | Textos | B1 1.5 |
| 1 · Sabemos | Opiniones en Google 4,8 / 132 | El cliente no puede corregirla | **Fuera** |
| 1 · Sabemos | Web propia: «No tenéis» | Si existe, cambia el trabajo | **Fusionar** en 1.7 y reformular (regla 4) |
| 1 · Sabemos | Redes sociales | Enlaces | **Fusionar** en 1.7 (está repetida en el bloque 10) |
| 1 · Sabemos | Aviso de los directorios | Convencer, no preguntar | **Al informe** (Chema) |
| 2 · Contacto | Nombre de quien nos atiende | Hablar con él | B1 2.1 ★ |
| 2 · Contacto | Móvil | Canal principal | B1 2.3 ★ |
| 2 · Contacto | ¿Tiene WhatsApp? | Canal principal | **Fusionar** en 2.3 |
| 2 · Contacto | Correo | Enviar el presupuesto | B1 2.4 ★ |
| 2 · Contacto | Mejor momento para llamar | Llamar cuando puedan | B1 2.5 |
| 2 · Contacto | ¿Qué contacto ponemos en la web? | §6.1 ya los incluye todos | **B2** 6.11, como «qué número y qué correo» |
| 2 · Contacto | WhatsApp para clientes | Botón de WhatsApp | **B2** 6.11 |
| 3 · Legales | Forma jurídica, titular, NIF, domicilio fiscal | Contrato, factura, aviso legal | **B2** 6.1 (salvo lo que diga el gestor) |
| 4 · Quiénes sois | Vuestros nombres | Textos | **B2** 6.2. En B1 basta 2.1 |
| 4 · Quiénes sois | Año en que abrieron vuestros padres | Experiencia (mínimo de Iván) | B1 3.1, como «¿desde qué año existe?» |
| 4 · Quiénes sois | Cómo se llamaban vuestros padres | Textos; son datos de terceros | **B2** 6.3, y solo si quieren que salgan |
| 4 · Quiénes sois | Desde cuándo lo lleváis vosotros | Textos | **B2** 6.3 |
| 4 · Quiénes sois | ¿Siempre en Octavio Cuartero? | Textos | **B2** 6.3 |
| 4 · Quiénes sois | ¿Trabaja alguien más? | Textos, equipo | **B2** 6.3 |
| 4 · Quiénes sois | Anécdota | Textos | **B2** 6.3, por teléfono |
| 4 · Quiénes sois | ¿Qué os define? (10 casillas) | Puntos fuertes, valores, posicionamiento | B1 3.2 (bloque de sector), sin «Cortes modernos» |
| 4 · Quiénes sois | ¿Algo más que os diferencie? | Lo mismo | **Fusionar** en 3.2 como «Otra» |
| 4 · Quiénes sois | Intro «casi 300 peluquerías» | Convencer | Corregir el dato (Chema) |
| 5 · Servicios | Tabla de servicios, precio, duración | Sección de servicios | B1 3.3 **sin duración** (solo sirve para reservas: B2-tipo) |
| 5 · Servicios | Intro «publicar precios trae más llamadas» | Convencer | Fuente o fuera (Chema) |
| 5 · Servicios | Citas (4 opciones) | Plan | B1 3.5 lo de hoy; el deseo, a 4.1 |
| 5 · Servicios | ¿Cómo dais las citas ahora? | Si usan una aplicación, integrarla es un extra | B1 3.5 ★ |
| 5 · Servicios | Formas de pago | Información práctica, no cambia el precio | **B2** 6.5 |
| 6 · Objetivos | ¿Para qué queréis la web? (8 casillas) | Plan y alcance | B1 4.1 ★: se aclara «vender **por internet**» y se añade «reservar desde la web» |
| 6 · Objetivos | «Rodeadla» | Prioridad | B1 4.2, en una línea |
| 6 · Objetivos | Cliente típico (7 casillas) | Ya lo dicen las reseñas | **Fusionar**: validar en 1.6 |
| 6 · Objetivos | ¿Qué cliente os gustaría tener más? | Posicionamiento | **Fusionar** en 4.1 («llegar a otro tipo de cliente») |
| 6 · Objetivos | Idiomas | Las traducciones no están incluidas | B1 4.3 |
| 7 · Opiniones | Permiso para mostrarlas | Contenido | **B2** 6.6, pendiente de la duda legal |
| 7 · Opiniones | Recuadro de citas | Convencer | **Al informe** |
| 8 · Textos | Frase principal, quiénes somos, por qué venir | Aprobar textos | **Fuera de B1**: muestra en el informe; se aprueba en la fase de textos |
| 9 · Fotos | 8 fotos × «¿la tenéis?» / «¿nos ayudáis?» | La fotografía es un extra; riesgo de plazo | B1 5.1–5.2 resumido; la lista, a **B2** 6.7 |
| 9 · Fotos | Vídeo | Mínimo de Iván; ningún plan dice si se incluye | B1 5.1 («fotos o vídeos»); el vídeo concreto, a **B2** 6.7 |
| 9 · Fotos | Consejos para hacer fotos | Instrucciones de trabajo | **B2** 6.7 |
| 9 · Fotos | Logotipo (3 opciones) | El logotipo es un extra | B1 5.3, con «queremos uno nuevo» |
| 10 · Internet | Ficha de Google: ¿quién la gestiona? | Alta o revisión de la ficha (§6.1) | B1 5.4 |
| 10 · Internet | Aviso de contraseñas | Seguridad (§12) | B1, más corto; completo en B2 6.12 |
| 10 · Internet | Redes (tabla) | Enlaces | **Fusionar** en 1.7 |
| 10 · Internet | Dominio | Registro | B1 solo «¿tenéis ya?» (1.7); elegirlo, en **B2** 6.10 |
| 11 · Gustos | Webs que gustan y que no; colores | Diseño | **B2** 6.9, si Lola lo necesita |
| Cierre | ¿Y ahora qué? | Expectativas | B1. Errata «Prefierís» y quitar «Prometemos…» |
