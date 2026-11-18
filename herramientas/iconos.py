"""Iconos Lucide (ISC) de herramientas/iconos/ para meterlos en línea en el HTML
de los PDF, en vez de copiar sus trazos a mano (estilo-documentos v0.3).

  sys.path.insert(0, "herramientas"); import iconos
  f'<span class="estado si">{iconos.svg("check")}Bien</span>'

Sale sin ancho ni alto ni colores propios: los pone estilo.css (`.estado svg`,
`.haremos svg`) y el trazo toma el color del texto. Es decorativo
(aria-hidden): la palabra de al lado es la que informa.
Solo biblioteca estándar.
"""
import re
from functools import lru_cache
from pathlib import Path

CARPETA = Path(__file__).resolve().parent / "iconos"


@lru_cache(maxsize=None)
def svg(nombre):
    ruta = CARPETA / f"{nombre}.svg"
    if not ruta.exists():
        raise SystemExit(f"No existe el icono «{nombre}» en {CARPETA} (herramientas/instalar.sh iconos)")
    interior = re.search(r"<svg[^>]*>(.*)</svg>", ruta.read_text(encoding="utf-8"), re.S).group(1)
    interior = re.sub(r"\s+", " ", interior).strip()
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{interior}</svg>'
