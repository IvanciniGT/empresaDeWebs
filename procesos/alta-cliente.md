# Alta de un cliente nuevo: de «quiero una web» al primer envío

> **Borrador v0.1 · 2026-11-17 · Federico.** Escrito al hacerlo a mano con un
> cliente simulado (Peluquería Hermanos Cotillas, Albacete). Es la semilla de
> las skills: todavía no es un procedimiento aprobado. Cuando Iván lo dé por
> bueno, se pide opinión a cada agente sobre su parte.
>
> Ejemplo completo: [clientes/peluqueria-hermanos-cotillas/](../clientes/peluqueria-hermanos-cotillas/expediente.md)

## 1. Qué recibimos y qué entregamos

**Entra:** quién es, a qué se dedica y si tiene web. Poco más.

**Sale**, antes de pedir nada al cliente:

| Entregable | Formato | ¿Al cliente? | Para qué |
|---|---|---|---|
| Expediente con datos comprobados y por confirmar | Markdown | No | Fuente única de verdad del cliente |
| Informe de mercado y SEO local | PDF | **Sí** | Vendernos: que vea que sabemos de su negocio |
| Cuestionario prerrellenado con textos propuestos | Word editable | **Sí** | Que complete y valide lo que nos falta |
| Email de primer envío | Texto | **Sí** (lo envía Menchu) | Acompañar los dos documentos |
| Guía de estilos previa | PDF | **No** | Adelantar diseño; se entrega al contratar |
| Previo de precio | Markdown | **No** | Priorizar y preparar el presupuesto |

## 2. Fases

```
0 Abrir expediente ─► 1 Recopilar ─► 2 Competencia/SEO ─┬─► 3 Cuestionario ─┐
                                                         ├─► 4 Guía estilos  ├─► 6 QA ─► 7 Aprobación ─► 8 Envío
                                                         └─► 5 Previo precio ┘
```

| # | Fase | Qué se hace | Sale | Agente propuesto |
|---|---|---|---|---|
| 0 | Abrir expediente | Carpeta `clientes/<negocio>/` y `expediente.md` | Expediente vacío | Federico |
| 1 | Recopilar | Web actual (si hay), buscadores, directorios, mapas, reseñas, redes. Capturas. | Expediente con datos comprobados / a confirmar | **Chema** |
| 2 | Competencia y SEO | Censo de competidores (OSM), marketplaces, webs de 3–5 competidores, búsquedas objetivo | Datos + informe PDF | **Chema** |
| 3 | Cuestionario | Lo que sabemos, lo que falta, textos propuestos | Word | **Reme** (qué preguntar) + **Chema** (textos) |
| 4 | Guía de estilos previa | Concepto, colores con contraste, tipografías, iconos, foto, tono, boceto móvil | PDF interno | **Lola** |
| 5 | Previo de precio | Plan que encaja, escenarios, extras, prioridad | Markdown interno | **Reme** |
| 6 | Revisión | Cada dato trazable al expediente; nada inventado; tono; [PROPUESTA] no comunicadas | Visto bueno o rechazo | **Puri** |
| 7 | Aprobación | Iván decide si se envía | Sí / no | Federico → Iván |
| 8 | Envío | Email con informe y cuestionario | Enviado | **Menchu** |

Las fases 3, 4 y 5 son independientes y pueden ir en paralelo.

## 3. Reglas que han salido al hacerlo

1. **Dato comprobado = dos fuentes independientes que coinciden, o una
   primaria** (el propio negocio o su ficha de Google). Lo demás va a «por
   confirmar» y se le pregunta al cliente.
2. **Los directorios mienten.** Más de diez fichas de la peluquería, todas con
   textos generados por máquina que inventan servicios, un horario distinto
   cada una y hasta el barrio. De ahí solo sirven el nombre, la dirección, el
   teléfono y las reseñas que reproducen literalmente.
3. **Toda afirmación del entregable tiene que poder señalarse en el
   expediente.** Al repasar mis propios textos encontré seis frases inventadas,
   y no puse ninguna a propósito: «el 80 %», «han abierto muchas barberías
   nuevas», «zona con mucho paso», «unos 20 minutos», «la que más opiniones
   tiene», «revisado por una persona». Esta regla es la principal tarea de Puri.
4. **No afirmar ausencias que no podemos probar.** «No hemos encontrado
   redes» no es lo mismo que «no tiene redes».
