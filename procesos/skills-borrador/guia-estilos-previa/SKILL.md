---
name: guia-estilos-previa
description: "Prepara una guía de estilos previa e interna para la web de un cliente nuevo (concepto, colores con contraste comprobado, tipografías, iconos, logotipo tipográfico, fotografía, tono y boceto móvil) para adelantar el diseño y el presupuesto. No se envía hasta que el cliente contrate. Úsala cuando el expediente tiene la información pública recopilada."
---

# guia-estilos-previa

> **BORRADOR v0.1** · Escrito por Federico · **Dueña: Lola** · En revisión (ronda 1)

## Cuándo

En paralelo con el cuestionario, cuando ya sabemos quién es el cliente.
**No se envía:** es trabajo de diseño que se entrega cuando contrata.

## Entrada

- Expediente: quién es, qué le hace especial, su público, su local.
- Capturas de su presencia actual y de la competencia (para diferenciarse).

## Contenido

1. **Concepto** en dos palabras y qué transmitir o evitar, con su porqué.
2. **Colores:** 4–6 con nombre, código y uso. **Tabla de contrastes WCAG 2.2 AA**
   calculada (4,5 : 1 texto normal; 3 : 1 texto grande).
3. **Tipografías** con licencia libre, muestras y tamaños para móvil y ordenador.
4. **Iconos:** estilo y muestras, con licencia.
5. **Logotipo tipográfico** provisional, si no tiene logotipo.
6. **Boceto móvil** de la portada y estructura de secciones.
7. **Fotografía:** sí y no.
8. **Tono de comunicación:** «así sí / así no».

## Pasos

1. Partir de lo que ya tenga el cliente (rótulo, colores del local, logotipo). Si
   no hay nada, proponer algo sencillo.
2. Mirar la competencia para **no parecerse** a ella.
3. Calcular los contrastes con la fórmula WCAG (está en el generador).
4. Maquetar en HTML y convertir a PDF con `herramientas/html_a_pdf.sh`.
5. Sello «INTERNO · NO ENVIAR AL CLIENTE» en cada página.

## Reglas

1. **La identidad es del cliente:** si tiene colores o rótulo, mandan.
2. **Solo recursos con licencia** (§10.3). Anotar la licencia de cada uno.
3. **En la web real, las fuentes se alojan en nuestro servidor,** sin cargarlas
   de Google (RGPD).
4. **Ningún color de texto sin contraste AA.**
5. El logotipo de verdad no entra en la creación (§6.1): solo se propone uno
   tipográfico provisional.

## Salida

- `interno/Guía de estilos previa - INTERNO - <negocio>.pdf`

## Dudas abiertas (para la revisión)

- ¿Tiene sentido hacerla sin haber visto el local ni el rótulo?
- ¿Cuánto detalle antes de que contrate: concepto y colores, o hasta el boceto?
- ¿Estilo propio de la empresa para los documentos que mandamos (informe, cuestionario)?
