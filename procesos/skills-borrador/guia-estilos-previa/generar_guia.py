"""Genera la guía de estilos previa (interna) de un cliente a partir de un JSON.

Plantilla de la skill guia-estilos-previa (Lola). El diseño vive aquí; los datos
de cada cliente, en su JSON. El JSON y el PDF van en una carpeta que no entra en
git: el repositorio es público (A-013).

Uso:
    .venv/bin/python procesos/skills-borrador/guia-estilos-previa/generar_guia.py datos.json salida.pdf

Se niega a generar (sale con 1) si algún color de texto no llega a 4,5 : 1, si
un elemento que no es texto no llega a 3 : 1, o si la acción principal del
esquema no es un canal comprobado. Son reglas de la skill: mejor que lo pare el
script que confiar en acordarse.
"""
import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(AQUI))
from contraste import contraste, veredicto, _coma  # noqa: E402

TEXTO, NO_TEXTO = 4.5, 3.0

# Papel de cada color en la web. «detalle» es solo decoración: no se le exige nada.
PAPELES = ("texto", "fondo", "superficie", "accion", "texto_accion", "secundario", "detalle")

# (delante, fondo, mínimo, para qué)
PARES = (
    ("texto", "fondo", TEXTO, "Texto sobre el fondo"),
    ("texto", "superficie", TEXTO, "Texto sobre tarjetas"),
    ("texto_accion", "accion", TEXTO, "Texto del botón principal"),
    ("accion", "fondo", TEXTO, "Enlaces y texto de acento"),
    ("accion", "superficie", TEXTO, "Enlaces sobre tarjetas"),
    ("secundario", "fondo", TEXTO, "Horario, notas"),
    ("secundario", "superficie", TEXTO, "Notas sobre tarjetas"),
    ("accion", "fondo", NO_TEXTO, "Borde del botón y del foco"),
    ("texto", "fondo", NO_TEXTO, "Borde del botón secundario, iconos"),
)

FOTOS = (
    ("Fachada de día, con el rótulo", "Portada y «cómo llegar»", "2000 px, horizontal y con aire"),
    ("Interior entero", "Quiénes somos", "1200 px"),
    ("El equipo, junto", "Quiénes somos", "1000 px"),
    ("Cada uno trabajando", "Servicios", "1200 px"),
    ("Detalles del oficio o del producto", "Servicios, galería", "1200 px"),
    ("Fotos antiguas del negocio (si las hay)", "Historia", "La mejor que tengan; escaneadas o de frente, sin reflejos"),
)

TAMANOS = (
    ("Texto", "17 px (mínimo 16), interlineado 1,5", "18 px, interlineado 1,5"),
    ("Notas y pies", "≥ 14 px", "≥ 14 px"),
    ("Titular principal", "30–34 px", "48–56 px"),
    ("Títulos de sección", "24 px", "32–36 px"),
    ("Botones", "17 px en negrita (necesita 4,5 : 1: no es texto grande)", "17 px"),
    ("Áreas de toque", "≥ 44 × 44 px", "—"),
    ("Ancho de línea", "—", "60–75 caracteres"),
)


def e(texto):
    return html.escape(str(texto), quote=True)


def comprobar(datos):
    """Errores que impiden generar la guía."""
    errores = []
    paleta = datos["paleta"]
    for papel in PAPELES:
        if papel not in paleta:
            errores.append(f"falta el color con papel «{papel}»")
    if errores:
        return errores, []
    filas = []
    for delante, fondo, minimo, para in PARES:
        r = contraste(paleta[delante]["hex"], paleta[fondo]["hex"])
        filas.append((delante, fondo, minimo, para, r))
        if r < minimo:
            errores.append(f"{para}: {paleta[delante]['nombre']} sobre {paleta[fondo]['nombre']} "
                           f"da {_coma(r)} : 1 y necesita {_coma(minimo)} : 1")
    accion = datos["accion_principal"]
    if not accion.get("comprobado"):
        errores.append(f"la acción principal («{accion['etiqueta']}») usa un canal sin comprobar: "
                       "usad el teléfono hasta que el cliente confirme otro (regla 3)")
    return errores, filas


PESOS = {"Thin": 100, "ExtraLight": 200, "Light": 300, "Regular": 400, "Medium": 500,
         "SemiBold": 600, "Bold": 700, "ExtraBold": 800, "Black": 900}


