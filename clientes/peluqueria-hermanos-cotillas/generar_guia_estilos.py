"""Genera la guía de estilos PREVIA e INTERNA de la Peluquería Hermanos Cotillas.

No se envía al cliente: es trabajo de diseño que solo se entrega si contrata.
Ejecutar desde la raíz del repositorio:
    .venv/bin/python clientes/peluqueria-hermanos-cotillas/generar_guia_estilos.py
"""
import re
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
MAQUETA = AQUI / "maquetas" / "guia-estilos.html"
SALIDA = AQUI / "interno" / "Guía de estilos previa - INTERNO - Peluquería Hermanos Cotillas.pdf"

COLORES = [
    # nombre, hex, uso
    ("Tinta", "#1F2A37", "Textos y fondos oscuros. El color principal."),
    ("Papel", "#F6F0E6", "Fondo general: cálido, como el de un local de toda la vida."),
    ("Cobre", "#9A5B2E", "Acento: botones, enlaces, detalles. Evoca tijeras y sillones de latón."),
    ("Rojo barbero", "#9E2B25", "Solo en detalles pequeños (la franja del poste de barbero)."),
    ("Piedra", "#5E6670", "Textos secundarios, horarios, notas."),
    ("Blanco", "#FFFFFF", "Tarjetas sobre el fondo papel."),
]


