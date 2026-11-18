#!/bin/bash
# Transcribe notas de voz EN ESTA MÁQUINA, con whisper.cpp (A-008): el audio no
# sale a ningún servicio de fuera (§12).
#
# Uso:  herramientas/transcribir.sh AUDIO… [--salida CARPETA] [--permitir-en-git]
#   Acepta lo que lea macOS: .opus/.ogg (notas de voz de WhatsApp), .m4a, .mp3, .wav, .caf…
#   Deja AUDIO.txt al lado de cada audio (o en CARPETA).
#
# Un audio de un cliente es un dato personal: si la transcripción iba a quedar en
# una carpeta que entra en git (el repositorio es público, A-013), no se escribe.
# Lo normal es trabajar en clientes/<negocio>/privado/.
#
# La transcripción es automática y se equivoca, sobre todo con números, nombres y
# precios: lo dice la cabecera del fichero. Comprobar con el audio antes de usarla.
set -euo pipefail
H="$(cd "$(dirname "$0")" && pwd)"
CLI="$H/vendor/whisper/bin/whisper-cli"
MODELO="$H/modelos/ggml-large-v3-turbo-q5_0.bin"
[[ -x "$CLI" && -s "$MODELO" ]] || { echo "Falta whisper.cpp o el modelo: herramientas/instalar.sh whisper" >&2; exit 3; }

audios=(); salida=""; permitir=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --salida) salida="$2"; shift 2 ;;
    --permitir-en-git) permitir=1; shift ;;
    -*) echo "Opción desconocida: $1" >&2; exit 2 ;;
    *) audios+=("$1"); shift ;;
  esac
done
[[ ${#audios[@]} -gt 0 ]] || { echo "Uso: transcribir.sh AUDIO… [--salida CARPETA] [--permitir-en-git]" >&2; exit 2; }

# ¿Entraría en git? Sí si está dentro de un repositorio y no lo excluye ningún .gitignore.
iria_a_git() {
  local dir; dir="$(dirname "$1")"
  [[ -d "$dir" ]] || return 1
  git -C "$dir" rev-parse --is-inside-work-tree >/dev/null 2>&1 || return 1
  ! git -C "$dir" check-ignore -q "$(cd "$dir" && pwd)/$(basename "$1")"
}

hilos=$(( $(sysctl -n hw.physicalcpu) < 16 ? $(sysctl -n hw.physicalcpu) : 16 ))
temporal="$(mktemp -d)"; trap 'rm -rf "$temporal"' EXIT
fallos=0
for audio in "${audios[@]}"; do
  if [[ ! -f "$audio" ]]; then echo "✗ No existe: $audio" >&2; fallos=$((fallos + 1)); continue; fi
  nombre="$(basename "$audio")"
  if [[ -n "$salida" ]]; then mkdir -p "$salida"; txt="$salida/$nombre.txt"; else txt="$audio.txt"; fi
  if [[ $permitir -eq 0 ]] && iria_a_git "$txt"; then
    echo "✗ $txt entraría en git (y el repositorio es público). Usa clientes/<negocio>/privado/ o --salida a una carpeta excluida." >&2
    fallos=$((fallos + 1)); continue
  fi
  # whisper.cpp necesita WAV de 16 kHz y un canal; afconvert (de macOS) lee el Ogg/Opus de WhatsApp.
  if ! afconvert -f WAVE -d LEI16@16000 -c 1 "$audio" "$temporal/audio.wav" 2>"$temporal/afconvert.log"; then
    echo "✗ macOS no sabe leer $audio: $(cat "$temporal/afconvert.log")" >&2; fallos=$((fallos + 1)); continue
  fi
  inicio=$(date +%s)
  "$CLI" -m "$MODELO" -l es -t "$hilos" -nt -np -f "$temporal/audio.wav" 2>"$temporal/whisper.log" \
    | sed -e 's/^[[:space:]]*//' -e '/^$/d' >"$temporal/texto.txt" \
    || { echo "✗ whisper ha fallado con $audio: ver el registro" >&2; tail -3 "$temporal/whisper.log" >&2; fallos=$((fallos + 1)); continue; }
  {
    echo "# Transcripción automática de «$nombre»"
    echo "# $(date '+%Y-%m-%d %H:%M') · whisper.cpp 1.9.5, modelo large-v3-turbo-q5_0, en local."
    echo "# Puede tener errores, sobre todo en números, nombres y precios: comprobar con el audio."
    echo
    printf '%s\n' "$(cat "$temporal/texto.txt")"
  } >"$txt"
  echo "✓ $txt  ($(( $(date +%s) - inicio )) s)"
done
exit $(( fallos > 0 ))