def _fuentes(datos):
    """Fuentes de herramientas/fuentes/<familia>/ si están; si no, Google (se acepta
    solo porque la guía es interna; en la web, nunca). `prefijo` elige el corte
    cuando hay varios: Fraunces trae Fraunces9pt (texto) y Fraunces72pt (titulares)."""
    locales = RAIZ / "herramientas" / "fuentes"
    reglas, remotas = [], []
    vistas = set()
    for clave in ("titulares", "texto"):
        tipo = datos["tipografias"][clave]
        familia = tipo["familia"]
        prefijo = tipo.get("prefijo", familia.replace(" ", ""))
        if (familia, prefijo) in vistas:
            continue
        vistas.add((familia, prefijo))
        archivos = sorted(locales.rglob(f"{prefijo}-*.ttf")) if locales.exists() else []
        if not archivos:
            remotas.append(familia)
            continue
        for archivo in archivos:
            estilo = archivo.stem.split("-", 1)[1]
            peso = PESOS.get(estilo.replace("Italic", "") or "Regular")
            if peso is None:
                continue
            cursiva = "italic" if "Italic" in estilo else "normal"
            reglas.append(f'@font-face {{ font-family: "{familia}"; font-weight: {peso}; '
                          f'font-style: {cursiva}; src: url("{archivo.as_uri()}"); }}')
    enlace = ""
    if remotas:
        consulta = "&".join(f"family={f.replace(' ', '+')}:wght@400;600;700" for f in remotas)
        enlace = f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{consulta}&display=block">'
    return enlace, "\n".join(reglas), remotas


def _hoja_comun():
    for candidata in (RAIZ / "herramientas" / "estilo.css",
                      RAIZ / "procesos/skills-borrador/estilo-documentos/prototipo/estilo.css"):
        if candidata.exists():
            return candidata.as_uri()
    raise SystemExit("No encuentro estilo.css (estilo-documentos)")


def _icono(nombre):
    svg = RAIZ / "herramientas" / "iconos" / f"{nombre}.svg"
    if svg.exists():
        return svg.read_text(encoding="utf-8")
    return ""  # hasta que Paco instale Lucide, solo el nombre


