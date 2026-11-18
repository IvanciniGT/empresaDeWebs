"""Pruebas de vigilar_frases.py con frases reales del envío de la ronda 1.
Ejecutar desde la raíz del repositorio:
    python3 -m unittest discover -s procesos/skills-borrador/textos-web/pruebas -v
"""
import subprocess
import sys
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import vigilar_frases as v  # noqa: E402

REGLAS = v.cargar()

# Frase del envío de la ronda 1 → nivel que tiene que dar.
CASOS = {
    "El primero de los dos que tenga una web bien hecha se queda con las búsquedas del barrio.": "B",
    "Los negocios que publican precios reciben más llamadas.": "B",
    "<td>Web propia</td><td>No existe</td>": "B",
    "Tampoco tiene web propia.": "B",
    "¿Os resulta más cómodo hablarlo? Os llamamos y lo rellenamos juntos por teléfono.": "B",
    "Hemos comprobado que hermanoscotillas.es parece libre.": "B",
    "Es la primera del listado de peluquerías de Albacete en Treatwell.": "B",
    "<b>0</b> páginas en internet que controléis vosotros": None,  # la cifra va en otra etiqueta: ver abajo
    "0 páginas en internet que controléis vosotros": "B",
    "Resultados garantizados.": "B",
    "Os garantizamos la primera página.": "B",
    "Nadie elige peluquería por ser la más cercana.": "R",
    "Estáis en una zona céntrica de Albacete.": "R",
    "33 a menos de 250 metros: en vuestra misma manzana y las de al lado": "R",
    "Peluquería familiar desde hace más de 30 años.": "R",
    "Puntuales: si tienes cita, no esperas.": "R",
    "Para toda la familia: del abuelo al nieto.": "R",
    "Las casi 300 peluquerías de alrededor.": "R",
    "Sobre todo el joven, que es el que busca en el móvil.": "R",
}

LIMPIAS = [
    "No hemos encontrado vuestra web en las fuentes que hemos consultado.",
    "Vuestra ficha de Google tiene una nota de 4,8 (consultada el 18/11/2026).",
    '<div class="caja-mas-clientes sin-esperas">Horario de hoy</div>',
    "¿En qué año abrieron vuestros padres?",
    "Nadie puede garantizar una posición concreta en Google, y desconfiad de quien lo haga.",
    "Garantía: 30 días tras la publicación para corregir cualquier error nuestro.",
]


def niveles(texto):
    return {nivel for _, nivel, _, _ in v.revisar(texto, REGLAS)}


class Vigilar(unittest.TestCase):
    def test_cada_error_de_la_ronda_1_da_su_nivel(self):
        for frase, nivel in CASOS.items():
            if nivel is None:
                continue
            with self.subTest(frase=frase):
                self.assertIn(nivel, niveles(frase))

    def test_las_promesas_bloquean_y_lo_dudoso_solo_avisa(self):
        for frase, nivel in CASOS.items():
            if nivel == "R":
                with self.subTest(frase=frase):
                    self.assertNotIn("B", niveles(frase))

    def test_textos_limpios_no_bloquean(self):
        for frase in LIMPIAS:
            with self.subTest(frase=frase):
                self.assertNotIn("B", niveles(frase))

    def test_no_mira_dentro_de_las_etiquetas_html(self):
        self.assertEqual(niveles('<div class="mas clientes" title="no tiene web">Horario</div>'), set())

    def test_limite_conocido_cifra_y_texto_en_etiquetas_distintas(self):
        # Se documenta, no se arregla: por eso la maqueta no lleva cifras escritas a mano (censo.py).
        self.assertNotIn("B", niveles(next(f for f, n in CASOS.items() if n is None)))

    def test_codigo_de_salida(self):
        orden = [sys.executable, str(AQUI.parent / "vigilar_frases.py"), "--frase"]
        self.assertEqual(subprocess.run(orden + ["Resultados garantizados."], capture_output=True).returncode, 1)
        self.assertEqual(subprocess.run(orden + ["Estáis en una zona céntrica."], capture_output=True).returncode, 0)

    def test_la_lista_tiene_formato_valido(self):
        self.assertGreater(len(REGLAS), 15)
        self.assertTrue(all(nivel in "BR" for nivel, _, _ in REGLAS))


if __name__ == "__main__":
    unittest.main()
