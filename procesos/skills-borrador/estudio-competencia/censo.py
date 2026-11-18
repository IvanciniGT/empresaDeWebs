"""Censo de competidores a partir de una respuesta de Overpass guardada.

Las cifras del informe salen de aquí y de ningún otro sitio. Nadie las teclea en
la maqueta: así salió «281» cuando eran 273 (revisión de Puri, R03–R05).

Solo usa la biblioteca estándar de Python.

Uso:
  1. Generar la consulta y guardarla junto a los datos:
       python3 censo.py consulta LAT LON [--radio 1500] > competencia/overpass-consulta.overpassql
  2. Lanzarla en la instancia de Overpass que diga herramientas-comunes (A-015) y
     guardar la respuesta tal cual en competencia/overpass-respuesta.json.
  3. Calcular las cifras:
       python3 censo.py cifras competencia/overpass-respuesta.json LAT LON \\
           --cliente node/13516520881 > competencia/cifras.json
     Si el cliente no está en OpenStreetMap: --cliente ninguno.
  4. Puntos para herramientas/mapa.py, sacados de las mismas cifras:
       python3 censo.py mapa competencia/cifras.json > competencia/puntos-mapa.json
     En la ronda 1 el mapa y la tabla calculaban la distancia de forma distinta
     (hasta un 1,5 % de diferencia), y un local podía cambiar de anillo.

cifras.json no se edita a mano. Si algo está mal, se corrige la consulta o los
datos y se vuelve a generar.
"""
import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

ACTIVIDAD = ("hairdresser", "barber")
# Valores de la etiqueta hairdresser=* que indican público masculino.
PUBLICO_POR_ETIQUETA = {"barber", "men", "male"}
# Cuando la etiqueta no lo dice, el nombre a veces sí. Se cuenta aparte porque es una inferencia.
PUBLICO_POR_NOMBRE = re.compile(r"barber|caballero", re.IGNORECASE)
ANILLOS_M = (250, 500, 1000, 1500)
DUPLICADO_M = 50
RADIO_TIERRA_M = 6371008.8
ATRIBUCION = "© colaboradores de OpenStreetMap, licencia ODbL · openstreetmap.org/copyright"


def consulta(lat, lon, radio):
    filtros = "\n".join(
        f'  nwr["shop"="{valor}"](around:{radio},{lat},{lon});' for valor in ACTIVIDAD
    )
    return f"[out:json][timeout:90];\n(\n{filtros}\n);\nout center tags;\n"