def documento(datos, filas):
    p = datos["paleta"]
    t = datos["tipografias"]
    enlace_fuentes, fuentes_locales, _ = _fuentes(datos)
    sello = '<div class="interno">INTERNO · NO ENVIAR AL CLIENTE</div>'

    sabemos = "".join(f"<li>{e(s['que'])} <span class='nota'>({e(s['fuente'])})</span></li>" for s in datos["sabemos"])
    no_sabemos = "".join(f"<li>{e(s)}</li>" for s in datos["no_sabemos"])
    fachada = ("Con foto de la fachada: la paleta parte de sus colores reales."
               if datos.get("foto_fachada") else
               "<strong>Propuesta a ciegas:</strong> sin foto de la fachada ni del rótulo. "
               "Si llegan y tienen colores propios, mandan ellos.")

    c = datos["concepto"]
    transmitir = "".join(f"<li><strong>{e(x['que'])}.</strong> {e(x['porque'])} "
                         f"<span class='nota'>({e(x['fuente'])})</span></li>" for x in c["transmitir"])
    evitar = "".join(f"<li><strong>{e(x['que'])}.</strong> {e(x['porque'])}</li>" for x in c["evitar"])

    muestras = "".join(
        f"<div class='color'><div class='muestra' style='background:{e(p[k]['hex'])}'></div>"
        f"<b>{e(p[k]['nombre'])}</b> <code>{e(p[k]['hex'].upper())}</code><small>{e(k.replace('_', ' '))} · "
        f"{e(p[k]['uso'])}</small></div>" for k in PAPELES)
    def _muestra(d, f, m):
        if m == TEXTO:
            return (f"<span class='ejemplo' style='color:{e(p[d]['hex'])};background:{e(p[f]['hex'])}'>"
                    "Llamar</span>")
        return (f"<span class='ejemplo borde' style='border-color:{e(p[d]['hex'])};"
                f"background:{e(p[f]['hex'])}'></span>")

    contrastes = "".join(
        f"<tr><td>{e(para)}</td><td>{_muestra(d, f, m)}</td><td>{e(p[d]['nombre'])} / {e(p[f]['nombre'])}</td>"
        f"<td>{_coma(r)} : 1</td><td>{'texto' if m == TEXTO else 'no texto'} ≥ {_coma(m)}</td></tr>"
        for d, f, m, para, r in filas)
    detalle = contraste(p["detalle"]["hex"], p["fondo"]["hex"])

    tamanos = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c_)}</td></tr>" for a, b, c_ in TAMANOS)
    iconos = "".join(f"<span class='icono'>{_icono(n)}<code>{e(n)}</code></span>" for n in datos["iconos"])

    a = datos["accion_principal"]
    secciones = "".join(
        f"<li><strong>{e(s['nombre'])}</strong>: {e(s['que'])}"
        + (f" <span class='nota'>· solo si {e(s['si'])}</span>" if s.get("si") else "") + "</li>"
        for s in datos["secciones"])
    fotos = "".join(f"<tr><td>{e(a_)}</td><td>{e(b)}</td><td>{e(c_)}</td></tr>"
                    for a_, b, c_ in datos.get("fotos", FOTOS))
    riesgos = "".join(f"<li>{e(r)}</li>" for r in datos["riesgos"])
    preguntas = "".join(f"<li>{e(q)}</li>" for q in datos.get("preguntas", []))

    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Guía de estilos previa · INTERNO · {e(datos['negocio'])}</title>
{enlace_fuentes}
<link rel="stylesheet" href="{_hoja_comun()}">
<style>
  {fuentes_locales}
  @page {{ size: A4; margin: 14mm 14mm 16mm;
          @bottom-left {{ content: "Guía previa · INTERNO · {e(datos['negocio'])}"; }} }}
  body {{ font-size: 10.5pt; }}
  .dos {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; }}
  .colores {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 2mm; margin-bottom: 3mm; }}
  .color .muestra {{ height: 11mm; border-radius: 2mm; border: 1px solid #D0D7DE; margin-bottom: 1mm; }}
  .color b, .color code {{ display: block; font-size: 9pt; }}
  .color small {{ display: block; color: var(--gris); font-size: 8pt; line-height: 1.3; }}
  /* Sin monoespaciada del sistema: Inter con cifras tabulares. */
  code {{ font-family: "Inter", sans-serif; font-feature-settings: "tnum"; }}
  .color code, td code {{ font-size: 8.5pt; color: var(--gris); }}
  .ejemplo {{ display: inline-block; padding: .5mm 3mm; border-radius: 1mm; border: 1px solid #D0D7DE; font-weight: 700; }}
  .ejemplo.borde {{ width: 16mm; height: 5mm; border-width: 2px; }}
  .tipo-titular {{ font-family: "{e(t['titulares']['familia'])}", serif; font-weight: {int(t['titulares'].get('peso', 700))};
                  font-size: 24pt; line-height: 1.1; }}
  .tipo-texto {{ font-family: "{e(t['texto']['familia'])}", sans-serif; font-size: 13pt; }}
  .icono {{ display: inline-flex; align-items: center; gap: 1.5mm; margin: 0 3mm 2mm 0; padding: 1mm 2.5mm;
           background: var(--fondo); border-radius: 99px; }}
  .icono svg {{ width: 5mm; height: 5mm; }}
  /* Esquema en grises a propósito: que no parezca un diseño terminado. */
  .movil {{ width: 64mm; border: 2.5mm solid #6B7280; border-radius: 6mm; background: #fff; overflow: hidden;
           font-size: 8.5pt; color: #374151; }}
  .movil .barra {{ background: #E5E7EB; padding: 2mm 3mm; font-weight: 700; }}
  .movil .zona {{ margin: 2mm 3mm; border: 1px dashed #9CA3AF; border-radius: 1.5mm; padding: 2mm; }}
  .movil .boton {{ margin: 2mm 3mm; border-radius: 1.5mm; padding: 2.5mm; text-align: center; font-weight: 700; }}
  .movil .principal {{ background: #374151; color: #fff; }}
  .movil .secundario {{ border: 1.5px solid #374151; }}
  .movil .foto {{ height: 22mm; background: repeating-linear-gradient(45deg, #E5E7EB 0 3mm, #F3F4F6 3mm 6mm);
                 display: grid; place-items: center; }}
  .movil .pliegue {{ border-top: 2px solid #B3261E; margin: 0 3mm; font-size: 7.5pt; color: #B3261E; text-align: right; }}
</style></head><body>

<section>{sello}
  <div class="cabecera"><div class="marca">Guía de estilos previa · interna · {e(datos['fecha'])} · {e(datos['autora'])}</div>
  <h1>{e(datos['negocio'])}</h1><div>Plan que encaja: {e(datos['plan'])}</div></div>
  <div class="caja conclusion"><p>{fachada} Es una <strong>hipótesis</strong> para presupuestar, pedir el material
  y ganar días si contrata. No es el diseño, ni un logotipo, ni los textos (los textos y el tono son de Chema).</p></div>
  <div class="dos">
    <div><h3>Lo que sabemos</h3><ul>{sabemos}</ul></div>
    <div><h3>Lo que no sabemos</h3><ul>{no_sabemos}</ul></div>
  </div>
  <h2>Concepto: «{e(c['nombre'])}»</h2>
  <div class="dos">
    <div><h3>Transmitir</h3><ul>{transmitir}</ul></div>
    <div><h3>Evitar</h3><ul>{evitar}</ul></div>
  </div>
  <h2>Tipografías</h2>
  <div class="dos">
    <div><div class="nota">Titulares · {e(t['titulares']['familia'])} · {e(t['titulares']['licencia'])}</div>
      <div class="tipo-titular">Horario · Servicios · Cómo llegar</div>
      <p class="nota">{e(t['titulares']['por_que'])}</p></div>
    <div><div class="nota">Texto · {e(t['texto']['familia'])} · {e(t['texto']['licencia'])}</div>
      <div class="tipo-texto">Lunes a viernes, de 9:00 a 14:00. Pide cita por teléfono.</div>
      <p class="nota">{e(t['texto']['por_que'])} En la web, alojadas en nuestro servidor (RGPD).</p></div>
  </div>
  <table class="junto"><thead><tr><th>Uso</th><th>Móvil</th><th>Ordenador</th></tr></thead><tbody>{tamanos}</tbody></table>
</section>

<section>{sello}
  <div class="junto"><h2>Paleta provisional</h2>
  <div class="colores">{muestras}</div></div>
  <table><thead><tr><th>Para qué</th><th>Muestra</th><th>Colores</th><th>Contraste</th><th>Mínimo</th></tr></thead>
  <tbody>{contrastes}</tbody></table>
  <p class="nota">Calculado con contraste.py (WCAG 2.2). Todos los pares llegan a su mínimo; si no, el generador
  no deja sacar la guía. El color de detalle ({e(p['detalle']['nombre'])}, {_coma(detalle)} : 1 sobre el fondo:
  {e(veredicto(detalle).lower())}) no se usa para texto ni para nada que haya que ver.</p>
  <h3>Iconos · Lucide (ISC)</h3><div>{iconos}</div>
</section>

<section>{sello}
  <div class="junto"><h2>Primera pantalla en el móvil y estructura</h2>
  <div class="dos" style="grid-template-columns: 70mm 1fr">
    <div class="movil">
      <div class="barra">{e(datos['negocio'])}</div>
      <div class="zona">[Frase principal · Chema · 40–45 caracteres]</div>
      <div class="boton principal">{e(a['etiqueta'])}</div>
      <div class="zona">Hoy: [horario de hoy] · <u>Ver horario</u></div>
      <div class="boton secundario">Cómo llegar</div>
      <div class="pliegue">fin de la primera pantalla</div>
      <div class="zona foto">[Foto: fachada o equipo]</div>
      <div class="zona">[Servicios · a confirmar]</div>
    </div>
    <div>
      <h3>Regla de los tres segundos</h3>
      <ul><li>Llamar: un toque (acción principal: <strong>{e(a['etiqueta'])}</strong>,
      canal comprobado: {e(a['dato'])}).</li><li>Horario de hoy, a la vista.</li><li>Cómo llegar: un toque al mapa.</li></ul>
      <h3>Secciones, en este orden</h3><ol>{secciones}</ol>
      <p class="nota">Esquema en grises y a baja fidelidad a propósito. El diseño de verdad se hace al contratar.</p>
    </div>
  </div></div>
  <h2>Fotos que harán falta (tanda B)</h2>
  <table class="junto"><thead><tr><th>Toma</th><th>Para</th><th>Mínimo (lado largo)</th></tr></thead><tbody>{fotos}</tbody></table>
  <p class="nota">Ni caras de clientes ni de niños sin consentimiento por escrito (§15). Las de Google no son nuestras.</p>
  <h2>Riesgos y preguntas</h2>
  <ul>{riesgos}</ul>
  {f"<h3>Para el cuestionario (a Reme, por Federico)</h3><ul>{preguntas}</ul>" if preguntas else ""}
</section>
</body></html>
"""


def main(argumentos=None):
    argumentos = argumentos if argumentos is not None else sys.argv[1:]
    if len(argumentos) != 2:
        raise SystemExit(__doc__)
    entrada, salida = Path(argumentos[0]), Path(argumentos[1])
    datos = json.loads(entrada.read_text(encoding="utf-8"))
    errores, filas = comprobar(datos)
    if errores:
        print("No se genera la guía:", *(f"  - {x}" for x in errores), sep="\n", file=sys.stderr)
        return 1
    _, _, remotas = _fuentes(datos)
    if remotas:
        print(f"Aviso: {', '.join(remotas)} se carga de Google Fonts (vale en un documento interno; "
              "comprobad con pdffonts que salió)", file=sys.stderr)
    with tempfile.TemporaryDirectory() as tmp:
        maqueta = Path(tmp) / "guia.html"
        maqueta.write_text(documento(datos, filas), encoding="utf-8")
        subprocess.run(["node", str(RAIZ / "herramientas/html_a_pdf.mjs"), str(maqueta), str(salida)], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
