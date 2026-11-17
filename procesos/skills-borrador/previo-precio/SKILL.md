---
name: previo-precio
description: "Hace una estimación interna de precio para un cliente nuevo antes de tener sus respuestas: qué plan le encaja, escenarios con IVA, extras fuera de plan y prioridad del cliente. Nunca se envía al cliente. Úsala cuando el expediente tiene la información pública recopilada."
---

# previo-precio

> **BORRADOR v0.1** · Escrito por Federico · **Dueña: Reme** · En revisión (ronda 1)

## Cuándo

Al tener el expediente con lo recopilado. Sirve para **priorizar** al cliente y
para tener preparado el presupuesto. El presupuesto de verdad sale con sus
respuestas.

## Entrada

- Expediente del cliente.
- AGENTS.md §6 (servicios) y §8 (precios y fiscalidad).

## Pasos

1. **Elegir el plan más sencillo** que resuelva lo que probablemente necesita
   (§6 y §8.2) y explicar por qué en una línea.
2. **Decir qué le haría cambiar de plan** (por ejemplo, reservas con agenda → Negocio).
3. **Escenarios del primer año:** creación más 12 meses de mantenimiento, con
   y sin SEO continuo, con base imponible, IVA previsible y total.
4. **Extras fuera de plan:** dominio, logotipo, fotografía, reservas…, con
   qué haríamos en cada caso.
5. **Prioridad del cliente** según encaje con §5, valor como caso de éxito,
   dificultad, riesgo e ingreso.

## Reglas

1. **Interno siempre.** No se envía ni se menciona al cliente.
2. Mientras las tarifas sean **[PROPUESTA]** y la fiscalidad no esté
   confirmada (§8.3), se avisa en la cabecera del documento.
3. **Las cuentas, con calculadora,** nunca de cabeza.
4. **Sin cifras inventadas** (ni porcentajes ni estimaciones sin base).
5. **Descuentos y excepciones:** ni se proponen. Si se ven necesarios, a Federico (§8.1).

## Salida

- `interno/previo-precio.md`

## Dudas abiertas (para la revisión)

- ¿Criterios de prioridad con puntuación o a ojo?
- Dominio: ¿incluido en el mantenimiento o aparte?
- ¿Cuándo proponer la suscripción sin pago inicial?
