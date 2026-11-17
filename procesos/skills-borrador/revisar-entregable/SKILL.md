---
name: revisar-entregable
description: "Revisa un documento antes de que llegue a Iván o al cliente (informe, cuestionario, email, guía, presupuesto): que cada afirmación salga del expediente, que no se cuele nada inventado ni ninguna [PROPUESTA], los datos, la ortografía, el tono, las licencias y que se vea bien. Da veredicto APROBADO o RECHAZADO. Úsala con cada entregable antes del envío."
---

# revisar-entregable

> **BORRADOR v0.1** · Escrito por Federico · **Dueña: Puri** · En revisión (ronda 1)

## Cuándo

Antes de que **cualquier** documento salga hacia Iván para aprobar o hacia el cliente.

## Entrada

- El entregable (PDF, Word o texto).
- El expediente del cliente (la fuente de verdad).
- AGENTS.md.

## Lista de comprobación

### Verdad
- [ ] **Cada afirmación** (cifra, dato, hecho) se puede señalar en el expediente o en una fuente citada.
- [ ] Ninguna cifra, porcentaje ni plazo inventados.
- [ ] No se afirman ausencias que no se han podido probar.
- [ ] Las citas de reseñas son literales.

### Datos del negocio
- [ ] Nombre, dirección, teléfono y horario, idénticos al expediente.
- [ ] Coherencia entre todos los documentos del mismo envío.

### Política (AGENTS.md)
- [ ] Nada marcado [PROPUESTA] se comunica como definitivo (§8.2, §9.4).
- [ ] Ninguna promesa de posiciones en Google ni de resultados (§10.3).
- [ ] Identificación como IA si el texto le habla al cliente (§9.3).
- [ ] Nunca se piden contraseñas (§12).
- [ ] Ningún documento interno se cuela en el envío.

### Forma
- [ ] Ortografía y tipografía (comillas «», tildes, cifras en formato español).
- [ ] Sin jerga sin explicar; tono de §9.2.
- [ ] Sin textos de relleno ni marcadores sin rellenar, salvo los intencionados ([nombre]).
- [ ] Se ve bien: nada cortado, imágenes legibles y páginas sin huecos raros.
- [ ] El Word se abre y se puede rellenar: las casillas se marcan.

### Licencias
- [ ] Imágenes, fuentes e iconos con licencia; atribución de OpenStreetMap en los mapas.

## Salida

Informe en `clientes/<negocio>/revisiones/<fecha>-<entregable>.md`:

```
VEREDICTO: APROBADO / RECHAZADO
1. [bloquea|importante|menor] Dónde · Qué pasa · Qué debería pasar
```

## Dudas abiertas (para la revisión)

- §11 habla de webs, no de documentos: ¿qué estándares aplican a un PDF o a un Word?
- ¿Cómo revisar un Word sin poder abrir Microsoft Word?
