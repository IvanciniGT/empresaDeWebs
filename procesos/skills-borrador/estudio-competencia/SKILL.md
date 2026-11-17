---
name: estudio-competencia
description: "Analiza la competencia local y el SEO local de un cliente nuevo (densidad de competidores con OpenStreetMap, competidores directos, los que Google muestra en sus búsquedas y un referente, búsquedas objetivo sin inventar volúmenes) y prepara el contenido del informe de venta de 2 páginas. Úsala cuando el expediente ya tiene la ficha de Google, la dirección y la actividad del cliente."
---

# estudio-competencia

> **BORRADOR v0.2 · revisado por Chema** · 2026-11-17 · **Dueño: Chema**
> Cambios respecto a v0.1 y motivos: [procesos/ronda-1/revision-chema.md](../../ronda-1/revision-chema.md) §4.

## Cuándo

Cuando el expediente (skill `investigar-cliente`) tiene la dirección, la actividad
y, si es posible, la ficha de Google del cliente. Puede ir en paralelo con el cuestionario.

## Entrada

- Expediente con coordenadas, actividad, categoría de Google y público.
- Capturas de su presencia actual.

## Pasos

### 1. Densidad (cuántos hay alrededor)

1. Overpass (OpenStreetMap) en 1,5 km con **solo la actividad del cliente**:
   para peluquerías, `shop=hairdresser` (incluye barberías con `hairdresser=barber`).
   **Nunca** `hairdresser_supply` (tiendas de productos) ni etiquetas parecidas.
2. Contar por anillos (250 m, 500 m, 1 km, 1,5 km) y, dentro de cada uno, cuántos son
   del **mismo público** (para el ejemplo: barberías y peluquerías de caballero).
3. **Comprobar una muestra:** 10 del anillo más cercano con el estado del negocio
   (Places `businessStatus`, si está aprobado, o la captura manual). Si hay cerrados,
   se dice «unas N, según OpenStreetMap; en una muestra de 10, X estaban cerrados».
4. Guardar en `competencia/` los datos de OSM y la consulta usada, con la fecha.
5. Mapa con `herramientas/mapa.py`. **Solo datos de OSM:** en la UE las condiciones de
   Google prohíben pintar sus datos en cualquier mapa.

### 2. Elegir competidores (máximo 4 en el informe)

| Tipo | Criterio | Cuántos |
|---|---|---|
| **Directos** | Mismo público y a menos de 500 m (a pie) | 1–2: el más cercano y el que mejor está en internet |
| **De búsqueda** | Los que devuelve Google para las 2–3 búsquedas objetivo principales desde la zona (Places Text Search o captura manual) | 1–2: los que el cliente tiene que adelantar |
| **Referente** | El mejor en digital de la ciudad con el mismo público | 0–1 |

- **Fuera** los de otro público (unisex, señora, estética) **salvo** que salgan en «de búsqueda».
- Un competidor con la web rota solo entra si es directo o de búsqueda: no se busca un «mal ejemplo» por buscarlo.

### 3. Analizar cada competidor

- Ficha de Google: categoría principal, nota y opiniones (fecha), fotos, si responde a reseñas.
- Web (si la tiene): secciones, precios, cita online o WhatsApp, cómo se ve en el móvil,
  título, descripción, H1 y datos estructurados (`LocalBusiness` o el tipo que toque).
  Rendimiento con PageSpeed Insights, si hay clave.
- Redes y marketplaces que **enlaza** o que hemos encontrado (con la fuente).
- Capturas de ordenador y de móvil, sin avisos de cookies.

### 4. Búsquedas objetivo (sin inventar volúmenes)

Se eligen **por intención**, a partir de fuentes:
1. Las **categorías de Google** de los competidores que mejor salen.
2. Lo que **escriben de verdad** los clientes: autocompletado oficial (API de Brave, si
   está aprobada) y palabras de las reseñas («pelar», «corte», «barba», «niño»).
