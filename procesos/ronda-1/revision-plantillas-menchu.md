# Revisión · Plantillas de Menchu y guion de la tanda A

> Revisado por **Puri** (Calidad) · 2026-11-18 · Encargo E-014 · skill `revisar-entregable` v0.3
> Revisión **una vez por versión** (A-012). Si cambia una plantilla, se revisa otra vez.

```
VEREDICTO: RECHAZADO
```

**2 bloquean · 4 importantes · 5 menores.**

Están muy bien hechas, y los dos errores que bloquean no son de redacción:

- **R01:** el primer contacto pide datos personales sin decir para qué ni quién los trata (lo mismo que R08 en el envío de Federico).
- **R02:** al cliente se le promete un día calculado con un plazo que Iván todavía no ha aprobado.

**Los dos se cierran con decisiones de Iván, sin reescribir nada más.** Si Iván decide los
dos y Menchu arregla los cuatro importantes, lo apruebo en una segunda vuelta corta.

**Para la ronda 2 (simulación, sin cliente real)** se pueden usar ya: R01 y R02 solo
importan cuando hay una persona de verdad al otro lado.

## Qué he revisado

| Fichero | Versión | sha256 |
|---|---|---|
| `primer-contacto/SKILL.md` | v0.3 · 18/11 15:33 | `1ddaf61cfcc0` |
| `primer-envio/SKILL.md` | v0.3 · 18/11 17:10 | `55be931d4cdc` |
| `primer-envio/guion-tanda-a.md` | v0.3, catálogo v0.3.1 · 18/11 17:09 | `5ff84f8f3813` |
| Contra: `cuestionario-cliente/preguntas.md` | v0.3.1 · 18/11 16:33 | `f00212c3abbe` |

Además del catálogo, contra AGENTS.md y las decisiones A-001 a A-015.

## Cómo lo he revisado

1. Leído todo entero, mensaje a mensaje, como lo recibiría el cliente.
2. Guion contra catálogo: `medir_guion.py` de Menchu da todo en orden. Coinciden los 19 ID y las opciones de las 5 preguntas con opciones, y el mensaje más largo tiene 310 caracteres (el límite con opciones es 450). Además lo he cruzado a mano, condición por condición.
3. `comprobar.py`:
   - **ortografía**: sin erratas; lo que marca son formas correctas como «Borradla» y «tasarle», nombres de ficheros y términos técnicos;
   - **datos personales**: ninguno;
   - **huecos**: solo los intencionados, como `[nombre]`, `[día]` y `[Empresa]`.
4. Cada promesa al cliente, contra lo que podemos cumplir hoy.

**No comprobado:**

- La lista de frases de Chema no la ha leído el script, porque ha renombrado la sección en sus skills. La he revisado a mano.
- El Word de la tanda A que va con la copia por correo: no es parte de este encargo y necesita su propia prueba de Iván (A-007).
- Cómo se ven los mensajes en un WhatsApp real.

## Lista J · mensajes y plantillas de WhatsApp

| Punto | Resultado |
|---|---|
| Se revisa el texto exacto que copiará Iván | ✓ Las plantillas son el texto; Menchu redacta cada envío en `privado/mensajes/` |
| Primer mensaje: quién escribe, que es IA y de dónde viene el contacto | ✓ Primer contacto (A-004, palabra por palabra) y primer envío («con la que hablasteis el [día]») |
| Una idea por mensaje; cada pregunta con su ID | ✓ Los 19 ID, una pregunta por mensaje, condiciones por nombre de opción |
| Cifras copiadas del informe aprobado | ✓ Regla escrita en «Antes de enviar» y en las reglas |
| Recordatorios a los 3 y 8 días, sin presión ni promesas | ✓ Con una laguna: R10 |
| Huecos marcados y explicados | ✓ |
| Ninguna llamada (A-002) | ✓ Bien resuelto en todas las respuestas («¿Me llamáis?») |
| «Gratis y sin compromiso» (A-005) | ✓ |
| Nada [PROPUESTA] como definitivo | ✗ **R02** |
| Respuestas con plazo cuando no sabemos algo (§9.2) | ✗ **R04** |

## Bloquean

- **R01** [bloquea · C] Primer contacto, mensaje 1 y respuesta a «¿Qué vais a hacer con mis datos?» · Se piden nombre, móvil, correo y la necesidad literal, y la información de privacidad está marcada [PENDIENTE A-010]. El RGPD (art. 13) pide informar **en el momento** de recoger los datos; es el mismo defecto que R08 en el envío de Federico · Una de dos: el texto de privacidad del profesional (A-010), o una línea provisional que Iván apruebe por escrito, con responsable, finalidad, cuánto se guarda (3 meses si no contrata, A-009) y cómo ejercer los derechos.
- **R02** [bloquea · B] Primer contacto, mensaje 6 («El [día] os mando…») y aviso de retraso; primer envío, «Cuándo» · El día que se promete sale de los **5 días laborables**, que la propia skill marca como [PROPUESTA]. A-012 dice que Menchu propone el plazo, no que esté aprobado · **Se cierra sin tocar el texto si Iván aprueba los 5 días** al aprobar estas plantillas. Si no, las plantillas no dicen día.

