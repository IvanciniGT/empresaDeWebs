---
name: extraer-web-existente
description: "Extrae y ordena la web actual de un cliente (páginas y su texto, menú, imágenes a tamaño original con su origen, documentos, teléfonos, horarios, precios, redes, datos estructurados, diagnóstico SEO, capturas de ordenador y móvil, tecnología, dominio y certificado) para reaprovecharla en la web nueva y preparar la migración. Úsala cuando un cliente ya tiene web, sea porque lo dice o porque aparece al investigarle."
---

# extraer-web-existente

> **BORRADOR v0.3 · revisado por Paco** · 2026-11-18 · **Dueño: Paco**
> Cambios respecto a v0.0 y motivos: [procesos/ronda-1/revision-paco.md](../../ronda-1/revision-paco.md) §4.
> Herramienta hecha y probada en local: [`herramientas/extraer_web.mjs`](../../../herramientas/extraer_web.mjs).
> **Todavía no se ha usado con una web real.**

## Cuándo

Federico lo encarga cuando el cliente tiene web (lo dice él o la encuentra Chema
en `investigar-cliente`). Se hace **una vez, al principio**. Se repite justo
antes de publicar la web nueva, para tener la foto del «antes» y la lista de
direcciones viejas que hay que redirigir.

## Antes de empezar

1. **Que la web es del cliente.** El dominio tiene que coincidir con el del
   expediente, o Chema tiene que haberlo comprobado. No se extrae la web de nadie
   más: ni competidores, ni «webs de ejemplo». Para mirar a un competidor
   basta una captura (`captura.sh`).
2. **Para qué se usa.** Antes de que el cliente contrate, la extracción es
   **solo para analizar**: no se publica ni se reutiliza nada (fotos, textos)
   hasta que el cliente confirme que es suyo (AGENTS.md §4, valor 3).
3. **Datos personales.** La web puede tener nombres, fotos y correos del equipo:
   se quedan en el expediente, y solo los usa quien trabaja con el cliente (§12).

## Con qué

Con `extraer_web.mjs`, que maneja Chrome sin ventana y no necesita instalar nada.

Lo que se descartó, y por qué:

| Opción | Por qué no |
|---|---|
| `wget --mirror` / HTTrack | No están instalados y **no ejecutan JavaScript**: en Wix y en muchos constructores de webs, la página llega vacía. |
| Playwright | Haría lo mismo, pero hay que instalarlo. `chrome.mjs` cubre lo que necesitamos con lo que ya hay. |
| Leer el HTML con `curl` | Igual que `wget`: sin JavaScript no hay contenido en muchas webs de pequeños negocios. |

## Cómo se hace

```
node herramientas/extraer_web.mjs https://www.su-dominio.es clientes/<negocio>/recopilado/web-actual
```

Opciones: `--max-paginas N` (30 por defecto), `--espera S` (1,5 s entre
páginas), `--sin-capturas`, `--sin-movil`, `--sin-dominio`, `--prefijo /ruta` y
`--ignorar-robots "motivo"` (ver «Reglas»). Una web de 30 páginas tarda unos 3–5 minutos.

Qué hace, en orden:

1. Lee `robots.txt` **antes** de pedir nada. Si el servidor falla al servirlo, no visita nada.
2. Abre la URL y sigue las redirecciones (http→https, con o sin www). El sitio es
   el dominio final; en `wixsite.com` y similares, además, solo la ruta del cliente.
3. Junta las páginas de los enlaces y del `sitemap.xml`. Se salta login, carrito,
   búsqueda y administración, y no sale del dominio.
4. En cada página: espera a que cargue, oculta el aviso de cookies sin
   aceptarlo, baja hasta el final (imágenes perezosas), lee el contenido y hace
   las capturas de ordenador y de móvil. Entre una página y otra, una pausa.
5. Descarga las imágenes **a tamaño original** (deshace las miniaturas de
   WordPress, Wix, Squarespace y Shopify) y los documentos enlazados (cartas y tarifas en PDF).
6. Consulta el dominio: DNS, correo, whois (en los `.es` no es público) y certificado.
7. Escribe `datos.json` y `resumen.md`.

## Qué deja y para quién

```
clientes/<negocio>/recopilado/web-actual/
├── resumen.md      ← empezar por aquí
├── datos.json      todo, para otras herramientas
├── paginas/        texto de cada página en Markdown (NN-nombre.md)
├── html/           cada página tal como la dibuja el navegador
├── capturas/       NN-nombre-ordenador.png y NN-nombre-movil.png, página completa
├── imagenes/       NNN-nombre.ext, a tamaño original
└── documentos/     PDF y otros enlazados
```

| Sección del resumen | Para qué | Para quién |
|---|---|---|
| Menú y páginas | Qué secciones tiene y cuáles hay que conservar | Lola, Reme |
| Texto de cada página | Reaprovechar contenido | Chema |
| Datos del negocio (datos estructurados, teléfonos, WhatsApp, correos, direcciones, horarios) | Completar el expediente | Chema, Reme |
| Precios | Partida del cuestionario | Reme, Chema |
| Redes y plataformas de reserva o pedidos | Lo que hay que mantener o integrar | Reme, Chema |
| SEO por página (título, descripción, H1, canónica, indexable, datos estructurados) | Diagnóstico y redirecciones | Chema |
| Adaptada al móvil, aviso de cookies, enlaces rotos | Argumentos para el informe, sin exagerar | Chema |
| Imágenes (medidas, texto alternativo, indicio de banco de imágenes) | Qué fotos sirven y cuáles hay que confirmar | Lola |
| Estilo actual (fuentes y colores) | Punto de partida o de ruptura | Lola |
| Tecnología, dominio, DNS, correo y certificado | Migración y presupuesto (¿quién tiene el dominio? ¿el correo va en el mismo sitio?) | Paco, Reme |

