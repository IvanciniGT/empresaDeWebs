# Guion de WhatsApp · tanda A

> **BORRADOR v0.4 · Menchu** · 2026-11-18
>
> **Catálogo:** v0.3.1 ([preguntas.md](../cuestionario-cliente/preguntas.md),
> tanda A cerrada: 8 obligatorias, 10 condicionales y 1 opcional).
>
> **Qué** se pregunta lo decide Reme. **Cómo** se dice por WhatsApp, y en qué
> orden, lo decido yo. Si el catálogo cambia de versión, este guion se revisa
> antes de usarlo, y [medir_guion.py](medir_guion.py) falla hasta que la
> versión de arriba coincida. Lo revisa Puri y lo aprueba Iván **una vez por
> versión** (A-012).

## Reglas del guion

1. **Una pregunta por mensaje**, y espero la respuesta antes de mandar la
   siguiente. Si contesta varias de golpe, me salto las que ya estén.
2. **Lo que ya sabemos, se confirma**: «Tenemos apuntado…, ¿está bien?».
   Nunca doy por comprobado lo que no lo está, ni afirmo una ausencia.
3. **Una obligatoria no se pregunta si ya la tenemos** (del primer contacto o
   de otra respuesta). Se anota de dónde sale.
4. **Las condicionales, solo si toca**, justo después de la respuesta que las
   activa. El cliente no ve las que no le tocan. **Las condiciones nombran la
   opción, no su número**: si el catálogo reordena las opciones, el guion no
   cambia de significado.
5. **Opciones numeradas, una por línea**, para que pueda contestar con números
   («1 y 3»). Si contesta con palabras, vale igual.
6. Mensajes de **300 caracteres como mucho**. Los que llevan lista de opciones
   pueden llegar a 450.
7. **No ofrezco ni prometo nada al contestar**: ni precios, ni plazos, ni
   extras. Si una respuesta saca algo fuera de catálogo, lo apunto, digo que
   lo consulto y aviso a Federico.
8. **Ninguna pregunta de la tanda B**: ni datos legales, ni nombres de los
   demás, ni fotos (salvo A 5.6, opcional y la última).
9. Plantillas en **vosotros**. Si el cliente trata de tú o de usted, se
   adaptan (§9.2).

## Cuánto dice que le queda

En el mensaje 3 de primer-envio digo «unas [N] preguntas». N son las
obligatorias que faltan más las condicionales que ya sé que tocarán: A 2.2 si
son varios, y A 5.7 y A 5.8 si tienen web. Si la cuenta cambia durante la
conversación: «Gracias, apuntado. Ya solo me quedan [N]». Nunca digo «la
última» salvo que lo sea.

## Orden

| # | ID | ★ | Activa |
|---|---|---|---|
| 1 | A 1.1–1.4 · confirmar nombre, dirección, teléfono y horario | | — |
| 2 | A 3.3 · servicios | ★ | — |
| 3 | A 3.5 · cómo dais las citas | ★ | A 3.7 si marca *aplicación o web de reservas* |
| 4 | A 4.1 · para qué queréis la web | ★ | A 4.6 si marca *pedir o reservar cita* · A 3.4 si marca *vender productos* · A 4.3 si marca *otro idioma* · A 4.7 si marca *buscar personal* |
| 5 | A 5.5 · qué tenéis ya | ★ | A 5.2 si no marca *fotos* · A 5.3 si no marca *logotipo* |
| 6 | A 5.7 · quién lleva la web actual | | Solo si en el primer contacto dijo que tiene web |
| 7 | A 5.8 · qué conservar de la web actual | | Ídem |
| 8 | A 5.4 · ficha de Google | | — |
| 9 | A 4.4 · cada cuánto cambiaríais algo | ★ | — |
| 10 | A 4.5 · para cuándo | | No se pregunta si ya lo dijo |
| 11 | A 2.2 · quién da el visto bueno | | Solo si son varios |
| 12 | A 5.6 · foto de la fachada | opcional | Siempre la última |

**Por qué este orden:** empiezo por lo fácil (confirmar y contar qué hacen),
que es de lo que más saben. Las citas van antes de «para qué queréis la web»
porque la una lleva a la otra. Lo que tienen ya va junto (fotos, logotipo,
web, ficha). Lo de después (cambios, fecha, quién decide) va al final, y la
foto, la última y sin presión.

## Las preguntas

### 1 · A 1.1–1.4 · Confirmar lo que sabemos

> Para empezar, lo fácil. Esto es lo que tenemos apuntado de [negocio]:
>
> 📍 [dirección]
> 📞 [teléfono]
> 🕘 [horario, un día o grupo de días por línea]
>
> ¿Está todo bien? Si hay algo que cambiar, decídmelo.

