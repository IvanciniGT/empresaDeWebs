"""Genera el informe PDF de mercado y SEO local de la Peluquería Hermanos Cotillas.

Ejecutar desde la raíz del repositorio:
    .venv/bin/python clientes/peluqueria-hermanos-cotillas/generar_informe.py
"""
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
MAQUETA = AQUI / "maquetas" / "informe.html"
SALIDA = AQUI / "entregables" / "Informe de mercado y SEO local - Peluquería Hermanos Cotillas.pdf"
EMPRESA = "[Nombre de nuestra empresa]"  # pendiente de decidir (AGENTS.md §15)
FECHA = "Noviembre de 2026"

CSS = "../../../herramientas/informe.css"
CAP = "../recopilado/capturas"
COMP = "../competencia"

HTML = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Informe de mercado y SEO local · Peluquería Hermanos Cotillas</title>
<link rel="stylesheet" href="{CSS}">
</head><body>

<section class="portada">
  <div class="etiqueta">Estudio de mercado y SEO local</div>
  <h1>¿Cómo os encuentran en internet?</h1>
  <div class="sub">Lo que ve hoy alguien que busca peluquería en Albacete, cómo lo hacen
  vuestros competidores y lo que podéis ganar con una web propia.</div>
  <div class="cliente"><strong>Peluquería Hermanos Cotillas</strong>
  C/ Octavio Cuartero, 57 · Albacete</div>
  <div class="pie">{EMPRESA} · {FECHA}</div>
</section>

<section>
  <h2>En 30 segundos</h2>
  <div class="cifras">
    <div class="cifra"><b>281</b><span>peluquerías y barberías a menos de 1,5 km de la vuestra</span></div>
    <div class="cifra"><b>33</b><span>a menos de 250 metros: en vuestra misma manzana y las de al lado</span></div>
    <div class="cifra"><b>4,8★</b><span>vuestra nota en Google, con unas 132 opiniones</span></div>
    <div class="cifra"><b>0</b><span>páginas en internet que controléis vosotros</span></div>
  </div>
  <div class="caja acento">
    <h3>La conclusión</h3>
    <p>Tenéis lo más difícil de conseguir: <strong>clientes que os quieren desde hace más de
    30 años</strong> y lo dicen en público. Lo que os falta es un sitio en internet que sea
    vuestro, donde se cuente bien quiénes sois y desde donde sea fácil llamaros o pedir cita.</p>
    <p>Hoy, quien os busca encuentra una docena de directorios con textos escritos por una
    máquina, algunos con errores. Quien busca «peluquería» sin conoceros encuentra antes a
    otros.</p>
  </div>
  <h3>Lo que hemos revisado</h3>
  <ul class="check">
    <li>Todo lo publicado sobre vosotros: buscadores, directorios, opiniones y mapas.</li>
    <li>Las peluquerías y barberías de vuestro entorno, a partir de OpenStreetMap.</li>
    <li>Cómo se presentan en internet los competidores que mejor lo hacen.</li>
    <li>Qué hace que una peluquería aparezca en Google cuando alguien la busca en su barrio.</li>
  </ul>
</section>

<section class="pagina">
  <h2>1. Vuestra situación hoy</h2>
  <table>
    <tr><th style="width:30%">Dónde</th><th style="width:22%">Estado</th><th>Qué significa</th></tr>
    <tr><td>Web propia</td><td><span class="semaforo s-mal"></span>No existe</td>
      <td>No hay ningún sitio donde contéis vosotros quiénes sois, qué hacéis y a qué precio.</td></tr>
    <tr><td>Ficha de Google (Maps)</td><td><span class="semaforo s-bien"></span>Muy buena nota</td>
      <td>4,8 sobre 5 con unas 132 opiniones. Es vuestro gran activo, y no sabemos si la estáis gestionando.</td></tr>
    <tr><td>Redes sociales</td><td><span class="semaforo s-regular"></span>No encontradas</td>
      <td>No hemos encontrado Instagram ni Facebook. Si los tenéis, no se encuentran fácilmente.</td></tr>
    <tr><td>Reservas online (Treatwell, Booksy)</td><td><span class="semaforo s-regular"></span>No aparecéis</td>
      <td>Vuestros competidores más activos sí. No es imprescindible, pero es una vía de clientes nuevos.</td></tr>
    <tr><td>Directorios automáticos</td><td><span class="semaforo s-mal"></span>Más de 10, sin control</td>
      <td>Hablan de vosotros con textos inventados. No los podéis corregir, pero sí hacer que vuestra web salga por encima.</td></tr>
  </table>

  <div class="dos">
    <figure class="recorte"><img src="{CAP}/01-busqueda-bing.png">
      <figcaption>Al buscar vuestro nombre aparecen la ficha del mapa y una lista de directorios. Ninguna web vuestra.</figcaption></figure>
    <figure class="recorte"><img src="{CAP}/05-directorio-texto-inventado.png">
      <figcaption>Uno de esos directorios. Dice que hacéis maquillaje y peinados de evento, y convierte los «baños» de vuestra ficha de Google en una «zona de relax».</figcaption></figure>
  </div>

  <div class="caja aviso">
    <h3>Lo que dicen de vosotros páginas que no controláis</h3>
    <p>Entre los diez directorios que hemos revisado hay <strong>tres horarios distintos</strong>,
    servicios que probablemente no hacéis (alisados, maquillaje, peinados de novia) y hasta el barrio
    equivocado. Un cliente nuevo no sabe cuál creer. Una web propia, bien enlazada con vuestra ficha
    de Google, se convierte en la fuente de referencia.</p>
  </div>
