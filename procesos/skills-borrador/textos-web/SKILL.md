---
name: textos-web
description: "Redacta los textos de la web de un cliente con su voz y pensados para que llame o reserve: la ficha de tono, la frase principal como muestra para el informe (antes de contratar), los textos propuestos para la tanda B y los definitivos. Cada frase, trazada al expediente y pasada por la lista de frases vigiladas. Úsala cuando haga falta cualquier texto de cara al público de un cliente."
---

# textos-web

> **BORRADOR v0.3 · revisado por Chema** · 2026-11-18 · **Dueño: Chema**
> v0.1 → v0.3: el tono de comunicación pasa aquí desde la guía de Lola, la lista de
> frases vigiladas (Puri), la frase principal de 45 caracteres como mucho (Lola), los
> modos según las dos tandas (Reme y Menchu) y la historia por audios (A-002).
> Detalle en [revision-chema.md](../../ronda-1/revision-chema.md) §8.

## Cuándo

| Modo | Cuándo | Qué sale | Va a |
|---|---|---|---|
| **Muestra** | Antes de contratar, con el informe | Ficha de tono (hipótesis) y **frase principal**, en 2 variantes | Informe, página 2, como «una idea» (`estudio-competencia`) |
| **Propuesta** | Al aceptar el presupuesto | Frase principal, quiénes somos y por qué venir, con huecos | Tanda B del cuestionario (Reme) |
| **Definitivo** | Con la tanda B respondida y los materiales | Textos de cada página, títulos, descripciones y botones | La web (Paco), con el SEO base. El cliente los aprueba a través de Menchu |

Reme decide **qué se pregunta**; esta skill decide **cómo se cuenta**.

## Regla de oro

**Una reseña es una pista, no un dato.** Lo que solo sale de reseñas se convierte en
**pregunta** o en **hueco**, nunca en afirmación. Y **nada que el cuestionario
pregunte se afirma en el texto** (Puri, R26–R27).

| Tipo de dato | En el texto |
|---|---|
| Comprobado (expediente §1) | Se escribe tal cual. |
| Por confirmar (§2) | Hueco con lo que creemos: «desde [año: ¿1990?]». |
| Lo intuimos (§3, reseñas) | Variante condicionada: «Si nos confirmáis que…, diríamos: …». |
| Desconocido | Hueco: «[vuestros nombres]». |

## Ficha de tono

Antes estaba en la guía previa de Lola; ahora es mía. La guía solo dice dónde va
cada texto y cuánto cabe. La ficha va en `clientes/<negocio>/textos/tono.md`.

**Fuentes, por orden:**
1. **Cómo escribe el negocio:** su web y sus redes, **sus respuestas a las reseñas**
   (captura de Iván) y sus mensajes a Menchu (registro de contactos).
2. **Cómo lo describen sus clientes** (reseñas): pista de lo que valoran, no de cómo habla.
3. Modo definitivo: sus respuestas y sus audios.

Si solo tenemos la 2, la ficha se marca **«hipótesis»** y se confirma en la tanda B.

**Qué lleva:**

| Apartado | Cómo |
|---|---|
| Tratamiento | Tú, usted o vosotros. Por defecto, tú (AGENTS.md §9.2), salvo que el negocio use usted. |
| Tres rasgos | Cada uno con su fuente: «cercano: contesta las reseñas por el nombre (captura 03)». |
| Humor | Solo si lo usa el negocio, y nunca a costa del cliente. |
| Palabras suyas | Literales y con fuente. Las frases entre comillas de las reseñas («listo para triunfar») son candidatas, a confirmar. |
| Palabras prohibidas | Jerga y relleno: «integral», «personalizado», «experiencia única», «disponemos de», «contacte con nosotros», «profesionales altamente cualificados», «viral», «garantizado». |
| Tres pares «así sí / así no» | El «así sí» **no lleva ningún dato sin comprobar**. |

Ejemplo de pares, con datos comprobados del caso de la ronda 1:

| Así sí | Así no |
|---|---|
| «Estamos en la calle Octavio Cuartero, 57.» | «Nuestras instalaciones se ubican en una zona privilegiada.» |
| «Llámanos: 967 23 57 91.» | «Contacte con nosotros para más información.» |
| «Te cortamos el pelo a tu gusto.» (se repite en dos reseñas: a confirmar) | «Ofrecemos un servicio integral de asesoramiento capilar personalizado.» |

Contraejemplo de la guía de la ronda 1: «Pide cita por WhatsApp y no esperes» lleva
dos datos sin comprobar (que tienen WhatsApp y que no se espera). No vale ni como ejemplo.

## Frase principal

- **45 caracteres como mucho, con espacios** (Lola: tres líneas en el móvil). Se
  mide, no se calcula a ojo: `python3 -c 'print(len("…"))'`. Lola lo comprueba con la maqueta.
- **2 variantes de tono** (por ejemplo, cercana y sobria) para que elija el cliente.
- Con la actividad o el lugar en al menos una de las dos: ayuda a que le encuentren.
- En el informe va como «una idea para vuestra web», con su condición si la tiene.

Ejemplo (ronda 1): «Le cortamos el pelo a tu padre. Ahora, a ti.» (44): variante
condicionada a que confirmen el relevo familiar. «Peluquería de caballero y niños en
Albacete.» (44): variante sobria, condicionada a que confirmen que cortan a niños.