- Los datos salen **solo** de `expediente.md` §1 y §2. Si un dato está «a
  confirmar», se pregunta igual: el cliente no tiene por qué ver la
  diferencia, pero yo no lo doy por bueno hasta que conteste.
- El nombre del negocio va en la primera línea («de [negocio]») y cuenta como
  A 1.1: si lo escribimos mal, lo dirá.
- **Si contesta** «sí» o «todo bien», A 1.1–1.4 quedan confirmados por el
  cliente. Si corrige algo, lo anoto literal en el ID que toque.
- **A 1.3: si nos da otro número y es un móvil personal**, va a
  `privado/contacto.md`. En el expediente queda solo «teléfono confirmado por
  el cliente, en `privado/contacto.md`».

### 2 · A 3.3 · Servicios ★

> ¿Qué servicios hacéis? Como os salga, sin orden: por ejemplo, [ejemplos del
> bloque de sector]. Si tenéis la lista de precios colgada, también vale una
> foto de la lista.

- Ejemplos para peluquería o barbería: «corte de caballero, de niño, barba,
  afeitado a navaja, degradado…». Para cualquier otro negocio: «contadnos qué
  hacéis o qué vendéis».
- La foto de la lista de precios **no es material para la web**: va a
  `privado/recibido/`, y yo paso los servicios a texto.
- No pregunto precios. Si los manda, los anoto, pero no comento nada.

### 3 · A 3.5 · Cómo dais las citas ★

> ¿Y cómo dais las citas ahora? Podéis decirme más de una:
>
> 1️⃣ Sin cita, por orden de llegada
> 2️⃣ Por teléfono
> 3️⃣ Por WhatsApp
> 4️⃣ Con una aplicación o web de reservas
> 5️⃣ De otra forma

#### ↳ A 3.7 · Qué aplicación (si A 3.5 marca *aplicación o web de reservas*)

> ¿Qué aplicación es? ¿Os bastaría con un botón en la web que lleve a ella?

Si pregunta si podemos meterla dentro de la web: «Lo apunto y os lo confirmo
en el presupuesto». Integrarla no está incluido (§6.1).

### 4 · A 4.1 · Para qué queréis la web ★

Ya nos lo dijo en el primer contacto, con sus palabras. Le cito, para que no
suene a «¿otra vez?», y le pregunto solo si hay algo más (catálogo v0.3.1). Van
**dos mensajes seguidos**, sin esperar entre ellos, para que la cita no alargue
la lista:

> Cuando nos escribisteis, nos dijisteis «[lo que quiere, literal]». Para
> afinar el presupuesto, os pongo unas opciones.

> Además de eso, ¿os interesa algo de esto? Podéis marcar varias.
>
> 1️⃣ Que nos encuentre gente nueva
> 2️⃣ Que vean horario, servicios y cómo llegar sin llamar
> 3️⃣ Que puedan pedir o reservar cita desde la web
> 4️⃣ Vender productos por internet
> 5️⃣ Que se pueda leer en otro idioma
> 6️⃣ Buscar personal
> 7️⃣ Otra cosa

- Si la cita literal es larga, la resumo **sin cambiarle el sentido**, o no la
  cito. Si en el primer contacto no lo dijo, solo mando el segundo mensaje, y
  empieza por «¿Para qué queréis la web?» en lugar de «Además de eso».
- No marco yo ninguna opción por él, aunque crea saber la respuesta. Si su
  frase del primer contacto encaja claramente con una opción y no la marca
  ahora, se lo pregunto en una línea («Nos dijisteis que queríais que os
  pidieran cita: ¿lo cuento?»). No adivino.
- Si marca *otra cosa*: «¿Qué tenéis en mente?», y lo anoto literal en A 4.1.

#### ↳ A 4.6 · Cómo se pide la cita (si A 4.1 marca *pedir o reservar cita*)

> Sobre las citas: ¿preferís que el cliente elija día y hora él solo en la
> web, o que os pida cita y se la confirméis vosotros?
>
> 1️⃣ Que elija él solo
> 2️⃣ Que pida y la confirmamos nosotros

Es **la pregunta que más decide** entre Esencial y Negocio (también cuenta
A 3.3: una carta larga lleva a Negocio). No le digo qué
plan sale de cada respuesta.

#### ↳ A 3.4 · Qué vender (si A 4.1 marca *vender productos*)

> ¿Qué productos querríais vender por internet, y cuántos, más o menos?

Después, sin prometer nada: «Apuntado. Esto lo tengo que consultar y os
digo algo [cuándo]». El [cuándo] lo fija Federico (regla en primer-contacto).
**Aviso a Federico en el momento**, porque está fuera de
catálogo (§5), y él se lo lleva a Iván. **Sigo con el resto de preguntas**,
salvo que Federico me diga que pare. El presupuesto no se cierra hasta que
decida Iván (confirmado por Federico y en el catálogo v0.3.1).

