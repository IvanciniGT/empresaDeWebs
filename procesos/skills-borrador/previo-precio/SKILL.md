---
name: previo-precio
description: "Hace la estimación interna de precio de un cliente nuevo antes de la tanda A: plan que le encaja, qué respuesta de la tanda A lo cambiaría, escenarios con IVA, extras y prioridad puntuada. Cuando llegan las respuestas, lo convierte en borrador de presupuesto. Nunca se envía al cliente ni va a git."
---

# previo-precio

> **BORRADOR v0.3.1 · revisado por Reme · 2026-11-18** · Dueña: Reme · En revisión (ronda 1b)

## Cuándo

| Momento | Para qué |
|---|---|
| Expediente con lo público, **antes de la tanda A** | Decir qué plan encaja y **qué preguntas de la tanda A lo deciden** para este cliente |
| Llegan las respuestas de la tanda A | Convertirlo en **borrador de presupuesto** para que Iván lo apruebe |

## Entrada

- Expediente del cliente y `privado/contacto.md` (lo que pidió, literal).
- AGENTS.md §5 (a quién atendemos), §6 (servicios) y §8 (precios y fiscalidad).
- Las decisiones de Iván sobre precios ([aprobaciones](../../../operacion/aprobaciones.md)).
- El [catálogo de preguntas](../cuestionario-cliente/preguntas.md), tanda A.
- Las respuestas de la tanda A, en el segundo momento.

## Pasos

1. **Filtro de §5.** Si el cliente no encaja, se para aquí y se pasa a
   Federico. No se puntúa.
2. **Necesidad probable**, en 3–5 líneas, cada una con su base (expediente o
   primer contacto). Sin base no es una necesidad: es una pregunta.
3. **Plan más sencillo** que la resuelve (§6, §8.2), en una línea.
4. **Qué lo cambiaría**, con el ID de la pregunta de la tanda A que lo averigua:

   | Si responde… | Pregunta | Cambia a… |
   |---|---|---|
   | Quiere que elijan día y hora solos | A 4.1 *cita* → A 4.6 | **Negocio** |
   | Lista de servicios o carta larga | A 3.3 | **Negocio** |
   | Vender por internet | A 4.1 *vender* → A 3.4 | **Fuera de catálogo**: a Federico |
   | Otro idioma | A 4.1 *idioma* → A 4.3 | Traducción **aparte** |
   | Integrar su aplicación de citas | A 3.5 *aplicación* → A 3.7 | **Aparte** (un botón que lleve a ella está incluido) |
   | Cambios 2–4 veces al mes, o más | A 4.4 | Mantenimiento **Plus** (más horas, si son más) |
   | Sin fotos y prefiere fotógrafo | A 5.5 → A 5.2 | Fotografía **aparte** |
   | Quiere logotipo nuevo | A 5.5 → A 5.3 | Logotipo **aparte** |
   | Tiene web con proveedor o contrato | A 5.7 | Más plazo |
   | Tiene web y quiere conservar algo | A 5.8 | Más trabajo |
   | La ficha de Google no la controla | A 5.4 | Más plazo |
   | Quiere recibir currículums | A 4.1 *personal* → A 4.7 | Más trabajo legal |

   Si este cliente necesita saber algo que no está en el catálogo, se pide
   **como condicional** en su tanda A (`cuestionario-cliente`, paso 4).

5. **Escenarios del primer año:** el recomendado y variaciones que cambian
   **una sola cosa** cada una (plan, mantenimiento o SEO), con base, IVA
   previsible y total, y los precios unitarios.
6. **Extras:** con importe solo si está en la tarifa. Si no hay tarifa: «sin
   tarifa: presupuesto aparte, lo decide Iván», **sin importe**.
7. **Prioridad**, con los criterios de abajo.
8. **Riesgos:** qué puede alargar o encarecer el proyecto y qué pregunta de
   la tanda A lo aclara.

## El dominio (A-011)

**Va dentro de la cuota de mantenimiento**, siempre a nombre del cliente. No
es un extra ni una línea aparte del presupuesto. El coste real depende del
registrador, que aún no está elegido; elegirlo es un gasto y lo decide Iván
(§10.2). Hasta entonces, **ningún importe** del dominio en el previo.

Si el cliente **ya tiene dominio** (A 5.5), se traslada a nuestra gestión sin
dejar de ser suyo. Si **no quiere mantenimiento**, A-011 no dice qué pasa con
el dominio: es una duda que sigue abierta (abajo).

## Prioridad

