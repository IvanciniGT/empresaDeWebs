---
name: investigar-cliente
description: "Recopila y comprueba la información pública de un cliente nuevo (ficha de Google mediante la captura manual de Iván, su web y redes, mapas, directorios y reseñas) y la deja en el expediente separando lo comprobado, lo que hay que confirmar y lo que solo intuimos. Úsala justo después de abrir el expediente de un cliente nuevo, antes de pedirle nada."
---

# investigar-cliente

> **BORRADOR v0.3 · revisado por Chema** · 2026-11-18 · **Dueño: Chema**
> v0.2 → v0.3: decisiones de Iván A-001, A-009, A-013 y A-015, y peticiones de Puri.
> Detalle en [revision-chema.md](../../ronda-1/revision-chema.md) §8.

## Cuándo

Al llegar un cliente nuevo, antes de pedirle nada. Con lo poco que nos da (nombre,
actividad, ciudad, si tiene web) averiguamos lo que ya está publicado y, sobre
todo, **qué ve hoy quien le busca**.

## Entrada

- Nombre del negocio, actividad y ciudad.
- Su web y sus redes, si nos las ha dado.
- Expediente abierto: `clientes/<negocio>/expediente.md`, con la carpeta `privado/`.

## Fuentes y lo que vale cada una

| Nivel | Fuentes | Para qué sirve |
|---|---|---|
| **Primaria** | El propio negocio (lo que nos dice o publica en su web o redes) · su **ficha de Google**, vista en la captura de Iván | Comprueba un dato por sí sola. |
| **Secundaria independiente** | OpenStreetMap · Bing Places · Apple Maps · Treatwell/Booksy · prensa local | Dos que coinciden comprueban un dato. |
| **Copia** | Directorios automáticos (mispelus, resserv, volumus…) | **No comprueban nada.** Sirven para la auditoría de citas y para leer reseñas copiadas de Google. |
| **Pista** | Reseñas de clientes | Tono, lo que valoran y lo que hace único al negocio. **Nunca un dato del negocio.** |

## Cómo buscamos (A-001)

- **Google lo mira una persona, no un robot.** Iván hace la captura manual con el
  guion (abajo). Ningún script lee páginas de resultados de Google, Bing,
  DuckDuckGo, Brave o Mojeek: su `robots.txt` lo prohíbe. `buscar.sh` está retirado.
- **Lo demás, con fuentes abiertas:** OpenStreetMap, URL directas y Treatwell,
  siempre después de leer su `robots.txt` (`herramientas/robots.mjs`, de Paco).
- **API (Places, Brave):** no se usan en la ronda 2. Se probarán después (A-001).
- **URL directas:** se puede comprobar una URL candidata (el dominio propio, o el
  Instagram que enlaza su ficha u OSM). Que una URL no responda **no** prueba que
  no tenga web o redes.

## Guion de captura manual para Iván (10 minutos como mucho)

Lo preparo yo; lo hace Iván; Federico se lo pasa.

1. **Preparo los enlaces** del cliente con el script de esta skill:

   ```
   python3 procesos/skills-borrador/investigar-cliente/enlaces_captura.py \
     --negocio "<nombre>" --ciudad "<ciudad>" --nombre-corto "<como en redes>" \
     --lat <lat> --lon <lon> \
     --busqueda "<búsqueda principal>" [--busqueda "<otra>"] [--busqueda "<otra>"] \
     --carpeta clientes/<negocio>
   ```

   Deja `clientes/<negocio>/privado/capturas-google/guion.html`: una página con los
   enlaces exactos, en orden. Admite **3 búsquedas como mucho**, porque más no caben
   en 10 minutos. Las búsquedas salen del paso 4 de `estudio-competencia`.
2. **Pido a Federico** que se la pase a Iván con esta frase: «Abre `guion.html` y
   sigue los pasos; son 9 capturas y unos 10 minutos».
