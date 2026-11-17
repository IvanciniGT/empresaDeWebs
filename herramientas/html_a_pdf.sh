#!/bin/bash
# Convierte un HTML en PDF con Chrome sin abrir ventana.
# Se mantiene por compatibilidad (lo llaman los generar_*.py); el trabajo lo hace
# html_a_pdf.mjs, que además avisa de imágenes y fuentes que no han cargado.
# Uso: html_a_pdf.sh entrada.html salida.pdf [--estricto]
set -euo pipefail
dir="$(cd "$(dirname "$0")" && pwd)"
node "$dir/html_a_pdf.mjs" "$@" >/dev/null
ls -la "$2"
