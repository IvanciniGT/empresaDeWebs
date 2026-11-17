#!/bin/bash
# Captura una web con Chrome sin ventana: página completa y sin avisos de cookies.
# Se mantiene por compatibilidad; el trabajo lo hace captura.mjs (ver su cabecera).
#
# Uso: captura.sh URL fichero.png [ancho] [alto] [opciones de captura.mjs…]
#   ancho y alto son los de la ventana; la captura es de la página entera.
#   Con un ancho menor de 768 se captura como un móvil (antes salía una web de
#   ordenador estrecha, que no es lo que ve un móvil).
#   Ejemplos: captura.sh https://ejemplo.es web.png
#             captura.sh https://ejemplo.es web-movil.png 390
#             captura.sh https://ejemplo.es portada.png 1366 900 --solo-pantalla
set -euo pipefail
dir="$(cd "$(dirname "$0")" && pwd)"
if [[ $# -lt 2 ]]; then
  echo "Uso: captura.sh URL fichero.png [ancho] [alto] [--movil] [--solo-pantalla] [--con-avisos]" >&2
  exit 2
fi
url="$1"; salida="$2"; shift 2
opciones=()
if [[ $# -gt 0 && "$1" =~ ^[0-9]+$ ]]; then
  ancho="$1"; shift
  opciones+=(--ancho "$ancho")
  (( ancho < 768 )) && opciones+=(--movil)
fi
if [[ $# -gt 0 && "$1" =~ ^[0-9]+$ ]]; then opciones+=(--alto "$1"); shift; fi
exec node "$dir/captura.mjs" "$url" "$salida" ${opciones[@]+"${opciones[@]}"} "$@"