5. **Las fotos del cliente que hay en Google no son nuestras.** Se las pedimos.
6. **Nada marcado [PROPUESTA] llega al cliente:** ni tarifas ni plazos.
7. **Lo que vende es lo que no se puede copiar.** Aquí, la historia familiar
   que cuentan los propios clientes en sus reseñas. Leer las reseñas es la
   mejor fuente de textos.

## 4. Herramientas

Todo en [herramientas/](../herramientas/), funcionando sin abrir ventanas:

| Herramienta | Qué hace | Estado |
|---|---|---|
| `captura.sh` | Captura de una web con Chrome sin ventana (ordenador o móvil) | ✅ Salen los avisos de cookies; no hace página completa |
| `buscar.sh` | Búsqueda en Bing sin ventana | ⚠️ **Poco fiable**: solo vale para búsquedas muy concretas (nombre exacto del negocio) |
| `mapa.py` | Mapa del local y mapa de competencia con OpenStreetMap | ✅ |
| `docx_util.py` | Piezas del Word: casillas clicables, huecos, recuadros, tablas | ✅ Probado en LibreOffice; **falta abrirlo en Word** |
| `html_a_pdf.sh` + `informe.css` | Informes PDF maquetados en HTML | ✅ |

Fuentes de datos que funcionan:

| Fuente | Para qué | Notas |
|---|---|---|
| OpenStreetMap (Nominatim, Overpass) | Ubicar el local y censar competidores en un radio | Gratis. Overpass a veces está saturado: reintentar con espera. Casi nunca trae la web del negocio. |
| Treatwell (JSON-LD de sus listados) | Competidores con reserva online, nota, opiniones y precios | Muy buena fuente |
| Directorios (mispelus, resserv…) | Reseñas literales de Google, nota y número de opiniones | Fiables solo para eso |
| DNS (`dig`) | Saber si un dominio parece libre | No es definitivo |

Lo que **no** funciona:

| Intento | Por qué falla |
|---|---|
| Google | Bloquea las consultas automáticas |
| DuckDuckGo | Pide un captcha a los robots (y no hay que saltárselo) |
| Bing sin ventana | Con búsquedas genéricas devuelve resultados al azar |
| Booksy | No se pudo leer el listado de Albacete |
| Vista incrustada de OpenStreetMap | Necesita WebGL, que Chrome sin ventana no tiene |
| `urllib` de Python | Al Python de python.org le faltan los certificados raíz: usar `curl` |

## 5. Decisiones que necesitamos de Iván

| Asunto | Opciones | Por qué importa |
|---|---|---|
| **Cómo buscamos en internet** | a) navegador visible (abre ventanas) · b) API de búsqueda con plan gratuito limitado · c) solo fuentes abiertas | Sin buscador fiable, la fase 1 se queda coja con clientes que tengan redes o web |
| Nombre, teléfono y correo de la empresa | — | Los documentos llevan «[Nombre de nuestra empresa]» |
| ¿Se envía el informe antes de contratar? | Sí (como venta) / no | Es trabajo que regalamos para vender |
| Dónde viven los expedientes | Provisional: `clientes/<negocio>/` en este repo | Reme lo necesita (§15) |
| ¿Quién aprueba el primer envío? | Iván siempre / Iván solo al principio | §10.2 no cubre explícitamente este envío |
| Dominio: ¿lo incluimos en el mantenimiento? | — | Previo de precio |

## 6. Skills propuestas

| Skill | Dueño | Usa |
|---|---|---|
| `investigar-cliente` | Chema | captura.sh, OSM, directorios, reglas 1–5 |
| `estudio-competencia` | Chema | mapa.py, Overpass, Treatwell, captura.sh, html_a_pdf.sh |
| `cuestionario-cliente` | Reme (+ Chema para textos) | docx_util.py |
| `guia-estilos-previa` | Lola | html_a_pdf.sh, contraste WCAG |
| `previo-precio` | Reme | AGENTS.md §8 |
| `primer-envio` | Menchu | plantilla de email |
| `revisar-entregable` | Puri | reglas 3, 4 y 6, lista de comprobación |

## 7. Pendiente de mejorar

- Capturas sin avisos de cookies y de página completa (con un script de
  Playwright propio y un perfil de Chrome).
- Medir con Lighthouse las webs de la competencia (hace falta instalarlo).
- Abrir el Word en Microsoft Word y comprobar que las casillas funcionan.
- Sacar a plantillas el contenido fijo del cuestionario y del informe, para no
  reescribirlos con cada cliente.
