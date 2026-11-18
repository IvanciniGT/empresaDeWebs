---
name: cuestionario-cliente
description: "Decide qué se le pregunta a un cliente nuevo y cuándo (tanda A antes del presupuesto, tanda B al aceptarlo), desde un catálogo de preguntas con ID, y convierte las respuestas en requisitos. Úsala cuando el expediente tiene la información pública y el previo de precio está hecho, y otra vez cuando llegan las respuestas."
---

# cuestionario-cliente

> **BORRADOR v0.3 · revisado por Reme · 2026-11-18** · Dueña: Reme (qué se
> pregunta) · Guion de WhatsApp: Menchu (cómo se dice) · Maquetación del Word:
> Lola · Herramientas: Paco · En revisión (ronda 1b)

## La regla que lo decide todo

Cada pregunta tiene un **para qué**: un destino concreto en el presupuesto, el
plazo, los requisitos, los textos o el diseño. **Si no lo tiene, se quita.**

- **Tanda A · para el presupuesto:** solo lo que puede cambiar **el plan, el
  precio o el plazo**. **10 obligatorias como máximo**; el resto,
  condicionales. Hoy son 8 obligatorias, 10 condicionales y 1 opcional (la
  foto de la fachada).
- **Tanda B · al aceptar el presupuesto:** todo lo demás, más los bloques
  según el tipo de web.

Las preguntas, con su ID, condición, ★ y destino, están en
[preguntas.md](preguntas.md). El formato de requisitos, en
[plantilla-requisitos.md](plantilla-requisitos.md).

## Cuándo

| Momento | Qué se hace | Quién |
|---|---|---|
| Expediente con lo público **y previo de precio hecho** | Preparar la tanda A de este cliente | Reme |
| Envío | Tanda A por WhatsApp, con `guion-tanda-a.md`; el Word, solo en la copia por correo | Menchu (A-003) |
| Llegan las respuestas de A | Requisitos v0.x y borrador de presupuesto | Reme |
| El cliente acepta el presupuesto | Preparar la tanda B | Reme |
| Llegan las respuestas de B | Completar los requisitos | Reme |

## Preparar la tanda A de un cliente

1. **Partir del catálogo:** las 8 obligatorias, las condicionales y el bloque
   de sector (o el genérico). No se inventan opciones.
2. **Quitar lo que ya sabemos** con fuente primaria: lo del primer contacto
   (`privado/contacto.md`) y lo comprobado del expediente. Se anota de dónde sale.
3. **Confirmar, no preguntar desde cero** (A 1.1–1.4). Los datos «a confirmar»
   se presentan como «lo que hemos visto». Las ausencias, como «no hemos
   encontrado».
4. **Lo que diga el previo:** si necesita saber algo que no está, se añade
   **como condicional**, o sustituye a una obligatoria. **Nunca más de 10
   obligatorias.** Si la pregunta sirve para otros clientes, entra en el catálogo.
5. **Entregar a Federico** la lista del cliente (los ID y lo que se salta) para
   Menchu. Si va también en Word, a Lola para la maqueta.
6. **Comprobar** (abajo) y pasar a Puri.

## Comprobación antes de Puri

Todas, en el guion y en el Word:

1. Como mucho **10 obligatorias**; cada condicional con su «solo si…».
2. Cada pregunta con su **ID del catálogo** y la versión del catálogo en el pie
   o en la cabecera («catálogo v0.3»).
3. **Ninguna pregunta de la tanda B:** ni datos legales, ni fotos (salvo la de
   la fachada, opcional y la última), ni aprobación de textos.
4. **Instrucciones que se pueden seguir en ese formato** (R36): por WhatsApp,
   contestar con un número; en Word, nada de «rodeadla».
5. **Ningún «¿correcto?» sobre una ausencia o un dato sin confirmar** (R33):
   «no hemos encontrado», «lo que hemos visto».
6. **Las preguntas sobre personas, en presente** (R32). Nada de dar por hecho
   que alguien ya no está.
7. **Ninguna promesa sin dueño:** ni llamadas (A-002), ni ayuda con las fotos,
   ni plazos (R07, R35).
8. **Nada en boca del cliente** que no haya dicho él (R27).
9. **Ninguna cifra ni frase general sin fuente** (R04, R10–R27).
10. **El permiso de las opiniones, igual que en el expediente** (R31,
    pendiente de A-010). Es tanda B.
11. **Fotos con personas:** solo con permiso por escrito, y el de los padres
    para los niños. Si no hay permiso, no salen, ni de espaldas (R34). Es tanda B.
