# Web · versión 2 (E-024, Paco, 2026-11-19)

Misma base que `../web/` (E-022), más trabajada. HTML + CSS estático, sin dependencias ni cookies.
Se abre con doble clic en `index.html`. No necesita servidor.

- **Amarillo `[…]`**: datos que faltan. **Rojo «BORRADOR»**: qué tiene que pasar antes. Nada inventado.
- `noindex`: no está pensada para publicarse así.
- `hoy.js` (opcional): marca el día de hoy en el horario y dice «Abierto/Cerrado ahora». Sin él, todo se ve igual.
  El horario es provisional (OpenStreetMap): si cambia, se cambia en `hoy.js` y en el HTML.
- `img/mapa*.jpg`: hecho con `herramientas/mapa.py` (teselas de OSM, atribución dentro de la imagen).
- Colores y tipos: guía previa de la ronda 1. Contrastes comprobados (todos ≥ 4,5 : 1).
- Capturas: `*-pantalla.png` es lo que se ve al abrir. `*-completa.png` es la página entera, hecha con
  la cabecera sin fijar (si no, la cabecera fija sale pintada en mitad de la captura).
