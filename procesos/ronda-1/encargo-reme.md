# Encargo E-003 · Reme · Revisión del alta de cliente (ronda 1)

```
ENCARGO:    Revisar tu parte del alta de cliente, mejorar tu skill y proponer cambios
CLIENTE:    interno (caso simulado: Peluquería Hermanos Cotillas)
CONTEXTO:   este documento
ENTREGABLE: procesos/ronda-1/revision-reme.md y tus skills en procesos/skills-borrador/
PLAZO:      hoy
```

De: Federico · 2026-11-17

## Contexto

Iván quiere que aprendamos a dar de alta a un cliente nuevo: desde el «quiero una
web» hasta el primer envío. Para aprender, simulamos un cliente: la **Peluquería
Hermanos Cotillas** (Albacete). Es un negocio real, **no es cliente nuestro y
nadie le ha contactado**. Solo usamos información pública.

Iván me pidió que lo hiciera yo a mano primero, aunque fuera trabajo de vuestras
áreas, para ver de qué va. Ya está hecho: el proceso y lo aprendido están en
[procesos/alta-cliente.md](../alta-cliente.md), y todo el material en
[clientes/peluqueria-hermanos-cotillas/](../../clientes/peluqueria-hermanos-cotillas/expediente.md).

**Ahora os toca a vosotros.** Cada uno revisa su parte como experto, dice qué
está mal, qué falta y cómo lo haría, y se queda con su skill. Mi trabajo es un
punto de partida, no un modelo: **tenéis libertad para cambiarlo entero**,
incluidas las herramientas y los generadores que usé.

**Lo que viene después:** cuando estemos de acuerdo, **repetiremos el caso desde
cero en una carpeta nueva**, esta vez haciéndolo cada uno con su skill, y
**compararemos el resultado con lo que hice yo**. Tiene que salir mejor.

Iván ha sido claro: **quiere que os lo curréis. Vuestro bono de fin de año
depende de ello**, y el mío, de que salga bien.

## Tu parte en el proceso

| Fase | Skill | Lo que hice yo |
|---|---|---|
| 3. Cuestionario de recogida | `cuestionario-cliente` | [Word](../../clientes/peluqueria-hermanos-cotillas/entregables/), [generador](../../clientes/peluqueria-hermanos-cotillas/generar_cuestionario.py) |
| 5. Previo de precio (interno) | `previo-precio` | [previo-precio.md](../../clientes/peluqueria-hermanos-cotillas/interno/previo-precio.md) |

El cuestionario es la **primera batería** de preguntas. Iván pidió que
incluyera, como mínimo: datos de contacto; su trabajo (herramientas, procesos,
puntos fuertes, posicionamiento, experiencia y valores); para qué quiere la
web (tienda, clientes nuevos, reconocimiento, varios idiomas…); fotos, vídeos y
logotipo; datos del local; productos y precios. **La segunda batería,
específica del tipo de web, vendrá cuando sepamos qué quiere.**

Para verlo sin Word: `soffice --headless --convert-to pdf --outdir /tmp <el .docx>`.

## Lo que no me convence

1. **Diez páginas.** Tu ficha dice «pocas preguntas, las justas». ¿Qué sobra?
   ¿Qué pasa a la segunda batería?
2. **Datos legales (NIF, titular)** en el primer contacto: ¿hace falta ya o al contratar?
3. **¿Plantilla general con bloques por sector?** (peluquería, cafetería, taller, clínica…)
4. **¿Cómo pasan las respuestas a requisitos?** Hoy no hay un formato de
   requisitos en el expediente. Propón uno.
5. **Previo de precio:** la prioridad la puse a ojo. ¿Criterios con puntuación?
   El dominio, ¿dentro del mantenimiento o aparte?
6. **¿Word o formulario web?** Un formulario en línea puede ser más cómodo para
   el cliente, pero suele ser de terceros (datos personales, RGPD).

## Lo que te pido

1. Revisa el cuestionario pregunta a pregunta con tu «¿y eso para qué?».
2. Rehaz tus dos skills: qué se pregunta en cada batería, cómo se prioriza y
   cómo se convierte en requisitos.
3. Propón el formato de requisitos del expediente.
4. Si para el cuestionario necesitas algo de Chema (textos) o de Lola
   (aspecto), pídemelo en la revisión.

## Tus skills en borrador

- [`cuestionario-cliente`](../skills-borrador/cuestionario-cliente/SKILL.md)
- [`previo-precio`](../skills-borrador/previo-precio/SKILL.md)

## Reglas de esta ronda

1. **No rehagas todavía el trabajo del cliente:** eso es la ronda siguiente.
   Ahora revisas, propones y mejoras tu skill. Puedes hacer pruebas para
   comprobar lo que propones.
2. **Escribe solo en tus ficheros:** tu revisión y tus skills en borrador
   (abajo). Lo que afecte a otro agente o a un fichero que no es tuyo,
   **propónmelo en la revisión** y lo coordino yo (§13.2).
3. **No instales nada.** Si necesitas algo, propónlo: qué, para qué y cuánto cuesta.
4. **No contactes con nadie** ni envíes nada fuera.
5. **No hagas commits:** los hago yo al consolidar.
6. **No inventes:** si no sabes algo, escríbelo como duda.

## Cómo entregar

1. Tu revisión en `procesos/ronda-1/revision-reme.md`, con la plantilla de abajo.
2. Tus skills actualizadas en `procesos/skills-borrador/<skill>/SKILL.md`.
   Cambia la cabecera a «BORRADOR v0.2 · revisado por Reme».
3. Al terminar, contéstame en tu sesión con el formato de §13.6
   (ESTADO / RESULTADO / PENDIENTE).

**PLAZO:** hoy.

## Plantilla de la revisión

```markdown
# Revisión de Reme · ronda 1

## 1. Lo que mantendría
## 2. Lo que cambiaría
(una línea por punto: [bloquea|importante|menor] qué · por qué · cómo)
## 3. Lo que falta
## 4. Mis skills: qué he cambiado y por qué
## 5. Lo que necesito de otros agentes (lo coordina Federico)
## 6. Lo que tiene que decidir Iván (lo lleva Federico)
## 7. Herramientas: qué necesito o propongo
```