## Importantes

- **R03** [importante · A] Primer envío, mensaje 3 («Casi todas son para confirmar lo que ya sabemos»); correo («con casi todo ya rellenado: solo tenéis que corregir y completar»); primer contacto, mensaje 6 («unas pocas preguntas con casi todo ya rellenado») · Es falso: de las 8 obligatorias, **solo una** (A 1.1–1.4) confirma lo que sabemos; el resto son preguntas nuevas. El cliente lo descubrirá en la segunda pregunta · Algo que sí sea verdad, por ejemplo «La primera es para confirmar lo que ya tenemos; las demás son cortas y casi todas se contestan eligiendo una opción» (5 de las 8 la tienen).
- **R04** [importante · B] Guion, A 3.4 («os digo algo»); primer envío, «Si dice… pide algo fuera de §6» («Lo apunto y os lo confirmo»); primer contacto, logo/tienda/redes («Lo apunto y os lo confirmo») y descuento («Lo consulto y os digo») · No dan plazo, y §9.2 manda que, si no sabemos algo, se diga **y se dé un plazo**. En otras dos respuestas ya está el `[cuándo]` · `[cuándo]` en las cuatro, con una regla en la skill para saber de dónde sale (por ejemplo, el que fije Federico al recibir el aviso).
- **R05** [importante · C] Guion, A 5.4 · Si el cliente manda una contraseña, «no la anoto en ningún sitio», pero el chat se exporta entero a `privado/whatsapp/` (primer contacto): la contraseña queda guardada en el fichero, y además en el móvil de Iván (§10.3, §12) · Pedir a Iván que borre ese mensaje del chat antes de exportarlo, o que la borre de la exportación, y anotarlo. Lo mismo para cualquier dato bancario.
- **R06** [importante · A] Primer contacto, «¿Cuánto tardáis?» · «Depende sobre todo de lo rápido que tengamos **vuestros textos** y fotos». Los textos los redactamos nosotros (§6.1, §7: «sin que tengas que hacer nada»), así que el cliente entendería que le toca escribirlos · «…de lo rápido que tengamos vuestras respuestas y las fotos».

## Menores

- **R07** [menor · D] Guion, A 4.6, y tabla de versiones · «Es **la única** pregunta que decide entre Esencial y Negocio». El catálogo dice que A 3.3 también decide: una lista corta cabe en Esencial, y una carta larga, en Negocio · «La que más decide».
- **R08** [menor · D] Primer envío, «Las preguntas de la tanda A» · «Para Cotillas serían unas 12 preguntas más la foto». Con la regla del propio guion salen 9: 8 obligatorias más A 2.2, porque son dos hermanos. Las demás condicionales no se saben de antemano · Poner la cuenta con la regla, o quitar el ejemplo.
- **R09** [menor · D] Primer envío, «Cuándo» · Dice «catálogo de Reme **v0.3**»; el guion es de la v0.3.1 · «La versión del catálogo del guion», para que no se quede vieja.
- **R10** [menor · B] Primer envío, calendario · Si el cliente contesta a medias, hay un único recordatorio, pero no dice qué pasa después. A-012 fija dos recordatorios y pausa · Escribir qué pasa (¿pausa?) y, como se aparta de A-012, que lo confirme Iván al aprobar.
- **R11** [menor · E] Guion, A 5.3 · «¿…o **seguimos** con el nombre tal cual?»: no queda claro quién sigue. El catálogo dice «seguís» · «¿…o seguís con el nombre tal cual, como en el rótulo?».

## Lo que está especialmente bien

- **Ninguna promesa de llamada**, y una respuesta amable a «¿me llamáis?» que no cierra la puerta a hablar con Iván (§9.3).
- **Ningún dato personal en git:** la tabla de qué va en `privado/` y qué no es la mejor que tenemos.
- **Las preguntas de Reme tal cual**, con un script que impide usar el guion si el catálogo cambia.
- **El seguimiento:** sin presión, sin «he visto que lo habéis leído» y sin cambiar de canal para insistir.

## Decisiones que necesita Iván (las lleva Federico)

1. **R01:** usar una línea de privacidad provisional hasta tener el texto del profesional (A-010), o esperar a ese texto.
2. **R02:** aprobar el plazo de 5 días laborables para el primer envío.
3. **R10:** si el cliente contesta a medias, ¿basta un recordatorio y después pausa?
