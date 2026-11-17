# Plantilla · requisitos de un cliente

> **BORRADOR v0.2 · revisado por Reme.** Se copia a
> `clientes/<negocio>/requisitos.md` cuando llegan las respuestas de B1.
> Lo mantiene Reme. Lo leen Lola, Paco, Chema y Puri. El expediente lo enlaza.

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

---

```markdown
# Requisitos · <Negocio>

| | |
|---|---|
| **Versión** | v0.1 |
| **Estado** | borrador · enviado con el presupuesto · **aprobado por el cliente** (fecha) |
| **Servicio y plan** | p. ej. Creación Esencial + Mantenimiento Básico |
| **Presupuesto** | enlace |
| **Visto bueno del cliente** | quién (B1 2.2) |
| **Entradas** | Cuestionario B1 vX (fecha, `recibido/…`) · expediente |

## 1. Para qué es la web

Una frase, con las palabras del cliente (B1 4.2).

## 2. Lo que entra

| ID | Requisito | Prioridad | Origen | Se comprueba así | Estado |
|---|---|---|---|---|---|
| R-01 | La web muestra el horario completo de cada día. | Imprescindible | §6.1 · B1 1.4 | En móvil, el horario se ve desde la página principal sin abrir menús, y coincide con el validado en B1 1.4. | pendiente |
| R-02 | Desde el móvil se puede llamar con un toque. | Imprescindible | §6.1 · B1 1.3 | En móvil, el botón de llamada está visible en todas las páginas y abre la marcación al número validado. | pendiente |
| R-… | | | | | |

**Prioridad:** *imprescindible* (sin esto no se publica) o *deseable* (si hay
que recortar, se recorta esto, y se dice).
**Estado:** pendiente · hecho · comprobado por Puri.

Los requisitos de §6.1 que trae cualquier creación (contacto, horario, mapa,
llamada y WhatsApp, formulario, textos legales, SEO base, ficha de Google) se
cargan siempre, con origen «§6.1».

## 3. Lo que NO entra

Lo que el cliente ha mencionado o podría suponer y no está incluido. Cada
línea, con su salida: «presupuesto aparte», «otro proyecto», «no lo hacemos».

- p. ej. Reserva online con agenda: no entra en Esencial. Se ofrece Negocio si la quiere.

## 4. Contenido y materiales

| Qué | Quién lo aporta | Para quién | Origen | Estado |
|---|---|---|---|---|
| Fotos de fachada, interior y equipo | Cliente | Lola | B2 6.7 | pendiente |
| Historia del negocio | Cliente (por teléfono) | Chema | B2 6.3 | pendiente |

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
| v0.1 | | Primera versión con las respuestas de B1 |
```
