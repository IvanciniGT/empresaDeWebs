#!/bin/bash
# Quita lo que instaló instalar.sh (A-008). Todo está dentro de herramientas/.
#
# Uso:  herramientas/desinstalar.sh [--simular] componente…
#       componentes: fuentes iconos lighthouse hunspell whisper descargas todo
#       --simular: dice qué borraría, sin borrar nada.
#
# Fuera de herramientas/ quedan dos cachés que no son de A-008 y no se tocan:
#   ~/.npm/_cacache                         caché común de npm (npm cache clean --force)
#   ~/Library/Caches/empresaDeWebs/         teselas de mapa.py (se puede borrar sin más)
# Detalle de cada componente: herramientas/INSTALACIONES.md
set -euo pipefail
H="$(cd "$(dirname "$0")" && pwd)"
simular=0
[[ "${1:-}" == "--simular" ]] && { simular=1; shift; }
[[ $# -gt 0 ]] || { echo "Uso: desinstalar.sh [--simular] fuentes|iconos|lighthouse|hunspell|whisper|descargas|todo …" >&2; exit 2; }

borrar() {
  for ruta in "$@"; do
    [[ -e "$ruta" ]] || continue
    if [[ $simular -eq 1 ]]; then echo "   borraría ${ruta#"$H"/} ($(du -sh "$ruta" | cut -f1))"
    else rm -rf "$ruta"; echo "   borrado ${ruta#"$H"/}"; fi
  done
}

for c in "$@"; do
  case "$c" in
    fuentes)
      echo "== fuentes (van en git: después, git rm -r herramientas/fuentes/inter herramientas/fuentes/fraunces)"
      borrar "$H/fuentes/inter" "$H/fuentes/fraunces" ;;
    iconos)
      echo "== iconos (van en git: después, git rm -r herramientas/iconos)"
      borrar "$H/iconos" ;;
    lighthouse)
      echo "== Lighthouse (package.json y package-lock.json se quedan: son la receta)"
      borrar "$H/node_modules" ;;
    hunspell)
      echo "== hunspell y diccionario"
      borrar "$H/vendor/hunspell" "$H/vendor/diccionarios" ;;
    whisper)
      echo "== whisper.cpp y modelo"
      borrar "$H/vendor/whisper" "$H/modelos" ;;
    descargas)
      echo "== copias de lo descargado (instalar.sh vuelve a bajarlo si hace falta)"
      borrar "$H/vendor/descargas" "$H/vendor/compilar" ;;
    todo)
      "$0" ${simular:+$([[ $simular -eq 1 ]] && echo --simular)} fuentes iconos lighthouse hunspell whisper descargas
      [[ $simular -eq 1 ]] || rmdir "$H/vendor" 2>/dev/null || true ;;
    *) echo "Componente desconocido: $c" >&2; exit 2 ;;
  esac
done
