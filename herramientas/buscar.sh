#!/bin/bash
# Busca en Bing con Chrome headless y devuelve «título | url» de los resultados.
# web_fetch no sirve con buscadores: devuelven páginas de bloqueo o resultados vacíos.
# Uso: buscar.sh "consulta"
set -euo pipefail
consulta="$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote_plus(sys.argv[1]))' "$1")"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
perfil="$(mktemp -d)"
trap 'rm -rf "$perfil"' EXIT
"$chrome" --headless=new --disable-gpu --no-first-run --user-data-dir="$perfil" --lang=es-ES \
  --virtual-time-budget=6000 --dump-dom "https://www.bing.com/search?q=${consulta}&setlang=es&cc=ES" 2>/dev/null |
python3 -c '
import sys, re, html, base64, urllib.parse
dom = sys.stdin.read()
for m in re.finditer(r"<h2[^>]*>\s*<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", dom, re.S):
    url, titulo = html.unescape(m.group(1)), re.sub("<[^>]+>", "", html.unescape(m.group(2)))
    # Bing envuelve los enlaces en /ck/a?...&u=a1<base64>
    u = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get("u", [""])[0]
    if u.startswith("a1"):
        b = u[2:]; b += "=" * (-len(b) % 4)
        try: url = base64.urlsafe_b64decode(b).decode()
        except Exception: pass
    if "bing.com/aclick" in url: continue
    print(titulo.strip(), "|", url)
'
