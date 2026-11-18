---
name: herramientas-comunes
description: "Mantiene las herramientas compartidas de la empresa en herramientas/ (capturas de webs, extracción de webs, PDF desde HTML, mapas de OpenStreetMap, piezas de Word) y su entorno: que funcionen sin abrir ventanas, cumplan las condiciones de los servicios que usan, estén probadas y no rompan lo que ya usan otros agentes. Úsala cuando haya que usar, crear, arreglar o mejorar una herramienta común."
---

# herramientas-comunes

> **BORRADOR v0.3 · revisado por Paco** · 2026-11-18 · **Dueño: Paco**
> Cambios respecto a v0.1 y motivos: [procesos/ronda-1/revision-paco.md](../../ronda-1/revision-paco.md) §4.

## Cuándo

- Un agente necesita una herramienta que no existe, una falla o se queda corta.
  Los demás **la piden a Federico**; Paco decide cómo se hace y la mantiene.
- Un agente va a usar una herramienta y quiere saber cómo se llama y qué límites tiene: la tabla de abajo.

## Lo que hay

Todo funciona **sin abrir ventanas** y sin instalar nada más que lo que ya hay en
la máquina (Chrome, Node, el `.venv` de Python y `curl`).

| Herramienta | Qué hace | Cómo se llama | Límites conocidos |
|---|---|---|---|
| `captura.sh` / `captura.mjs` | Captura una web: **página completa** y **sin avisos de cookies** (los oculta, no los acepta). En móvil, emula un móvil de verdad y avisa si la web no está adaptada. | `herramientas/captura.sh URL salida.png [ancho] [alto] [--solo-pantalla] [--con-avisos] [--json]` · ancho < 768 = móvil | Los avisos de cookies que no conocemos pueden colarse: mirar la captura. Tope de 16.000 px de alto. |
| `extraer_web.mjs` | Extrae la web de un cliente: textos, imágenes originales, contacto, precios, SEO, capturas, tecnología y dominio. Ver la skill [`extraer-web-existente`](../extraer-web-existente/SKILL.md). | `node herramientas/extraer_web.mjs URL clientes/<negocio>/recopilado/web-actual` | Solo webs de clientes. |
| `html_a_pdf.sh` / `html_a_pdf.mjs` | De HTML a PDF. Espera a fuentes e imágenes y **avisa de lo que no ha cargado**. PDF etiquetado (accesible) y con marcadores. | `herramientas/html_a_pdf.sh entrada.html salida.pdf [--estricto]` | Las fuentes de Google Fonts se descargan al generar (ver §Pendiente). |
| `informe.css` | Estilo común de los informes PDF (A4). | `<link rel="stylesheet" href="…/herramientas/informe.css">` | Pendiente de la guía de Lola (`estilo-documentos`). |
| `mapa.py` | Mapa del local y mapa de competencia con teselas de OpenStreetMap. Con **caché de 7 días** y la atribución que exige OSM. | `.venv/bin/python herramientas/mapa.py LAT LON salida.png [zoom] [puntos.json RADIO_M]` | Solo teselas estándar de OSM. |
| `docx_util.py` | Piezas del Word: casillas, huecos, recuadros, tablas, imagen con texto alternativo. Documento **en español**, sin rastro de la plantilla de python-docx, y `guardar()` que no machaca un Word abierto. | `sys.path.insert(0, "herramientas"); import docx_util as w` | Validado en LibreOffice y contra el esquema; **falta abrirlo una vez en Word** (§Pendiente). |
| `robots.mjs` | Lee `robots.txt` (RFC 9309). Lo usa `extraer_web.mjs`. | `import { interpretarRobots } from './robots.mjs'` | — |
| `chrome.mjs` | Base de las herramientas de Node: Chrome sin ventana, por tubería (sin abrir puertos). | `import { abrirChrome } from './chrome.mjs'` | — |
| `requirements.txt` | Dependencias del `.venv`. | `python3 -m venv .venv && .venv/bin/pip install -r herramientas/requirements.txt` | — |
| `pruebas/` | Web de prueba local, pruebas y mutaciones. Ver «Cómo se prueba». | `node herramientas/pruebas/probar.mjs` | — |
| ~~`buscar.sh`~~ | **Retirada.** Leía los resultados de Bing, cuyo `robots.txt` lo prohíbe. | — | Sustituta: pendiente de Iván. |

## Reglas

1. **Sin ventanas.** Iván trabaja en la misma máquina. Chrome siempre con
   `--headless`, LibreOffice con `--headless` y perfil aparte
   (`-env:UserInstallation=file:///tmp/…`), nunca `open` ni AppleScript sobre apps
   con interfaz.
