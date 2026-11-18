# Instalaciones (A-008)

Todo dentro de `herramientas/`, nada en el sistema. Instalar: `herramientas/instalar.sh [componente…]`
(comprueba la SHA-256 de cada descarga). Quitar: `herramientas/desinstalar.sh [--simular] componente…`.

| Componente | Qué | Dónde | Tamaño | En git | Se quita con |
|---|---|---|---|---|---|
| fuentes | Inter 4.1 y Fraunces 1.000 (SIL OFL 1.1), estáticas, con `OFL.txt` | `fuentes/inter/`, `fuentes/fraunces/` | 9 MB | Sí | `desinstalar.sh fuentes` + `git rm -r` |
| iconos | Lucide 1.75.0 (ISC; algunos MIT de Feather), SVG, con `LICENSE.txt` | `iconos/` | 8 MB | Sí | `desinstalar.sh iconos` + `git rm -r` |
| lighthouse | Lighthouse 13.6.0 (Apache-2.0), versión fijada en `package-lock.json` | `node_modules/` | 174 MB | No | `desinstalar.sh lighthouse` |
| hunspell | hunspell 1.7.6 compilado + diccionario es_ES de LibreOffice (RLA-ES) | `vendor/hunspell/`, `vendor/diccionarios/` | 8 MB | No | `desinstalar.sh hunspell` |
| whisper | whisper.cpp 1.9.5 (MIT), solo CPU + modelo `large-v3-turbo-q5_0` | `vendor/whisper/`, `modelos/` | 565 MB | No | `desinstalar.sh whisper` |
| descargas | Copias de lo descargado | `vendor/descargas/` | 58 MB | No | `desinstalar.sh descargas` |

Herramientas que lo usan: `estilo.css` e `iconos.py` (fuentes, iconos), `medir_web.mjs` (Lighthouse),
`ortografia.py` (hunspell), `transcribir.sh` (whisper). Fuera de `herramientas/` solo quedan cachés
ajenas a A-008: `~/.npm/_cacache` y `~/Library/Caches/empresaDeWebs/` (teselas de `mapa.py`).
