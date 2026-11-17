# Encargo E-004 · Lola · Revisión del alta de cliente (ronda 1)

```
ENCARGO:    Revisar tu parte del alta de cliente, mejorar tu skill y proponer cambios
CLIENTE:    interno (caso simulado: Peluquería Hermanos Cotillas)
CONTEXTO:   este documento
ENTREGABLE: procesos/ronda-1/revision-lola.md y tus skills en procesos/skills-borrador/
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
| 4. Guía de estilos previa (interna) | `guia-estilos-previa` | [PDF](../../clientes/peluqueria-hermanos-cotillas/interno/), [generador](../../clientes/peluqueria-hermanos-cotillas/generar_guia_estilos.py) |
| Aspecto de lo que mandamos al cliente | (sin skill todavía) | [informe.css](../../herramientas/informe.css), [docx_util.py](../../herramientas/docx_util.py), informe y cuestionario en [entregables/](../../clientes/peluqueria-hermanos-cotillas/entregables/) |

La guía **no se envía** hasta que el cliente contrate. Iván: «no le regalamos
el diseño; el informe de SEO sí, para que flipe y nos contrate».

## Lo que no me convence

1. **Diseñé sin ver el local ni el rótulo.** Concepto «Oficio de familia», tinta,
   papel y cobre. ¿Tiene sentido una guía previa sin eso? ¿Qué hacemos cuando
   lleguen sus fotos?
2. **Nivel de detalle antes de contratar:** llegué hasta un boceto móvil. ¿Sobra o falta?
3. **Iconos dibujados a mano** en SVG. ¿Un juego libre (Lucide, ISC)?
4. **Fuentes:** Fraunces e Inter (SIL OFL). En el PDF se cargan de Google al
   generarlo; en la web irían alojadas en nuestro servidor.
5. **Nuestros documentos no tienen identidad propia:** el informe va en azul y
   naranja, la guía en tinta y cobre, el Word en otra cosa. ¿Una plantilla de
   empresa? (Aún no tenemos nombre: §15.)
6. **El mapa de competencia, el informe y el cuestionario:** ¿se entienden y se
   leen bien? Mira sobre todo el Word en móvil: muchos clientes lo abrirán ahí.

## Lo que te pido

1. Revisa la guía como directora de arte y como experta en accesibilidad.
2. Rehaz tu skill: qué incluye la guía previa y qué no, y cómo se hace.
3. Revisa el aspecto del informe y del cuestionario y propón mejoras concretas.
   Si tocan herramientas comunes (`informe.css`, `docx_util.py`), propónlas: las
   mantiene Paco.
4. Di si quieres una skill más (por ejemplo, para el estilo de nuestros documentos).

## Tus skills en borrador

- [`guia-estilos-previa`](../skills-borrador/guia-estilos-previa/SKILL.md)

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

1. Tu revisión en `procesos/ronda-1/revision-lola.md`, con la plantilla de abajo.
2. Tus skills actualizadas en `procesos/skills-borrador/<skill>/SKILL.md`.
   Cambia la cabecera a «BORRADOR v0.2 · revisado por Lola».
3. Al terminar, contéstame en tu sesión con el formato de §13.6
   (ESTADO / RESULTADO / PENDIENTE).

**PLAZO:** hoy.

## Plantilla de la revisión

```markdown
# Revisión de Lola · ronda 1

## 1. Lo que mantendría
## 2. Lo que cambiaría
(una línea por punto: [bloquea|importante|menor] qué · por qué · cómo)
## 3. Lo que falta
## 4. Mis skills: qué he cambiado y por qué
## 5. Lo que necesito de otros agentes (lo coordina Federico)
## 6. Lo que tiene que decidir Iván (lo lleva Federico)
## 7. Herramientas: qué necesito o propongo
```
