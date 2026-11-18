#!/bin/bash
# Instala lo aprobado por Iván en A-008, DENTRO del proyecto (herramientas/),
# sin tocar el sistema: nada en /usr/local, nada de brew, nada global de npm.
#
# Uso:  herramientas/instalar.sh [componente…]
#       componentes: fuentes iconos lighthouse hunspell whisper   (sin nada: todos)
#
# Se puede repetir: lo que ya está instalado y bien, no se vuelve a hacer.
# Cada descarga se comprueba con su suma SHA-256: si no coincide, se para.
# Qué instala, dónde, cuánto ocupa y cómo se quita: herramientas/INSTALACIONES.md
# Para quitarlo: herramientas/desinstalar.sh [componente…]
set -euo pipefail

H="$(cd "$(dirname "$0")" && pwd)"
VENDOR="$H/vendor"
DESCARGAS="$VENDOR/descargas"
AGENTE="empresaDeWebs/0.3 (+mailto:ivan.osuna.ayuste@gmail.com)"
mkdir -p "$DESCARGAS"

paso() { printf '\n== %s\n' "$*"; }

# descargar URL FICHERO SHA256
descargar() {
  local url="$1" destino="$DESCARGAS/$2" suma="$3"
  if [[ ! -s "$destino" ]]; then
    echo "   descargando $url"
    curl -sSfL --retry 3 -A "$AGENTE" -o "$destino.parcial" "$url"
    mv "$destino.parcial" "$destino"
  fi
  if [[ "$(shasum -a 256 "$destino" | cut -d' ' -f1)" != "$suma" ]]; then
    echo "!! La suma SHA-256 de $2 no coincide. No se instala nada de esto." >&2
    echo "   Puede ser una descarga corrupta o un fichero cambiado en origen: bórralo de $DESCARGAS y repite." >&2
    exit 1
  fi
}

instalar_fuentes() {
  paso "Fuentes Inter 4.1 y Fraunces 1.000 (SIL OFL 1.1) → herramientas/fuentes/"
  descargar https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip \
    Inter-4.1.zip 9883fdd4a49d4fb66bd8177ba6625ef9a64aa45899767dde3d36aa425756b11e
  descargar https://github.com/undercasetype/Fraunces/releases/download/1.000/UnderCaseType_Fraunces_1.000.zip \
    Fraunces-1.000.zip 8d8b81dfaeb89433f5c908e1d8d0a4b202bd627bd80d4cd5ff56f311fdcad19f
  # El zip de Fraunces no trae la licencia: se toma la del repositorio, en la misma versión.
  descargar https://raw.githubusercontent.com/undercasetype/Fraunces/1.000/OFL.txt \
    Fraunces-OFL.txt bdf4c22802eaf804f998195871c6b8938aac2ac14b2d78a8bd66a6f1eced833b
  local tmp; tmp="$(mktemp -d)"
  rm -rf "$H/fuentes/inter" "$H/fuentes/fraunces"
  mkdir -p "$H/fuentes/inter" "$H/fuentes/fraunces"
  unzip -q -j "$DESCARGAS/Inter-4.1.zip" 'extras/ttf/Inter-*.ttf' LICENSE.txt -d "$tmp/inter"
  mv "$tmp/inter/"*.ttf "$H/fuentes/inter/"
  mv "$tmp/inter/LICENSE.txt" "$H/fuentes/inter/OFL.txt"
  # Solo la versión normal (ni Soft ni SuperSoft), en dos tamaños ópticos:
  # 9pt para texto y 72pt para títulos. Todos los pesos.
  unzip -q -j "$DESCARGAS/Fraunces-1.000.zip" '*/static/ttf/Fraunces9pt-*.ttf' '*/static/ttf/Fraunces72pt-*.ttf' -d "$H/fuentes/fraunces"
  cp "$DESCARGAS/Fraunces-OFL.txt" "$H/fuentes/fraunces/OFL.txt"
  rm -rf "$tmp"
  echo "   $(ls "$H/fuentes/inter"/*.ttf | wc -l | tr -d ' ') de Inter y $(ls "$H/fuentes/fraunces"/*.ttf | wc -l | tr -d ' ') de Fraunces"
}

instalar_iconos() {
  paso "Iconos Lucide 1.75.0 (ISC; algunos, MIT de Feather) → herramientas/iconos/"
  descargar https://github.com/lucide-icons/lucide/releases/download/1.75.0/lucide-icons-1.75.0.zip \
    lucide-icons-1.75.0.zip 412abe5b2420afbee2c797cacf9398bbc5e87e97f9a8bcb19b2d33c55b2fbbf3
  descargar https://raw.githubusercontent.com/lucide-icons/lucide/1.75.0/LICENSE \
    lucide-LICENSE.txt b495047bd93a9b06913511076f504daba17d5bbeb3e0650f3bb53a4220329c57
  rm -rf "$H/iconos"
  mkdir -p "$H/iconos"
  # Solo los SVG: los .json de cada icono son metadatos para su web.
  unzip -q -j "$DESCARGAS/lucide-icons-1.75.0.zip" 'icons/*.svg' -d "$H/iconos"
  cp "$DESCARGAS/lucide-LICENSE.txt" "$H/iconos/LICENSE.txt"
  echo "   $(ls "$H/iconos"/*.svg | wc -l | tr -d ' ') iconos"
}