</section>

<section class="pagina">
  <h2>2. Vuestro mercado: una calle llena de tijeras</h2>
  <div class="tres">
    <figure><img src="{COMP}/mapa-competencia.png">
      <figcaption>Cada punto es una peluquería o barbería registrada en OpenStreetMap. En naranja, las
      que se anuncian como barberías. En rojo, vosotros.</figcaption></figure>
    <div>
      <table>
        <tr><th>Distancia</th><th>Peluquerías</th><th>Barberías</th></tr>
        <tr><td>250 m</td><td>33</td><td>7</td></tr>
        <tr><td>500 m</td><td>89</td><td>16</td></tr>
        <tr><td>1 km</td><td>213</td><td>38</td></tr>
        <tr><td>1,5 km</td><td>281</td><td>48</td></tr>
      </table>
      <p class="nota">Las barberías son las que se identifican como tales en el mapa; seguramente
      hay más peluquerías de caballero entre el resto.</p>
    </div>
  </div>
  <div class="caja">
    <h3>Qué quiere decir esto</h3>
    <p>Con tanta oferta, nadie elige peluquería por ser la más cercana: hay otra a 50 metros. Se
    elige por <strong>confianza</strong> (opiniones, recomendación) y por <strong>comodidad</strong>
    (ver el horario y el precio, pedir cita sin llamar). En confianza vais muy por delante. En
    comodidad, hoy no competís.</p>
    <p>Además, 48 de esos negocios se anuncian como barberías: compiten por el mismo cliente
    masculino y, sobre todo, por el joven, que es el que busca en el móvil.</p>
  </div>
</section>

<section class="pagina">
  <h2>3. Cómo lo hacen los demás</h2>
  <p>Hemos analizado a cuatro competidores representativos: el que mejor lo hace en internet, uno
  con web propia, uno con una web abandonada y vuestro vecino más cercano.</p>

  <div class="ficha">
    <header><h3>NenaMelenas Peluquería &amp; BarberShop</h3><span class="nota">C/ Nicolás Belmonte, 1</span></header>
    <span class="chip si">Reserva online</span><span class="chip si">Precios publicados</span>
    <span class="chip si">5,0★ · 589 opiniones en Treatwell</span><span class="chip no">Sin web propia encontrada</span>
    <div class="tres" style="margin-top:8px">
      <div>
        <p>Es la primera del listado de peluquerías de Albacete en Treatwell. Todo su negocio online está
        en esa plataforma: <strong>precios a la vista</strong> (corte de hombre 16 €, niños y
        adolescentes 14 €, barba desde 16 €), <strong>cita en dos clics</strong> con los huecos
        libres del día, fotos del equipo y opiniones verificadas.</p>
        <p><strong>Lo que funciona:</strong> el cliente sabe qué cuesta y cuándo puede ir sin
        llamar. <strong>El precio que paga:</strong> la plataforma cobra comisión y el cliente
        es de Treatwell antes que suyo.</p>
      </div>
      <figure class="movil"><img src="{COMP}/capturas/nenamelenas-precios-movil.png">
        <figcaption>Sus precios en Treatwell, vistos en el móvil.</figcaption></figure>
    </div>
  </div>

  <div class="ficha">
    <header><h3>Salón Julia López</h3><span class="nota">salonjulia.es · a 800 m</span></header>
    <span class="chip si">Web propia</span><span class="chip si">WhatsApp</span>
    <span class="chip no">Sin reserva online</span><span class="chip no">Se rompe en el móvil</span>
    <div class="tres" style="margin-top:8px">
      <div>
        <p>Una de las pocas peluquerías de la zona con web propia. Secciones: Inicio, Servicios,
        Productos, Peinados, Nuestro salón y Contacto. Teléfono y WhatsApp siempre visibles, y
        algún precio orientativo (peinados de boda desde 40 €).</p>
        <p><strong>Fallos que se ven:</strong> en el móvil el contenido se sale de la pantalla por
        la derecha; el titular principal que lee Google es «INICIO»; y no incluye los datos de
        negocio local (dirección, horario, tipo de negocio) en el formato que Google entiende.</p>
      </div>
      <figure class="movil"><img src="{COMP}/capturas/julia-lopez-movil.png">
        <figcaption>Su web en el móvil: el texto y las fotos se cortan por la derecha.</figcaption></figure>
    </div>
  </div>
