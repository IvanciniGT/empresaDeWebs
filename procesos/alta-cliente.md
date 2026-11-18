# Alta de un cliente nuevo: de «quiero una web» al presupuesto

> **v0.2 · 2026-11-18 · Federico.** Proceso acordado con los seis agentes en la
> ronda 1 ([consolidación](ronda-1/consolidacion.md)) y con las decisiones de Iván
> ([bandeja](../operacion/aprobaciones.md), A-001 a A-015). La v0.1 fue la que
> hice yo a mano: Puri la rechazó con 10 errores que bloquean, 35 importantes y
> 21 menores ([veredicto](../clientes/peluqueria-hermanos-cotillas/revisiones/2026-11-17-primer-envio.md)).
>
> El **cómo** de cada fase está en la skill de su dueño, en
> [skills-borrador/](skills-borrador/). Este documento dice **qué, quién y en
> qué orden**.

## 1. Qué entra y qué sale

**Entra:** alguien escribe diciendo «quiero una web».

**Sale, antes de pedirle nada más:** un mensaje por WhatsApp con un informe
corto de su situación en internet (gratis y sin compromiso) y la tanda A de
preguntas, las justas para darle un presupuesto cerrado.

| Entregable | Dueño | ¿Al cliente? |
|---|---|---|
| Expediente: datos comprobados, por confirmar y «lo que intuimos» | Chema | No |
| Previo de precio | Reme | No |
| Informe de 2 páginas más un anexo, en A5 | Chema (contenido) y Lola (maqueta) | **Sí** |
| Tanda A: guion de WhatsApp, y Word como copia por correo | Reme (qué se pregunta) y Menchu (cómo se dice) | **Sí** |
| Guía de estilos previa (3–4 páginas, como hipótesis) | Lola | No, hasta que contrate |
| Requisitos y borrador de presupuesto | Reme | No, hasta que lo apruebe Iván |

## 2. Fases

```
0 Primer contacto ─► 1 Investigar ─┬─► 2 Competencia e informe ─┐
                                    ├─► 3 Previo de precio ─► 4 Tanda A ─┤
                                    └─► 5 Guía previa (interna)          ├─► 6 Revisión ─► 7 Iván ─► 8 Envío ─► 9 Seguimiento ─► 10 Requisitos y presupuesto
```

| # | Fase | Dueño | Skill | Termina cuando |
|---|---|---|---|---|
| 0 | Primer contacto: se presenta como IA, comprueba el encaje y recoge lo mínimo (cinco preguntas) | Menchu | `primer-contacto` | Expediente abierto con la petición literal |
| 1 | Investigar: su web (si la tiene, la extrae Paco), ficha y mapas, directorios, reseñas y redes. **Captura manual de Google, la hace Iván** (A-001) | Chema (+ Paco, + Iván) | `investigar-cliente`, `extraer-web-existente` | Expediente con fuentes, fechas y niveles de fiabilidad |
| 2 | Competencia e informe: censo con Overpass (A-015), competidores con criterio, cifras calculadas por script | Chema + Lola | `estudio-competencia`, `textos-web`, `estilo-documentos` | Informe A5 generado |
| 3 | Previo de precio: plan, escenarios y prioridad. **Va antes de la tanda A** | Reme | `previo-precio` | Qué preguntas condicionales activa |
| 4 | Tanda A: 8 obligatorias, condicionales según el caso y la foto de la fachada, opcional | Reme + Menchu | `cuestionario-cliente`, guion en `primer-envio` | Guion y Word generados |
| 5 | Guía previa: hipótesis de estilo con el contraste comprobado | Lola | `guia-estilos-previa` | PDF interno |
| 6 | **Revisión hasta APROBADO**, con re-revisión de los arreglos | Puri | `revisar-entregable` | APROBADO |
| 7 | Aprobación del primer envío | Federico → Iván | — | Iván dice sí |
| 8 | Envío: **WhatsApp primero**, correo como copia; Iván copia y pega (A-003) | Menchu | `primer-envio` | Enviado; fecha del siguiente contacto en `encargos.md` |
| 9 | Seguimiento: recordatorios a los 3 y a los 8 días laborables, después pausa (A-012). Respuestas, en `privado/` | Menchu | `primer-envio` | Respuestas de la tanda A recibidas, o pausa |
| 10 | Requisitos y borrador de presupuesto | Reme | `cuestionario-cliente` (`requisitos.md`) | Borrador para Iván |

Las fases 2, 3 y 5 pueden ir en paralelo. La 4 espera a la 3.

## 3. Reglas

1. **Fuentes con nivel.** Un dato está comprobado si lo da una fuente primaria (el
   negocio o su ficha de Google) o dos independientes. **Dos copias de lo mismo
   cuentan como una sola fuente.** Una reseña es una pista, no un dato: se
   convierte en pregunta.
2. **Toda afirmación sale del expediente**, y **toda cifra, de un script** sobre
   datos guardados, con su fecha.
3. **No se afirman ausencias** («no hemos encontrado», nunca «no tenéis»).
4. **No se promete nada que no hagamos:** ni llamadas (A-002), ni posiciones en
   Google, ni plazos o precios marcados [PROPUESTA].
5. **Solo lo necesario, y cuando haga falta.** Datos legales, fotos y aprobación de
   textos, a la tanda B, después de aceptar el presupuesto.
6. **El repositorio es público (A-013).** Ningún dato personal en git: va a
   `clientes/<negocio>/privado/`. Lo de quien no contrata se borra a los 3 meses.
7. **Ningún robot contra buscadores** ni contra lo que prohíba un `robots.txt`.
8. **Nada sale sin el APROBADO de Puri** y sin el sí de Iván.

## 4. Herramientas

En [herramientas/](../herramientas/). Las mantiene Paco (`herramientas-comunes`).
Pruebas: `node herramientas/pruebas/probar.mjs`. Para reconstruir lo que no está
en git: `herramientas/instalar.sh`.

## 5. Cómo se mide si sale mejor

Lo mide Puri con `comparar.py` (su skill, «Comparar dos versiones»):

- errores por gravedad en la primera entrega;
- afirmaciones sin fuente;
- regresiones;
- si llega a APROBADO y en cuántas vueltas;
- si el cliente recibe los ocho mensajes clave.

Base (la v0.1): **10 errores que bloquean, 35 importantes y 21 menores; 36 afirmaciones sin fuente.**

## 6. Pendiente

- Política de precios (A-011): sin ella no hay presupuesto real ni respuesta a «¿cuánto cuesta?».
- Textos legales (A-010): sin cláusula de privacidad no se puede enviar a un cliente real.
- Nombre de la empresa, teléfono y correo (§15).
- Pasar las skills de `procesos/skills-borrador/` a `.github/skills/` cuando la ronda 2 las valide.
