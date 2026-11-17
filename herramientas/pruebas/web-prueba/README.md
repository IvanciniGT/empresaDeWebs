# Web de prueba de `extraer_web.mjs` y `captura.mjs`

Un negocio **inventado** (Peluquería La Prueba), con datos ficticios, para probar
las herramientas sin descargar webs de terceros. La sirve `servidor.mjs` en
127.0.0.1; `{{BASE}}` y `{{EXTERNO}}` se sustituyen al servirla.

Trampas a propósito (las comprueba `probar.mjs`):

| Trampa | Dónde | Qué se espera |
|---|---|---|
| Zona prohibida en robots.txt | `/privado/secreto.html` | No se pide nunca |
| Excepción permitida (Allow más largo) | `/privado/publico.html` | Se visita |
| Página solo en el sitemap | `oculta.html` | Se encuentra |
| Enlace a otra web | `{{EXTERNO}}/otra.html` | No se visita |
| Administración | `/wp-admin/` | No se visita |
| Enlace roto | `/no-existe.html` | Sale en «rotas» |
| Aviso de cookies desconocido | `index.html` (magenta) | Se oculta |
| Aviso de OneTrust | `servicios.html` (magenta) | Se oculta |
| Precio pintado por JavaScript | `servicios.html` | Se extrae |
| Imagen perezosa (JavaScript) al final | `servicios.html` | Se descarga (hay que bajar por la página) |
| Miniatura de WordPress | `foto-salon-300x200.jpg` | Se descarga el original 1200×800 |
| Foto de banco por el nombre | `shutterstock_123456.jpg` | Se marca |
| Foto de banco por los metadatos | `equipo.jpg` | Se marca |
| Sin `<meta viewport>` | `sin-movil.html` | «No adaptada al móvil» |
| Carta en PDF | `carta.pdf` | Se descarga |