</section>

<section class="pagina">
  <div class="ficha">
    <header><h3>Peluquería Jesús Morote</h3><span class="nota">a 630 m</span></header>
    <span class="chip no">Web caída</span>
    <p style="margin-top:8px">OpenStreetMap todavía enlaza su web (peluqueriajesusmorote.com), pero el dominio ya
    no funciona. Quien pulsa ese enlace se encuentra un error. <strong>Una web abandonada resta
    más que no tener web</strong>: transmite que el negocio puede haber cerrado.</p>
  </div>
  <div class="ficha">
    <header><h3>Barber Shop Gentleman</h3><span class="nota">C/ Pérez Galdós, 48 · a 80 m</span></header>
    <span class="chip">Vuestro vecino más cercano</span><span class="chip no">Sin web propia encontrada</span>
    <p style="margin-top:8px">A una calle de vosotros y con un público parecido. Tampoco tiene web propia:
    <strong>el primero de los dos que tenga una web bien hecha se queda con las búsquedas del
    barrio</strong>.</p>
  </div>

  <h3>Lo que hacen los que mejor funcionan</h3>
  <table>
    <tr><th>Qué</th><th>Por qué importa</th><th>Vosotros hoy</th></tr>
    <tr><td>Precios visibles</td><td>El cliente nuevo no llama para preguntar: compara y elige.</td><td><span class="semaforo s-mal"></span>No</td></tr>
    <tr><td>Cita sin llamar</td><td>Hay clientes, sobre todo jóvenes, que prefieren no llamar: WhatsApp o reserva online.</td><td><span class="semaforo s-mal"></span>No</td></tr>
    <tr><td>Opiniones a la vista</td><td>Es lo que más convence a quien no os conoce.</td><td><span class="semaforo s-regular"></span>Solo en Google</td></tr>
    <tr><td>Fotos reales del local y del equipo</td><td>La gente quiere saber a dónde va y quién le va a cortar el pelo.</td><td><span class="semaforo s-mal"></span>No</td></tr>
    <tr><td>Bien en el móvil</td><td>Quien busca «peluquería cerca» suele hacerlo desde el móvil, en la calle.</td><td><span class="semaforo s-mal"></span>Sin web</td></tr>
    <tr><td>Una historia que contar</td><td>Lo que no se puede copiar. Ningún competidor la cuenta.</td><td><span class="semaforo s-bien"></span>La tenéis, sin contar</td></tr>
  </table>
</section>

<section class="pagina">
  <h2>4. SEO local: cómo os encuentra alguien que no os conoce</h2>
  <p>El SEO local es lo que hace que Google os muestre cuando alguien de vuestra zona busca lo que
  ofrecéis. Google se fija sobre todo en tres cosas:</p>
  <div class="dos">
    <div class="caja"><h3>1. Que seáis relevantes</h3>
      <p>Que vuestra web y vuestra ficha digan con claridad qué hacéis: «peluquería de caballero»,
      «corte de niño», «barba»… Hoy esa información la dan directorios, y mal.</p></div>
    <div class="caja"><h3>2. Que estéis cerca</h3>
      <p>Esto no se puede cambiar, y en vuestro caso juega a favor: estáis en una zona céntrica
      de Albacete.</p></div>
    <div class="caja"><h3>3. Que tengáis buena fama</h3>
      <p>Número y nota de opiniones, y que otras webs hablen de vosotros con datos coherentes.
      Aquí ya partís con ventaja.</p></div>
    <div class="caja"><h3>4. Que todo cuadre</h3>
      <p>Mismo nombre, dirección, teléfono y horario en todas partes. Hoy hay tres horarios
      distintos en internet.</p></div>
  </div>

  <h3>Búsquedas en las que deberíais aparecer</h3>
  <table>
    <tr><th>Búsqueda</th><th>Quién la hace</th></tr>
    <tr><td>peluquería caballero Albacete</td><td>Hombres que buscan peluquería nueva o están de paso</td></tr>
    <tr><td>peluquería cerca de mí</td><td>Cualquiera desde el móvil, en el centro</td></tr>
    <tr><td>peluquería niños Albacete</td><td>Padres y madres; vuestras opiniones hablan mucho de niños</td></tr>
    <tr><td>barbería Albacete / arreglo de barba</td><td>Clientes jóvenes</td></tr>
    <tr><td>peluquería barrio Feria / Octavio Cuartero</td><td>Vecinos de la zona</td></tr>
    <tr><td>hermanos cotillas</td><td>Quien ya os conoce: hoy acaba en un directorio</td></tr>
  </table>
  <p class="nota">No hemos medido cuántas veces se hace cada búsqueda al mes: hace falta una
  herramienta de pago y, para un negocio de barrio, importa más estar que la cifra exacta.</p>

  <div class="caja aviso">
    <h3>Lo que no os vamos a prometer</h3>
    <p>Nadie puede garantizar una posición concreta en Google, y desconfiad de quien lo haga.
    Lo que sí podemos hacer es ponerlo todo de vuestra parte para que Google entienda quiénes sois,
    dónde estáis y por qué os recomiendan.</p>
  </div>
