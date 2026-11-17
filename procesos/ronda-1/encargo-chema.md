# Encargo E-002 · Chema · Revisión del alta de cliente (ronda 1)

```
ENCARGO:    Revisar tu parte del alta de cliente, mejorar tu skill y proponer cambios
CLIENTE:    interno (caso simulado: Peluquería Hermanos Cotillas)
CONTEXTO:   este documento
ENTREGABLE: procesos/ronda-1/revision-chema.md y tus skills en procesos/skills-borrador/
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

Eres quien más pesa en esta fase:

| Fase | Skill | Lo que hice yo |
|---|---|---|
| 1. Investigar al cliente | `investigar-cliente` | [expediente.md](../../clientes/peluqueria-hermanos-cotillas/expediente.md), [capturas](../../clientes/peluqueria-hermanos-cotillas/recopilado/capturas/) |
| 2. Competencia y SEO local | `estudio-competencia` | [informe PDF](../../clientes/peluqueria-hermanos-cotillas/entregables/), [datos y mapa](../../clientes/peluqueria-hermanos-cotillas/competencia/), [generador](../../clientes/peluqueria-hermanos-cotillas/generar_informe.py) |
| 3. Textos propuestos del cuestionario | (dentro de `cuestionario-cliente`, que es de Reme) | Sección 8 del [cuestionario](../../clientes/peluqueria-hermanos-cotillas/entregables/) y de [generar_cuestionario.py](../../clientes/peluqueria-hermanos-cotillas/generar_cuestionario.py) |

## Lo que no me convence (revísalo con lupa)

1. **El buscador.** Google bloquea, DuckDuckGo pide captcha y Bing en segundo
   plano devuelve resultados al azar en cuanto la búsqueda no es un nombre
   exacto. No pude comprobar redes sociales ni encontrar competidores por
   búsqueda (los saqué de OpenStreetMap). **¿Cómo lo resolverías?** Si la
   solución cuesta dinero o abre ventanas, la decide Iván: dame las opciones
   con lo que cuesta cada una.
2. **La ficha de Google Business Profile** no la pude leer directamente: la nota
   y el número de opiniones salen de directorios que la copian.
3. **Búsquedas objetivo sin volumen:** las puse a ojo. ¿Hay forma gratuita y
   honesta de estimarlo?
4. **El informe:** nueve páginas. ¿Es demasiado para un peluquero? ¿Estamos
   regalando la estrategia? Iván lo quiere para que el cliente «flipe» y nos
   contrate.
5. **Elección de competidores:** NenaMelenas es unisex y no es exactamente su
   público. ¿Qué criterio usarías?
6. **Los textos propuestos.** «Le cortamos el pelo a tu padre. Ahora, a ti.»,
   «más de 30 años» (sale de una reseña de «34 años») y «Puntuales: si tienes
   cita, no esperas» (sale de **una** reseña que dice «siempre puntuales»).
   ¿Me he pasado de inferir?
7. **Reseñas:** las cito en el informe y en el cuestionario. ¿Bien así? ¿Y en
   la web, con qué permisos?

## Lo que te pido

1. Revisa el expediente, el informe y los textos como lo haría el mejor SEO
   local del país.
2. Rehaz tus dos skills a tu manera: pasos, reglas, fuentes y criterios.
3. Decide si los textos propuestos merecen una skill propia (por ejemplo,
   `textos-propuestos`) o van dentro de otra.
4. Propón cómo resolver la búsqueda (punto 1). **Es lo más urgente.**

## Tus skills en borrador

- [`investigar-cliente`](../skills-borrador/investigar-cliente/SKILL.md)
- [`estudio-competencia`](../skills-borrador/estudio-competencia/SKILL.md)

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

1. Tu revisión en `procesos/ronda-1/revision-chema.md`, con la plantilla de abajo.
2. Tus skills actualizadas en `procesos/skills-borrador/<skill>/SKILL.md`.
   Cambia la cabecera a «BORRADOR v0.2 · revisado por Chema».
3. Al terminar, contéstame en tu sesión con el formato de §13.6
   (ESTADO / RESULTADO / PENDIENTE).

**PLAZO:** hoy.

## Plantilla de la revisión

```markdown
# Revisión de Chema · ronda 1

## 1. Lo que mantendría
## 2. Lo que cambiaría
(una línea por punto: [bloquea|importante|menor] qué · por qué · cómo)
## 3. Lo que falta
## 4. Mis skills: qué he cambiado y por qué
## 5. Lo que necesito de otros agentes (lo coordina Federico)
## 6. Lo que tiene que decidir Iván (lo lleva Federico)
## 7. Herramientas: qué necesito o propongo
```
