# Bandeja de aprobaciones de Iván

> La mantiene Federico. Aquí solo entra lo que AGENTS.md §10.2 reserva a Iván,
> una solicitud por asunto y con el formato de §10.4. Federico las revisa
> antes de que lleguen aquí y se las recuerda a Iván si tardan.
>
> Cuando Iván decide, la solicitud pasa a «Resueltas» con su decisión y la
> fecha, y Federico avisa al agente que la pidió.

## Pendientes

> Salen de la ronda 1 de revisión ([consolidación](../procesos/ronda-1/consolidacion.md)).
> Si te vale la propuesta, basta con «OK a A-00X».

### 🔴 Urgente hoy

#### A-013 · El repositorio de GitHub es público
```
QUÉ:         Hacer privado github.com/IvanciniGT/empresaDeWebs (o sacar de él clientes/ y operacion/)
CLIENTE:     interno, y la Peluquería Hermanos Cotillas (negocio real que no es cliente)
POR QUÉ:     Ya se ven el expediente de un negocio real al que nadie ha contactado, su previo de
             precio interno, los entregables y tu correo personal (va en el User-Agent de las
             herramientas). Con clientes de verdad serían sus datos (§10.3, §12).
PROPUESTA:   (Paco) Hacerlo privado hoy. Ningún agente lo ha tocado: es tu cuenta. Hasta que
             decidas, no subo nada (mis commits se quedan en local).
ALTERNATIVA: Dos repositorios: uno público con la política y las herramientas, y otro privado
             para clientes/ y operacion/. Ojo: lo publicado puede seguir en copias de terceros;
             hacerlo privado no lo borra del todo.
URGENCIA:    hoy
PEDIDA POR:  Paco · 2026-11-17
```

### Bloque 1 · Para la ronda 2

#### A-001 · Cómo buscamos en internet
```
QUÉ:         Sustituir buscar.sh, que incumple el robots.txt de Bing
CLIENTE:     interno
POR QUÉ:     Google, Bing, DuckDuckGo, Brave y Mojeek prohíben a los robots leer sus resultados. Sin
             buscador no se comprueban redes, webs ni competidores, ni se lee la ficha de Google.
PROPUESTA:   (Chema) Google Places API para leer la ficha y ver la competencia, y Brave Search API
             para webs y redes, con tope duro de consultas para quedarnos en 0 €. Más una captura
             manual de Google por cliente (unos 10 min tuyos).
             Necesita dos cuentas, probablemente con tarjeta: es contratar servicios (§10.2).
ALTERNATIVA: Para la ronda 2, solo la captura manual y fuentes abiertas: 0 €, sin cuentas. Las API
             se prueban después. Es mi recomendación si no quieres abrir cuentas todavía.
URGENCIA:    esta semana
ENLACE:      procesos/ronda-1/revision-chema.md §6 y §7
PEDIDA POR:  Chema · 2026-11-17
```

#### A-002 · ¿Ofrecemos llamadas al cliente?
```
QUÉ:         Si se ofrece rellenar el cuestionario por teléfono
POR QUÉ:     Lo prometíamos tres veces y nadie puede llamar: §9.1 no tiene teléfono y los agentes no llaman.
PROPUESTA:   No ofrecerlas hasta que alguien las haga. En su lugar, Menchu hace las preguntas por
             WhatsApp, de una en una.
ALTERNATIVA: Las haces tú, con un horario fijo.
URGENCIA:    esta semana
PEDIDA POR:  Menchu, Puri · 2026-11-17
```

#### A-003 · Canal del primer envío y cómo se envía
```
QUÉ:         WhatsApp primero y correo como copia. De momento, tú copias y pegas lo que redacta Menchu.
POR QUÉ:     §9.1 dice que WhatsApp es el canal principal. Menchu no tiene acceso a WhatsApp ni al correo.
PROPUESTA:   La de arriba, mientras haya pocos clientes.
ALTERNATIVA: La API de WhatsApp Business (se paga por conversación). No se han mirado precios.
URGENCIA:    sin prisa (en la ronda 2 no se envía nada)
PEDIDA POR:  Menchu · 2026-11-17
```