Cinco criterios de 0 a 2. **Lo que no se sabe vale 1**, nunca 0 ni 2.

| Criterio | De dónde sale | 2 | 1 | 0 |
|---|---|---|---|---|
| **Encaje en plan** | A 4.1, A 4.6, A 3.3 | Cabe en Esencial o Negocio sin extras obligatorios | Necesita algún extra | A medida o fuera de catálogo |
| **Material** | A 5.5, A 5.2 | Tiene fotos y datos utilizables | Tiene parte, o no se sabe | Sabemos que no tiene nada |
| **Ingreso** (base del 1.er año, escenario recomendado) | Escenarios | ≥ 1.500 € | 800–1.499 € | < 800 € |
| **Urgencia del cliente** | A 4.5 | Fecha concreta y próxima | Razonable, o no se sabe | «Sin prisa» |
| **Dependencias** | A 5.4, A 5.7 | Las controla el cliente | Alguna sin aclarar, o no se sabe | Las tiene un tercero que no responde |

**Total sobre 10:** alta ≥ 8 · media 5–7 · baja ≤ 4. Los cortes son
**[PROPUESTA]** y los importes del criterio «Ingreso» dependen de las tarifas
de §8.2, que también lo son. Se ajustan con los primeros clientes reales.

**Antes de la tanda A casi todo vale 1:** la prioridad previa solo sirve para
descartar y detectar los casos a medida. **La que cuenta es la que se
recalcula con las respuestas.** Probado con Cotillas: 6 de 10, media (revisión
de Reme, §4).

El «valor como caso de éxito» no puntúa: es una suposición, y enseñar su web
necesita su permiso.

## Del previo al borrador de presupuesto

1. Repasar cada fila de «qué lo cambiaría» con su respuesta y fijar el plan.
2. Las líneas del presupuesto salen de los requisitos (`requisitos.md`) y de
   «lo que NO entra», que también se escribe.
3. Recalcular la prioridad.
4. Pasarlo a Federico para Iván (§10.2). **Mientras las tarifas sean
   [PROPUESTA] o la fiscalidad no esté confirmada (§8.3), el presupuesto no
   sale**, y así lo dice su cabecera. Hoy es el caso (A-011, resto).

## Reglas

1. **Interno siempre.** No se envía ni se menciona al cliente.
2. **Fuera de git.** El repositorio es público (A-013): una valoración interna
   de un negocio con nombre («prioridad media», «riesgo de que tarden») no
   puede leerla cualquiera, empezando por el propio cliente. Va a `privado/`.
3. **Cabecera de aviso** mientras las tarifas sean [PROPUESTA] o la
   fiscalidad esté pendiente (§8.3).
4. **Cuentas con calculadora, y reproducibles**, por ejemplo:
   `python3 -c "c,m=490,29; b=c+12*m; print(b, round(b*.21,2), round(b*1.21,2))"`.
5. **Sin cifras ni suposiciones sin base:** nada de «paga en efectivo» ni
   «unos 10–15 €» si no está en el expediente o en una fuente con fecha.
6. **Recomendar siempre lo más sencillo** que resuelve el problema, aunque
   ingresemos menos (§4.1).
7. **Descuentos y excepciones:** ni se proponen. Si se ven necesarios, a
   Federico (§8.1).

## Salida

`clientes/<negocio>/privado/previo-precio.md` (y después
`privado/presupuesto-vX.md`):

```markdown
# Previo de precio · <Negocio>
> 🔒 INTERNO. Fuera de git. (+ aviso de [PROPUESTA] y fiscalidad si sigue pendiente)

## Necesidad probable        (cada línea con su base)
## Plan recomendado          (una línea de por qué)
## Qué lo cambiaría          | Si responde… | Pregunta | Cambia a… |   (solo las que aplican)
## Escenarios del 1.er año   | Escenario | Qué cambia | Base | IVA | Total |  + precios unitarios
## Extras                    | Extra | ¿Tarifa? | Qué haríamos |   (sin el dominio: va en la cuota)
## Prioridad                 | Criterio | Puntos | Por qué |  → total y nivel
## Riesgos                   | Riesgo | Qué lo aclara |
```

## Pendiente de Iván (A-011, resto)

- Qué se contesta a «¿cuánto cuesta?» en el primer contacto.
- **¿Se puede contratar la creación sin mantenimiento?** Si se puede, falta
  el escenario «solo creación» y saber quién paga y renueva el dominio.
- **Suscripción sin pago inicial:** cuándo se ofrece y qué pasa en el mes 13.
- **¿El vídeo entra en los planes?**