</section>

<section class="pagina">
  <h2>5. Lo que proponemos</h2>
  <div class="paso"><b>1</b><div><strong>Una web propia, sencilla y rápida, pensada para el móvil.</strong>
    Quiénes sois, vuestra historia, servicios y precios, horario, mapa, fotos reales y botones para
    llamar o escribir por WhatsApp con un toque.</div></div>
  <div class="paso"><b>2</b><div><strong>Vuestra ficha de Google, revisada y al día.</strong>
    Horario correcto, servicios, fotos y enlace a la web. Es lo primero que ve quien os busca.</div></div>
  <div class="paso"><b>3</b><div><strong>Vuestras opiniones, a la vista.</strong>
    Tal cual están en Google, sin retocar. Hablan mejor de vosotros que cualquier texto.</div></div>
  <div class="paso"><b>4</b><div><strong>Datos que cuadren en todas partes.</strong>
    La web lleva vuestros datos en el formato que entiende Google, para que sea la fuente de
    referencia por encima de los directorios.</div></div>
  <div class="paso"><b>5</b><div><strong>Vuestra dirección en internet: hermanoscotillas.es.</strong>
    Hemos comprobado que parece libre. Se registra a vuestro nombre: es vuestra, pase lo que pase.</div></div>

  <h3>Lo que dicen vuestros clientes (y lo que diría vuestra web)</h3>
  <blockquote>«Llevo casi toda mi vida pelando allí… primero con sus padres y ahora con sus hijos.»</blockquote>
  <blockquote>«Te cortan el pelo a tu gusto sin que peligren tus orejas, y dejándote "listo para triunfar".»</blockquote>
  <p class="nota">Opiniones reales publicadas en Google por vuestros clientes.</p>

  <div class="caja acento">
    <h3>Siguiente paso</h3>
    <p>Junto a este informe os enviamos un cuestionario con lo que ya sabemos de vosotros y lo que
    nos falta. Con vuestras respuestas os preparamos un presupuesto cerrado, por escrito y sin
    letra pequeña.</p>
  </div>
</section>

<section class="pagina">
  <h2>Cómo hemos hecho este informe</h2>
  <table>
    <tr><th style="width:32%">Fuente</th><th>Para qué la hemos usado</th></tr>
    <tr><td>OpenStreetMap</td><td>Ubicación del local y censo de peluquerías y barberías en 1,5 km
      (consulta del 17/11/2026). Datos © colaboradores de OpenStreetMap, licencia ODbL.</td></tr>
    <tr><td>Bing</td><td>Qué aparece al buscar vuestro nombre.</td></tr>
    <tr><td>Directorios de peluquerías</td><td>Datos publicados sobre vosotros y opiniones de Google
      que reproducen.</td></tr>
    <tr><td>Treatwell</td><td>Competidores con reserva online, sus precios y opiniones.</td></tr>
    <tr><td>Webs de los competidores</td><td>Estructura, contenido y aspectos técnicos básicos.</td></tr>
  </table>
  <h3>Límites</h3>
  <ul>
    <li>Los datos de OpenStreetMap los mantienen voluntarios: puede haber negocios cerrados o que
    falten. Las cifras son orientativas, pero el orden de magnitud es fiable.</li>
    <li>No hemos podido consultar Google directamente: bloquea las consultas automáticas.</li>
    <li>No hemos medido volúmenes de búsqueda.</li>
    <li>Las capturas son de noviembre de 2026; las webs cambian.</li>
  </ul>
  <p class="nota" style="margin-top:20mm">Informe preparado por {EMPRESA} con la ayuda de asistentes
  de inteligencia artificial.</p>
</section>

</body></html>
"""


def main():
    MAQUETA.parent.mkdir(parents=True, exist_ok=True)
    MAQUETA.write_text(HTML, encoding="utf-8")
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([str(RAIZ / "herramientas/html_a_pdf.sh"), str(MAQUETA), str(SALIDA)], check=True)


if __name__ == "__main__":
    main()
