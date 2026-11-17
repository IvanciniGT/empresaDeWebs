---
name: investigar-cliente
description: "Recopila y comprueba la información pública de un cliente nuevo (ficha de Google, su web y redes si las tiene, mapas, directorios y reseñas) y la deja en el expediente separando lo comprobado, lo que hay que confirmar y lo que solo intuimos. Úsala justo después de abrir el expediente de un cliente nuevo, antes de pedirle nada."
---

# investigar-cliente

> **BORRADOR v0.2 · revisado por Chema** · 2026-11-17 · **Dueño: Chema**
> Cambios respecto a v0.1 y motivos: [procesos/ronda-1/revision-chema.md](../../ronda-1/revision-chema.md) §4.

## Cuándo

Al llegar un cliente nuevo, antes de pedirle nada. Con lo poco que nos da (nombre,
actividad, ciudad, si tiene web) averiguamos lo que ya está publicado y, sobre
todo, **qué ve hoy quien le busca**.

## Entrada

- Nombre del negocio, actividad y ciudad.
- Su web y sus redes, si nos las ha dado.
- Expediente abierto: `clientes/<negocio>/expediente.md`.

## Fuentes y lo que vale cada una

| Nivel | Fuentes | Para qué sirve |
|---|---|---|
| **Primaria** | El propio negocio (lo que nos dice o publica en su web/redes) · su **ficha de Google** | Comprueba un dato por sí sola. |
| **Secundaria independiente** | OpenStreetMap · Bing Places · Apple Maps · Treatwell/Booksy · prensa local | Dos que coinciden comprueban un dato. |
| **Copia** | Directorios automáticos (mispelus, resserv, volumus…) | **No comprueban nada.** Sirven para la auditoría de citas y para leer reseñas copiadas de Google. |
| **Pista** | Reseñas de clientes | Tono, lo que valoran, lo que hace único al negocio. **Nunca un dato del negocio.** |

## Cómo buscamos (sin saltarnos nada)

- **Nunca** leemos con un robot las páginas de resultados de Google, Bing,
  DuckDuckGo, Brave o Mojeek: su `robots.txt` lo prohíbe (`Disallow: /search`).
  `herramientas/buscar.sh` está **retirado**.
- **Ficha de Google y competidores que devuelve Google:** API de Google Places
  (si Iván la aprueba). Lo que devuelve **se consulta, no se guarda**: en el
  expediente solo va el identificador de la ficha (`place_id`) y nuestras
  conclusiones con fecha («nota y horario comprobados el 17/11/2026: coinciden
  con…»), nunca copias de reseñas ni listados.
- **Web, redes, prensa:** API de Brave Search (si Iván la aprueba).
- **Lo que ve una persona en Google:** captura manual. Preparo la lista de
  enlaces exactos y Federico se la pasa a quien la haga.
- **URL directas:** se puede comprobar una URL candidata (dominio propio, el
  Instagram que enlaza su ficha o OSM). Una URL que no responde **no** prueba
  que no tenga web o redes.
- Antes de automatizar cualquier fuente nueva: leer su `robots.txt` y sus
  condiciones. Si dudas, no se automatiza: se pide a Federico.

## Pasos

1. **Si tiene web:** pedir a Federico la extracción (skill `extraer-web-existente`, de Paco)
   y trabajar sobre lo que devuelva.
2. **Ficha de Google** (la fuente más importante del SEO local). Anotar, con fecha:
   - Si existe y si está reclamada (si no se puede saber, «por confirmar»).
   - **Categoría principal** y secundarias.
   - Horario, teléfono, web enlazada, número de fotos.
   - Nota, número de opiniones, fecha de la última reseña y **si el negocio responde** a las reseñas.
   - `place_id` (lo único que se puede guardar de la API).
3. **Ubicar el local** en OpenStreetMap (Nominatim, con `curl` y User-Agent propio)
   y guardar coordenadas y barrio (el barrio, «por confirmar» si solo sale de OSM).
4. **Otros mapas:** Bing Places y Apple Maps. ¿Existen? ¿Coinciden con Google?
5. **Auditoría de citas:** tabla con **cada** directorio encontrado: URL, nombre,
   dirección, teléfono, horario, errores y fecha de consulta. No basta con «10+ fichas».
6. **Redes y marketplaces:** Instagram, Facebook, TikTok, Treatwell, Booksy. Primero
   las que enlace su ficha de Google u OSM; después búsqueda (Brave). Si no aparecen:
   «no encontradas en [fuentes]», nunca «no tiene».
