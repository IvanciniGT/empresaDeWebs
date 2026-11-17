---
name: extraer-web-existente
description: "Descarga y ordena la web actual de un cliente (páginas, textos, imágenes con su origen, precios, datos de contacto, datos estructurados y capturas en ordenador y móvil) para reutilizar su contenido en la web nueva. Úsala cuando un cliente nuevo ya tiene web."
---

# extraer-web-existente

> **BORRADOR v0.0, sin probar** · Escrito por Federico · **Dueño: Paco** · En revisión (ronda 1)
>
> El cliente simulado no tenía web, así que esta parte está sin hacer. Es la
> primera cosa que pidió Iván: «si ya tiene web, nos la tragamos».

## Cuándo

Cuando el cliente nos dice que tiene web, o la encontramos al investigarle.

## Qué debería sacar

| Qué | Para qué | Para quién |
|---|---|---|
| Lista de páginas y estructura (menú) | Ver qué secciones tiene | Lola, Reme |
| Texto de cada página, limpio | Reaprovechar contenido | Chema |
| Imágenes a tamaño original, con la página de origen | Reutilizar sus fotos (son suyas) | Lola |
| Precios, horarios, teléfonos y direcciones detectados | Rellenar el expediente | Chema, Reme |
| Datos estructurados, título, descripción y H1 | Diagnóstico SEO | Chema |
| Capturas de ordenador y móvil de cada página | Informe y comparación antes/después | Chema, Lola |
| Tecnología (WordPress, Wix…), dominio y alojamiento | Migración y presupuesto | Paco, Reme |

## Reglas

1. **Solo el dominio del cliente,** con límite de páginas y sin saturar su servidor.
2. **Respetar `robots.txt`** salvo que el cliente nos autorice por escrito.
3. **Sin iniciar sesión** en nada ni usar sus contraseñas (§12).
4. Las fotos son del cliente, pero puede que algunas sean de un banco de
   imágenes: **marcar el origen** y no reutilizar ninguna sin confirmarlo.

## Salida (propuesta)

- `clientes/<negocio>/recopilado/web-actual/` con `paginas/`, `imagenes/`,
  `capturas/` y un `resumen.md`.

## Dudas abiertas (para la revisión)

- ¿Con qué herramienta? (`wget --mirror`, script propio, Playwright…)
- ¿Cómo se prueba sin descargar webs de terceros que no son clientes?
