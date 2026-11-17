# Encargo E-005 · Paco · Revisión del alta de cliente (ronda 1)

```
ENCARGO:    Revisar tu parte del alta de cliente, mejorar tu skill y proponer cambios
CLIENTE:    interno (caso simulado: Peluquería Hermanos Cotillas)
CONTEXTO:   este documento
ENTREGABLE: procesos/ronda-1/revision-paco.md y tus skills en procesos/skills-borrador/
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

En esta fase no se construye ninguna web, pero **todo el proceso se apoya en
herramientas**, y eso es tuyo. Te propongo dos cosas:

| Qué | Skill | Estado |
|---|---|---|
| Mantener las herramientas comunes | `herramientas-comunes` | Hechas por mí, funcionan con limitaciones: [herramientas/](../../herramientas/) |
| Extraer la web actual de un cliente | `extraer-web-existente` | **Sin hacer.** El cliente simulado no tenía web, pero es lo primero que pidió Iván: «si ya tiene web, nos la tragamos». |

Los generadores de cada documento (`clientes/.../generar_*.py`) son de cada
dueño (Chema, Reme, Lola). Tú mantienes las piezas comunes que usan.

## Lo que no me convence

1. **`captura.sh`:** salen los avisos de cookies y no hace página completa.
   Por ejemplo, en [la captura de Treatwell](../../clientes/peluqueria-hermanos-cotillas/competencia/capturas/nenamelenas-treatwell-movil.png)
   tuve que recortar y aclarar a mano.
2. **`buscar.sh`:** en la práctica no sirve (ver «Lo que no funciona» en
   [alta-cliente.md](../alta-cliente.md)). Chema propondrá qué fuentes quiere;
   tú, cómo se hace técnicamente.
3. **El Python de python.org no tiene certificados raíz:** lo esquivé con `curl`.
   ¿Arreglarlo? Sería un cambio en la máquina de Iván: propónlo, no lo hagas.
4. **No hay `requirements.txt`** del `.venv`.
5. **El Word solo se ha probado en LibreOffice.** Las casillas son controles de
   contenido `w14`. ¿Se puede asegurar que funcionan en Word?
6. **Lighthouse** para medir las webs de la competencia: ¿merece la pena?
7. **Uso de servicios gratuitos de OpenStreetMap** (teselas, Overpass, Nominatim):
   revisa que cumplimos sus políticas de uso.

## Lo que te pido

1. Revisa y prueba todas las herramientas. Arregla lo que se pueda **sin
   instalar nada**: en esta ronda puedes tocar `herramientas/`, sin romper los
   generadores que ya existen.
2. Diseña `extraer-web-existente`: con qué, qué saca, dónde lo deja y **cómo se
   prueba sin descargar webs de terceros que no son clientes** (por ejemplo,
   con una web de prueba local).
3. Rehaz tus dos skills.
4. Lo que necesite instalación, con su propuesta para Iván.

## Tus skills en borrador

- [`herramientas-comunes`](../skills-borrador/herramientas-comunes/SKILL.md)
- [`extraer-web-existente`](../skills-borrador/extraer-web-existente/SKILL.md)

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

1. Tu revisión en `procesos/ronda-1/revision-paco.md`, con la plantilla de abajo.
2. Tus skills actualizadas en `procesos/skills-borrador/<skill>/SKILL.md`.
   Cambia la cabecera a «BORRADOR v0.2 · revisado por Paco».
3. Al terminar, contéstame en tu sesión con el formato de §13.6
   (ESTADO / RESULTADO / PENDIENTE).

**PLAZO:** hoy.

## Plantilla de la revisión

```markdown
# Revisión de Paco · ronda 1

## 1. Lo que mantendría
## 2. Lo que cambiaría
(una línea por punto: [bloquea|importante|menor] qué · por qué · cómo)
## 3. Lo que falta
## 4. Mis skills: qué he cambiado y por qué
## 5. Lo que necesito de otros agentes (lo coordina Federico)
## 6. Lo que tiene que decidir Iván (lo lleva Federico)
## 7. Herramientas: qué necesito o propongo
```
