---
name: herramientas-comunes
description: "Mantiene las herramientas compartidas de la empresa en herramientas/ (capturas sin ventana, búsqueda, mapas de OpenStreetMap, generación de Word y de PDF) y el entorno .venv: que funcionen, estén documentadas y no rompan lo que ya usan otros. Úsala cuando haya que crear, arreglar o mejorar una herramienta común."
---

# herramientas-comunes

> **BORRADOR v0.1** · Escrito por Federico · **Dueño: Paco** · En revisión (ronda 1)

## Cuándo

Cuando un agente necesita una herramienta que no existe, una falla o se queda
corta. Los demás **piden**; Paco decide cómo y la mantiene.

## Lo que hay

| Herramienta | Qué hace | Limitaciones conocidas |
|---|---|---|
| `captura.sh` | Captura con Chrome sin ventana | Salen los avisos de cookies; no hace página completa |
| `buscar.sh` | Búsqueda en Bing sin ventana | Solo fiable con nombres exactos |
| `mapa.py` | Mapa del local y de competencia (teselas de OSM) | Descarga teselas con `curl` (el Python del sistema no tiene certificados) |
| `docx_util.py` | Piezas del Word: casillas, huecos, recuadros y tablas | Probado en LibreOffice, no en Word |
| `html_a_pdf.sh` + `informe.css` | De HTML a PDF con Chrome sin ventana | Las fuentes web se descargan al generarlo |
| `.venv` | python-docx y Pillow | No hay `requirements.txt` |

## Reglas

1. **Sin ventanas:** todo debe funcionar en segundo plano (Iván trabaja en la misma máquina).
2. **No instalar nada sin aprobación de Iván** (a través de Federico). Las
   propuestas de instalación dicen qué, para qué, dónde y cuánto cuesta.
3. **Nada que salte captchas, bloqueos o términos de uso.**
4. **Uso respetuoso de servicios gratuitos:** User-Agent identificable, pocas
   peticiones, reintentos con espera (Overpass, Nominatim, teselas de OSM).
5. **Compatibilidad:** si cambias una herramienta, los generadores de los
   clientes anteriores deben seguir funcionando.
6. **Cada herramienta, con su uso** explicado en la cabecera.
7. **Código y nombres en español.**

## Dudas abiertas (para la revisión)

- Capturas de página completa y sin avisos de cookies: ¿script propio de Playwright?
- ¿Lighthouse para medir las webs de la competencia?
- ¿Cómo comprobar que el Word funciona bien en Microsoft Word?
