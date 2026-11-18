"""Pruebas de enlaces_captura.py. Ejecutar desde la raíz del repositorio:
    python3 -m unittest discover -s procesos/skills-borrador/investigar-cliente/pruebas -v
"""
import re
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

AQUI = Path(__file__).resolve().parent
SCRIPT = AQUI.parent / "enlaces_captura.py"
BASE = ["--negocio", "Peluquería Hermanos Cotillas", "--ciudad", "Albacete",
        "--nombre-corto", "Hermanos Cotillas", "--lat", "38.9925046", "--lon", "-1.8616289"]


class Enlaces(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.urls.append(dict(attrs)["href"])


def ejecutar(*busquedas, carpeta):
    args = BASE + [x for b in busquedas for x in ("--busqueda", b)] + ["--carpeta", str(carpeta)]
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)


class Guion(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.carpeta = Path(self.tmp.name) / "clientes" / "prueba"

    def tearDown(self):
        self.tmp.cleanup()

    def guion(self, *busquedas):
        r = ejecutar(*busquedas, carpeta=self.carpeta)
        self.assertEqual(r.returncode, 0, r.stderr)
        fichero = self.carpeta / "privado" / "capturas-google" / "guion.html"
        texto = fichero.read_text(encoding="utf-8")
        enlaces = Enlaces()
        enlaces.feed(texto)
        return texto, enlaces.urls, r.stdout

    def test_va_a_privado_para_que_no_entre_en_git(self):
        texto, _, salida = self.guion("barbería Albacete")
        self.assertIn("privado/capturas-google", salida)
        self.assertIn("privado/capturas-google", texto)

    def test_la_carpeta_se_muestra_con_ruta_completa(self):
        r = subprocess.run([sys.executable, str(SCRIPT), *BASE, "--busqueda", "a", "--carpeta", "clientes/prueba"],
                           cwd=self.tmp.name, capture_output=True, text=True, check=True)
        texto = (Path(self.tmp.name) / "clientes/prueba/privado/capturas-google/guion.html").read_text(encoding="utf-8")
        self.assertIn(f"<code>{Path(self.tmp.name).resolve()}/clientes/prueba/privado/capturas-google</code>", texto)

    def test_busquedas_de_google_en_espanol_y_bien_codificadas(self):
        _, urls, _ = self.guion("barbería Albacete", "peluquería caballero Albacete")
        consultas = [parse_qs(urlparse(u).query) for u in urls if urlparse(u).path == "/search"]
        self.assertIn(["barbería Albacete"], [c["q"] for c in consultas])
        self.assertTrue(all(c["hl"] == ["es"] and c["gl"] == ["es"] for c in consultas))
        self.assertIn(['site:instagram.com "Hermanos Cotillas"'], [c["q"] for c in consultas])

    def test_ficha_con_formato_oficial_y_mapa_centrado_en_el_cliente(self):
        _, urls, _ = self.guion("barbería Albacete")
        self.assertTrue(any("maps/search/?api=1" in u and "Peluquer%C3%ADa+Hermanos+Cotillas+Albacete" in u for u in urls))
        self.assertTrue(any(u.endswith("/@38.9925046,-1.8616289,17z") and "barber%C3%ADa" in u for u in urls))

    def test_cuenta_las_capturas_y_cabe_en_diez_minutos(self):
        texto, _, salida = self.guion("a", "b", "c")
        total = int(re.search(r"· (\d+) capturas", salida).group(1))
        self.assertEqual(total, 3 + 3 + 1 + 2)
        self.assertLessEqual(total, 10)
        self.assertIn(f"{total} capturas, unos 10 minutos", texto)

    def test_no_admite_mas_de_tres_busquedas(self):
        r = ejecutar("a", "b", "c", "d", carpeta=self.carpeta)
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse((self.carpeta / "privado").exists())

    def test_ventana_privada_y_solo_la_ventana_del_navegador(self):
        texto, _, _ = self.guion("a")
        self.assertIn("ventana privada", texto)
        self.assertIn("⌘ ⇧ 4", texto)
        self.assertIn('lang="es"', texto)

    def test_escapa_el_html_del_nombre(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--negocio", "Pelu <b>&</b> Co", "--ciudad", "X",
                            "--lat", "1", "--lon", "2", "--busqueda", "a", "--carpeta", str(self.carpeta)],
                           capture_output=True, text=True, check=True)
        texto = (self.carpeta / "privado" / "capturas-google" / "guion.html").read_text(encoding="utf-8")
        self.assertNotIn("<b>&</b>", texto)
        self.assertIn("Pelu &lt;b&gt;&amp;&lt;/b&gt; Co", texto)


if __name__ == "__main__":
    unittest.main()
