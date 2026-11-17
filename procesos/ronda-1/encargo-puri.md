# Encargo E-006 · Puri · Revisión del alta de cliente (ronda 1)

```
ENCARGO:    Revisar tu parte del alta de cliente, mejorar tu skill y proponer cambios
CLIENTE:    interno (caso simulado: Peluquería Hermanos Cotillas)
CONTEXTO:   este documento
ENTREGABLE: procesos/ronda-1/revision-puri.md y tus skills en procesos/skills-borrador/
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
| 6. Revisar antes de enviar | `revisar-entregable` | **Nada.** Me revisé a mí mismo, que es justo lo que no debe pasar. |

Al releer mis documentos encontré y quité **seis frases inventadas**: «el 80 %»,
«han abierto muchas barberías nuevas», «zona con mucho paso», «unos 20
minutos», «la que más opiniones tiene» y «revisado por una persona». No puse
ninguna a propósito. **Seguramente quedan más.**

## Lo que te pido

1. **Revisa de verdad lo que se enviaría al cliente,** como si fuera a salir mañana:
   - [Informe de mercado y SEO local (PDF)](../../clientes/peluqueria-hermanos-cotillas/entregables/)
   - [Cuestionario (Word)](../../clientes/peluqueria-hermanos-cotillas/entregables/). Para verlo sin Word:
     `soffice --headless --convert-to pdf --outdir /tmp <el .docx>`.
   - [Borrador del email](../../clientes/peluqueria-hermanos-cotillas/entregables/email-borrador.md)

   Contra el [expediente](../../clientes/peluqueria-hermanos-cotillas/expediente.md) y AGENTS.md. **Veredicto
   APROBADO o RECHAZADO** con la lista de errores y su gravedad. Déjalo en
   `clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md`
   (puedes crear esa carpeta). Este veredicto es la vara de medir de la
   ronda siguiente.
2. Rehaz tu skill: la lista de comprobación de documentos, que no es la misma
   que la de una web (§11 habla de webs).
3. Propón cómo comprobar que el Word funciona en Microsoft Word (Iván lo tiene
   instalado; nosotros, no).
4. Si ves un error que se repetirá con cada cliente, propón cómo evitarlo en
   la skill de quien lo causa.

## Tus skills en borrador

- [`revisar-entregable`](../skills-borrador/revisar-entregable/SKILL.md)

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

1. Tu revisión en `procesos/ronda-1/revision-puri.md`, con la plantilla de abajo.
2. Tus skills actualizadas en `procesos/skills-borrador/<skill>/SKILL.md`.
   Cambia la cabecera a «BORRADOR v0.2 · revisado por Puri».
3. Al terminar, contéstame en tu sesión con el formato de §13.6
   (ESTADO / RESULTADO / PENDIENTE).

**PLAZO:** hoy.

## Plantilla de la revisión

```markdown
# Revisión de Puri · ronda 1

## 1. Lo que mantendría
## 2. Lo que cambiaría
(una línea por punto: [bloquea|importante|menor] qué · por qué · cómo)
## 3. Lo que falta
## 4. Mis skills: qué he cambiado y por qué
## 5. Lo que necesito de otros agentes (lo coordina Federico)
## 6. Lo que tiene que decidir Iván (lo lleva Federico)
## 7. Herramientas: qué necesito o propongo
```