#### A-004 · Cómo te presentamos ante el cliente
```
QUÉ:         «Lo importante (presupuestos, publicar vuestra web) lo revisa y aprueba Iván, el
             responsable. Si preferís hablar con él, decídnoslo.»
POR QUÉ:     Decíamos que revisas «todo», y no es verdad: lo de §10.1 no pasa por ti. Nombrarte
             lo decides tú.
ALTERNATIVA: «una persona del equipo», sin nombre.
URGENCIA:    esta semana
PEDIDA POR:  Menchu, Puri · 2026-11-17
```

#### A-005 · Informe de venta corto y pensado para el móvil
```
QUÉ:         Informe de 2 páginas más un anexo de fuentes (Chema), maquetado para leerse en el
             móvil, en A5 (Lola), en vez de 9 páginas A4.
POR QUÉ:     Lo abrirán en el móvil, por WhatsApp. Lo que convence es ver su caso, no el volumen, y
             las 9 páginas regalaban el plan entero.
PROPUESTA:   Lo de arriba. Y decir en el mensaje que es «gratis y sin compromiso».
ALTERNATIVA: Mantener el informe largo, pero solo para quien contrate.
URGENCIA:    esta semana
PEDIDA POR:  Chema, Lola, Menchu · 2026-11-17
```

#### A-006 · Identidad común provisional para nuestros documentos
```
QUÉ:         Un estilo común (tipografía libre, colores, cabecera) para todo lo que mandamos, sin
             esperar al nombre de la empresa. Y la guía de estilos previa, de 3–4 páginas.
POR QUÉ:     Hoy cada documento tiene un estilo distinto. Cuando llegue el nombre, solo cambia la cabecera.
ALTERNATIVA: Esperar al nombre.
URGENCIA:    esta semana
PEDIDA POR:  Lola · 2026-11-17
```

#### A-007 · Cómo probamos el Word en Microsoft Word
```
QUÉ:         Las casillas solo se han probado en LibreOffice.
PROPUESTA:   (Puri) Tú, con su lista de 10 minutos, una vez por versión de plantilla (no por cliente),
             en el ordenador y en el móvil. Y la comprobación automática que ya ha hecho Puri.
ALTERNATIVA: Usamos tu Word con una copia en /tmp. Abre ventanas y no prueba bien los clics.
URGENCIA:    esta semana
PEDIDA POR:  Puri, Reme, Lola · 2026-11-17
```

#### A-008 · Descargas e instalaciones gratuitas
```
QUÉ:         Todo a 0 € y en local:
             - fuentes Inter y Fraunces (licencia SIL OFL), en herramientas/fuentes/;
             - iconos Lucide (licencia ISC);
             - hunspell con el diccionario español de LibreOffice (corrector ortográfico);
             - whisper.cpp con un modelo, para transcribir notas de voz sin que salgan de la máquina;
             - Lighthouse 13.6.0 dentro de herramientas/ (npm, no global; Apache-2.0, unos 19 MB),
               para medir webs: §11 exige ≥ 90 antes de publicar.
POR QUÉ:     Los PDF dependen hoy de que Google responda; no hay corrector ortográfico; los clientes
             mandarán audios; sin Lighthouse no podemos cumplir §11.
PROPUESTA:   Aprobar las cinco. No hace falta arreglar los certificados del Python del sistema: Paco
             ya lo resuelve sin tocar la máquina (SSL_CERT_FILE).
URGENCIA:    esta semana (las fuentes y los iconos, para la ronda 2; Lighthouse, antes de la primera web)
PEDIDA POR:  Lola, Puri, Menchu, Paco · 2026-11-17
```

#### A-009 · Dónde viven los expedientes y los datos personales
```
QUÉ:         Confirmar clientes/<negocio>/ en este repositorio para expedientes y requisitos, y decidir
             dónde van fuera de git los datos personales (NIF, fotos, audios).
POR QUÉ:     Si un dato personal entra en el historial de git, borrarlo cuando el cliente lo pida (RGPD)
             es muy difícil.
PROPUESTA:   Depende de A-013. Si el repositorio pasa a privado: clientes/ en git, salvo una carpeta
             privado/ por cliente, excluida de git y con copia de seguridad aparte, para NIF, fotos
             de personas, audios y extracciones de webs. Lo de quien no contrata se borra a los 3 meses.
URGENCIA:    antes del primer cliente real
PEDIDA POR:  Reme, Menchu, Paco · 2026-11-17
```

