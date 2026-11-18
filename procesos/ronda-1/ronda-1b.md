# Ronda 1b · Cerrar el consenso

> Federico · 2026-11-17 · Antes, lee la [consolidación](consolidacion.md) y las
> [decisiones de Iván](../../operacion/aprobaciones.md) («Resueltas»).

Vuestras revisiones han sido muy buenas. Puri rechazó mi envío con 63 errores,
y entre todos habéis visto cosas que a mí se me pasaron: el `robots.txt` de
Bing, las tiendas contadas como peluquerías, el repositorio público, la llamada
que nadie puede hacer, el Word en inglés… Iván ha aprobado **todas** las
recomendaciones salvo parte de la política de precios.

En esta ronda se **cierra el consenso**: cada uno lleva sus skills a **v0.3**
con las decisiones de Iván, los acuerdos y la resolución de los choques. Con
eso, repetiremos el caso desde cero.

## Decisiones de Iván que os afectan

| ID | Decisión | A quién |
|---|---|---|
| A-013 | **El repositorio se queda público.** Todo lo que entre en git es público. | todos |
| A-009 | Datos personales del cliente, en `clientes/<negocio>/privado/` (ya está excluida de git) | todos |
| A-001 | Ronda 2: **captura manual de Google por cliente, la hace Iván**, y fuentes abiertas. Sin API | Chema |
| A-002 | **Ninguna llamada.** Preguntas por WhatsApp | Menchu, Reme |
| A-003 | **WhatsApp primero**, correo como copia; Iván copia y pega | Menchu |
| A-004 | «Lo importante lo revisa y aprueba **Iván, el responsable**» | Menchu |
| A-005 | Informe de **2 páginas más un anexo, A5**, «gratis y sin compromiso» | Chema, Lola, Menchu |
| A-006 | **`estilo-documentos`** aprobado; guía previa de 3–4 páginas | Lola, Paco |
| A-007 | Iván prueba el Word con la lista de Puri, una vez por plantilla | Puri |
| A-008 | Fuentes, Lucide, hunspell, whisper.cpp y Lighthouse aprobados | Paco |
| A-011 | El dominio, dentro de la cuota de mantenimiento. El resto de precios, **pendiente** | Reme |
| A-012 | Recordatorios a los 3 y a los 8 días laborables, plantillas aprobadas una vez | Menchu |
| A-015 | Overpass por una instancia que acepte uso comercial | Paco, Chema |

## Lo que cierra cada uno

### Chema
1. `textos-web`: incorpora el **tono de comunicación**, que Lola saca de su guía.
2. `estudio-competencia`: el informe pasa a **2 páginas más un anexo en A5**, con lo
   que no se regala escrito, y las cifras **calculadas por script** desde el JSON
   guardado (con la consulta de Overpass guardada al lado).
3. `investigar-cliente`: el **guion de captura manual para Iván** (A-001): enlaces
   exactos, qué capturar y dónde guardarlo. Que le lleve 10 minutos como mucho.
4. Lo que te pide Puri (lista negra, cada cita de reseña con su prueba) y Lola
   (frase principal de 40–45 caracteres, primera página que funcione sola).
5. En los mapas, la atribución lleva `openstreetmap.org/copyright` (Paco).

### Reme
1. **La lista definitiva de la tanda A**: como mucho **10 preguntas obligatorias** y el
   resto, condicionales (choque 1). Ten en cuenta las 8 que propone Menchu en su
   revisión (§5). Incluye **una pregunta opcional por la foto de la fachada** (choque 3).
2. `previo-precio` antes de la tanda A; el dominio, dentro de la cuota (A-011).
3. `requisitos.md`: lo que te diga Puri sobre la columna «se comprueba así».
4. Lo que te pide Puri para tu lista de comprobación del cuestionario.
5. Cuando la tengas, avísame: **Menchu escribirá el guion de WhatsApp a partir de tu lista**.

### Lola
1. **`estilo-documentos`, completo:** paleta, tipografías, componentes, A5 para el
   informe y Word para la tanda A, con el prototipo de bloques que pide Paco.
   **Paco lo implementa en las herramientas comunes cuando lo termines:** avísame.
2. `guia-estilos-previa`: 3–4 páginas, como hipótesis; el tono pasa a Chema.

### Paco
1. **Instalar lo aprobado (A-008)**, dentro del proyecto siempre que se pueda:
   - fuentes Inter y Fraunces, en `herramientas/fuentes/` con su `OFL.txt`;
   - Lucide, en `herramientas/iconos/`;
   - Lighthouse 13.6.0, en `herramientas/`;
   - hunspell y whisper.cpp con un modelo.

   Para cada uno, documenta qué, dónde y cómo se desinstala.
2. Overpass con una instancia que acepte uso comercial (A-015): lee antes sus condiciones.
3. Lo que te piden Reme (`id` en las casillas, `leer_cuestionario.py`) y Puri, que no
   dependa del estilo de Lola.
4. Cuando Lola termine `estilo-documentos`, te aviso para que lo implementes en
   `informe.css`, `docx_util.py` y `mapa.py`.
5. Ventanas, ninguna. Para probar en Word, Iván (A-007).

### Puri
1. Añade a tu lista lo que te piden Chema, Lola, Menchu y Reme. Para el Word, usa
   `herramientas/pruebas/revisar_docx.py` de Paco en lugar de duplicarlo.
2. **Define cómo compararemos la ronda 2 con mi versión:** qué se mide (errores por
   gravedad, páginas, preguntas, afirmaciones sin fuente…) y cómo. Será la vara de
   medir del bono.
3. Contesta a Reme sobre la columna «se comprueba así» de `requisitos.md`
   (escríbelo en tu revisión: se lo paso yo).

### Menchu
1. `primer-contacto` y `primer-envio` en v0.3 con A-002, A-003, A-004, A-005 y A-012.
2. **Propón el plazo interno del alta** (A-012) en tu skill: por ejemplo, «primer envío
   en N días laborables desde el primer contacto».
3. El **guion de WhatsApp de la tanda A**, cuando Reme cierre la lista: te aviso.

## Reglas (las de la ronda 1, más una)

- Escribe solo en tus ficheros; lo que afecte a otros, a mí.
- Nada de commits; nada de contactar con nadie.
- **Nuevo:** el repositorio es público. **Nada de datos personales en git**, ni siquiera
  de prueba. Usa `privado/` o `/tmp`.
- En tu revisión, añade una sección «## 8. Ronda 1b» con lo que has cambiado.
- Al terminar: ESTADO / RESULTADO / PENDIENTE en tu sesión.

**PLAZO:** hoy.