instalar_lighthouse() {
  paso "Lighthouse 13.6.0 (Apache-2.0) → herramientas/node_modules/"
  # package.json y package-lock.json fijan la versión exacta de todo el árbol.
  (cd "$H" && npm ci --no-audit --no-fund --loglevel=error)
  echo "   $("$H/node_modules/.bin/lighthouse" --version)"
}

instalar_hunspell() {
  paso "hunspell 1.7.6 (MPL/GPL/LGPL) → herramientas/vendor/hunspell/ y diccionario es_ES"
  descargar https://github.com/hunspell/hunspell/releases/download/v1.7.6/hunspell-1.7.6.tar.gz \
    hunspell-1.7.6.tar.gz 9c650ace31d4d8cc1da925a9507c3de1d50f1a54857af2f72429f517d5d53467
  if [[ ! -x "$VENDOR/hunspell/bin/hunspell" ]]; then
    local fuente="$VENDOR/compilar/hunspell-1.7.6"
    rm -rf "$fuente"; mkdir -p "$VENDOR/compilar"
    tar -xzf "$DESCARGAS/hunspell-1.7.6.tar.gz" -C "$VENDOR/compilar"
    (cd "$fuente" && ./configure --quiet --prefix="$VENDOR/hunspell" --disable-nls --without-ui --without-readline \
      && make -s -j"$(sysctl -n hw.ncpu)" && make -s install) >"$VENDOR/compilar/hunspell.log" 2>&1 \
      || { echo "!! Falla la compilación de hunspell: ver $VENDOR/compilar/hunspell.log" >&2; exit 1; }
    rm -rf "$fuente"
  fi
  # Diccionario: el de RLA-ES que trae LibreOffice (ya está en la máquina). Se
  # copia para no depender de dónde ni de qué versión de LibreOffice haya.
  local lo="/Applications/LibreOffice.app/Contents/Resources/extensions/dict-es"
  if [[ ! -f "$lo/es_ES.dic" ]]; then
    echo "!! No encuentro el diccionario de LibreOffice en $lo" >&2; exit 1
  fi
  mkdir -p "$VENDOR/diccionarios"
  cp "$lo/es_ES.aff" "$lo/es_ES.dic" "$VENDOR/diccionarios/"
  cp "$lo/LICENSE.md" "$VENDOR/diccionarios/LICENSE-es_ES.md"
  cp "$lo/README_hunspell_es.txt" "$VENDOR/diccionarios/README-es_ES.txt"
  echo "   $("$VENDOR/hunspell/bin/hunspell" -v | head -1); diccionario es_ES de LibreOffice $(/usr/local/bin/soffice --version 2>/dev/null | awk '{print $2}')"
}

instalar_whisper() {
  paso "whisper.cpp 1.9.5 (MIT) → herramientas/vendor/whisper/ y modelo large-v3-turbo-q5_0 → herramientas/modelos/"
  descargar https://github.com/ggml-org/whisper.cpp/archive/refs/tags/v1.9.5.tar.gz \
    whisper.cpp-1.9.5.tar.gz ff1a9053feb509ff9d7729703355541ae9690073a6b1c40eb692c962e0dc1720
  if [[ ! -x "$VENDOR/whisper/bin/whisper-cli" ]]; then
    local fuente="$VENDOR/compilar/whisper.cpp-1.9.5"
    rm -rf "$fuente"; mkdir -p "$VENDOR/compilar"
    tar -xzf "$DESCARGAS/whisper.cpp-1.9.5.tar.gz" -C "$VENDOR/compilar"
    # Estático (sin bibliotecas sueltas) y solo con la CPU: Metal está pensado
    # para los Mac con chip de Apple y este es Intel.
    (cd "$fuente" \
      && cmake -B build -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DGGML_METAL=OFF \
               -DWHISPER_BUILD_TESTS=OFF -DWHISPER_BUILD_SERVER=OFF \
      && cmake --build build -j"$(sysctl -n hw.ncpu)" --config Release --target whisper-cli) \
      >"$VENDOR/compilar/whisper.log" 2>&1 \
      || { echo "!! Falla la compilación de whisper.cpp: ver $VENDOR/compilar/whisper.log" >&2; exit 1; }
    mkdir -p "$VENDOR/whisper/bin"
    cp "$fuente/build/bin/whisper-cli" "$VENDOR/whisper/bin/"
    cp "$fuente/LICENSE" "$VENDOR/whisper/LICENSE"
    rm -rf "$fuente"
  fi
  mkdir -p "$H/modelos"
  if [[ ! -s "$H/modelos/ggml-large-v3-turbo-q5_0.bin" ]]; then
    DESCARGAS="$H/modelos" descargar \
      https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q5_0.bin \
      ggml-large-v3-turbo-q5_0.bin 394221709cd5ad1f40c46e6031ca61bce88931e6e088c188294c6d5a55ffa7e2
  fi
  echo "   whisper-cli y modelo listos ($(du -h "$H/modelos/ggml-large-v3-turbo-q5_0.bin" | cut -f1))"
}

componentes=("$@")
[[ ${#componentes[@]} -eq 0 ]] && componentes=(fuentes iconos lighthouse hunspell whisper)
for c in "${componentes[@]}"; do
  case "$c" in
    fuentes|iconos|lighthouse|hunspell|whisper) "instalar_$c" ;;
    *) echo "Componente desconocido: $c (fuentes iconos lighthouse hunspell whisper)" >&2; exit 2 ;;
  esac
done
rmdir "$VENDOR/compilar" 2>/dev/null || true
paso "Hecho. Comprobar con: node herramientas/pruebas/probar.mjs instalado"