#### A-014 · Gestor de secretos provisional: el llavero de macOS
```
QUÉ:         Guardar las claves de las API en el llavero, con la orden `security` de macOS
POR QUÉ:     Cualquier API (Places, Brave, PageSpeed) necesita una clave, y nunca puede ir en el código.
PROPUESTA:   (Paco) Tú metes cada clave una vez y las herramientas la leen. 0 €, sin instalar nada.
             Falta comprobar contigo que leerla no abre una ventana de permiso.
ALTERNATIVA: Un gestor de verdad (1Password, Bitwarden…): hay que instalarlo y quizá pagarlo.
URGENCIA:    esta semana, si apruebas las API de A-001
PEDIDA POR:  Paco · 2026-11-17
```

#### A-015 · Censo de competidores siendo una empresa (Overpass)
```
QUÉ:         El servidor principal de Overpass pide que el uso comercial vaya por servidores propios
             o de pago.
PROPUESTA:   (Paco) Usar una instancia que acepte cualquier proyecto, después de leer sus condiciones,
             y guardar siempre la consulta y la respuesta.
ALTERNATIVA: Descargar el extracto de la región de Geofabrik (gratis, ODbL) y filtrarlo en local.
             Hay que instalar osmium.
URGENCIA:    esta semana (antes de la ronda 2)
PEDIDA POR:  Paco · 2026-11-17
```

### Bloque 2 · Antes del primer cliente real

#### A-010 · Textos legales con un profesional (§15)
```
QUÉ:         - Cláusula de privacidad para el cuestionario: responsable, finalidad, base y derechos.
             - Modelo de consentimiento de imagen para clientes y niños.
             - Cómo mostrar reseñas de Google en las webs: módulo oficial en directo o permiso del autor.
             - Si podemos poner nombres y capturas de competidores en un documento comercial.
POR QUÉ:     Sin cláusula no se puede pedir ningún dato personal. Reseñas: derechos de autor, datos
             personales y directiva «Ómnibus».
PROPUESTA:   Un paquete único para quien revise los textos legales.
URGENCIA:    antes del primer cliente real
PEDIDA POR:  Reme, Puri, Chema, Menchu · 2026-11-17
```

#### A-011 · Política de precios pendiente (§8)
```
QUÉ:         - Qué contestamos a «¿cuánto cuesta?» en el primer contacto.
             - Dominio: dentro de la cuota de mantenimiento (propuesta de Reme) o aparte.
             - ¿Se puede contratar la creación sin mantenimiento?
             - Suscripción sin pago inicial: qué pasa en el mes 13.
             - ¿El vídeo entra en los planes?
POR QUÉ:     Reme no puede cerrar un presupuesto ni Menchu responder a la primera pregunta de todo cliente.
URGENCIA:    antes del primer cliente real
PEDIDA POR:  Reme, Menchu · 2026-11-17
```

#### A-012 · Seguimiento y plantillas
```
QUÉ:         - Dos recordatorios (a los 3 y a los 8 días laborables) y luego pausa.
             - Aprobar una sola vez las plantillas de primer contacto y recordatorio.
             - Un plazo interno para el primer envío.
POR QUÉ:     Lo que más alarga estos proyectos es esperar al cliente, y sin plazo no podemos decirle cuándo le escribimos.
PROPUESTA:   Lo de arriba. El primer envío de cada cliente sigue pasando por ti.
URGENCIA:    sin prisa
PEDIDA POR:  Menchu · 2026-11-17
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

### A-000 · Dónde se guardan la plantilla y los encargos
- **Decisión:** aprobada — 2026-11-17
- **Resultado:** carpeta `operacion/` en este repositorio, en Markdown y con git.
- **Pendiente de Iván:** actualizar el punto de AGENTS.md §15.

<!-- Siguiente ID libre: A-013 -->