## Pasos

### Modo muestra (antes de contratar)

1. Leer el expediente y elegir **el ángulo**: lo que el negocio tiene y los demás no
   pueden copiar, sacado de lo que **se repite** en las reseñas (con cuántas lo dicen).
2. Ficha de tono, marcada como hipótesis si no hay fuente del propio negocio.
3. Frase principal en 2 variantes, con su traza y su condición.
4. `vigilar_frases.py --frase "…"` → 0 avisos B.
5. Entregar a `estudio-competencia` para la página 2 del informe.

### Modo propuesta (tanda B)

1. Bloques: **frase principal**, **quiénes somos** y **por qué venir**. Como mucho, 120 palabras entre los tres.
2. Al lado de cada frase, su **traza**: la fila del expediente o «hueco». Sin traza, se quita.
3. Convertir en preguntas para Reme (a través de Federico) lo que haya hecho falta suponer:
   el origen del nombre, si una frase entre comillas de una reseña es suya, etc.
4. Pasar `vigilar_frases.py` por la tabla.

### Modo definitivo

1. La **historia** del negocio, de sus audios de WhatsApp (A-002: no hay llamadas),
   transcritos en local con whisper.cpp (A-008, Paco). Audios y transcripción, en
   `privado/`. Cada frase de la historia se traza al minuto del audio.
2. Los mismos bloques, ya con los datos de la tanda B.
3. Integrar las búsquedas objetivo **con naturalidad**: actividad y lugar en el
   titular, en el primer párrafo y en los títulos de sección. Nunca una lista de palabras.
4. Por cada página: título (≤ 60 caracteres), descripción (≤ 155), H1 y textos de los botones.
5. Llamada a la acción con el canal comprobado (Lola: por defecto, **Llamar**).
6. `vigilar_frases.py` → 0 avisos B. Después, Puri. El cliente los aprueba a través de Menchu (§11).

## Reglas

1. **Cada frase, trazable al expediente, al cuestionario o a un audio.**
2. **Nada de cifras que caduquen** dentro del texto («4,8 con 132 opiniones»): la nota va en vivo o no va.
3. **Ninguna promesa** que el negocio no haya hecho («si tienes cita, no esperas»).
4. **Las reseñas no se copian en la web** sin una vía aprobada (módulo oficial de Google
   o permiso del autor; pendiente del paquete legal, A-010). En el informe se citan
   como mucho dos, literales y sin autor, cada una con su prueba.
5. **La voz del negocio, no la nuestra:** la de su ficha de tono.
6. **Para personas primero:** frases cortas, sin jerga, sin relleno.
7. **Lista de frases vigiladas** ([`frases-vigiladas.txt`](frases-vigiladas.txt)): los avisos B
   no salen nunca; los R salen solo con traza. Si encuentras un error nuevo, añade su
   patrón **y su prueba**.

## Herramientas

| Herramienta | Para qué |
|---|---|
| [`vigilar_frases.py`](vigilar_frases.py) + [`frases-vigiladas.txt`](frases-vigiladas.txt) | Lista negra de Puri, con nivel B (bloquea) o R (revisar). Sale con 1 si hay algún B. Sobre el envío de la ronda 1 marca 5 B en el informe y 5 en el cuestionario, todos errores reales. 7 pruebas y 10 mutaciones en `pruebas/`. **No aprueba nada:** señala dónde mirar. |

Límite conocido: no ve una frase partida entre dos etiquetas HTML («<b>0</b> páginas»).
Por eso las cifras no se escriben en la plantilla (`estudio-competencia`, regla 1).

## Salida

- Muestra: `textos/tono.md` (hipótesis) y la tabla `Variante | Frase | Caracteres | Traza | Condición`.
- Propuesta: tabla `Bloque | Texto | Traza`, lista para Reme, y la lista de preguntas que salen de los huecos.
- Definitivo: `textos/` con un fichero por página (título, descripción, H1, cuerpo y botones) y su traza.

## Comprobación final

- [ ] Ninguna frase sin traza; nada que el cuestionario pregunte, afirmado.
- [ ] `vigilar_frases.py`: 0 avisos B; cada R con traza.
- [ ] Frase principal: 2 variantes, ≤ 45 caracteres medidos.
- [ ] La ficha de tono dice de dónde sale cada rasgo, o está marcada como hipótesis.
- [ ] (Definitivo) Título y descripción dentro de su longitud y con actividad y lugar.

## Ejemplo (caso Hermanos Cotillas, ronda 1)

| Antes | Problema | Después |
|---|---|---|
| «desde hace más de 30 años» | Una reseña de un cliente | «desde [año]» y la pregunta «¿En qué año abrieron?» |
| «Puntuales: si tienes cita, no esperas» | Promesa sacada de una reseña | Fuera hasta que marquen «trabajamos con cita» |
| «abrieron esta peluquería en la calle Octavio Cuartero» | El cuestionario lo pregunta | «abrieron esta peluquería en [año]» |
| «los hermanos Cotillas» | Supone el apellido | Pregunta: «¿De dónde viene el nombre?» |
| «listo para triunfar» | Puede ser su frase | Pregunta: «¿Es vuestra frase?»; si lo es, lema candidato |
| «Para toda la familia: del abuelo al nieto» | No sabemos si cortan a mujeres ni a abuelos | Fuera hasta la tanda B |
