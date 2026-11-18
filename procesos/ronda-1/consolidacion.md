# Consolidación de la ronda 1

> Federico · 2026-11-17 · Revisiones de [Chema](revision-chema.md), [Reme](revision-reme.md),
> [Lola](revision-lola.md), [Paco](revision-paco.md), [Puri](revision-puri.md) y [Menchu](revision-menchu.md).
> Veredicto de Puri sobre mi trabajo: [RECHAZADO](../../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md).

## 1. Lo que hemos aprendido

| # | Lección | Lo ha visto |
|---|---|---|
| 1 | **Mi trabajo no se podía enviar.** Puri cuenta 9 errores que bloquean, 33 importantes y 21 menores. Después de quitar yo seis frases inventadas, quedaban más de veinte afirmaciones sin fuente. La buena voluntad no basta: hacen falta cifras calculadas por script, una lista negra de frases y una revisión independiente. | Puri, Chema |
| 2 | **Pedíamos demasiado y demasiado pronto:** diez páginas, el NIF, las fotos y la aprobación de textos antes de dar un precio. | Reme, Menchu, Puri |
| 3 | **El canal es WhatsApp,** no un correo con dos adjuntos. Un `.docx` no se rellena en el móvil. | Menchu, Lola |
| 4 | **Prometíamos una llamada que nadie puede hacer.** | Menchu, Puri |
| 5 | **`buscar.sh` incumple el `robots.txt` de Bing.** Leer los resultados de Google, Bing, DuckDuckGo, Brave o Mojeek con un robot va contra lo que piden. Las API de Bing y de Custom Search de Google ya no existen o están cerradas a clientes nuevos. | Chema |
| 6 | **«Comprobado» estaba mal definido:** dos directorios que copian la misma ficha de Google son una sola fuente, y una reseña es una pista, no un dato. | Chema |
| 7 | **Cifras mal:** 281 incluía 9 tiendas de productos de peluquería (son 273), y el «vecino más cercano» no lo era (hay tres más cerca). | Puri, Chema, Reme |
| 8 | **Competidores mal elegidos:** dos de los cuatro son salones unisex o de señora, y hay 16 de caballero a menos de 500 m. | Chema |
| 9 | **Nada se leía bien en el móvil:** letra de unos 7 px en el informe, el Word en inglés y un código de colores que no se distingue. | Lola |
| 10 | **Datos personales sin cláusula de privacidad** y sin un sitio fuera de git donde guardarlos. | Reme, Puri, Menchu |

## 2. Acuerdos (se aplican sin más)

| Acuerdo | Lo propone | Lo aplica |
|---|---|---|
| Cuestionario en **dos tandas**: A (para el presupuesto) y B (para construir, después de aceptar) | Reme, Menchu | Reme |
| **Datos legales, fotos y aprobación de textos**, a la tanda B | Reme, Menchu, Puri | Reme |
| **Ninguna promesa de llamada** hasta que Iván decida quién llama | Menchu, Puri | todos |
| El **previo de precio va antes** de la tanda A: dice qué preguntas cambian el plan | Reme | Reme |
| **Retirar `buscar.sh`** | Chema | Paco |
| **Regla de independencia de fuentes** y sección «Lo que intuimos (preguntar)» en el expediente | Chema | Chema |
| **Las cifras se calculan con un script** a partir de datos guardados; nunca se teclean en la maqueta | Puri, Chema | Chema, Paco |
| Censo solo con `shop=hairdresser` (fuera `hairdresser_supply`) | Puri | Chema |
| **Criterio de competidores:** directos (mismo público, menos de 500 m), de búsqueda y un referente. Cuatro como máximo | Chema | Chema |
| **Skill nueva `textos-web`** (Chema): una reseña se convierte en pregunta, no en afirmación. El tono de comunicación pasa aquí desde la guía de Lola | Chema, Lola | Chema |
| **Skill nueva `estilo-documentos`** (Lola): identidad común provisional para todo lo que mandamos | Lola | Lola |
| **Guía previa más corta** (3–4 páginas) y como hipótesis; sin logotipo ni boceto con aspecto de terminado. En el boceto, la acción principal es **Llamar** | Lola | Lola |
| **Catálogo de preguntas con ID** y lector automático de las respuestas del Word | Reme | Reme, Paco |
| **`requisitos.md`** en el expediente, con columna «se comprueba así» | Reme | Reme, Puri |
| **Registro de contactos** con el cliente en el expediente y **fecha del próximo contacto** en `encargos.md` | Menchu | Menchu, Federico |
| Word en **es-ES**, con metadatos reales, texto alternativo en las imágenes y **sin regenerar si alguien lo tiene abierto** | Puri, Lola | Paco |
| La revisión de Puri se repite **hasta APROBADO** | Puri | Federico |
| En `entregables/` solo lo que se envía | Puri | todos |

## 3. Choques entre vosotros y cómo los resuelvo

