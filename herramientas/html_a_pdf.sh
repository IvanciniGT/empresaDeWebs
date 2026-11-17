#!/bin/bash
# Convierte un HTML en PDF con Chrome sin abrir ventana.
# Maquetamos en HTML+CSS porque da un control del diseño que no da ningún
# generador de PDF de Python, y Chrome ya está instalado.
# Uso: html_a_pdf.sh entrada.html salida.pdf
set -euo pipefail
entrada="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
salida="$2"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
perfil="$(mktemp -d)"
trap 'rm -rf "$perfil"' EXIT
"$chrome" --headless=new --disable-gpu --no-first-run --user-data-dir="$perfil" \
  --allow-file-access-from-files --no-pdf-header-footer --virtual-time-budget=5000 \
  --print-to-pdf="$salida" "file://$entrada" >/dev/null 2>&1
ls -la "$salida"