3. Si hay cuenta de Google Ads: **intervalos** del Planificador de palabras clave, a
   nivel ciudad. Se citan como intervalo, nunca como cifra.
4. Google Trends (manual) solo para comparar dos palabras («barbería» frente a «peluquería»).

En el informe: «**prioridad estimada, no medida**». Volumen real, solo después de
contratar (búsquedas de la ficha de Google y Search Console).

### 5. Contenido del informe de venta

**Dos páginas más un anexo.** El formato es de Lola; el contenido, mío.

| Página | Contenido |
|---|---|
| **1 · Lo que ve hoy quien os busca** | Captura de Google con su nombre y con la búsqueda principal · 3 cifras comprobadas, con fecha · la conclusión en dos frases |
| **2 · Tres cosas que os están costando clientes** y **lo que haríamos** | Los tres fallos más concretos de **su** caso (por ejemplo, horarios distintos en internet o directorios que inventan servicios) · el *qué* haríamos, no el *cómo* · siguiente paso |
| **Anexo · Cómo lo hemos hecho** | Fuentes con fecha, límites y atribución de OSM. «Preparado con ayuda de asistentes de IA.» |

**No se regala:** la lista completa de búsquedas objetivo, las fichas de fallos de
cada competidor ni el plan paso a paso. Eso es el entregable de arranque cuando contrata.
Tampoco se da un curso de SEO: una frase de explicación por término, no una página.

## Reglas

1. **Cifras solo con fuente y fecha.** Lo que no se ha medido se dice que no se ha medido.
2. **Nunca prometer posiciones ni resultados** (§10.3), ni siquiera de forma encubierta
   («el primero que tenga web se queda con las búsquedas»).
3. **Nada de ausencias** («no tiene web»), salvo las comprobadas: «su dominio no responde».
4. **Ninguna generalización sin fuente** («los jóvenes buscan en el móvil», «quien publica
   precios recibe más llamadas»). O se cita un estudio con enlace, o fuera.
5. **El orden de un marketplace no es un ranking:** puede ser patrocinado.
6. **Sin jerga:** cada término técnico, explicado en una frase.
7. **Primero lo que tiene, después lo que le falta.**
8. **Las capturas de competidores** sirven para analizar, nunca para copiar.
9. **Atribución de OpenStreetMap** en mapas y fuentes. Del API de Google no se guarda ni se publica contenido (solo `place_id`).
10. **Dominio libre:** solo se dice si se ha comprobado en el registro (dominios.es para `.es`).
    No tener DNS no significa estar libre.

## Frases que se revisan antes de entregar

Buscar en el borrador y justificar o quitar: «el primero», «se queda con», «siempre»,
«nunca», «todos», «la mayoría», «suele», «más llamadas», «más clientes», «garantiz»,
«no tiene», «tampoco tiene», «céntric», «el que mejor», «la primera del listado».

## Salida

- `competencia/` con la consulta de OSM, los datos, el mapa, las capturas y una tabla de
  competidores elegidos con el tipo y el motivo.
- Contenido del informe (HTML o Markdown) para que Lola lo maquete y Paco lo genere.

## Comprobación final

- [ ] La consulta del censo usa solo la actividad del cliente (sin `hairdresser_supply`).
- [ ] Cada cifra del informe sale de `competencia/` o del expediente y lleva fecha.
- [ ] Cada competidor tiene tipo (directo, de búsqueda o referente) y motivo.
- [ ] Ninguna frase de la lista de revisión queda sin justificar.
- [ ] Las búsquedas objetivo van como «prioridad estimada, no medida».
- [ ] El informe cabe en 2 páginas más el anexo.

## Dudas abiertas

- Cobertura real de la API de Brave para negocios pequeños de España: hay que probarla.
- Si Places Text Search se parece lo suficiente al «pack local» de Google: comparar con la captura manual en los dos primeros clientes.
- Formato del informe para el móvil: lo decide Lola.