| # | Choque | Resolución |
|---|---|---|
| 1 | **Tamaño de la tanda A.** Menchu propone 8 preguntas; Reme, unas 25 en un máximo de 4 páginas. | Qué se pregunta lo decide Reme (su área), con su regla: **solo lo que cambia plan, precio o plazo**. Pero la tanda A se hace por WhatsApp, así que: **10 preguntas obligatorias como máximo**, y el resto, condicionales («solo si habéis marcado…»). Reme y Menchu cierran la lista en la ronda 1b. |
| 2 | **Informe.** Chema: 2 páginas más un anexo. Lola: formato A5 para el móvil. | Se complementan. **Chema escribe para 2 páginas; Lola maqueta para el móvil.** El formato (A5 o vertical) es de Lola, que lo propone a Iván con mi recomendación. |
| 3 | **Foto de la fachada.** Lola la necesita para la guía previa (antes de contratar); Menchu y Reme dejan las fotos para después. | **Una sola pregunta opcional en la tanda A:** «Si tenéis a mano una foto de la fachada con el rótulo, mandádnosla». Ninguna foto más hasta que acepte. Sin ella, la guía previa sigue siendo una hipótesis. |
| 4 | **Herramientas dentro de las skills** (`contraste.py` de Lola, `comprobar.py` de Puri). | Se quedan en la skill de su dueña. Paco las revisa técnicamente y decide si alguna pasa a `herramientas/`, sin cambiar lo que comprueban. |
| 5 | **¿Quién revisa a Puri?** | Yo reviso sus veredictos por muestreo. Si no estamos de acuerdo, decide Iván. |
| 6 | **«Webs que os gustan».** Reme preguntaba si Lola las necesita. | No las necesita. Se quedan en una línea sobre colores y en la foto de la fachada. |

## 4. Cambios en el proceso ([alta-cliente.md](../alta-cliente.md), mío)

- Fase 0, **primer contacto** (Menchu), y fase 9, **seguimiento y respuestas** (Menchu).
- **Previo de precio antes de la tanda A.**
- Fase nueva: **requisitos y borrador de presupuesto** (Reme), con las respuestas de la tanda A.
- Fase 6, **revisión hasta APROBADO**, con re-revisión.
- Regla 1, con **independencia de fuentes**; §4, sin `buscar.sh`; skills nuevas: `textos-web` y `estilo-documentos`.

Lo aplico al cerrar la ronda 1b, cuando las skills estén en v0.3.

## 5. Paco

Ha trabajado sin instalar nada: 22 pruebas automáticas y 17 mutaciones (estropea
cada arreglo a propósito y comprueba que su prueba falla).

- 🔴 **El repositorio de GitHub es público** → A-013, urgente.
- **Hecho en `herramientas/`:**
  - `buscar.sh`, retirada;
  - capturas de página completa, sin avisos de cookies y con móvil de verdad;
  - `html_a_pdf` avisa de lo que no carga y genera PDF accesibles;
  - el Word sin los 64 errores de estructura y en español;
  - `mapa.py` cumple la política de teselas de OSM;
  - `requirements.txt`;
  - **`extraer_web.mjs`**, probado con una web de prueba local.

  Los PDF del caso salen idénticos a los de antes (16 de 16 páginas).
- **Le toca a los dueños de los generadores:**
  - Chema y Reme, añadir la dirección de OSM al pie del mapa;
  - Reme, usar `nuevo_documento(titulo, autor)` y `guardar()`.
- **Lo de Lola** (paleta, A5, piezas nuevas), en la ronda 2, cuando Iván apruebe A-006.
- **Puri** puede usar `herramientas/pruebas/revisar_docx.py` para el Word en lugar de duplicarlo.
- **Decisiones de Iván:**
  - A-013 (repositorio público);
  - A-014 (llavero como gestor de secretos);
  - A-015 (Overpass y uso comercial);
  - Lighthouse, dentro de A-008;
  - la retención de extracciones, dentro de A-009.

**Aviso a Iván:** tus instrucciones generales dicen que `timeout` está en
`/usr/local/opt/coreutils/libexec/gnubin/timeout`, y no está (lo han visto Lola y Paco).

## 6. Decisiones para Iván

Están en la [bandeja de aprobaciones](../../operacion/aprobaciones.md), de la A-001 en adelante.

## 7. Ronda 1b: lo que cierra cada uno

| Agente | Qué |
|---|---|
| **Reme + Menchu** | La lista final de la tanda A (choque 1): Reme, qué se pregunta; Menchu, cómo se dice por WhatsApp |
| **Chema** | Aceptar el tono de comunicación en `textos-web`; las frases de muestra para el informe y la frase principal de 40–45 caracteres (petición de Lola) |
| **Lola** | La maqueta del informe de 2 páginas para el móvil y de la tanda A en Word, con `estilo-documentos` |
| **Paco** | Las peticiones de herramientas de todos (sección 5 de cada revisión) que no necesiten instalar nada |
| **Puri** | Añadir a su lista lo que le piden Chema, Lola y Menchu |
| **Todos** | Skills en v0.3, coherentes con esta consolidación |

## 8. Cierre de la ronda 1b (2026-11-18)

Consenso cerrado. Todas las skills están en v0.3 (las de Paco, en su §8), y el
proceso está en [alta-cliente.md](../alta-cliente.md) v0.2.

- **Herramientas:** 37 pruebas en verde con el estilo de Lola ya dentro, y 33 de
  34 mutaciones detectadas. Pendiente para Paco:
  - la mutación «alt vacío tratado como si faltara» no se detecta;
  - en el mapa nuevo, las etiquetas de 250 m y 500 m quedan tapadas por los puntos.
- **`w:tag` de las opciones:** «A 3.5|2» (Paco y Reme) y no «A 3.5.2» (Lola),
  porque el punto choca con el del ID. Lo decido yo: es técnico.
- **Chema:** en `puntos.json`, el tercer campo es ahora «es barbería».
- **Plantillas de Menchu:** Puri las rechazó por R01 (cláusula de privacidad,
  A-010) y R02 (plazo de 5 días sin aprobar). Las dos las decide Iván y **no
  bloquean la ronda 2**, que es una simulación. Los importantes, ya arreglados por Menchu.
- **A Iván:** Reme ha pasado a la tanda B experiencia, puntos fuertes, valores y
  posicionamiento, porque no cambian el precio. Caben dos más en la tanda A si los quiere ahí.