def _lum(hexa):
    canales = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in canales]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contraste(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def veredicto(ratio):
    # WCAG 2.2 AA: 4,5 para texto normal y 3 para texto grande (≥ 24 px, o 18,7 px en negrita).
    if ratio >= 4.5:
        return '<span class="chip si">AA texto normal</span>'
    if ratio >= 3:
        return '<span class="chip">Solo texto grande</span>'
    return '<span class="chip no">No usar para texto</span>'


def tabla_contrastes():
    pares = [("Tinta", "Papel"), ("Tinta", "Blanco"), ("Cobre", "Papel"), ("Cobre", "Blanco"),
             ("Blanco", "Cobre"), ("Blanco", "Tinta"), ("Piedra", "Papel"), ("Rojo barbero", "Papel"),
             ("Blanco", "Rojo barbero")]
    hexa = {n: h for n, h, _ in COLORES}
    filas = []
    for texto, fondo in pares:
        r = contraste(hexa[texto], hexa[fondo])
        muestra = (f'<span style="background:{hexa[fondo]};color:{hexa[texto]};padding:2px 10px;'
                   f'border:1px solid #ddd;border-radius:4px;font-weight:600">Pide cita</span>')
        filas.append(f"<tr><td>{texto} sobre {fondo}</td><td>{muestra}</td>"
                     f"<td>{str(round(r, 1)).replace('.', ',')} : 1</td><td>{veredicto(r)}</td></tr>")
    return "\n".join(filas)


def muestras_color():
    return "\n".join(
        f'<div class="color"><div class="muestra" style="background:{h}"></div>'
        f'<b>{n}</b><code>{h}</code><small>{u}</small></div>' for n, h, u in COLORES
    )


# Iconos de línea dibujados para esta guía (sin licencias de terceros).
ICONOS = {
    "Tijeras": '<circle cx="7" cy="17" r="3"/><circle cx="17" cy="17" r="3"/><path d="M9 15 19 3M15 15 5 3"/>',
    "Horario": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "Cómo llegar": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "Llamar": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    "Mensaje": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    "Niños": '<circle cx="12" cy="7" r="3"/><path d="M6 21v-2a6 6 0 0 1 12 0v2"/>',
    "Navaja": '<path d="M3 16 14 5l5 5-11 6z"/><path d="M14 5l2-2 5 5-2 2"/>',
    "Opiniones": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
}


def iconos():
    return "\n".join(
        f'<div class="icono"><svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="#1F2A37" '
        f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{svg}</svg><span>{n}</span></div>'
        for n, svg in ICONOS.items()
    )


def html():
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Guía de estilos previa · INTERNO</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,800&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../../herramientas/informe.css">
<style>
  :root {{ --tinta:#1F2A37; --acento:#9A5B2E; --acento-suave:#efe2d3; }}
  body {{ font-family: Inter, sans-serif; }}
  h1, h2, .display {{ font-family: Fraunces, Georgia, serif; }}
  h2 {{ color: var(--tinta); }}
  /* Un sello por sección y no uno fijo: Chrome coloca los fijos según la primera página (sin
     márgenes) y en las demás salen recortados. */
  .interno {{ float: right; margin: 0 0 4px 12px; white-space: nowrap;
             font: 700 7.5pt Inter; letter-spacing: .12em; color: #9E2B25;
             border: 1.5px solid #9E2B25; border-radius: 4px; padding: 2px 8px; background: #fff; }}
  .portada {{ background: #1F2A37; }}
  .portada .interno {{ position: absolute; top: 12mm; right: 16mm; }}
  .portada h1 {{ font-family: Fraunces, serif; font-weight: 800; font-size: 40pt; }}
  .poste {{ height: 10px; margin: 6mm 0; width: 60mm;
           background: repeating-linear-gradient(-45deg,#9E2B25 0 10px,#F6F0E6 10px 20px,#1F2A37 20px 30px,#F6F0E6 30px 40px); }}
  .colores {{ display:grid; grid-template-columns: repeat(3,1fr); gap: 12px; }}
  .color .muestra {{ height: 26mm; border-radius: 8px; border: 1px solid #ddd; margin-bottom: 6px; }}
  .color b {{ display:block; }} .color code {{ font-size: 8.5pt; color:#5E6670; }}
  .color small {{ display:block; color:#5E6670; font-size: 8.5pt; line-height:1.35; }}
  .iconos {{ display:grid; grid-template-columns: repeat(4,1fr); gap: 10px; }}
  .icono {{ background:#F6F0E6; border-radius:10px; padding:12px; text-align:center; }}
  .icono span {{ display:block; font-size:9pt; margin-top:4px; }}
  .muestra-tipo {{ background:#F6F0E6; border-radius:10px; padding:14px 18px; margin-bottom:12px; }}
  .logo {{ background:#F6F0E6; border-radius:12px; padding:18mm 10mm; text-align:center; }}
  .logo .peq {{ font: 600 9pt Inter; letter-spacing:.4em; color:#9A5B2E; }}
  .logo .gran {{ font: 800 34pt/1 Fraunces, serif; color:#1F2A37; margin: 6px 0; }}
  .logo .linea {{ font: 500 9pt Inter; letter-spacing:.3em; color:#5E6670; }}
  .movil {{ width: 74mm; border: 8px solid #1F2A37; border-radius: 26px; overflow: hidden; background:#F6F0E6; }}
  .movil .barra {{ background:#1F2A37; color:#F6F0E6; padding:10px 14px; font: 700 10pt Fraunces, serif; }}
  .movil .heroe {{ padding: 16px 14px; }}
  .movil .heroe h3 {{ font: 800 18pt/1.1 Fraunces, serif; margin: 0 0 8px; }}
  .movil .foto {{ height: 34mm; border-radius: 10px; margin: 8px 0;
                  background: repeating-linear-gradient(45deg,#d9cbb8 0 8px,#e6dccd 8px 16px);
                  display:grid; place-items:center; color:#5E6670; font-size:8pt; }}
  .boton {{ display:block; text-align:center; padding:10px; border-radius:10px; font-weight:700; margin-top:8px; }}
  .b1 {{ background:#9A5B2E; color:#fff; }} .b2 {{ background:#fff; color:#1F2A37; border:1.5px solid #1F2A37; }}
  .servicio {{ display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px dashed #cbbfae; font-size:9.5pt; }}
  .si-no {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
  .si-no div {{ border-radius:10px; padding:10px 14px; }}
  .si-no .si {{ background:#e3f3e8; }} .si-no .no {{ background:#fbe4e2; }}
</style>
</head><body>
<section class="portada">
  <div class="etiqueta">Guía de estilos previa · borrador interno</div>
  <h1>Hermanos Cotillas</h1>
  <div class="poste"></div>
  <div class="sub">Propuesta de identidad para su web: colores, tipografías, iconos, fotografía y tono.
  Sirve para preparar el diseño y para el presupuesto. <strong>No se envía hasta que el cliente contrate.</strong></div>
  <div class="cliente"><strong>Concepto: «Oficio de familia»</strong>
  Una peluquería de caballero de las de siempre, contada con un diseño limpio y actual.</div>
  <div class="pie">Borrador · Federico · 17/11/2026 · Pendiente de revisión por Lola (diseño)</div>
</section>

<section>
  <h2>1. El concepto</h2>
  <p>Todo lo que sabemos del negocio apunta a lo mismo: <strong>dos hermanos que heredaron el oficio
  de sus padres</strong> y una clientela que va por generaciones. Ese es el valor que no puede copiar
  ninguna de las 281 peluquerías de alrededor, y la identidad tiene que transmitirlo.</p>
  <div class="dos">
    <div class="caja"><h3>Lo que queremos transmitir</h3>
      <ul class="check"><li>Oficio y experiencia</li><li>Confianza de barrio</li>
      <li>Cercanía y algo de humor</li><li>Limpio y cuidado, no anticuado</li></ul></div>
    <div class="caja aviso"><h3>Lo que hay que evitar</h3>
      <ul><li>El estilo «barbería hipster» (negro, calaveras, neones): es el de la competencia nueva.</li>
      <li>Fotos de banco de imágenes con modelos.</li><li>Parecer un salón de belleza femenino.</li></ul></div>
  </div>
  <p class="nota">Pendiente: ver la fachada y el rótulo reales. Si el local tiene colores propios, mandan
  sobre esta propuesta.</p>
</section>

<section class="pagina">
  <h2>2. Colores</h2>
  <div class="colores">{muestras_color()}</div>
  <h3>Contraste (WCAG 2.2 AA, obligatorio según AGENTS.md §11)</h3>
  <table><tr><th>Combinación</th><th>Ejemplo</th><th>Contraste</th><th>Resultado</th></tr>
  {tabla_contrastes()}
  </table>
  <p class="nota">Calculado con la fórmula de luminancia relativa de las WCAG. Mínimos: 4,5 : 1 para
  texto normal, 3 : 1 para texto grande.</p>
</section>

<section class="pagina">
  <h2>3. Tipografías</h2>
  <div class="muestra-tipo">
    <div class="nota">Titulares · Fraunces (Google Fonts, licencia SIL OFL)</div>
    <div class="display" style="font-size:30pt;font-weight:800;line-height:1.1">Le cortamos el pelo a tu padre. Ahora, a ti.</div>
    <p class="nota">Una serifa con carácter, con un punto clásico de rótulo antiguo, pero de diseño actual.</p>
  </div>
  <div class="muestra-tipo">
    <div class="nota">Textos · Inter (Google Fonts, licencia SIL OFL)</div>
    <p style="font-size:12pt">Somos [nombre] y [nombre], los hermanos Cotillas. Aprendimos el oficio de
    nuestros padres, que abrieron esta peluquería en la calle Octavio Cuartero.</p>
    <p style="font-size:10pt;color:#5E6670">Lunes a viernes, de 9:00 a 14:00 y de 16:30 a 20:30 · Sábados, de 8:30 a 14:00</p>
    <p class="nota">Muy legible en el móvil, también en tamaños pequeños.</p>
  </div>
  <table><tr><th>Uso</th><th>Fuente</th><th>Móvil</th><th>Ordenador</th></tr>
    <tr><td>Titular principal</td><td>Fraunces 800</td><td>32 px</td><td>56 px</td></tr>
    <tr><td>Títulos de sección</td><td>Fraunces 600</td><td>24 px</td><td>34 px</td></tr>
    <tr><td>Texto</td><td>Inter 400</td><td>17 px</td><td>18 px</td></tr>
    <tr><td>Botones</td><td>Inter 700</td><td>17 px</td><td>17 px</td></tr>
  </table>
  <div class="caja"><h3>Nota técnica para Paco</h3>
    <p>Las fuentes se alojan en nuestro servidor, no se cargan desde Google: cargarlas desde Google
    envía la IP del visitante a un tercero sin su consentimiento (RGPD).</p></div>
</section>

<section class="pagina">
  <h2>4. Iconos</h2>
  <p>De línea, trazo fino y extremos redondeados, siempre en Tinta. Acompañan, no decoran:
  siempre con texto al lado.</p>
  <div class="iconos">{iconos()}</div>
  <p class="nota">Dibujados para esta guía. En producción se puede usar un juego libre equivalente
  (por ejemplo, Lucide, licencia ISC) para tener todos los que hagan falta con el mismo estilo.</p>

  <h2 style="margin-top:10mm">5. Idea de logotipo (solo tipográfica)</h2>
  <div class="logo">
    <div class="peq">PELUQUERÍA</div>
    <div class="gran">Hermanos Cotillas</div>
    <div class="poste" style="margin:10px auto;width:40mm"></div>
    <div class="linea">ALBACETE · DESDE [AÑO]</div>
  </div>
  <p class="nota">Si no tienen logotipo, esto basta para la web. Un logotipo de verdad no está incluido
  en la creación de la web (AGENTS.md §6.1) y se presupuesta aparte.</p>
</section>

<section class="pagina">
  <h2>6. Así se vería en el móvil</h2>
  <div class="tres">
    <div class="movil">
      <div class="barra">Hermanos Cotillas</div>
      <div class="heroe">
        <h3>Le cortamos el pelo a tu padre. Ahora, a ti.</h3>
        <div style="font-size:9pt;color:#5E6670">Peluquería familiar en la Feria · Albacete</div>
        <div class="foto">[Foto: los dos hermanos en el local]</div>
        <span class="boton b1">Pedir cita por WhatsApp</span>
        <span class="boton b2">Llamar · 967 23 57 91</span>
        <div style="margin-top:14px;font:600 11pt Fraunces,serif">Servicios</div>
        <div class="servicio"><span>Corte de caballero</span><b>[precio]</b></div>
        <div class="servicio"><span>Corte de niño</span><b>[precio]</b></div>
        <div class="servicio"><span>Arreglo de barba</span><b>[precio]</b></div>
        <div style="margin-top:12px;font-size:9pt">★★★★★ <b>4,8</b> en Google · 132 opiniones</div>
      </div>
    </div>
    <div>
      <h3>Estructura propuesta (una sola página, plan Esencial)</h3>
      <ol>
        <li><b>Portada:</b> frase, foto de los hermanos, botones de WhatsApp y llamar.</li>
        <li><b>Quiénes somos:</b> la historia familiar, con foto antigua si la hay.</li>
        <li><b>Servicios y precios.</b></li>
        <li><b>Opiniones</b> de Google, tal cual.</li>
        <li><b>Horario y cómo llegar</b>, con mapa.</li>
        <li><b>Contacto</b> y textos legales.</li>
      </ol>
      <p class="nota">Boceto orientativo para el presupuesto. El diseño de verdad lo hace Lola
      cuando el cliente contrate.</p>
    </div>
  </div>
</section>

<section class="pagina">
  <h2>7. Fotografía</h2>
  <div class="si-no">
    <div class="si"><h3>Sí</h3><ul>
      <li>Fotos reales del local y de los dos hermanos trabajando.</li>
      <li>Luz natural, tonos cálidos.</li>
      <li>Detalles del oficio: tijeras, navaja, el sillón.</li>
      <li>Fotos antiguas del negocio y de sus padres: son oro.</li>
      <li>Clientes solo con permiso; si no, de espaldas.</li></ul></div>
    <div class="no"><h3>No</h3><ul>
      <li>Fotos de banco de imágenes.</li>
      <li>Filtros exagerados o blanco y negro en todo.</li>
      <li>Caras de clientes sin consentimiento por escrito.</li>
      <li>Fotos de otras peluquerías «de inspiración».</li></ul></div>
  </div>

  <h2 style="margin-top:8mm">8. Tono de comunicación</h2>
  <p>Como hablan ellos con sus clientes: <strong>de tú, cercano, con algo de humor</strong> y sin
  palabras rimbombantes. Sus propios clientes nos dan el tono: «listo para triunfar», «sin que peligren
  tus orejas».</p>
  <table><tr><th>Así sí</th><th>Así no</th></tr>
    <tr><td>Te cortamos el pelo como te gusta. Y si no sabes cómo, te aconsejamos.</td>
        <td>Ofrecemos un servicio integral de asesoramiento capilar personalizado.</td></tr>
    <tr><td>¿Vienes con tu hijo? Para los peques, paciencia de sobra.</td>
        <td>Disponemos de servicios especializados para el público infantil.</td></tr>
    <tr><td>Pide cita por WhatsApp y no esperes.</td>
        <td>Contacte con nosotros para concertar una cita previa.</td></tr>
  </table>
</section>

</body></html>
"""


def con_sellos(documento):
    sello = '<div class="interno">INTERNO · NO ENVIAR AL CLIENTE</div>'
    return re.sub(r"(<section[^>]*>)", r"\1\n" + sello, documento)


def main():
    MAQUETA.parent.mkdir(parents=True, exist_ok=True)
    MAQUETA.write_text(con_sellos(html()), encoding="utf-8")
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([str(RAIZ / "herramientas/html_a_pdf.sh"), str(MAQUETA), str(SALIDA)], check=True)


if __name__ == "__main__":
    main()