12. **Nunca pedir contraseñas** (§12), y decirlo.
13. **Sin precios ni plazos [PROPUESTA].**
14. **La línea de privacidad** (A-010), cuando exista. Mientras no exista, el
    envío a un cliente real queda bloqueado.

Solo el Word, además:

15. **Los ID, visibles** junto a cada pregunta: el cliente puede contestar por
    WhatsApp con el número (Lola).
16. **Una sola columna:** la pregunta arriba y la respuesta debajo (Lola).
17. **«Está bien» / «Hay algo mal»** en lugar de una casilla «¿Correcto?» (Lola).
18. **Generado con `w.nuevo_documento(titulo=…, autor=…)` y `w.guardar(doc, ruta)`**,
    no con `doc.save()`: así sale en es-ES, con propiedades reales, y no se
    sobrescribe si alguien lo tiene abierto (Paco, R39, R40, R63).
19. **`herramientas/pruebas/revisar_docx.py`** sin avisos, y Iván lo prueba en
    Word **una vez por versión de plantilla** (A-007).

## Pasar las respuestas a requisitos

1. **Las respuestas, literales, en `privado/`.** Menchu las anota con su ID en
   `privado/respuestas-tanda-a.md` (y `-tanda-b.md`). Un Word devuelto se
   guarda intacto en `privado/recibido/`. **Nada de esto va a git** (A-009,
   A-013).
2. **Leerlas por ID.** Del Word, con el lector de Paco cuando exista
   (`leer_cuestionario.py`); mientras tanto, a mano.
3. **Repartirlas por destino:**

   | Destino | Qué se hace | ¿En git? |
   |---|---|---|
   | `DATO` | Al expediente §1, con fuente «cliente, A x.y, fecha». Sale de «a confirmar». Solo datos del negocio | Sí |
   | `PRECIO`, `PLAZO` | Al borrador de presupuesto (skill `previo-precio`) | **No**: `privado/` |
   | `REQ` | Requisito `R-xx` en `requisitos.md`, con el ID como origen | Sí |
   | `CONT`, `DIS` | Fila en «Contenido y materiales» y aviso a Federico para Chema o Lola | Sí |
   | `PRIVADO` | Solo en `privado/` | **No** |

4. **`requisitos.md` cita el ID, nunca la respuesta literal** si lleva datos de
   personas. Ni nombres ni teléfonos ni correos: «la persona de contacto
   (`privado/contacto.md`)».
5. **Lo que falta o es ambiguo** va a «Falta saber» y se pide a Federico. **No
   se supone la respuesta.** Una ★ sin respuesta bloquea el presupuesto.
6. **Versiones:** v0.x mientras se negocia; **v1.0 cuando el cliente acepta
   el presupuesto**. Desde ahí, solo cambia con el control de cambios (`C-xx`).
7. **Anotar en el historial del expediente y avisar a Federico** (§13.2.6).

## Reglas

1. **Pocas preguntas, las justas.** Si entra una obligatoria, sale otra.
2. **No preguntar lo que ya nos han dicho.**
3. **No se pide lo que aún no hace falta** (§12): datos legales, fotos y
   nombres, en la tanda B.
4. **Cada pregunta, una sola cosa,** y que se pueda contestar con un número o
   una línea.
5. **Sin jerga,** con un ejemplo en cada pregunta abierta.
6. **El canal es WhatsApp** (A-002, A-003). Sin llamadas. Para lo largo de
   contar (la historia de la tanda B), audios.
7. **Aprobar textos no se hace en el cuestionario,** sino en la fase de textos
   (§13.5, paso 4), con sus 2 rondas.

## Herramientas

- `herramientas/docx_util.py` (Paco): `nuevo_documento`, `guardar`, casillas
  como controles de contenido (`w14:checkbox`). Las casillas se pueden leer
  automáticamente: probado el 2026-11-17, 3 marcadas de 3 en una copia.
- Pedido a Paco: parámetro `id` en casillas, opciones y huecos (como `w:tag`) y
  `leer_cuestionario.py`.
- `herramientas/pruebas/revisar_docx.py` (Paco): comprobación del Word.

## Salida

- La tanda A del cliente: la lista de ID que se preguntan, a Federico para Menchu.
- Si hay copia por correo: `clientes/<negocio>/entregables/Cuestionario A - <negocio>.docx`.
- `clientes/<negocio>/requisitos.md`, desde [plantilla-requisitos.md](plantilla-requisitos.md).

## Dudas abiertas

- **Columna «se comprueba así» de `requisitos.md`:** pendiente de lo que diga Puri.
- **Línea de privacidad y permiso de las opiniones:** A-010.
- **¿El vídeo entra en los planes?** A-011. Hasta entonces, A 5.5 pregunta si
  tienen vídeos, pero no se promete usarlos.
