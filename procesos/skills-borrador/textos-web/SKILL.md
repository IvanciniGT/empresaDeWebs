---
name: textos-web
description: "Redacta los textos de la web de un cliente con su voz y pensados para que llamen o reserven: primero como propuestas para el cuestionario (antes de contratar) y después como textos definitivos (con el cuestionario respondido). Cada frase, trazada al expediente. Úsala cuando haga falta la sección de textos propuestos del cuestionario o los textos finales de una web."
---

# textos-web

> **BORRADOR v0.1 · escrito por Chema** · 2026-11-17 · **Dueño: Chema**
> Nace de la revisión de la ronda 1: [procesos/ronda-1/revision-chema.md](../../ronda-1/revision-chema.md) §2 y §4.

## Cuándo

| Modo | Cuándo | Para quién |
|---|---|---|
| **Propuesta** | Fase 3 del alta, antes de contratar | Sección «Textos que hemos preparado» del cuestionario (de Reme) |
| **Definitivo** | Con el cuestionario respondido y los materiales | La web (Paco la monta), con el SEO base |

Reme decide **qué se pregunta**; esta skill decide **cómo se cuenta**.

## Entrada

- Expediente: datos comprobados, por confirmar, «lo que intuimos» y reseñas.
- Modo definitivo: cuestionario respondido y estudio de competencia (búsquedas objetivo).

## Regla de oro

**Una reseña es una pista, no un dato.** Lo que solo sale de reseñas se convierte en
**pregunta** o en **hueco**, nunca en afirmación.

| Tipo de dato | En el texto |
|---|---|
| Comprobado | Se escribe tal cual. |
| Por confirmar | Hueco con lo que creemos: «desde [año: ¿1990?]». |
| Lo intuimos (reseñas) | Variante condicionada: «Si nos confirmáis que…, diríamos: …». |
| Desconocido | Hueco: «[vuestros nombres]». |

## Pasos (modo propuesta)

1. Leer el expediente y elegir **el ángulo**: lo que el negocio tiene y los demás no
   pueden copiar (historia, oficio, trato…), sacado de lo que **se repite** en las reseñas.
2. Escribir como mucho tres bloques: **frase principal**, **quiénes somos** y **por qué venir**.
3. Para la frase principal, **2 variantes de tono** (por ejemplo, cercana y sobria), para que elija el cliente.
4. Al lado de cada frase, su **traza**: la fila del expediente o «hueco». Si no hay traza, la frase se quita.
5. Convertir en preguntas para Reme (a través de Federico) lo que haya hecho falta suponer:
   el origen del nombre, si una frase entre comillas de una reseña es suya, etc.
6. Pasar la lista de frases prohibidas (abajo).

## Pasos (modo definitivo)

1. Los mismos bloques, ya con los datos del cuestionario.
2. Integrar las búsquedas objetivo **con naturalidad**: actividad + ciudad o barrio en
   el titular, en el primer párrafo y en los títulos de sección. Nunca una lista de palabras.
3. Por cada página: título (≤ 60 caracteres), descripción (≤ 155), H1 y textos de los botones.
4. Llamada a la acción visible y concreta: «Llamar», «Pedir cita por WhatsApp».
5. El cliente aprueba los textos a través de Menchu (§11: todo el contenido, aprobado por el cliente).

## Reglas

1. **Cada frase, trazable al expediente o al cuestionario.**
2. **Nada de cifras que caduquen** dentro del texto («4,8 con 132 opiniones»): la nota va en vivo o no va.
3. **Ninguna promesa** que el negocio no haya hecho («si tienes cita, no esperas»).
4. **Las reseñas no se copian en la web** sin una vía aprobada (módulo oficial de Google
   o permiso del autor). En la propuesta se pueden citar al dueño, sin nombres de autor.
5. **La voz del negocio, no la nuestra:** tuteo o usted según el negocio, sus palabras.
6. **Para personas primero:** frases cortas, sin jerga, sin relleno.
7. **Prohibido:** «viral», «garantizado», «el mejor de», «número 1», «líder», superlativos sin prueba.

## Frases que se revisan antes de entregar

«desde hace más de», «generaciones», «siempre», «nunca», «todos», «el mejor», «único»,
«especialistas en», «garantiz», «sin esperas», cualquier número y cualquier lugar o fecha.
Cada una necesita traza o se convierte en hueco.

## Salida

- Modo propuesta: tabla `Bloque | Variante | Texto | Traza`, lista para que Reme la meta en el cuestionario, y la lista de preguntas que salen de los huecos.
- Modo definitivo: `clientes/<negocio>/textos/` con un fichero por página (título, descripción, H1, cuerpo, botones) y su traza.

## Comprobación final

- [ ] Ninguna frase sin traza.
- [ ] Lo que sale de una sola reseña es pregunta o hueco.
- [ ] Sin cifras que caduquen ni promesas.
- [ ] La frase principal tiene 2 variantes.
- [ ] (Definitivo) Título y descripción dentro de su longitud y con actividad y lugar.

## Ejemplo (caso Hermanos Cotillas, ronda 1)

| Antes | Problema | Después |
|---|---|---|
| «desde hace más de 30 años» | Una reseña de un cliente | «desde [año]» y la pregunta «¿En qué año abrieron?» |
| «Puntuales: si tienes cita, no esperas» | Promesa sacada de una reseña | Fuera hasta que marquen «trabajamos con cita» |
| «los hermanos Cotillas» | Supone el apellido | Pregunta: «¿De dónde viene el nombre?» |
| «listo para triunfar» | Puede ser su frase | Pregunta: «¿Es vuestra frase?»; si lo es, lema candidato |
