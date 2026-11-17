---
name: estudio-competencia
description: "Analiza la competencia local y el SEO local de un cliente nuevo (censo de competidores en un radio, marketplaces, webs de 3 a 5 competidores representativos y búsquedas objetivo) y genera el informe PDF de mercado que se le envía para vendernos. Úsala cuando el expediente ya tiene los datos básicos del cliente."
---

# estudio-competencia

> **BORRADOR v0.1** · Escrito por Federico · **Dueño: Chema** · En revisión (ronda 1)

## Cuándo

En cuanto el expediente tiene la dirección y la actividad del cliente. Puede
ir en paralelo con el cuestionario.

## Entrada

- Expediente del cliente con coordenadas y actividad.
- Capturas de su presencia actual.

## Pasos

1. **Censo de competidores** en 1,5 km con Overpass (OpenStreetMap):
   `shop=hairdresser|barber` o la etiqueta que corresponda a la actividad.
   Contar por anillos (250 m, 500 m, 1 km y 1,5 km) y guardar los datos en
   `competencia/`.
2. **Mapa de competencia** con `herramientas/mapa.py` (modo puntos y radio).
3. **Marketplaces del sector** (Treatwell, Booksy…): quién aparece, con qué
   nota y qué precios. Los listados de Treatwell traen JSON-LD con los datos.
4. **Elegir 3–5 competidores representativos:** el que mejor lo hace en
   internet, uno con web propia, uno con la web rota o abandonada y el vecino
   más cercano.
5. **Analizar cada uno:** secciones, contenido, si publica precios, si tiene
   cita online o WhatsApp, cómo se ve en el móvil y su SEO básico (título,
   descripción, H1, datos estructurados). Capturas de ordenador y de móvil.
6. **Búsquedas objetivo:** qué buscaría un cliente nuevo de ese negocio.
7. **Informe PDF:** resumen en 30 segundos, situación actual, mercado, cómo
   lo hacen los demás, SEO local explicado sin jerga, propuesta y fuentes.
   HTML más `herramientas/informe.css`, convertido con
   `herramientas/html_a_pdf.sh`.

## Reglas

1. **Cifras solo con fuente.** Si no se ha medido (por ejemplo, volúmenes de
   búsqueda), se dice que no se ha medido.
2. **Nunca prometer posiciones** en Google (§10.3). El informe lo dice
   explícitamente.
3. **Sin jerga:** cada término técnico, explicado en una frase.
4. **Cuenta la parte buena y la mala:** primero lo que tiene, después lo que
   le falta.
5. **Las capturas de competidores** sirven para analizar, nunca para copiar.
6. **Atribución de OpenStreetMap** en mapas y fuentes.
7. **No se regala la estrategia:** el informe muestra el diagnóstico y la
   oportunidad; el cómo detallado es para cuando contrate.

## Salida

- `competencia/` con datos, capturas y mapa.
- `entregables/Informe de mercado y SEO local - <negocio>.pdf`.

## Comprobación final

- [ ] Cada cifra del informe sale de `competencia/` o del expediente.
- [ ] Ninguna promesa de resultados ni de plazos.
- [ ] Se ve bien impreso y en el móvil.

## Dudas abiertas (para la revisión)

- ¿Nueve páginas son demasiadas para un peluquero?
- ¿Dónde está la línea entre impresionar y regalar el trabajo?
- ¿Cómo estimar volúmenes de búsqueda sin herramientas de pago?
