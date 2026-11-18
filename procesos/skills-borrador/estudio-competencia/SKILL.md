---
name: estudio-competencia
description: "Analiza la competencia local y el SEO local de un cliente nuevo (censo de OpenStreetMap calculado por script, competidores directos, los que salen en Google en la captura de Iván y un referente, búsquedas objetivo sin inventar volúmenes) y escribe el contenido del informe de venta: 2 páginas más un anexo, en A5. Úsala cuando el expediente ya tiene la dirección, la actividad y el nodo de OSM del cliente."
---

# estudio-competencia

> **BORRADOR v0.3 · revisado por Chema** · 2026-11-18 · **Dueño: Chema**
> v0.2 → v0.3: decisiones de Iván A-001, A-005 y A-015; cifras por script; peticiones de
> Puri, Lola, Reme y Menchu. Detalle en [revision-chema.md](../../ronda-1/revision-chema.md) §8.

## Cuándo

Cuando el expediente (`investigar-cliente`) tiene la dirección, la actividad y el
nodo de OpenStreetMap del cliente. Las búsquedas objetivo (paso 4) hacen falta
**antes** del guion de captura de Iván, porque van dentro.

## Entrada

- Expediente con coordenadas, id de OSM, actividad y público.
- Capturas de Google de Iván (`privado/capturas-google/`), para los pasos 3 y 5.

## Pasos

### 1. Censo: las cifras salen de un script, nunca del teclado

```
S=procesos/skills-borrador/estudio-competencia/censo.py
python3 $S consulta LAT LON > clientes/<negocio>/competencia/overpass-consulta.overpassql
#   → se lanza en la instancia de Overpass que fije herramientas-comunes (A-015)
#     y la respuesta se guarda tal cual en competencia/overpass-respuesta.json
python3 $S cifras competencia/overpass-respuesta.json LAT LON --cliente node/<id> > competencia/cifras.json
python3 $S mapa competencia/cifras.json > competencia/puntos-mapa.json
.venv/bin/python herramientas/mapa.py LAT LON competencia/mapa-competencia.png 15 competencia/puntos-mapa.json 1500
```

- **Solo la actividad del cliente**, con etiquetas exactas: para peluquerías,
  `shop=hairdresser` y `shop=barber`. Nunca `hairdresser_supply` ni expresiones
  regulares (`~`), que la cuelan.
- **Instancia de Overpass:** la que fije Paco en `herramientas-comunes` después de
  leer sus condiciones (A-015). Si todavía no está fijada, **no se lanza**: se avisa a Federico.
- `cifras.json` da los anillos (250 m, 500 m, 1 km y 1,5 km), el total y el
  **mismo público**, separando lo que dice la etiqueta de OSM de lo que solo dice el
  nombre. Da también los tres más cercanos (en total y del mismo público), los
  excluidos con su motivo, los duplicados, la fecha de los datos de OSM y la huella
  de la respuesta.
- **El mapa y la tabla salen del mismo cálculo.** En la ronda 1 iban por separado y
  diferían hasta un 1,5 %.
- `cifras.json` **no se edita.** Si algo está mal, se corrige la consulta o los datos y se regenera.
- Las cifras se dicen como son: «unas N, según OpenStreetMap a [fecha]». OSM puede
  tener negocios cerrados o no tener todos. En la ronda 2 no hay forma de comprobar
  una muestra sin API: se dice en los límites.

### 2. Elegir competidores (como mucho 4, y solo para el análisis interno)

| Tipo | Criterio | De dónde sale |
|---|---|---|
| **Directos** | Mismo público y a menos de 500 m | `cifras.json` → `mas_cercanos_mismo_publico` (el más cercano y el que mejor esté en internet) |
| **De búsqueda** | Los que salen en Google para la búsqueda principal | Captura de Iván (paso 5 del guion: el mapa centrado en el local) |
| **Referente** | El mejor en digital de la ciudad con el mismo público | Captura de Iván y su web |