#### ↳ A 4.3 · Qué idioma (si A 4.1 marca *otro idioma*)

> ¿En qué idioma? ¿Tenéis a alguien que lo traduzca?

#### ↳ A 4.7 · Buscar personal (si A 4.1 marca *buscar personal*)

> Para lo de buscar personal: ¿os basta con un aviso en la web («buscamos
> peluquero, escribidnos») o queréis recibir currículums desde la web?

### 5 · A 5.5 · Qué tenéis ya ★

> ¿Qué de esto tenéis ya? No hace falta que lo mandéis ahora; solo quiero
> saberlo.
>
> 1️⃣ Una dirección de internet propia (tipo www.vuestronegocio.es). ¿Cuál?
> 2️⃣ Logotipo en archivo
> 3️⃣ Fotos vuestras del local o de vuestro trabajo
> 4️⃣ Vídeos
> 5️⃣ Nada de esto

- «Fotos vuestras» quiere decir hechas por ellos. Las que hay en Google no son
  suyas ni nuestras (alta-cliente, regla 5).
- Si manda fotos sin que se las pida: «¡Gracias! Las guardo para más
  adelante». Van a `privado/fotos/` y no las uso hasta la tanda B.

#### ↳ A 5.2 · Quién hace las fotos (si A 5.5 no marca *fotos*)

> Para la web harán falta fotos. ¿Las haríais vosotros con el móvil (os
> damos unos consejos) o preferís un fotógrafo?
>
> 1️⃣ Con el móvil, nosotros
> 2️⃣ Un fotógrafo

Si pregunta cuánto cuesta el fotógrafo: «Eso no lo sé todavía; os lo digo en
el presupuesto». La fotografía no está incluida y no tiene tarifa.

#### ↳ A 5.3 · Logotipo (si A 5.5 no marca *logotipo*)

> ¿Os gustaría un logotipo nuevo, o seguís con el nombre tal cual, como en
> el rótulo?
>
> 1️⃣ Logotipo nuevo
> 2️⃣ El nombre tal cual

Si elige el logotipo nuevo: «Apuntado; os lo confirmo en el presupuesto». No
está incluido (§6.1).

### 6 · A 5.7 · Quién lleva la web actual (solo si tiene web)

> Sobre vuestra web de ahora: ¿quién os la lleva? ¿La seguís pagando?

### 7 · A 5.8 · Qué conservar de la web actual (solo si tiene web)

> ¿Hay algo de vuestra web de ahora que queráis conservar? Los textos, las
> fotos, la dirección…

### 8 · A 5.4 · Ficha de Google

> La ficha de Google Maps, la que sale con vuestras opiniones: ¿quién la lleva?
>
> 1️⃣ Nosotros
> 2️⃣ Otra persona
> 3️⃣ No sabíamos que existía
> 4️⃣ No lo sé

Ni ahora ni después pido la contraseña. Si me la manda: «Mejor que no me la
mandéis: nunca necesitamos vuestra contraseña. Borradla del chat, por favor, y
os recomendamos cambiarla». Aviso a Federico y no la anoto en ningún sitio
(§12). **Antes de exportar el chat**, Iván borra ese mensaje en su móvil, y si
ya estaba exportado, lo quita del fichero de `privado/whatsapp/`. Lo mismo con
cualquier dato bancario (regla en primer-contacto).

### 9 · A 4.4 · Cada cuánto cambiaríais algo ★

> Cuando la web esté hecha, ¿cada cuánto creéis que habría que cambiar algo?
> Por ejemplo, el horario de verano, los precios o una promoción.
>
> 1️⃣ Una vez al mes o menos
> 2️⃣ De dos a cuatro veces al mes
> 3️⃣ Más a menudo

Si no lo sabe: «Lo que os parezca; luego se puede cambiar». No le explico qué
plan sale de cada respuesta: las tarifas siguen en [PROPUESTA].

### 10 · A 4.5 · Para cuándo

No se pregunta si ya nos dio una fecha en el primer contacto.

> ¿Para cuándo os gustaría tenerla? Una fecha, o «sin prisa». Es para
> tenerlo en cuenta; el plazo os lo daremos por escrito en el presupuesto.

Si da una fecha, no le digo si llegamos o no. Solo: «Apuntado».

### 11 · A 2.2 · Quién da el visto bueno (solo si son varios)

Sin que suene a «¿quién manda aquí?»:

> Cuando haya que dar el visto bueno (al presupuesto, a los diseños…),
> ¿basta con que me conteste uno de vosotros, o preferís decidirlo juntos?