7. **Leer las reseñas** (como mínimo las 20–30 más recientes, si es posible). Anotar:
   - Citas literales útiles, **sin el nombre del autor** ni nada que identifique a nadie.
   - Lo que se repite (con cuántas reseñas lo dicen: «puntualidad: 1 reseña» pesa poco).
   - Frases entre comillas que parezcan del propio negocio (posibles lemas).
8. **Capturas** de lo relevante (`herramientas/captura.sh`), sin avisos de cookies
   cuando la herramienta lo permita. Ficha de Google y búsqueda: captura manual (paso «Cómo buscamos»).
9. **Rellenar el expediente** con la plantilla de abajo.

## Reglas

1. **Dato comprobado = una fuente primaria, o dos secundarias independientes que coinciden.**
2. **Dos copias de lo mismo son una sola fuente.** Dos directorios que reproducen la
   ficha de Google no comprueban la nota: la comprueba la ficha.
3. **Una reseña es una pista, no un dato.** «Llevo 34 años yendo» no prueba la
   antigüedad del negocio; lo convierte en pregunta para el cliente.
4. **Los directorios automáticos inventan.** Solo sirven para la auditoría de citas
   y para leer reseñas literales.
5. **No afirmar ausencias:** «no lo hemos encontrado en X e Y» no es «no tiene».
6. **Cada dato con fuente y fecha de consulta.** La nota y las opiniones caducan.
7. **Las fotos del negocio que hay en Google no son nuestras.** Se mencionan y se piden.
8. **Solo información pública,** sin saltarse captchas, bloqueos, `robots.txt` ni condiciones de uso.
9. **No se guarda contenido de la API de Google** salvo el `place_id`.
10. **No se contacta con el negocio** ni con nadie: eso es de Menchu, a través de Federico.

## Plantilla del expediente (secciones de esta skill)

```markdown
## 1. Datos comprobados
| Dato | Valor | Fuente(s) y nivel | Consultado |

## 2. Datos a confirmar con el cliente
| Dato | Lo que hemos visto | Por qué no nos fiamos |

## 3. Lo que intuimos (preguntar, no afirmar)
| Intuición | De dónde sale (p. ej. «2 de 30 reseñas») | Pregunta para el cliente |

## 4. Ficha de Google
place_id · categoría principal/secundarias · reclamada · nota y nº (fecha) · última reseña · responde a reseñas · web enlazada · fotos

## 5. Lo que dicen los clientes
Citas literales sin autor · temas que se repiten, con cuántas reseñas

## 6. Presencia en internet
| Dónde | Estado | Fuente y fecha |

## 7. Auditoría de citas
| Directorio (URL) | Nombre | Dirección | Teléfono | Horario | Errores | Consultado |
```

## Herramientas

- `herramientas/captura.sh URL salida.png [ancho] [alto]`
- Nominatim: `https://nominatim.openstreetmap.org/search?q=...&format=json` (con `curl`, User-Agent propio, 1 petición/s como mucho).
- Google Places API y Brave Search API: **pendientes de aprobación de Iván** (revisión de Chema §6–7). Las herramientas las hace Paco.
- ~~`herramientas/buscar.sh`~~: retirado (va contra el `robots.txt` de Bing).

## Salida

- `expediente.md` con las secciones 1–7.
- `recopilado/capturas/` numeradas y con nombre descriptivo.
- Lista de enlaces para la captura manual, si hace falta.

## Comprobación final

- [ ] Ningún dato comprobado se apoya solo en copias o en reseñas.
- [ ] Cada dato tiene fuente y fecha de consulta.
- [ ] Lo que sale de una sola reseña está en «Lo que intuimos», no en «comprobados».
- [ ] No hay ausencias afirmadas («no tiene…»).
- [ ] La auditoría de citas lista cada directorio con su URL.
- [ ] Del API de Google solo se ha guardado el `place_id`.
- [ ] Ninguna cita de reseña lleva el nombre del autor.

## Dudas abiertas

- Si Iván aprueba Places y Brave (o una suscripción con buscador), afinar el paso «Cómo buscamos».
- Si se puede escribir «4,8 en Google» en un documento a partir de la API de Places, o hay que sacarlo de la captura manual (duda legal).
- Cómo saber si la ficha está reclamada sin acceso de gestor: la API no lo da.