3. **Iván:**

   | Paso | Qué | Capturas |
   |---|---|---|
   | 0 | Guardar las capturas en la carpeta del guion (`⌘⇧5` → Opciones), abrir una ventana privada (`⌘⇧N`), arrastrar el guion y rechazar las cookies | — |
   | 1 | Google con el nombre del negocio y la ciudad | 1 |
   | 2 | La ficha en Google Maps, con el horario desplegado (se ve si pone «Reclamar esta empresa») | 1 |
   | 3 | Sus opiniones, ordenadas por «Más recientes» | 1 |
   | 4 | Las búsquedas objetivo (hasta 3) | 1 cada una |
   | 5 | El mapa centrado en la calle del cliente, con la búsqueda principal | 1 |
   | 6 | Redes: `site:instagram.com` y `site:facebook.com` con el nombre | 2 |

   Cada captura, con `⌘⇧4`, espacio y clic en la ventana: solo sale el navegador.
   No renombra nada. Al terminar le dice a Federico **desde qué ciudad** las ha hecho,
   porque los resultados de Google cambian según dónde se busca.
4. **Yo** renombro las capturas (`01-google-nombre.png`…) según el orden del guion, y
   anoto en el expediente la fecha, la hora y la ciudad desde la que se hicieron.

**Las capturas no salen de `privado/`**: llevan nombres y fotos de personas en las
reseñas. Para el informe, un **recorte sin datos personales** va a
`recopilado/capturas/`, con el nombre de la captura de la que sale.

## Pasos

1. **Si tiene web:** pedir a Federico la extracción (skill `extraer-web-existente`,
   de Paco) y trabajar sobre lo que devuelva.
2. **Ubicar el local** en OpenStreetMap: el nodo del negocio (y su id, que usa
   `censo.py`) o, si no está, Nominatim (`curl`, User-Agent propio, 1 petición/s).
   El barrio va a «por confirmar» si solo sale de OSM.
3. **Preparar el guion de captura** (arriba) y pedirlo a Federico. Mientras llega, seguir con los pasos 5 y 6.
4. **Ficha de Google**, leída en las capturas de Iván. Anotar, con fecha:
   - categoría principal (la que sale bajo el nombre);
   - si sale «Reclamar esta empresa»: entonces **no** está reclamada. Si no sale,
     probablemente sí, pero se confirma con el cliente;
   - horario, teléfono, web enlazada;
   - nota, número de opiniones, fecha de la última reseña y si el negocio responde.
5. **Otros mapas:** Bing Places y Apple Maps, mirando URL directas (no buscadores).
   ¿Existen? ¿Coinciden con Google?
6. **Auditoría de citas:** tabla con **cada** directorio encontrado: URL, nombre,
   dirección, teléfono, horario, errores y fecha. Captura de cada uno con
   `herramientas/captura.sh` (página entera; `--solo-pantalla` para la vista de arriba).
7. **Redes y marketplaces:** primero las que enlace su ficha o OSM; después, las
   capturas `site:` de Iván. Si no aparecen: «no encontradas en [fuentes], a [fecha]».
   Nunca «no tiene».
8. **Leer las reseñas** (en las capturas y en los directorios que las copian). Anotar:
   - citas literales útiles, **sin el nombre del autor**, **cada una con su prueba**
     (ver la regla 7);
   - lo que se repite y en cuántas reseñas («puntualidad: 1 reseña» pesa poco);
   - frases entre comillas que parezcan del propio negocio (posibles lemas);
   - **cómo contesta el negocio** a las reseñas: es su voz, y la usa `textos-web`.
9. **Rellenar el expediente** con la plantilla de abajo y pasar
   `textos-web/vigilar_frases.py` por él antes de darlo por terminado.

## Reglas

1. **Dato comprobado = una fuente primaria, o dos secundarias independientes que coinciden.**
2. **Dos copias de lo mismo son una sola fuente.**
3. **Una reseña es una pista, no un dato.** «Llevo 34 años yendo» no prueba la
   antigüedad del negocio: se convierte en pregunta para el cliente.
4. **Los directorios automáticos inventan.** Solo sirven para la auditoría de citas
   y para leer reseñas literales.
5. **No afirmar ausencias:** «no lo hemos encontrado en X e Y» no es «no tiene».
6. **Cada dato con fuente y fecha de consulta.** La nota y las opiniones caducan.
7. **Cada cita de una reseña con su prueba** (Puri, R30): la captura (de Iván, o de un
   directorio con su URL y fecha), guardada en `privado/` porque lleva el nombre del
   autor. En el expediente, la cita sin nombre y el enlace a la prueba.
