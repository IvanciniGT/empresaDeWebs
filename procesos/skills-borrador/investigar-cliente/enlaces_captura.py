"""Genera el guion de captura manual de Google para Iván (A-001): una página con
los enlaces exactos de un cliente, en orden, y cuántas capturas hacer en cada uno.

Iván es quien busca en Google, con su navegador y en una ventana privada: ningún
robot lee los resultados de Google (su robots.txt lo prohíbe).

Uso:
  python3 enlaces_captura.py --negocio "Peluquería Hermanos Cotillas" --ciudad Albacete \\
      --nombre-corto "Hermanos Cotillas" --lat 38.9925046 --lon -1.8616289 \\
      --busqueda "barbería Albacete" --busqueda "peluquería caballero Albacete" \\
      --carpeta clientes/peluqueria-hermanos-cotillas

Deja privado/capturas-google/guion.html dentro de la carpeta del cliente. Las
capturas van a esa misma carpeta: privado/ no entra en git (A-009), y las reseñas
llevan nombres de personas.
"""
import argparse
import html
import sys
from pathlib import Path
from urllib.parse import quote, urlencode

MAX_BUSQUEDAS = 3  # más búsquedas no caben en los 10 minutos


def google(consulta):
    return "https://www.google.com/search?" + urlencode({"q": consulta, "hl": "es", "gl": "es"})


def ficha_maps(negocio, ciudad):
    # Formato oficial de Google Maps URLs (api=1).
    return "https://www.google.com/maps/search/?" + urlencode({"api": "1", "query": f"{negocio} {ciudad}"})


def maps_centrado(busqueda, lat, lon):
    # Formato no documentado, pero es el único que centra el mapa en la calle del cliente.
    return f"https://www.google.com/maps/search/{quote(busqueda)}/@{lat},{lon},17z"


def pasos(a):
    lista = [
        ("Google con el nombre del negocio",
         [(f"{a.negocio} {a.ciudad}", google(f"{a.negocio} {a.ciudad}"))],
         1, "Que se vea la ficha de la derecha entera, si sale."),
        ("La ficha en Google Maps",
         [(f"{a.negocio} {a.ciudad} en Maps", ficha_maps(a.negocio, a.ciudad))],
         1, "Antes de capturar, pulsa en el horario para desplegarlo. Si sale «Reclamar esta "
            "empresa» o «¿Es el propietario?», que se vea: dice si la ficha la gestiona alguien."),
        ("Las opiniones, las más recientes",
         [("En la misma ficha: pestaña «Opiniones» → «Ordenar» → «Más recientes»", None)],
         1, "Llevan nombres de personas: por eso todo esto va a privado/."),
    ]
    for b in a.busqueda:
        lista.append((f"Búsqueda: {b}", [(b, google(b))], 1, "Basta con lo que se ve sin bajar."))
    lista.append(("El mapa alrededor del local",
                  [(f"{a.busqueda[0]}, centrado en la calle del cliente",
                    maps_centrado(a.busqueda[0], a.lat, a.lon))],
                  1, "Si no centra en su calle, busca la dirección y acerca el mapa a mano."))
    lista.append(("Redes sociales",
                  [(f'site:instagram.com "{a.nombre_corto}"', google(f'site:instagram.com "{a.nombre_corto}"')),
                   (f'site:facebook.com "{a.nombre_corto}" {a.ciudad}',
                    google(f'site:facebook.com "{a.nombre_corto}" {a.ciudad}'))],
                  2, "Una captura por búsqueda. Si no sale nada, captura igual: también es un dato."))
    return lista


def generar(a):
    # Ruta completa: es la que Iván tiene que buscar en el diálogo de macOS.
    carpeta = (Path(a.carpeta) / "privado" / "capturas-google").resolve()
    lista = pasos(a)
    total = sum(n for _, _, n, _ in lista)
    e = html.escape
    filas = []
    for i, (titulo, enlaces, n, nota) in enumerate(lista, 1):
        li = "".join(
            f'<li><a href="{e(url)}">{e(texto)}</a></li>' if url else f"<li>{e(texto)}</li>"
            for texto, url in enlaces)
        filas.append(f'<section><h2>{i}. {e(titulo)} <small>· {n} captura{"s" if n > 1 else ""}</small></h2>'
                     f"<ul>{li}</ul><p>{e(nota)}</p></section>")
    pagina = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Capturas de Google · {e(a.negocio)}</title>
<style>body{{font:18px/1.5 system-ui,sans-serif;max-width:46em;margin:2em auto;padding:0 1em}}
a{{font-size:1.1em}} small{{color:#555;font-weight:normal}} section{{border-top:1px solid #ccc}}
.caja{{background:#f3efe8;padding:.5em 1em;border-left:6px solid #9C4A14}}</style></head><body>
<h1>Capturas de Google · {e(a.negocio)}</h1>
<p><strong>{total} capturas, unos 10 minutos.</strong> Guion de Chema (A-001).</p>
<div class="caja"><h2>Antes de empezar (1 minuto)</h2><ol>
<li>Pulsa <kbd>⌘ ⇧ 5</kbd> → <em>Opciones</em> → <em>Guardar en</em> → <em>Otra ubicación…</em> y elige:<br>
<code>{e(str(carpeta))}</code></li>
<li>Abre una <strong>ventana privada</strong> (<kbd>⌘ ⇧ N</kbd>) y arrastra este archivo dentro. Así Google no usa tu cuenta ni tu historial.</li>
<li>Si Google pregunta por las cookies: <em>Rechazar todo</em>.</li>
<li>Cada captura: <kbd>⌘ ⇧ 4</kbd>, <kbd>espacio</kbd> y clic en la ventana del navegador. Solo sale esa ventana, no el resto de tu pantalla.</li>
</ol><p>No renombres nada: el orden y la hora del nombre del archivo me bastan.</p></div>
{"".join(filas)}
<div class="caja"><h2>Al terminar</h2><p>Dile a Federico: «capturas de {e(a.negocio)} hechas, desde [tu ciudad]».
Los resultados de Google cambian según desde dónde se busca, y lo anoto en el expediente.</p></div>
</body></html>
"""
    carpeta.mkdir(parents=True, exist_ok=True)
    salida = carpeta / "guion.html"
    salida.write_text(pagina, encoding="utf-8")
    return salida, total


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--negocio", required=True)
    p.add_argument("--ciudad", required=True)
    p.add_argument("--nombre-corto", help="el nombre que usaría en redes (por defecto, el del negocio)")
    p.add_argument("--lat", type=float, required=True)
    p.add_argument("--lon", type=float, required=True)
    p.add_argument("--busqueda", action="append", required=True,
                   help=f"búsqueda objetivo; como mucho {MAX_BUSQUEDAS}, la principal primero")
    p.add_argument("--carpeta", required=True, help="carpeta del cliente: clientes/<negocio>")
    a = p.parse_args(argv)
    a.nombre_corto = a.nombre_corto or a.negocio
    if len(a.busqueda) > MAX_BUSQUEDAS:
        p.error(f"como mucho {MAX_BUSQUEDAS} búsquedas: más no caben en 10 minutos")
    salida, total = generar(a)
    print(f"{salida} · {total} capturas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
