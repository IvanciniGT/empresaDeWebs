#!/bin/bash
# Comprueba que las pruebas sirven: estropea a propósito cada arreglo, en una
# copia de herramientas/, y mira que la prueba que lo vigila FALLA.
# Una prueba que sigue pasando con el código roto da una confianza falsa.
#
# Uso (desde la raíz del repositorio):  herramientas/pruebas/mutaciones.sh
# Tarda unos 15 minutos (cada extracción completa son ~60 s).
# Al añadir una prueba nueva, añade aquí su mutación.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
export PYTHON="${PYTHON:-$REPO/.venv/bin/python}"
TRABAJO="$(mktemp -d)"
trap 'rm -rf "$TRABAJO"' EXIT
fallidas=0

mutar() {  # descripción  fichero  texto_original  texto_estropeado  filtro_de_pruebas
  local nombre="$1" fichero="$2" viejo="$3" nuevo="$4" filtro="$5"
  local copia="$TRABAJO/mutante"; rm -rf "$copia"; mkdir -p "$copia"; cp -R "$REPO/herramientas" "$copia/"
  if ! python3 - "$copia/herramientas/$fichero" "$viejo" "$nuevo" <<'PY'
import sys
f, viejo, nuevo = sys.argv[1:]
s = open(f, encoding="utf-8").read()
if viejo not in s:
    sys.exit(1)
open(f, "w", encoding="utf-8").write(s.replace(viejo, nuevo, 1))
PY
  then echo "!! $nombre: no encuentro el texto que hay que estropear en $fichero"; fallidas=$((fallidas + 1)); return; fi
  local salida; salida=$(node "$copia/herramientas/pruebas/probar.mjs" "$filtro" 2>&1)
  if grep -q "^✗" <<<"$salida"; then
    echo "✓ $nombre → la prueba falla, como debe"
    grep -A1 "^✗" <<<"$salida" | sed 's/^/      /' | head -2
  else
    echo "✗ $nombre → la prueba NO lo detecta"; fallidas=$((fallidas + 1))
  fi
}

mutar "sin respetar robots.txt" extraer_web.mjs "if (!permitido(url)) {" "if (false) {" "no pide nunca"
mutar "sin limitarse al sitio" extraer_web.mjs "if (!esDelSitio(n) || EXT_NO_PAGINA.test(pathname)) return;" "if (EXT_NO_PAGINA.test(pathname)) return;" "no sale del sitio"
mutar "sin la regla más larga de robots" robots.mjs "if (!mejor || r.patron.length > mejor.patron.length" "if (!mejor" "robots: gana"
mutar "sin ocultar avisos de cookies" chrome.mjs "el.style.setProperty('display', 'none', 'important');" "void 0;" "captura: ordenador"
mutar "sin página completa" chrome.mjs "(completa ? m.cssContentSize.height : m.cssLayoutViewport.clientHeight)" "m.cssLayoutViewport.clientHeight" "captura: ordenador"
mutar "sin bajar por la página (perezosas)" extraer_web.mjs "      await ordenador.recorrerHastaElFinal();" "" "tamaño original"
mutar "sin traer la pestaña al frente" chrome.mjs "alFrente() { return this.enviar('Page.bringToFront'); }" "alFrente() { return Promise.resolve(); }" "tamaño original"
mutar "sin buscar el original de WordPress" extraer_web.mjs "if (/\/wp-content\/uploads\//.test(abs))" "if (false)" "tamaño original"
mutar "sin avisos de imágenes sin dibujar" html_a_pdf.mjs "for (const i of sinCargar.imagenes) avisos.push" "for (const i of []) avisos.push" "html_a_pdf: avisa"
mutar "sin avisos de fallos de red" html_a_pdf.mjs "const avisos = pestana.registro.fallos.map" "const avisos = [].map" "html_a_pdf: avisa"
mutar "sin avisos de fuentes" html_a_pdf.mjs "for (const f of new Set(sinCargar.fuentes))" "for (const f of [])" "html_a_pdf: avisa"
mutar "sin caché de teselas" mapa.py "CADUCIDAD_S = 7 * 24 * 3600" "CADUCIDAD_S = 0" "mapa"
mutar "sin petición condicional" mapa.py 'orden += ["-z", str(fichero)]' 'pass' "mapa"
mutar "Word sin ordenar el XML de las tablas" docx_util.py "_colocar(tblPr, bordes)" "tblPr.append(bordes)" "docx_util: el Word"
mutar "sin arreglar las propiedades del Word" docx_util.py "    _propiedades(doc, titulo, autor, idioma)" "    pass" "docx_util: el Word"
mutar "sin texto alternativo en imagen()" docx_util.py 'docpr.set("descr", alternativo)' 'pass' "docx_util: el Word"
mutar "guardar() sin mirar si está abierto" docx_util.py "    bloqueo = documento_abierto(ruta)" "    bloqueo = None" "docx_util: no guarda"