8. **El repositorio es público (A-013).** En `expediente.md` no va ningún dato
   personal: ni nombres de autores de reseñas, ni nombres de los dueños o empleados,
   ni sus teléfonos móviles. Eso va a `privado/` (A-009), y el expediente dice
   «[en privado/]». Los datos del negocio (nombre comercial, dirección y teléfono
   del local) sí van.
9. **Las fotos del negocio que hay en Google no son nuestras.** Se mencionan y se piden.
10. **Solo información pública,** sin saltarse captchas, bloqueos, `robots.txt` ni condiciones de uso.
11. **No se contacta con el negocio** ni con nadie: eso es de Menchu, a través de Federico.

## Plantilla del expediente (secciones de esta skill)

```markdown
## 1. Datos comprobados
| Dato | Valor | Fuente(s) y nivel | Consultado |

## 2. Datos a confirmar con el cliente
| Dato | Lo que hemos visto | Por qué no nos fiamos |

## 3. Lo que intuimos (preguntar, no afirmar)
| Intuición | De dónde sale (p. ej. «2 de 30 reseñas») | Pregunta para el cliente |

## 4. Ficha de Google (captura manual de Iván, AAAA-MM-DD HH:MM, desde <ciudad>)
categoría principal · «Reclamar esta empresa» sí/no · nota y nº · última reseña · responde a reseñas · web enlazada

## 5. Lo que dicen los clientes
| Cita (sin autor) | Prueba (privado/…) | Fecha |
Temas que se repiten, con cuántas reseñas · cómo contesta el negocio

## 6. Presencia en internet
| Dónde | Estado | Fuente y fecha |

## 7. Auditoría de citas
| Directorio (URL) | Nombre | Dirección | Teléfono | Horario | Errores | Consultado |
```

## Herramientas

| Herramienta | Para qué |
|---|---|
| [`enlaces_captura.py`](enlaces_captura.py) (esta skill) | Guion de captura manual de Iván. Pruebas en `pruebas/`. |
| `herramientas/captura.sh URL salida.png [ancho] [alto] [--solo-pantalla]` | Página entera y sin avisos de cookies. Con un ancho menor de 768, móvil de verdad, a 780 px. Avisa si la web no está adaptada al móvil. |
| `herramientas/robots.mjs` | Leer el `robots.txt` de una fuente antes de automatizarla. |
| Nominatim | Solo si el local no está en OSM: `https://nominatim.openstreetmap.org/search?q=...&format=json`, con `curl` y User-Agent propio. |
| [`../textos-web/vigilar_frases.py`](../textos-web/vigilar_frases.py) | Repasar el expediente antes de darlo por terminado. |

## Salida

- `expediente.md` con las secciones 1–7, sin datos personales.
- `privado/capturas-google/` con el guion y las capturas de Iván, renombradas.
- `privado/resenas/` con la prueba de cada cita.
- `recopilado/capturas/` con los directorios y los recortes sin datos personales.

## Comprobación final

- [ ] Ningún dato comprobado se apoya solo en copias o en reseñas.
- [ ] Cada dato tiene fuente y fecha; la captura de Iván, también la ciudad.
- [ ] Lo que sale de una sola reseña está en «Lo que intuimos», no en «comprobados».
- [ ] No hay ausencias afirmadas: `vigilar_frases.py` sin avisos B.
- [ ] Cada cita de reseña tiene su prueba en `privado/`.
- [ ] `expediente.md` y `recopilado/` sin nombres de personas ni datos personales
      (`git check-ignore` confirma que `privado/` queda fuera).
- [ ] La auditoría de citas lista cada directorio con su URL.

## Dudas abiertas

- El enlace del mapa centrado usa un formato de Google Maps que no está documentado.
  Si no centra, el guion dice cómo hacerlo a mano. Que Iván lo confirme en la ronda 2.
- Que Iván confirme que las 9 capturas le caben en 10 minutos. Si no, se quita la tercera búsqueda.
- Si se pueden usar recortes de capturas de Google en un documento de venta: está en
  el paquete de dudas legales (A-010).