def distancia_m(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * RADIO_TIERRA_M * math.asin(math.sqrt(a))


def _normalizar(nombre):
    sin_tildes = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", sin_tildes.lower()).strip()


def _coordenadas(elemento):
    if "lat" in elemento:
        return elemento["lat"], elemento["lon"]
    centro = elemento.get("center")
    if centro:
        return centro["lat"], centro["lon"]
    return None


def _publico(etiquetas):
    if etiquetas.get("shop") == "barber" or etiquetas.get("hairdresser") in PUBLICO_POR_ETIQUETA:
        return "etiqueta"
    if PUBLICO_POR_NOMBRE.search(etiquetas.get("name", "")):
        return "nombre"
    return None


def cifras(respuesta, lat, lon, cliente, anillos=ANILLOS_M):
    excluidos, locales = [], []
    for elemento in respuesta.get("elements", []):
        ident = f'{elemento.get("type")}/{elemento.get("id")}'
        etiquetas = elemento.get("tags", {})
        nombre = etiquetas.get("name", "")
        if ident == cliente:
            continue
        if etiquetas.get("shop") not in ACTIVIDAD:
            excluidos.append({"id": ident, "nombre": nombre, "motivo": f'shop={etiquetas.get("shop")}'})
            continue
        punto = _coordenadas(elemento)
        if punto is None:
            excluidos.append({"id": ident, "nombre": nombre, "motivo": "sin coordenadas"})
            continue
        d = distancia_m(lat, lon, *punto)
        metros_por_grado = 2 * math.pi * RADIO_TIERRA_M / 360
        if d > anillos[-1]:
            excluidos.append({"id": ident, "nombre": nombre, "motivo": f"a {round(d)} m, fuera del radio"})
            continue
        locales.append({
            "id": ident, "nombre": nombre, "distancia_m": round(d), "_punto": punto,
            # Metros al este y al norte del cliente, como los espera herramientas/mapa.py.
            "este_m": round((punto[1] - lon) * metros_por_grado * math.cos(math.radians(lat)), 1),
            "norte_m": round((punto[0] - lat) * metros_por_grado, 1),
            "publico": _publico(etiquetas),
            "web": etiquetas.get("website") or etiquetas.get("contact:website") or "",
            "redes": sorted(k for k in etiquetas if k.startswith("contact:") and k != "contact:website"),
        })

    locales.sort(key=lambda x: (x["distancia_m"], x["id"]))
    unicos, duplicados = [], []
    for local in locales:
        gemelo = next((u for u in unicos
                       if local["nombre"] and _normalizar(u["nombre"]) == _normalizar(local["nombre"])
                       and distancia_m(*u["_punto"], *local["_punto"]) < DUPLICADO_M), None)
        if gemelo:
            duplicados.append({"id": local["id"], "nombre": local["nombre"], "igual_que": gemelo["id"]})
        else:
            unicos.append(local)

    def contar(hasta):
        dentro = [x for x in unicos if x["distancia_m"] <= hasta]
        return {
            "hasta_m": hasta,
            "total": len(dentro),
            "mismo_publico_por_etiqueta": sum(x["publico"] == "etiqueta" for x in dentro),
            "mismo_publico_por_nombre": sum(x["publico"] == "nombre" for x in dentro),
        }

    limpiar = lambda x: {k: v for k, v in x.items() if not k.startswith("_")}
    mismo_publico = [x for x in unicos if x["publico"]]
    return {
        "anillos": [contar(r) for r in anillos],
        "mas_cercanos": [limpiar(x) for x in unicos[:3]],
        "mas_cercanos_mismo_publico": [limpiar(x) for x in mismo_publico[:3]],
        "sin_nombre": sum(1 for x in unicos if not x["nombre"]),
        "con_web_en_osm": sum(1 for x in unicos if x["web"]),
        "excluidos": excluidos,
        "duplicados": duplicados,
        "locales": [limpiar(x) for x in unicos],
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="orden", required=True)
    c = sub.add_parser("consulta")
    c.add_argument("lat", type=float)
    c.add_argument("lon", type=float)
    c.add_argument("--radio", type=int, default=ANILLOS_M[-1])
    f = sub.add_parser("cifras")
    f.add_argument("respuesta", type=Path)
    f.add_argument("lat", type=float)
    f.add_argument("lon", type=float)
    f.add_argument("--cliente", required=True, help="node/123, way/456 o «ninguno»")
    m = sub.add_parser("mapa")
    m.add_argument("cifras", type=Path)
    a = p.parse_args(argv)

    if a.orden == "consulta":
        sys.stdout.write(consulta(a.lat, a.lon, a.radio))
        return 0
    if a.orden == "mapa":
        datos = json.loads(a.cifras.read_text(encoding="utf-8"))
        puntos = [[x["este_m"], x["norte_m"], x["publico"] is not None, x["nombre"]] for x in datos["locales"]]
        json.dump(puntos, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0

    bruto = a.respuesta.read_bytes()
    respuesta = json.loads(bruto)
    resultado = {
        "generado_por": "procesos/skills-borrador/estudio-competencia/censo.py",
        "generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fuente": {
            "fichero": a.respuesta.name,
            "sha256": hashlib.sha256(bruto).hexdigest(),
            # Fecha de los datos de OSM, no de cuando se lanzó la consulta.
            "datos_osm_a": respuesta.get("osm3s", {}).get("timestamp_osm_base", "desconocida"),
            "atribucion": ATRIBUCION,
        },
        "centro": {"lat": a.lat, "lon": a.lon, "cliente": a.cliente},
        "criterio": {
            "actividad": [f"shop={v}" for v in ACTIVIDAD],
            "mismo_publico_por_etiqueta": "shop=barber o hairdresser=" + "|".join(sorted(PUBLICO_POR_ETIQUETA)),
            "mismo_publico_por_nombre": PUBLICO_POR_NOMBRE.pattern + " (inferencia: decirlo así)",
            "duplicado": f"mismo nombre a menos de {DUPLICADO_M} m",
        },
    }
    resultado.update(cifras(respuesta, a.lat, a.lon, a.cliente))
    json.dump(resultado, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