## Después de extraer

1. **Leer `resumen.md` y mirar las capturas.** Ver si se ha colado algún aviso de
   cookies, si falta alguna página importante o si salen cosas raras.
2. **Lo detectado es candidato, no dato.** La web del cliente es fuente
   primaria, pero la lectura automática se equivoca (un número de fax tomado por
   teléfono, un horario antiguo en una entrada del blog). Cada dato pasa al
   expediente **revisado** y con su origen: «web del cliente, página X, fecha».
3. **No afirmar ausencias.** «No se ha detectado aviso de cookies» no es «no
   tiene aviso de cookies». El resumen ya lo dice así: no cambiarlo.
4. **Fotos:** el indicio de banco de imágenes es un indicio. Ninguna foto se
   reutiliza sin que el cliente confirme que es suya o que tiene licencia.
5. Contestar a Federico con ESTADO / RESULTADO / PENDIENTE y lo que interesa a
   cada uno (tabla de arriba).

## Reglas

1. **Solo la web del cliente.** Con tope de páginas, pausas entre páginas y sin
   peticiones en paralelo. Las imágenes y los documentos sí se descargan aunque
   estén en el servidor de la plataforma (Wix, Squarespace…): son del cliente.
2. **Respetar `robots.txt`.** Si prohíbe algo que necesitamos, se pide al cliente
   (por Federico y Menchu) **autorización por escrito** y se usa
   `--ignorar-robots "quién y cuándo lo autorizó"`. El motivo queda escrito en el resumen.
3. **Nunca iniciar sesión** ni usar contraseñas del cliente (§12), ni enviar
   formularios, ni entrar en carrito, login o administración.
4. **No inflar sus estadísticas:** la herramienta bloquea Analytics, el píxel
   de Facebook y similares, y se identifica en el User-Agent.
5. **No se aceptan cookies en nombre de nadie:** los avisos se ocultan.
6. **No probar con webs de terceros.** Para probar la herramienta, la web de
   prueba local (abajo).

## Casos especiales

| Caso | Qué hacer |
|---|---|
| La web está caída o no carga | Anotarlo en el expediente (es un dato para el informe). Reintentar otro día. Recuperarla de archive.org es una opción **sin decidir** (duda para Iván). |
| `robots.txt` lo prohíbe todo | Regla 2: autorización por escrito o nada. |
| Web en `wixsite.com/negocio`, `sites.google.com/…` | Se limita sola a la ruta del cliente. Para otros casos: `--prefijo`. |
| Web de una sola página (secciones con `#`) | Sale como una página; las secciones están en el texto y en los H2. |
| Web muy grande (blog, tienda) | `--max-paginas`. Las páginas que no entran salen en «Lo que no se ha leído». Si es una tienda con catálogo grande, avisar a Federico: puede estar fuera de lo que hacemos (§5). |
| Reservas o pedidos en una plataforma (Booksy, Treatwell, TheFork…) | Se detecta el enlace; el contenido del widget no se extrae. Reme decide qué se hace con ello. |
| El dominio redirige a otro | Se sigue y se anota. Si es de otra empresa (por ejemplo, una franquicia), avisar a Federico antes de seguir. |

## Cómo se prueba (sin webs de terceros)

Con la web de prueba local, un negocio inventado con trampas a propósito
([lista](../../../herramientas/pruebas/web-prueba/README.md)):

```
node herramientas/pruebas/probar.mjs extraer
```

La prueba levanta la web en 127.0.0.1, junto con una «otra web» en otro puerto,
y comprueba, contando las peticiones que recibe cada servidor:

- que nunca pide lo que `robots.txt` prohíbe, que no visita la otra web ni
  `/wp-admin/`, y que se identifica;
- que encuentra la página que solo está en el sitemap, y que anota la rota;
- los textos, el menú, los precios (también los que pinta JavaScript), el
  contacto, el horario y los datos estructurados;
- las imágenes: el original de la miniatura, la perezosa y las de banco;
- que en las capturas no sale el aviso de cookies y que llegan hasta el final;
  que detecta la página sin adaptar al móvil, y que descarga el PDF.

`herramientas/pruebas/mutaciones.sh` estropea cada una de esas defensas y comprueba que la prueba falla.

## Límites conocidos

- Los avisos de cookies que no conocemos pueden colarse en capturas y textos: revisar.
- No se extrae: el contenido de iframes (widgets de reservas, mapas, vídeos), el
  texto que está dentro de imágenes, los logos dibujados en SVG dentro de la
  página, los vídeos ni las fuentes (por licencia).
- La detección de horarios, direcciones y precios es por líneas de texto: si el
  horario está en una imagen o en una tabla rara, no sale.
- El whois de los `.es` no es público: la fecha de caducidad del dominio hay que
  pedirla al cliente o verla en su panel.
- Si la web bloquea a los navegadores automáticos, no se esquiva (regla 3 de
  `herramientas-comunes`): se anota y se pide ayuda al cliente.

## Novedades v0.3

- Sin cambios de fondo. Firma `empresaDeWebs/0.3`. Para medir la web del cliente, `medir_web.mjs` (Lighthouse).

## Dudas abiertas

- Si el cliente no contrata, ¿cuánto tiempo guardamos la extracción? Propuesta:
  borrarla a los 3 meses (§12, recoger solo lo necesario). Lo decide Iván.
- ¿Usamos archive.org para recuperar webs caídas o versiones antiguas?
- Primera prueba con una web real: cuando haya un cliente con web (o un caso
  simulado con el permiso de su dueño).
