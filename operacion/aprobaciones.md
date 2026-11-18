# Bandeja de aprobaciones de Iván

> La mantiene Federico. Aquí solo entra lo que AGENTS.md §10.2 reserva a Iván,
> una solicitud por asunto y con el formato de §10.4. Federico las revisa
> antes de que lleguen aquí y se las recuerda a Iván si tardan.
>
> Cuando Iván decide, la solicitud pasa a «Resueltas» con su decisión y la
> fecha, y Federico avisa al agente que la pidió.

## Pendientes


### A-011 (resto) · Política de precios pendiente (§8)
```
QUÉ:         - Qué contestamos a «¿cuánto cuesta?» en el primer contacto.
             - ¿Se puede contratar la creación sin mantenimiento?
             - Suscripción sin pago inicial: qué pasa en el mes 13.
             - ¿El vídeo entra en los planes?
POR QUÉ:     No había propuesta. Reme no puede cerrar un presupuesto ni Menchu responder a la primera
             pregunta de todo cliente hasta que se cierren las tarifas de §8.2.
URGENCIA:    antes del primer cliente real
PEDIDA POR:  Reme, Menchu · 2026-11-17
```

<!--
### A-0XX · título corto
QUÉ:
CLIENTE:
POR QUÉ:
PROPUESTA:
ALTERNATIVA:
URGENCIA:    hoy / esta semana / sin prisa
ENLACE:
PEDIDA POR:  agente · fecha
ENCARGO:     E-xxx (si lo hay)
-->


## Resueltas

### A-001 a A-015 (salvo A-011) · Ronda 1 · Aprobadas las recomendaciones — 2026-11-17
Iván: «OK a todas las recomendaciones». El detalle de cada una está en el historial de git
(commit 676177e) y en la [consolidación](../procesos/ronda-1/consolidacion.md).

| ID | Decisión |
|---|---|
| A-001 | Para la ronda 2, búsqueda con una **captura manual de Google por cliente (la hace Iván)** y fuentes abiertas. Las API (Places, Brave) se prueban después. |
| A-002 | **No se ofrecen llamadas.** Menchu hace las preguntas por WhatsApp. |
| A-003 | **WhatsApp primero** y correo como copia. De momento, Iván copia y pega lo que redacta Menchu. |
| A-004 | Ante el cliente: «lo importante (presupuestos, publicar vuestra web) lo revisa y aprueba **Iván, el responsable**». |
| A-005 | Informe de venta de **2 páginas más un anexo, en A5**, pensado para el móvil. Se dice «gratis y sin compromiso». |
| A-006 | **Estilo común provisional** para nuestros documentos (`estilo-documentos`) y guía previa de 3–4 páginas. |
| A-007 | Iván prueba el Word en Microsoft Word con la lista de 10 minutos de Puri, **una vez por versión de plantilla**, más la comprobación automática. |
| A-008 | Aprobadas: fuentes Inter y Fraunces (OFL), iconos Lucide (ISC), hunspell con diccionario español, whisper.cpp con un modelo y Lighthouse 13.6.0 dentro de `herramientas/`. Las instala Paco. |
| A-009 | Expedientes en `clientes/<negocio>/`. Datos personales en `clientes/<negocio>/privado/`, **excluida de git**. Lo de quien no contrata se borra a los 3 meses. |
| A-010 | Se prepara un paquete de dudas legales para un profesional: cláusula de privacidad, consentimiento de imagen, reseñas y competidores. Contratarlo lo decide Iván. |
| A-011 | **Solo el dominio:** dentro de la cuota de mantenimiento, a nombre del cliente. El resto sigue pendiente. |
| A-012 | Dos recordatorios (a los 3 y a los 8 días laborables) y pausa. Las plantillas se aprueban una vez. Menchu propone el plazo interno. |
| A-014 | Llavero de macOS como gestor de secretos provisional, cuando haya API. |
| A-015 | Overpass por una instancia que acepte uso comercial, después de leer sus condiciones, guardando la consulta y la respuesta. |

### A-013 · El repositorio de GitHub es público
- **Decisión:** se queda público. Iván lo asume: es un proyecto de formación. — 2026-11-17
- **Consecuencia:** todo lo que entre en git es público. Con un cliente real, sus datos personales
  no pueden ir al repositorio (ver A-009).

### A-000 · Dónde se guardan la plantilla y los encargos
- **Decisión:** aprobada — 2026-11-17
- **Resultado:** carpeta `operacion/` en este repositorio, en Markdown y con git.
- **Pendiente de Iván:** actualizar el punto de AGENTS.md §15.

<!-- Siguiente ID libre: A-016 -->
