"""Rellena un cuestionario como lo haría el cliente en Word, para las pruebas.

Uso: python3 rellenar_docx.py ENTRADA.docx SALIDA.docx respuestas.json
  respuestas.json: {"B1 1.7|2": true, "B1 2.1": "Ana", "__fuera__": ["texto suelto"]}
  - casilla (true/false): cambia w14:checked y el símbolo, como Word;
  - texto: lo escribe en el primer párrafo del control y vacía los demás;
  - "__fuera__": párrafos que el cliente escribe fuera de los recuadros, al final.
Solo biblioteca estándar. Datos inventados: nunca se usa con respuestas reales.
"""
import json
import shutil
import sys
import zipfile
from xml.etree import ElementTree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W14 = "http://schemas.microsoft.com/office/word/2010/wordml"


def rellenar(entrada, salida, respuestas):
    with zipfile.ZipFile(entrada) as z:
        xml = z.read("word/document.xml")
    # ElementTree pierde los prefijos si no se registran, y Word los necesita (mc:Ignorable="w14").
    for prefijo, uri in {m[0]: m[1] for m in __import__("re").findall(rb'xmlns:(\w+)="([^"]+)"', xml)}.items():
        ElementTree.register_namespace(prefijo.decode(), uri.decode())
    raiz = ElementTree.fromstring(xml)
    usadas = set()
    for sdt in raiz.iter(f"{{{W}}}sdt"):
        tag = sdt.find(f"{{{W}}}sdtPr/{{{W}}}tag")
        clave = tag.get(f"{{{W}}}val") if tag is not None else None
        if clave not in respuestas:
            continue
        usadas.add(clave)
        valor = respuestas[clave]
        contenido = sdt.find(f"{{{W}}}sdtContent")
        casilla = sdt.find(f"{{{W}}}sdtPr/{{{W14}}}checkbox")
        textos = list(contenido.iter(f"{{{W}}}t"))
        if casilla is not None:
            casilla.find(f"{{{W14}}}checked").set(f"{{{W14}}}val", "1" if valor else "0")
            textos[0].text = "☒" if valor else "☐"
        else:
            # Al escribir, Word quita la marca de «texto de ayuda» y deja solo lo escrito.
            pr = sdt.find(f"{{{W}}}sdtPr")
            ayuda = pr.find(f"{{{W}}}showingPlcHdr")
            if ayuda is not None:
                pr.remove(ayuda)
            parrafos = list(contenido.iter(f"{{{W}}}p")) or [contenido]  # en línea: los runs van directos
            for p in parrafos:
                for r in p.findall(f"{{{W}}}r"):
                    p.remove(r)
            r = ElementTree.SubElement(parrafos[0], f"{{{W}}}r")
            ElementTree.SubElement(r, f"{{{W}}}t").text = valor
    faltan = set(respuestas) - usadas - {"__fuera__"}
    if faltan:
        raise SystemExit(f"No hay controles con estas etiquetas: {sorted(faltan)}")
    cuerpo = raiz.find(f"{{{W}}}body")
    for texto in respuestas.get("__fuera__", []):
        p = ElementTree.Element(f"{{{W}}}p")
        ElementTree.SubElement(ElementTree.SubElement(p, f"{{{W}}}r"), f"{{{W}}}t").text = texto
        cuerpo.insert(len(cuerpo) - 1, p)  # antes de sectPr, que va al final
    shutil.copy(entrada, salida)
    with zipfile.ZipFile(entrada) as origen, zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as destino:
        for item in origen.infolist():
            datos = ElementTree.tostring(raiz, xml_declaration=True, encoding="UTF-8") if item.filename == "word/document.xml" else origen.read(item.filename)
            destino.writestr(item, datos)


if __name__ == "__main__":
    rellenar(sys.argv[1], sys.argv[2], json.loads(open(sys.argv[3], encoding="utf-8").read()))