- **Fuera** los de otro público (unisex, señora, estética), **salvo** que salgan en la captura de la búsqueda.
- Una web rota solo entra si es de un competidor directo o de búsqueda.

### 3. Analizar cada competidor (interno, va a `competencia/`)

- Ficha de Google (de la captura): categoría, nota y opiniones con fecha.
- Web: secciones, precios, cita online o WhatsApp, móvil (`captura.sh` con 390 de
  ancho), título, descripción, H1 y datos estructurados. Rendimiento con Lighthouse
  (A-008), cuando Paco lo instale.
- Redes que **enlaza** o que se ven en las capturas.

### 4. Búsquedas objetivo (sin inventar volúmenes)

Se eligen por intención y de fuentes, **antes** del guion de Iván:
1. Las palabras que usan los clientes en sus reseñas («pelar», «corte», «barba», «niño»).
2. La categoría de Google del cliente y de los competidores directos.
3. Actividad + ciudad y actividad + barrio.

Se eligen **tres como mucho**, con la principal primero; son las que van al guion. En
el informe solo se nombra la principal, como «la búsqueda que más nos importa»,
nunca con cifras. No hay volúmenes medidos hasta que contrate (A-001: sin API ni
cuenta de Ads; Search Console y las estadísticas de la ficha, después).

### 5. Contenido del informe (A-005: 2 páginas más un anexo, en A5)

Escribo el contenido; Lola lo maqueta con `estilo-documentos`; el generador **lee
las cifras** de `competencia/cifras.json` y de `competencia/datos-informe.json`
(abajo). Los límites de palabras son orientativos: los ajusta la maqueta de Lola.

| Página | Contenido | Límite |
|---|---|---|
| **1 · ¿Cómo os encuentran en internet?** (funciona sola: es la imagen que verá en WhatsApp) | Nombre del negocio · 3 o 4 cifras (2 × 2), cada una con su fuente corta · la conclusión en dos frases · «Estudio gratis y sin compromiso» | ~90 palabras |
| **2 · Lo que hemos visto y lo que haríamos** | **Tres cosas que hemos encontrado**, de su caso y cada una con su prueba: lo que vimos y, en una frase, por qué importa, sin generalizar · el **aviso de los directorios** (Reme) · una o dos **opiniones** literales, sin autor · **una idea de frase principal** (de `textos-web`, como idea a confirmar) · **lo que haríamos**: el qué, no el cómo · **siguiente paso** | ~170 palabras y 1 captura recortada |
| **Anexo · Cómo lo hemos hecho** | Fuentes con fecha (OSM y la fecha de sus datos; la captura de Google con fecha, hora y ciudad; los directorios) · límites · «© colaboradores de OpenStreetMap · openstreetmap.org/copyright» · «Preparado con ayuda de asistentes de IA» · **cierra con el siguiente paso y el contacto** (Lola: la última página dice qué pasa ahora) | ~180 palabras |

**Lo que no se regala** (es el entregable de arranque, cuando contrata):
- La lista completa de búsquedas objetivo: solo se nombra la principal.
- El análisis de cada competidor y cómo superarlo.
- La auditoría de citas completa: se dice «N directorios con datos distintos», no cuáles ni qué corregir.
- Las categorías que pondríamos en su ficha de Google y los cambios concretos.
- La estructura de la web y los textos: solo la frase principal, como muestra.
- Nada de curso de SEO: una frase por término, no un apartado.

**`competencia/datos-informe.json`**: cada dato que no sale del censo, con su fuente:

```json
{"nota_google": {"valor": "<nota>", "fuente": "privado/capturas-google/02-ficha-maps.png", "fecha": "<AAAA-MM-DD HH:MM>", "desde": "<ciudad de Iván>"},
 "directorios_con_datos_distintos": {"valor": "<N>", "fuente": "expediente §7", "fecha": "<AAAA-MM-DD>"}}
```

### 6. Antes de pasarlo a Puri

