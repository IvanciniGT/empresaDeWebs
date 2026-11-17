---
name: previo-precio
description: "Hace la estimación interna de precio de un cliente nuevo: plan que le encaja, qué respuesta lo cambiaría, escenarios con IVA, extras y prioridad con criterios puntuados. Se hace antes del cuestionario B1 y se convierte en borrador de presupuesto cuando llegan las respuestas. Nunca se envía al cliente."
---

# previo-precio

> **BORRADOR v0.2 · revisado por Reme** · Dueña: Reme · En revisión (ronda 1)

## Cuándo

| Momento | Para qué |
|---|---|
| Expediente con lo público, **antes de montar B1** | Decir qué plan encaja y **qué preguntas de B1 lo deciden** |
| Llegan las respuestas de B1 | Pasarlo a **borrador de presupuesto** para que Iván lo apruebe |

## Entrada

- Expediente del cliente.
- AGENTS.md §5 (a quién atendemos), §6 (servicios) y §8 (precios y fiscalidad).
- Las respuestas de B1, en el segundo momento.

## Pasos

1. **Filtro de §5.** Si el cliente no encaja con lo que atendemos, se para aquí
   y se pasa a Federico. No se puntúa.
2. **Necesidad probable**, en 3–5 líneas. Cada una con su base en el
   expediente. Si no hay base, no es una necesidad: es una pregunta para B1.
3. **Plan más sencillo** que la resuelve (§6, §8.2), en una línea.
4. **Qué lo cambiaría:** cada respuesta que movería el plan o el precio, con el
   **ID de la pregunta de B1** que lo averigua
   (catálogo de [cuestionario-cliente](../cuestionario-cliente/preguntas.md)).
   Si falta una pregunta, se añade a B1.
5. **Escenarios del primer año:** el recomendado y variaciones que cambian
   **una sola cosa** cada una (plan, mantenimiento o SEO). Para cada uno:
   base, IVA previsible y total. Se dan también los precios unitarios.
6. **Extras:** solo con precio si está en la tarifa. Si no hay tarifa, se
   escribe «sin tarifa: presupuesto aparte, lo decide Iván», **sin importe**.
   Los costes de terceros (dominio, etc.) solo llevan importe si hay fuente y fecha.
7. **Prioridad**, con los criterios de abajo.
8. **Riesgos:** qué puede alargar o encarecer el proyecto y qué pregunta o
   acción lo reduce.

## Prioridad

Cinco criterios de 0 a 2. **Lo que no se sabe vale 1**, nunca 0 ni 2.

| Criterio | 2 | 1 | 0 |
|---|---|---|---|
| **Encaje en plan** | Cabe en Esencial o Negocio sin extras obligatorios | Necesita algún extra | A medida o probablemente fuera de catálogo |
| **Material** | Tiene fotos y datos utilizables | Tiene parte, o no se sabe | Sabemos que no tiene nada |
| **Ingreso** (base del 1.er año, escenario recomendado) | ≥ 1.500 € | 800–1.499 € | < 800 € |
| **Urgencia del cliente** | Fecha concreta y próxima | Razonable, o no se sabe | «Sin prisa» |
| **Dependencias** (ficha de Google, dominio, web actual) | Las controla el cliente | Alguna sin aclarar, o no se sabe | Las tiene un tercero que no responde |

**Total sobre 10:** alta ≥ 8 · media 5–7 · baja ≤ 4. Los cortes son
**[PROPUESTA]**: se ajustan con los primeros clientes reales.

**Antes de B1 casi todo vale 1**, así que la prioridad previa solo sirve para
descartar y para detectar los casos a medida. **La prioridad que cuenta es la
que se recalcula con las respuestas.**

El «valor como caso de éxito» no puntúa: es una suposición y, además, mostrar
su web como ejemplo necesita el permiso del cliente. Si se ve claro, se añade
como nota.

## Del previo al borrador de presupuesto

Cuando llegan las respuestas de B1:

1. Se repasa cada «qué lo cambiaría» con su respuesta, y se fija el plan.
2. Se sacan las líneas del presupuesto de los requisitos (`requisitos.md`) y
   de lo que **no** entra, que también se escribe.
3. Se recalcula la prioridad.
4. Se pasa a Federico para que lo lleve a Iván (§10.2). Mientras las tarifas
   sean [PROPUESTA] o la fiscalidad no esté confirmada (§8.3), **el
   presupuesto no puede salir**, y así se dice en su cabecera.

## Reglas

1. **Interno siempre.** No se envía ni se menciona al cliente.
2. **Cabecera de aviso** mientras las tarifas sean [PROPUESTA] o la fiscalidad
   esté pendiente (§8.3).
3. **Cuentas con calculadora, y reproducibles**, por ejemplo:
   `python3 -c "c,m=490,29; b=c+12*m; print(b, round(b*.21,2), round(b*1.21,2))"`.
4. **Sin cifras ni suposiciones sin base.** Nada de «paga en efectivo» o «unos
   10–15 €» si no está en el expediente o en una fuente con fecha.
5. **Recomendar siempre lo más sencillo que resuelve el problema,** aunque
   ingresemos menos (§4.1).
6. **Descuentos y excepciones:** ni se proponen. Si se ven necesarios, a Federico (§8.1).

## Salida

`clientes/<negocio>/interno/previo-precio.md`:

```markdown
# Previo de precio · <Negocio>
> 🔒 INTERNO. (+ aviso de [PROPUESTA] y fiscalidad si sigue pendiente)

## Necesidad probable        (cada línea con su base en el expediente)
## Plan recomendado          (una línea de por qué)
## Qué lo cambiaría          | Si responde… | Cambia a… | Pregunta B1 |
## Escenarios del 1.er año   | Escenario | Qué cambia | Base | IVA | Total |  + precios unitarios
## Extras                    | Extra | ¿Tarifa? | Qué haríamos |
## Prioridad                 | Criterio | Puntos | Por qué |  → total y nivel
## Riesgos                   | Riesgo | Qué lo reduce |
```

## Pendiente de Iván

- **Dominio:** §6.2 ya incluye su renovación en el mantenimiento. ¿El coste va
  dentro de la cuota o se cobra aparte, a precio de coste?
- **¿Se puede contratar la creación sin mantenimiento?** Si se puede, falta el
  escenario «solo creación» y quién aloja la web.
- **Suscripción sin pago inicial (§8.2):** cuándo se ofrece y qué pasa al
  acabar los 12 meses.
