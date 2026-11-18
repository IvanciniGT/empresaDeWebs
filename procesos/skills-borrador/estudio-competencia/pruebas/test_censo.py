"""Pruebas de censo.py. Ejecutar desde la raíz del repositorio:
    python3 -m unittest discover -s procesos/skills-borrador/estudio-competencia/pruebas -v
"""
import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import censo  # noqa: E402

LAT, LON = 38.9925046, -1.8616289
METROS_POR_GRADO = 2 * math.pi * censo.RADIO_TIERRA_M / 360


def nodo(ident, norte_m, este_m=0.0, **etiquetas):
    return {
        "type": "node", "id": ident,
        "lat": LAT + norte_m / METROS_POR_GRADO,
        "lon": LON + este_m / (METROS_POR_GRADO * math.cos(math.radians(LAT))),
        "tags": etiquetas,
    }


def respuesta(*elementos):
    return {"osm3s": {"timestamp_osm_base": "2026-11-18T10:00:00Z"}, "elements": list(elementos)}


class Censo(unittest.TestCase):
    def calcular(self, *elementos, cliente="node/1"):
        return censo.cifras(respuesta(*elementos), LAT, LON, cliente)

    def anillo(self, resultado, hasta):
        return next(a for a in resultado["anillos"] if a["hasta_m"] == hasta)

    def test_las_tiendas_de_productos_no_cuentan(self):
        r = self.calcular(
            nodo(2, 100, shop="hairdresser", name="Peluquería"),
            nodo(3, 120, shop="hairdresser_supply", name="Tienda de productos"),
        )
        self.assertEqual(self.anillo(r, 250)["total"], 1)
        self.assertEqual([e["motivo"] for e in r["excluidos"]], ["shop=hairdresser_supply"])

    def test_el_cliente_no_se_cuenta(self):
        r = self.calcular(nodo(1, 0, shop="hairdresser", name="El cliente"),
                          nodo(2, 50, shop="hairdresser", name="Otra"))
        self.assertEqual(self.anillo(r, 250)["total"], 1)
        self.assertEqual(r["mas_cercanos"][0]["id"], "node/2")

    def test_anillos_con_su_limite(self):
        r = self.calcular(
            nodo(2, 240, shop="hairdresser", name="A"),
            nodo(3, 260, shop="hairdresser", name="B"),
            nodo(4, 0, 990, shop="hairdresser", name="C"),
            nodo(5, -1600, shop="hairdresser", name="Fuera"),
        )
        self.assertEqual([a["total"] for a in r["anillos"]], [1, 2, 3, 3])
        self.assertIn("fuera del radio", r["excluidos"][0]["motivo"])

    def test_distancia_correcta(self):
        r = self.calcular(nodo(2, 300, 400, shop="hairdresser", name="A"))
        self.assertAlmostEqual(r["mas_cercanos"][0]["distancia_m"], 500, delta=1)

    def test_mismo_publico_por_etiqueta_y_por_nombre_por_separado(self):
        r = self.calcular(
            nodo(2, 100, shop="hairdresser", hairdresser="barber", name="Los Rizos"),
            nodo(3, 110, shop="barber", name="Navaja"),
            nodo(4, 120, shop="hairdresser", name="Barbería Central"),
            nodo(5, 130, shop="hairdresser", name="Peluquería de Caballeros Roberto"),
            nodo(6, 140, shop="hairdresser", hairdresser="unisex", name="Salón Ana"),
        )
        a = self.anillo(r, 250)
        self.assertEqual((a["total"], a["mismo_publico_por_etiqueta"], a["mismo_publico_por_nombre"]), (5, 2, 2))
        self.assertEqual([x["id"] for x in r["mas_cercanos_mismo_publico"]], ["node/2", "node/3", "node/4"])

    def test_duplicado_cerca_se_cuenta_una_vez_pero_mismo_nombre_lejos_son_dos(self):
        r = self.calcular(
            nodo(2, 100, shop="hairdresser", name="Jose"),
            {"type": "way", "id": 9, "center": {"lat": LAT + 110 / METROS_POR_GRADO, "lon": LON},
             "tags": {"shop": "hairdresser", "name": "José"}},
            nodo(3, 900, shop="hairdresser", name="Jose"),
        )
        self.assertEqual(self.anillo(r, 1000)["total"], 2)
        self.assertEqual(r["duplicados"], [{"id": "way/9", "nombre": "José", "igual_que": "node/2"}])

    def test_la_consulta_pide_etiquetas_exactas(self):
        q = censo.consulta(LAT, LON, 1500)
        self.assertIn(f'nwr["shop"="hairdresser"](around:1500,{LAT},{LON});', q)
        self.assertIn('nwr["shop"="barber"]', q)
        self.assertNotIn("~", q)  # nada de expresiones regulares que cuelen hairdresser_supply

    def test_mapa_y_tabla_salen_de_la_misma_distancia(self):
        r = self.calcular(nodo(2, 900, -1100, shop="hairdresser", name="Lejos"),
                          nodo(3, 245, 0, shop="barber", name="Borde"))
        for local in r["locales"]:
            self.assertAlmostEqual(math.hypot(local["este_m"], local["norte_m"]), local["distancia_m"], delta=1)
        lejos = next(x for x in r["locales"] if x["nombre"] == "Lejos")
        self.assertGreater(lejos["norte_m"], 0)
        self.assertLess(lejos["este_m"], 0)
        with tempfile.TemporaryDirectory() as tmp:
            fichero = Path(tmp) / "cifras.json"
            fichero.write_text(json.dumps(r))
            salida = subprocess.run([sys.executable, str(AQUI.parent / "censo.py"), "mapa", str(fichero)],
                                    capture_output=True, text=True, check=True).stdout
        self.assertIn([0.0, 245.0, True, "Borde"], json.loads(salida))

    def test_la_salida_lleva_fecha_de_datos_huella_y_atribucion(self):
        with tempfile.TemporaryDirectory() as tmp:
            fichero = Path(tmp) / "overpass-respuesta.json"
            fichero.write_text(json.dumps(respuesta(nodo(2, 10, shop="hairdresser", name="A"))))
            salida = subprocess.run(
                [sys.executable, str(AQUI.parent / "censo.py"), "cifras", str(fichero), str(LAT), str(LON),
                 "--cliente", "ninguno"], capture_output=True, text=True, check=True).stdout
        datos = json.loads(salida)
        self.assertEqual(datos["fuente"]["datos_osm_a"], "2026-11-18T10:00:00Z")
        self.assertEqual(len(datos["fuente"]["sha256"]), 64)
        self.assertIn("openstreetmap.org/copyright", datos["fuente"]["atribucion"])


if __name__ == "__main__":
    unittest.main()