Si nombra a alguien, el nombre va a `privado/`.

### 12 · A 5.6 · Foto de la fachada (opcional, la última)

> Una última cosa, y solo si la tenéis a mano: ¿nos mandáis una foto de la
> fachada con el rótulo? Mejor de día y sin gente delante. Si no la tenéis, no
> pasa nada.

- Si la manda: a `privado/fotos/`, y aviso a Federico para Lola.
- Si no la manda, no se recuerda: es opcional.

## Cierre

> ¡Ya está, [nombre]! Muchas gracias. Con esto os preparamos el presupuesto,
> y en cuanto lo tengamos os escribo.

Si quedó pendiente lo de vender por internet (A 3.4):

> ¡Ya está, [nombre]! Muchas gracias. Antes del presupuesto os confirmo lo de
> vender por internet, y en cuanto lo tengamos todo os escribo.

[PENDIENTE A-011] Cuando haya tarifas y un plazo para el presupuesto: «Os lo
mando el [día]».

## Si falta una ★ al final

Se lo pido una sola vez, diciendo por qué lo necesito:

> Me falta solo una cosa, y sin ella no puedo cerrar el presupuesto:
> [pregunta]. Es para [lo que cambia, en una frase sin jerga].

Si sigue sin contestarla, se lo paso a Federico. No insisto más.

## Cómo se anotan las respuestas

En `clientes/<negocio>/privado/respuestas-tanda-a.md`, una fila por ID, en el
orden del catálogo, no en el de la conversación:

```markdown
# Respuestas · tanda A · [negocio] · catálogo v0.3.1
| ID | Fecha | Canal | Respuesta literal | Opciones | Notas |
|---|---|---|---|---|---|
| A 1.1–1.4 | 2026-__-__ | WhatsApp | «Todo bien menos el sábado, que cerramos a las 13:30» | — | A 1.4 corregido |
| A 3.5 | | | «Por teléfono y por wasap» | por teléfono, por WhatsApp | |
| A 4.5 | 2026-__-__ | primer contacto | «Para antes de Navidad» | — | No se ha vuelto a preguntar |
| A 3.7 | — | — | — | — | No aplica: A 3.5 no marca *aplicación* |
```

- **Literal**, con sus faltas y sus palabras. En la columna «Opciones» va mi
  lectura, **con el nombre de la opción y no su número**: así sigue valiendo si
  el catálogo las reordena. Si la respuesta es ambigua, le pregunto en una
  línea («¿Eso es por teléfono, por WhatsApp o las dos?»). No adivino.
- Las condicionales que no tocan se anotan como «No aplica», con el porqué:
  así Reme sabe que no se olvidaron.
- Las fotos van a `privado/fotos/` o a `privado/recibido/`, y en «Notas»
  apunto el nombre del fichero.

## Comprobación antes de pasarlo a Puri

```
/usr/bin/python3 procesos/skills-borrador/primer-envio/medir_guion.py
```

El script comprueba cinco cosas:

1. Que la versión del catálogo de la cabecera coincide con la de
   `preguntas.md`.
2. Que están todos los ID de la tanda A del catálogo, y ninguno más.
3. Que cada pregunta con opciones numeradas en el catálogo tiene las mismas
   opciones en el guion.
4. Que ningún mensaje pasa de 300 caracteres, o de 450 si lleva opciones.
5. Que ninguna condición nombra una opción por su número.

Si algo falla, el script termina con error y no se pasa a Puri.

## Si algo no se puede preguntar bien por WhatsApp

Se lo digo a Federico para Reme, y no lo arreglo yo cambiando la pregunta. Lo
de cada versión está en la [revisión de Menchu](../../ronda-1/revision-menchu.md), §8.

## Versiones

| Versión | Catálogo | Fecha | Qué cambia |
|---|---|---|---|
| v0.1 | — | 2026-11-18 | Solo el formato, a la espera de la lista de Reme |
| v0.2 | v0.3 | 2026-11-18 | Guion completo: orden, mensajes, condicionales, cierre y cómo se anota |
| v0.3 | v0.3.1 | 2026-11-18 | A 4.1 con 7 opciones y una sola de cita; A 4.6, la que más decide el plan; A 5.7 y A 5.8 por separado; las condiciones y la columna «Opciones», por nombre; A 3.4 sigue la conversación; A 1.3, móvil personal a `privado/`; cierre con A 3.4 pendiente; script de comprobación |
| v0.4 | v0.3.1 | 2026-11-18 | Revisión de Puri: A 3.4 con [cuándo] (R04); contraseñas y datos bancarios, fuera del chat exportado (R05); A 4.6, «la que más decide» (R07); A 5.3, «seguís» (R11) |
