#!/bin/bash
# RETIRADA (Paco, ronda 1, 2026-11-17). No se usa.
#
# Buscaba en Bing con Chrome sin ventana y leía la página de resultados. El
# robots.txt de Bing prohíbe /search a cualquier robot («User-agent: *» +
# «Disallow: /search»), así que incumple la regla 3 de herramientas-comunes
# («nada que salte bloqueos o términos de uso»), la misma que exigimos a
# extraer_web.mjs. Además, con búsquedas genéricas devolvía resultados al azar.
#
# Alternativa propuesta a Iván (procesos/ronda-1/revision-paco.md §6): una API de
# búsqueda con crédito prepago. Mientras no decida, la fase de recopilación usa
# fuentes abiertas y lo que nos diga el cliente.
#
# La versión anterior está en el historial de git (commit e38b879).
echo "buscar.sh está retirado: Bing prohíbe en su robots.txt que un programa lea sus resultados." >&2
echo "Ver procesos/ronda-1/revision-paco.md (alternativas pendientes de decisión de Iván)." >&2
exit 3
