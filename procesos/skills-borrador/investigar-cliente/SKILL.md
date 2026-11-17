---
name: investigar-cliente
description: "Recopila y comprueba la información pública de un cliente nuevo (su web si la tiene, buscadores, ficha de Google, directorios, reseñas, mapas y redes) y la deja en el expediente separando lo comprobado de lo que hay que confirmar. Úsala justo después de abrir el expediente de un cliente nuevo."
---

# investigar-cliente

> **BORRADOR v0.1** · Escrito por Federico · **Dueño: Chema** · En revisión (ronda 1)

## Cuándo

Al llegar un cliente nuevo, antes de pedirle nada. Con lo poco que nos da
(nombre, actividad, si tiene web) averiguamos todo lo que ya está publicado.

## Entrada

- Nombre del negocio, actividad y ciudad.
- Su web y sus redes, si nos las ha dado.
- Expediente abierto: `clientes/<negocio>/expediente.md`.

## Pasos

1. **Si tiene web:** pedir a Paco la extracción (skill `extraer-web-existente`)
   y trabajar sobre lo que devuelva: textos, fotos, precios, estructura y
   capturas.
2. **Buscar el nombre exacto** del negocio y la ciudad. Anotar todo lo que
   aparezca: ficha local, directorios, redes, marketplaces y prensa.
3. **Ubicar el local** en OpenStreetMap (Nominatim) y guardar las coordenadas.
4. **Leer las reseñas** literales. Son la mejor fuente de lo que hace especial
   al negocio y de su tono.
5. **Buscar redes y marketplaces** (Instagram, Facebook, TikTok, Treatwell,
   Booksy, Google Business Profile…).
6. **Hacer capturas** de todo lo relevante (`herramientas/captura.sh`), en
   ordenador y en móvil.
7. **Rellenar el expediente:** tabla de datos **comprobados** (con sus fuentes),
   tabla de datos **por confirmar** (con el motivo), citas de reseñas y estado
   de su presencia en internet.

## Reglas

1. **Dato comprobado = dos fuentes independientes que coinciden, o una
   primaria** (el propio negocio o su ficha de Google). Lo demás, «por confirmar».
2. **Los directorios automáticos inventan.** Solo sirven para nombre,
   dirección, teléfono y reseñas reproducidas literalmente.
3. **No afirmar ausencias:** «no hemos encontrado redes» no es «no tiene redes».
4. **Las fotos del negocio que hay en Google no son nuestras.** Se mencionan y
   se piden al cliente.
5. **Solo información pública,** y sin saltarse captchas ni bloqueos.
6. **Cada dato, con su fuente** en el expediente.

## Herramientas

- `herramientas/captura.sh URL salida.png [ancho] [alto]`
- `herramientas/buscar.sh "consulta"`: ⚠️ solo fiable con el nombre exacto.
- Nominatim: `https://nominatim.openstreetmap.org/search?q=...&format=json`, con `curl` y User-Agent propio.

## Salida

- `expediente.md` completo (secciones 1–4).
- `recopilado/capturas/` numeradas y con nombre descriptivo.

## Comprobación final

- [ ] Cada dato comprobado tiene al menos una fuente primaria o dos coincidentes.
- [ ] Lo que no cuadra entre fuentes está en «por confirmar», con el motivo.
- [ ] Ninguna frase afirma algo que no esté en una fuente.

## Dudas abiertas (para la revisión)

- Cómo buscar de forma fiable sin ventana: Google bloquea, DuckDuckGo pide captcha y Bing no sirve.
- Cómo comprobar si tiene redes sin iniciar sesión.
- Cómo leer la ficha de Google Business Profile directamente.