# Ronda 1b
mutar "puntos encima de las etiquetas del mapa" mapa.py "        dibujo.text((c + 8, c - r + 6), etiqueta, fill=(*TINTA, 255), font=fuente)" "        dibujo.text((c + 8, c - r + 6), etiqueta, fill=(*TINTA, 255), font=fuente)
        [_forma(dibujo, *a_px(dx, dy), barberia=bool(d)) for dx, dy, d, _n in puntos]" "mapa: los puntos"
mutar "alt vacío tratado como si faltara" html_a_pdf.mjs "filter((i) => !i.hasAttribute('alt'))" "filter((i) => !i.getAttribute('alt'))" "html_a_pdf: avisa"
mutar "captura sin recorte de zona" captura.mjs "const captura = o.elemento || o.recorte" "const captura = false" "captura: --elemento"
mutar "instalar.sh sin comprobar la suma" instalar.sh 'if [[ "$(shasum -a 256 "$destino" | cut -d'"'"' '"'"' -f1)" != "$suma" ]]; then' 'if false; then' "instalado: si una descarga"
mutar "ortografía sin la lista de la empresa" ortografia.py "    if EMPRESA.exists():" "    if False:" "ortografía"
mutar "ortografía sin filtrar siglas" ortografia.py ' and not re.fullmatch(r"[A-ZÁÉÍÓÚÑ]{2,5}", p)' '' "ortografía"
mutar "transcribir sin mirar si va a git" transcribir.sh 'if [[ $permitir -eq 0 ]] && iria_a_git "$txt"; then' 'if false; then' "transcribir: no deja"
mutar "medir sin bloquear medidores" medir_web.mjs "blockedUrlPatterns: conMedidores ? [] : RASTREADORES," "blockedUrlPatterns: []," "medir"
mutar "medir sin identificarse" medir_web.mjs '} ${FIRMA}`,' '}`,' "medir"
mutar "overpass repite consultas guardadas" overpass.mjs "if (!repetir && existsSync(rutas.meta)" "if (false && existsSync(rutas.meta)" "overpass: guarda"
mutar "overpass sin esperar ante un 429" overpass.mjs "if (![429, 504].includes(respuesta.status) || intento > REINTENTOS) break;" "break;" "overpass: guarda"
mutar "overpass envía datos personales" overpass.mjs "throw new Error('La consulta parece llevar un correo" "void ('La consulta parece llevar un correo" "overpass: guarda"
mutar "overpass contra el servidor principal" overpass.mjs "https://overpass.private.coffee/api/interpreter" "https://overpass-api.de/api/interpreter" "overpass: por defecto"
mutar "hueco sin control con ID" docx_util.py "        _control_de_texto(q, id)" "        pass" "cuestionario: cada respuesta"
mutar "lector toma la ayuda por respuesta" leer_cuestionario.py 'ayuda = pr.find(f"{W}showingPlcHdr") is not None' 'ayuda = False' "cuestionario: sin contestar"
mutar "lector sin ver lo escrito fuera" leer_cuestionario.py "cambios += [t for t in despues[j1:j2] if t]" "pass" "cuestionario: cada respuesta"
mutar "lector sin rangos del catálogo" leer_cuestionario.py "range(desde, int(hasta or desde) + 1)" "range(desde, desde + 1)" "cuestionario: lee los dos"
mutar "lector escribe en git" leer_cuestionario.py "if not permitir and iria_a_git(" "if False and iria_a_git(" "cuestionario: no escribe"

echo
if (( fallidas )); then echo "$fallidas mutaciones sin detectar"; exit 1; fi
echo "Todas las mutaciones se detectan"
