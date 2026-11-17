---
name: cuestionario-cliente
description: "Decide qué se le pregunta a un cliente nuevo y cuándo (B1 antes del presupuesto, B2 al contratar), monta el cuestionario desde el catálogo de preguntas y convierte las respuestas en requisitos del expediente. Úsala cuando el expediente tiene la información pública recopilada y otra vez cuando llegan las respuestas."
---

# cuestionario-cliente

> **BORRADOR v0.2 · revisado por Reme** · Dueña: Reme · Textos de ayuda: Chema ·
> Maquetación: Lola · Generador: Paco · En revisión (ronda 1)

## La regla que lo decide todo

Cada pregunta tiene un **para qué**: un destino concreto en el presupuesto, en
los requisitos, en los textos, en el diseño o en el contacto. **Si no lo tiene,
se quita.**

- **B1 · Conoceros** (antes del presupuesto): solo lo que puede cambiar el
  **plan, el precio o el plazo**, lo necesario para hablar con el cliente, los
  datos públicos que tiene que validar y los mínimos de Iván en versión corta.
- **B2 · Al contratar** (tras aceptar el presupuesto): todo lo demás, más los
  bloques según el tipo de web.

Las preguntas, con su ID, su para qué y su destino, están en
[preguntas.md](preguntas.md). El formato de requisitos, en
[plantilla-requisitos.md](plantilla-requisitos.md).

## Cuándo

| Momento | Qué se hace |
|---|---|
| Expediente con lo público **y previo de precio hecho** | Montar B1 |
| Llegan las respuestas de B1 | Pasarlas a requisitos y a presupuesto |
| El cliente acepta el presupuesto | Montar B2 |
| Llegan las respuestas de B2 | Completar los requisitos |

El previo va **antes** que B1 porque dice qué preguntas deciden el plan de este
cliente.

## Montar B1

1. **Partir del catálogo:** núcleo común + bloque de sector. Si el sector no
   tiene bloque, el genérico. No se inventan opciones.
2. **«Lo que ya sabemos»:** solo filas que estén en el expediente. Los datos
   «a confirmar» se presentan como «lo que hemos visto» y se preguntan. Las
   ausencias, como «no hemos encontrado».
3. **Quitar lo que ya está respondido** con fuente primaria en el expediente.
4. **Añadir las preguntas que marque el previo** como decisivas, si faltan.
5. **Pedir a Federico:** a Chema, los textos de ayuda; a Lola, la maquetación;
   a Paco, el generador con los ID del catálogo.
6. **Comprobar antes de pasarlo a Puri:**
   - 4 páginas como máximo (`soffice --headless --convert-to pdf` y `pdfinfo`);
   - cada pregunta tiene su ID del catálogo;
   - la versión del cuestionario («B1 v0.2») va en el pie;
   - lleva la cláusula de protección de datos;
   - nada marcado [PROPUESTA] ni afirmaciones sin fuente.

## Pasar las respuestas a requisitos

1. **El original no se toca:** Menchu lo guarda en `clientes/<negocio>/recibido/`.
   Si se respondió por teléfono, Menchu anota las respuestas con su ID.
2. **Sacar las respuestas por ID.** Con el lector automático cuando Paco lo
   tenga. Mientras tanto, a mano.
3. **Repartirlas por destino:**

   | Destino | Qué se hace |
   |---|---|
   | `DATO` | Al expediente §1, con fuente «cliente, B1 vX, fecha». Sale de «a confirmar». |
   | `PRECIO` | Al borrador de presupuesto (skill `previo-precio`). |
   | `REQ` | Requisito `R-xx` con origen y criterio de aceptación. |
   | `CONT`, `DIS` | Fila en «Contenido y materiales», y aviso a Federico para Chema o Lola. |
   | `CONTACTO` | Al expediente. |
   | `LEGAL` | Al expediente; nunca a mensajes ni a código. |

4. **Lo que falta o es ambiguo** va a «Falta saber» y se pide a Federico. **No
   se supone la respuesta.** Una ★ sin respuesta bloquea el presupuesto.
5. **Versiones:** v0.x mientras se negocia; **v1.0 cuando el cliente aprueba
   el presupuesto**. Desde ahí, solo cambia mediante el control de cambios (`C-xx`).
6. **Anotar en el historial del expediente y avisar a Federico** (§13.2.6:
   escribir en el expediente no es avisar).

## Reglas

1. **Pocas preguntas, las justas.** B1: 4 páginas como máximo y unos 15
   minutos. Si una pregunta nueva entra, otra sale o pasa a B2.
2. **Se entiende sin nosotros delante:** sin jerga y con un ejemplo en cada
   pregunta abierta.
3. **No se pide lo que aún no hace falta.** Los datos legales y el NIF se piden
   al contratar, no antes (§12: solo los datos que hacen falta).
4. **Cada pregunta, una sola cosa.** Nada de «rodeadla», columnas con dos
   lecturas ni la misma pregunta en dos bloques.
5. **Nada que el cliente no pueda corregir** en «lo que ya sabemos».
6. **Ningún dato ni afirmación sin fuente,** tampoco en las introducciones
   («los negocios que publican precios reciben más llamadas» necesita fuente o
   se quita).
7. **Nunca pedir contraseñas** (§12), y decirlo en el documento.
8. **Sin precios ni plazos** marcados [PROPUESTA].
9. **Siempre la alternativa por teléfono,** con las mismas preguntas y los mismos ID.
10. **Aprobar textos no se hace en el cuestionario,** sino en la fase de textos
    (§13.5, paso 4), con sus 2 rondas.

## Herramientas

- `herramientas/docx_util.py` (de Paco): casillas, huecos y tablas. Las
  casillas son controles de contenido de Word (`w14:checkbox`) y se pueden
  leer automáticamente: probado el 2026-11-17 con una copia en la que se
  simularon 3 casillas marcadas; se leyeron las 3 y ninguna más.
- Pendiente (pedido a Paco): ID en cada control y un lector de respuestas.

## Salida

- `clientes/<negocio>/entregables/Cuestionario B1 - <negocio>.docx` (y luego B2).
- `clientes/<negocio>/requisitos.md`, desde [plantilla-requisitos.md](plantilla-requisitos.md).

## Dudas abiertas

- **Formato:** Word, formulario propio o teléfono guiado. Lo decide Iván
  (revisión, §6).
- **Cláusula de protección de datos** del cuestionario: necesita el nombre de
  la empresa y un texto revisado por un profesional (§15).
- **Opiniones de Google:** ¿basta el permiso del negocio para mostrarlas, o
  hace falta algo más? Es una duda legal.
