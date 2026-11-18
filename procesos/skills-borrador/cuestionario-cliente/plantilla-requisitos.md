# Plantilla · requisitos de un cliente

> **BORRADOR v0.3 · revisado por Reme · 2026-11-18.** Se copia a
> `clientes/<negocio>/requisitos.md` cuando llegan las respuestas de la tanda A.
> Lo mantiene Reme. Lo leen Lola, Paco, Chema y Puri. El expediente lo enlaza.
>
> **Este fichero va a git, y el repositorio es público (A-013).** Ni nombres de
> personas, ni teléfonos, ni correos, ni respuestas literales que los lleven:
> se cita el ID de la pregunta, y el dato se queda en `privado/` (A-009).

**Por qué un fichero aparte del expediente:** el expediente es el **registro**
(qué ha pasado). Los requisitos son el **acuerdo** (qué vamos a entregar).
Puri revisa contra el acuerdo, y el acuerdo cambia solo por el control de
cambios, no porque alguien añada una línea al historial.

**Reglas de redacción:**

1. Un requisito tiene **una sola interpretación** y Puri puede comprobarlo sin
   preguntar a nadie.
2. Todo requisito tiene **origen**: una pregunta del cuestionario (con su ID),
   un punto de AGENTS.md o un cambio aprobado. Sin origen no hay requisito.
3. Los estándares de §11 se aplican **siempre** y no se copian aquí.
4. Dice **qué** hace falta, nunca **cómo** queda (eso es de Lola y Paco).
5. **Sin datos personales** (ver arriba). Tampoco precios: el presupuesto está en `privado/`.

---

```markdown
# Requisitos · <Negocio>

| | |
|---|---|
| **Versión** | v0.1 |
| **Estado** | borrador · enviado con el presupuesto · **aprobado por el cliente** (fecha) |
| **Servicio y plan** | p. ej. Creación Esencial + Mantenimiento Básico |
| **Presupuesto** | `privado/presupuesto-vX.md` (fuera de git) |
| **Visto bueno del cliente** | la persona de contacto, o quien diga A 2.2 (en `privado/contacto.md`) |
| **Entradas** | Tanda A, catálogo vX (fecha; respuestas en `privado/respuestas-tanda-a.md`) · expediente |

## 1. Para qué es la web

Una frase, sacada de lo que el cliente quiere conseguir (primer contacto) y de A 4.1. Sin citar datos personales.

## 2. Lo que entra

| ID | Requisito | Prioridad | Origen | Se comprueba así | Estado |
|---|---|---|---|---|---|
| R-01 | La web muestra el horario completo de cada día. | Imprescindible | §6.1 · A 1.4 | En móvil, el horario se ve desde la página principal sin abrir menús, y coincide con el confirmado en A 1.4. | pendiente |
| R-02 | Desde el móvil se puede llamar con un toque. | Imprescindible | §6.1 · A 1.3 | En móvil, el botón de llamada está visible en todas las páginas y abre la marcación al número confirmado en A 1.3. | pendiente |
| R-… | | | | | |

**Prioridad:** *imprescindible* (sin esto no se publica) o *deseable* (si hay
que recortar, se recorta esto, y se dice).
**Estado:** pendiente · hecho · comprobado por Puri.

**«Se comprueba así»:** pendiente de lo que diga Puri (ronda 1b). Hasta
entonces, cada criterio dice **dónde** se mira (móvil u ordenador, qué página)
y **qué** tiene que verse, sin palabras como «bien», «claro» o «rápido».

Los requisitos de §6.1 que trae cualquier creación (contacto, horario, mapa,
llamada y WhatsApp, formulario, textos legales, SEO base, ficha de Google) se
cargan siempre, con origen «§6.1».

## 3. Lo que NO entra

Lo que el cliente ha mencionado o podría suponer y no está incluido. Cada
línea, con su salida: «presupuesto aparte», «otro proyecto», «no lo hacemos».

- p. ej. Reserva online con agenda: no entra en Esencial. Se ofrece Negocio si la quiere (A 4.6).

## 4. Contenido y materiales

| Qué | Quién lo aporta | Para quién | Origen | Estado |
|---|---|---|---|---|
| Fotos de fachada, interior y equipo | Cliente (archivos en `privado/`) | Lola | B 6.7 | pendiente |
| Historia del negocio | Cliente (audios de WhatsApp) | Chema | B 6.3 | pendiente |

## 5. Falta saber

Preguntas sin respuesta o con respuesta ambigua. Van a Federico → Menchu.
Mientras estén abiertas, **no se supone la respuesta**.

| ID | Qué falta | Por qué importa | Pedido (fecha) | Respuesta |
|---|---|---|---|---|
| F-01 | | | | |

## 6. Cambios

Todo cambio después de la versión aprobada. Reme decide si entra en las 2
rondas (§6.1) o es un extra. Si es un extra, el presupuesto lo aprueba Iván (§10.2).

| ID | Fecha | Pedido por | Qué | ¿Ronda o extra? | Efecto en plazo y precio | Aprobado por | Requisitos afectados |
|---|---|---|---|---|---|---|---|
| C-01 | | | | | | | |

## 7. Versiones

| Versión | Fecha | Qué cambia |
|---|---|---|
| v0.1 | | Primera versión con las respuestas de la tanda A |
```
