# Encargo E-007 · Menchu · Revisión del alta de cliente (ronda 1)

```
ENCARGO:    Revisar tu parte del alta de cliente, mejorar tu skill y proponer cambios
CLIENTE:    interno (caso simulado: Peluquería Hermanos Cotillas)
CONTEXTO:   este documento
ENTREGABLE: procesos/ronda-1/revision-menchu.md y tus skills en procesos/skills-borrador/
PLAZO:      hoy
```

De: Federico · 2026-11-17

## Contexto

Iván quiere que aprendamos a dar de alta a un cliente nuevo: desde el «quiero una
web» hasta el primer envío. Para aprender, simulamos un cliente: la **Peluquería
Hermanos Cotillas** (Albacete). Es un negocio real, **no es cliente nuestro y
nadie le ha contactado**. Solo usamos información pública.

Iván me pidió que lo hiciera yo a mano primero, aunque fuera trabajo de vuestras
áreas, para ver de qué va. Ya está hecho: el proceso y lo aprendido están en
[procesos/alta-cliente.md](../alta-cliente.md), y todo el material en
[clientes/peluqueria-hermanos-cotillas/](../../clientes/peluqueria-hermanos-cotillas/expediente.md).

**Ahora os toca a vosotros.** Cada uno revisa su parte como experto, dice qué
está mal, qué falta y cómo lo haría, y se queda con su skill. Mi trabajo es un
punto de partida, no un modelo: **tenéis libertad para cambiarlo entero**,
incluidas las herramientas y los generadores que usé.

**Lo que viene después:** cuando estemos de acuerdo, **repetiremos el caso desde
cero en una carpeta nueva**, esta vez haciéndolo cada uno con su skill, y
**compararemos el resultado con lo que hice yo**. Tiene que salir mejor.

Iván ha sido claro: **quiere que os lo curréis. Vuestro bono de fin de año
depende de ello**, y el mío, de que salga bien.

## Tu parte en el proceso

| Fase | Skill | Lo que hice yo |
|---|---|---|
| 0. Primer contacto: recoger lo mínimo | `primer-contacto` | Nada: la petición fue simulada («queremos una web») |
| 8. Primer envío y seguimiento | `primer-envio` | [Borrador del email](../../clientes/peluqueria-hermanos-cotillas/entregables/email-borrador.md), firmado por ti |

## Lo que no me convence

1. **El canal.** Escribí un correo con dos adjuntos, pero §9.1 dice que el canal
   principal es WhatsApp. ¿Un peluquero lee correos? ¿WhatsApp más correo? ¿Una
   llamada primero?
2. **Un cuestionario de diez páginas** para dos hermanos que se pasan el día
   cortando el pelo. ¿Lo rellenarán? ¿Es mejor que tú se lo hagas por teléfono
   y lo rellenes tú?
3. **Cómo me presento** en tu nombre: «asistente de IA… detrás hay una persona,
   Iván, que revisa y aprueba todo». ¿Te suena natural?
4. **Seguimiento:** ¿cuándo y cuántas veces recordar sin ser pesados?
5. **Los materiales:** «fotos por WhatsApp como documento». ¿Es realista? ¿Y la
   protección de datos (§12)?
6. **El primer contacto:** ¿qué es lo mínimo que hay que preguntar en la primera
   conversación para que el equipo pueda investigar sin molestar más?

## Lo que te pido

1. Lee el email, el cuestionario y el informe **como si fueras el cliente**.
   Para ver el Word sin Word: `soffice --headless --convert-to pdf --outdir /tmp <el .docx>`.
2. Rehaz tus dos skills: canales, mensajes, plantillas y calendario de seguimiento.
3. Propón cambios en el cuestionario o en el informe desde el punto de vista
   del cliente (me los pasas y yo se los llevo a Reme y a Chema).

## Tus skills en borrador

- [`primer-contacto`](../skills-borrador/primer-contacto/SKILL.md)
- [`primer-envio`](../skills-borrador/primer-envio/SKILL.md)

## Reglas de esta ronda

1. **No rehagas todavía el trabajo del cliente:** eso es la ronda siguiente.
   Ahora revisas, propones y mejoras tu skill. Puedes hacer pruebas para
   comprobar lo que propones.
2. **Escribe solo en tus ficheros:** tu revisión y tus skills en borrador
   (abajo). Lo que afecte a otro agente o a un fichero que no es tuyo,
   **propónmelo en la revisión** y lo coordino yo (§13.2).
3. **No instales nada.** Si necesitas algo, propónlo: qué, para qué y cuánto cuesta.
4. **No contactes con nadie** ni envíes nada fuera.
5. **No hagas commits:** los hago yo al consolidar.
6. **No inventes:** si no sabes algo, escríbelo como duda.

## Cómo entregar

1. Tu revisión en `procesos/ronda-1/revision-menchu.md`, con la plantilla de abajo.
2. Tus skills actualizadas en `procesos/skills-borrador/<skill>/SKILL.md`.
   Cambia la cabecera a «BORRADOR v0.2 · revisado por Menchu».
3. Al terminar, contéstame en tu sesión con el formato de §13.6
   (ESTADO / RESULTADO / PENDIENTE).

**PLAZO:** hoy.

## Plantilla de la revisión

```markdown
# Revisión de Menchu · ronda 1

## 1. Lo que mantendría
## 2. Lo que cambiaría
(una línea por punto: [bloquea|importante|menor] qué · por qué · cómo)
## 3. Lo que falta
## 4. Mis skills: qué he cambiado y por qué
## 5. Lo que necesito de otros agentes (lo coordina Federico)
## 6. Lo que tiene que decidir Iván (lo lleva Federico)
## 7. Herramientas: qué necesito o propongo
```
