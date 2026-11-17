#!/bin/bash
# Captura una web con Chrome sin abrir ventana (headless), para no interrumpir a Iván.
# Uso: captura.sh URL fichero.png [ancho] [alto]
# Chrome headless no hace capturas de página completa: un alto grande se acerca bastante.
set -euo pipefail
url="$1"; salida="$2"; ancho="${3:-1366}"; alto="${4:-2400}"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
perfil="$(mktemp -d)"
trap 'rm -rf "$perfil"' EXIT
"$chrome" --headless=new --disable-gpu --hide-scrollbars --no-first-run \
  --user-data-dir="$perfil" --lang=es-ES \
  --virtual-time-budget=8000 --window-size="${ancho},${alto}" \
  --screenshot="$salida" "$url" >/dev/null 2>&1
ls -la "$salida"