2. **No instalar nada sin aprobación de Iván**, a través de Federico. La propuesta
   dice qué, para qué, dónde se instala, cuánto ocupa y cuánto cuesta. Descargar
   fuentes, iconos o modelos también cuenta como instalar.
3. **Nada que salte captchas o bloqueos, ni que vaya contra el `robots.txt` o las
   condiciones de un servicio.** Antes de automatizar la lectura de una web que no
   es de un cliente, se mira su `robots.txt` con `robots.mjs`. Si lo prohíbe, no
   se hace, aunque «funcione».
4. **Nos identificamos y no inflamos las estadísticas de nadie.** Las herramientas
   añaden `empresaDeWebs/<versión>` al User-Agent (`FIRMA` en `chrome.mjs`,
   `AGENTE` en `mapa.py`) y bloquean los medidores de visitas (`RASTREADORES`).
   No nos hacemos pasar por otro navegador ni por una persona.
5. **Servicios gratuitos, con su política de uso** (comprobadas el 2026-11-17):

   | Servicio | Lo que exige | Cómo lo cumplimos |
   |---|---|---|
   | Teselas de OSM ([política](https://operations.osmfoundation.org/policies/tiles/)) | User-Agent propio; caché ≥ 7 días con petición condicional; nada de descargas masivas; atribución visible; en PDF, con la dirección `openstreetmap.org/copyright` impresa | `mapa.py` lo hace solo. Servidor cambiable con `OSM_TESELAS`. |
   | Nominatim ([política](https://operations.osmfoundation.org/policies/nominatim/)) | Máximo 1 petición/s, User-Agent propio, guardar los resultados, nada de búsquedas sistemáticas | Una consulta por cliente, con `curl -A`, y el resultado se guarda en el expediente. |
   | Overpass (overpass-api.de) | Menos de 10.000 consultas y 1 GB al día; sin consultas en paralelo; esperar 30 s ante un 429. **Para uso comercial piden servidor propio o de pago** | Una o dos consultas por cliente, guardadas. **El uso comercial está pendiente de decisión de Iván** (revisión §6). |

6. **Compatibilidad.** Los generadores (`clientes/*/generar_*.py`) son de cada
   dueño y deben seguir funcionando: las órdenes `.sh` mantienen sus argumentos
   y las funciones de Python, su firma (los parámetros nuevos, con valor por defecto).
7. **Cada herramienta, con su uso** en la cabecera, y **cada arreglo, con su
   prueba** (ver abajo).
8. **Sin secretos en el código.** Las claves de API van al gestor de secretos
   (por decidir, §15 de AGENTS.md). Una herramienta que necesite clave la lee del
   gestor y, si no la encuentra, falla con un mensaje claro.
9. **Código y nombres en español.** Los comentarios explican por qué, no qué.

## Cómo se cambia una herramienta

1. Llega la petición por Federico. Si cambia lo que ven otros agentes (salida,
   argumentos, aspecto), se acuerda antes con Federico.
2. **Primero la prueba**, que debe fallar con el código de hoy. En
   [`herramientas/pruebas/probar.mjs`](../../../herramientas/pruebas/probar.mjs),
   contra la **web de prueba local** (`pruebas/web-prueba/`) o un servidor falso
   (como el de teselas). **Nunca contra webs o servicios de terceros.**
3. El cambio.
4. `node herramientas/pruebas/probar.mjs`: todas en verde.
5. **Comprobar que la prueba sirve:** añadir su mutación a
   [`pruebas/mutaciones.sh`](../../../herramientas/pruebas/mutaciones.sh)
   (estropea el arreglo en una copia) y ver que falla. Tarda unos 8 minutos.
6. **Si afecta a un generador:** generar en una **copia** del repositorio con la
   versión vieja y con la nueva, y comparar página a página:
   `pdftoppm -r 40 -png viejo.pdf v; pdftoppm -r 40 -png nuevo.pdf n` y comparar
   las imágenes (Pillow, `ImageChops.difference`). Para el Word, pasarlo antes a PDF
   con LibreOffice sin ventana. **Nunca regenerar los entregables de un cliente**: no son tuyos.
7. Actualizar la tabla de esta skill y avisar a Federico (ESTADO / RESULTADO /
   PENDIENTE) de lo que cambia para otros agentes.

## Cómo se prueba

```
node herramientas/pruebas/probar.mjs              # todas (≈ 1,5 min)
node herramientas/pruebas/probar.mjs captura      # solo las que se llaman «captura…»
herramientas/pruebas/mutaciones.sh                # que las pruebas detectan los fallos (≈ 8 min)
.venv/bin/python herramientas/pruebas/revisar_docx.py documento.docx   # estructura y propiedades de un Word
```

La web de prueba es un negocio **inventado** con trampas a propósito: zona
prohibida en `robots.txt`, enlace a otra web, dos tipos de aviso de cookies,
precios pintados con JavaScript, imagen perezosa, fotos de banco, página sin
adaptar al móvil… Su lista está en
[`pruebas/web-prueba/README.md`](../../../herramientas/pruebas/web-prueba/README.md).
Si aparece un caso real que falla, se añade aquí como trampa nueva.

## Recetas

- **Captura de ordenador y de móvil:**
  `herramientas/captura.sh https://ejemplo.es ordenador.png` y
  `herramientas/captura.sh https://ejemplo.es movil.png 390`.
- **Solo lo que se ve al abrir** (para un informe): `--solo-pantalla`.
- **Enseñar el aviso de cookies** de un competidor: `--con-avisos`.
- **PDF que no debe salir con nada roto:** `html_a_pdf.sh entrada.html salida.pdf --estricto`.
- **Word:** `w.nuevo_documento(titulo="Cuestionario · <negocio>", autor="<empresa>")`,
  `w.imagen(doc, ruta, 16, pie="…", descripcion="…")` y `w.guardar(doc, ruta)`.
- **Python y HTTPS:** el Python de python.org no trae certificados raíz. Sin
  instalar nada: `SSL_CERT_FILE=/etc/ssl/cert.pem .venv/bin/python …` (usa los
  del sistema). O `curl`, como hace `mapa.py`.
- **Sin `timeout`:** en esta máquina no existe (ni en coreutils). Para limitar el
  tiempo, usar el de la propia herramienta (`curl -m`, `AbortSignal.timeout` en Node).

## Pendiente

- **Abrir el Word en Microsoft Word una vez por versión de plantilla** (lo hace
  Iván: necesita ventana). La estructura ya se valida con `revisar_docx.py`.
- **Fuentes e iconos en local** (Lola: Inter, Fraunces y Lucide, licencias OFL e
  ISC): para no depender de Google Fonts al generar. Necesita el visto bueno de Iván.
- **Medir webs (Lighthouse):** propuesto a Iván (revisión §7).
- **Búsqueda en internet:** sin herramienta hasta que Iván decida (revisión §6).
- `informe.css`, `docx_util.py` y `mapa.py` con la guía de estilo de Lola, cuando se apruebe.

## Novedades v0.3 (ronda 1b)

| Herramienta | Qué hace | Cómo se llama |
|---|---|---|
| `instalar.sh` / `desinstalar.sh` / `INSTALACIONES.md` | Lo de A-008, dentro de `herramientas/` | `herramientas/instalar.sh [componente]` |
| `estilo.css` + `iconos.py` | Estilo común de los PDF (Lola, v0.3), A5, Inter, «página X de Y»; iconos Lucide en línea | `<link href="…/herramientas/estilo.css">` · `iconos.svg("check")` |
| `docx_util.py` | Paleta v0.3, Arial 11; piezas `bloque`, `pregunta`, `validar_dato`, `estado`, `como_contestar`, `pie`; `id` en casillas, huecos y tablas (`w:tag` = «A 3.5|2») | igual que antes |
| `leer_cuestionario.py` | Respuestas del Word por ID a Markdown; avisa de lo escrito fuera de los recuadros; no escribe donde iría a git | `python3 herramientas/leer_cuestionario.py recibido.docx --original enviado.docx --catalogo preguntas.md -o privado/respuestas.md` |
| `overpass.mjs` | Overpass por `overpass.private.coffee` (A-015), guarda consulta, respuesta y metadatos; no repite; espera 30 s ante 429 | `node herramientas/overpass.mjs consulta.overpassql carpeta` |
| `ortografia.py` | hunspell + es_ES + `diccionarios/empresa.txt` | `python3 herramientas/ortografia.py fichero` |
| `transcribir.sh` | Notas de voz en local con whisper.cpp; se niega a escribir donde iría a git | `herramientas/transcribir.sh audio.opus` |
| `medir_web.mjs` | Lighthouse en móvil y ordenador; `--con-medidores` para nuestras webs (§11) | `node herramientas/medir_web.mjs URL carpeta` |
| `captura.mjs` | `--elemento SEL` y `--recorte X,Y,ANCHO,ALTO` (capturas recortadas) | — |
| `html_a_pdf.mjs` | Avisa también de imágenes sin `alt` | — |
| `mapa.py` | Estilo v0.3: «Vosotros», peluquerías ● y barberías ■, leyenda dentro, Inter | igual que antes |
