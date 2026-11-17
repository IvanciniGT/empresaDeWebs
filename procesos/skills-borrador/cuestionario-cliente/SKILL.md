---
name: cuestionario-cliente
description: "Prepara el cuestionario Word editable que se envía a un cliente nuevo: lo que ya sabemos de él para que lo valide, lo que nos falta para que lo complete y los textos que le proponemos para que los apruebe. Úsala cuando el expediente tiene la información pública recopilada."
---

# cuestionario-cliente

> **BORRADOR v0.1** · Escrito por Federico · **Dueña: Reme** (los textos propuestos, de Chema) · En revisión (ronda 1)

## Cuándo

Cuando el expediente ya tiene lo publicado sobre el cliente. Es la
**primera batería** de preguntas. La segunda, específica del tipo de web que
quiera, se hace cuando sepamos qué quiere.

## Entrada

- Expediente con datos comprobados y por confirmar.
- Textos propuestos por Chema (frase principal, quiénes somos y por qué venir).

## Contenido (primera batería)

| # | Bloque | Qué se pide |
|---|---|---|
| 1 | Lo que ya sabemos | Validar los datos comprobados (casilla «¿Correcto?» y hueco para corregir) |
| 2 | Contacto | Persona, móvil, WhatsApp, correo; qué contacto se muestra en la web |
| 3 | Datos legales | Titular y NIF para el aviso legal |
| 4 | Quiénes sois | Nombres, historia, años, equipo, qué os define |
| 5 | Servicios y precios | Qué hacen, precio y duración; cita y formas de pago |
| 6 | Objetivos | Para qué quieren la web, cliente típico, idiomas |
| 7 | Opiniones | Permiso para mostrar sus reseñas de Google |
| 8 | Textos propuestos | Aprobar o cambiar |
| 9 | Fotos, vídeo y logotipo | Qué tienen y consejos para hacerlas |
| 10 | Presencia en internet | Ficha de Google, redes, dominio |
| 11 | Gustos | Webs que les gustan o no, colores |

Lo imprescindible para empezar va marcado con ★.

## Pasos

1. Copiar el generador de un cliente anterior (`generar_cuestionario.py`) y
   adaptar el contenido al negocio.
2. Rellenar «Lo que ya sabemos» **solo** con datos del expediente.
3. Incluir los textos de Chema en recuadro verde, con casillas para aprobar o cambiar.
4. Generar el Word: `.venv/bin/python clientes/<negocio>/generar_cuestionario.py`.
5. Convertirlo a PDF con LibreOffice para revisarlo a ojo
   (`soffice --headless --convert-to pdf`).

## Reglas

1. **Pocas preguntas, las justas.** Lo que no sirve para la web o el presupuesto, fuera.
2. **Que se entienda sin nosotros delante:** sin jerga, ejemplos en cada pregunta abierta.
3. **Código de colores fijo:** gris, lo que sabemos; naranja, para que escriba;
   verde, nuestras propuestas.
4. **Nunca pedir contraseñas** (§12); se dice en el propio documento.
5. **Sin precios ni plazos** marcados como [PROPUESTA].
6. **Ofrecer siempre la alternativa de hacerlo por teléfono.**

## Herramientas

- `herramientas/docx_util.py`: casillas clicables, huecos, recuadros, tablas y textos propuestos.

## Salida

- `entregables/Cuestionario - <negocio>.docx`

## Dudas abiertas (para la revisión)

- ¿Diez páginas es demasiado? ¿Qué se puede quitar o dejar para la segunda batería?
- ¿Los datos legales van aquí o al contratar?
- ¿Una plantilla general con bloques por sector (peluquería, cafetería, taller…)?
- ¿Cómo pasan las respuestas del Word a requisitos en el expediente?