```
python3 procesos/skills-borrador/textos-web/vigilar_frases.py <borrador.html>    # 0 avisos B; cada R justificado
grep -nE '[0-9]' <plantilla del informe>    # en la plantilla no hay cifras: todas vienen de los JSON
pdftoppm -f 1 -l 1 -scale-to-x 390 -scale-to-y -1 -png <informe.pdf> pagina-1   # ¿se entiende sola en el móvil?
```

## Reglas

1. **Cada cifra sale de `cifras.json` o `datos-informe.json`, con fecha.** Ninguna se teclea en la maqueta.
2. **Nunca prometer posiciones ni resultados** (§10.3), ni de forma encubierta.
3. **Nada de ausencias** («no tiene web»), salvo las comprobadas («su dominio no responde»).
4. **Ninguna frase general sobre clientes o mercado sin fuente**, ni superlativos sin contar
   (Puri, R10–R23). La lista está en [`../textos-web/frases-vigiladas.txt`](../textos-web/frases-vigiladas.txt).
5. **El orden de un marketplace no es un ranking.**
6. **Sin jerga:** cada término técnico, explicado en una frase. El título no dice «SEO local».
7. **Primero lo que tiene, después lo que le falta.**
8. **Las capturas de competidores** sirven para analizar, nunca para copiar. En el
   informe, recortadas y sin datos personales.
9. **Atribución de OpenStreetMap** con `openstreetmap.org/copyright` en el mapa (`mapa.py` ya la lleva) y en el anexo.
10. **Dominio libre:** solo se dice si se ha comprobado en el registro, no por DNS. En el
    informe no se menciona: va al presupuesto (A-011: el dominio va dentro de la cuota).
11. **«Gratis y sin compromiso»** (A-005), sin urgencias ni plazos inventados.

## Salida

- `competencia/`: `overpass-consulta.overpassql`, `overpass-respuesta.json`,
  `cifras.json`, `puntos-mapa.json`, `mapa-competencia.png`, `datos-informe.json`,
  `competidores.md` (los elegidos, con su tipo, motivo y análisis) y capturas.
- Contenido del informe para Lola, con cada frase trazada a su fuente.
- `pagina-1.png` para que Menchu la mande por WhatsApp (la genera quien genere el PDF).

## Comprobación final

- [ ] La consulta guardada usa etiquetas exactas, sin `hairdresser_supply` ni `~`.
- [ ] `cifras.json` es la salida de `censo.py`, sin editar (su `sha256` coincide con la respuesta guardada).
- [ ] Cada cifra del informe está en `cifras.json` o en `datos-informe.json`, con fecha.
- [ ] Cada competidor tiene tipo (directo, de búsqueda o referente) y motivo.
- [ ] `vigilar_frases.py`: 0 avisos B; cada R, justificado o quitado.
- [ ] Dos páginas más el anexo; la primera se entiende sola; el anexo acaba con el siguiente paso y el contacto.
- [ ] Nada de la lista «Lo que no se regala».

## Herramientas

| Herramienta | Para qué |
|---|---|
| [`censo.py`](censo.py) (esta skill) | Consulta de Overpass, cifras y puntos del mapa. 9 pruebas y 11 mutaciones en `pruebas/`. |
| `herramientas/mapa.py` | Mapa de competencia (Paco), con los puntos de `censo.py mapa`. |
| `herramientas/captura.sh` | Webs de competidores; con 390 de ancho, como un móvil. |
| [`../textos-web/vigilar_frases.py`](../textos-web/vigilar_frases.py) | Lista negra antes de Puri. |

## Dudas abiertas

- Instancia de Overpass para uso comercial (A-015): la fija Paco.
- Si se pueden poner en el informe recortes de la captura de Google con nombres de
  competidores: está en el paquete legal (A-010). Mientras, solo la ficha del propio cliente.
- Los límites de palabras por página, a confirmar con la maqueta A5 de Lola.
