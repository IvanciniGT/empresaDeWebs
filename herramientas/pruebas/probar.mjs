#!/usr/bin/env node
/**
 * Pruebas de las herramientas comunes. Todo en local: no se descarga ninguna
 * web de terceros ni se piden teselas a OpenStreetMap.
 *
 * Uso (desde la raíz del repositorio):
 *   node herramientas/pruebas/probar.mjs            todas
 *   node herramientas/pruebas/probar.mjs extraer    solo las que contienen «extraer»
 *   node herramientas/pruebas/probar.mjs --conservar   no borra la carpeta de resultados
 *
 * Variable PYTHON: el Python con python-docx y Pillow (por defecto, .venv de la raíz).
 *
 * Una prueba que no falla cuando el código está mal no sirve: cada comprobación
 * se ha visto fallar estropeando a propósito lo que vigila (ver la skill
 * herramientas-comunes, «Cómo se prueba»).
 */
import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync, statSync, utimesSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { promisify } from 'node:util';
import { interpretarRobots } from '../robots.mjs';
import { servir } from './servidor.mjs';

const ejecutar = promisify(execFile);
const AQUI = path.dirname(fileURLToPath(import.meta.url));
const HERRAMIENTAS = path.dirname(AQUI);
const RAIZ = path.dirname(HERRAMIENTAS);
const PYTHON = process.env.PYTHON ?? path.join(RAIZ, '.venv/bin/python');
const argumentos = process.argv.slice(2);
const conservar = argumentos.includes('--conservar');
const filtro = argumentos.find((a) => !a.startsWith('--'));
const SALIDA = mkdtempSync(path.join(tmpdir(), 'pruebas-herramientas-'));

const pruebas = [];
const prueba = (nombre, fn) => pruebas.push({ nombre, fn });

async function pixeles(png) {
  const { stdout } = await ejecutar(PYTHON, ['-c', `
import json, sys
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGB")
colores = {c for _, c in im.getcolors(1 << 24)}
w, h = im.size
print(json.dumps({"ancho": w, "alto": h, "magenta": (255, 0, 255) in colores,
                  "verde": (0, 255, 0) in colores, "abajo": im.getpixel((5, h - 5))}))`, png]);
  return JSON.parse(stdout);
}

async function conWebDePrueba(fn) {
  const otra = await servir(path.join(AQUI, 'otra-web'));
  const web = await servir(path.join(AQUI, 'web-prueba'), { '{{EXTERNO}}': otra.url });
  try { return await fn(web, otra); } finally { await web.cerrar(); await otra.cerrar(); }
}

// ───────────────────────────── robots.txt

prueba('robots: gana la regla más larga (Allow dentro de un Disallow)', () => {
  const r = interpretarRobots('User-agent: *\nDisallow: /privado/\nAllow: /privado/publico.html\n');
  assert.equal(r.permitido('/privado/secreto.html'), false);
  assert.equal(r.permitido('/privado/publico.html'), true);
  assert.equal(r.permitido('/'), true);
});

prueba('robots: comodines y fin de ruta ($)', () => {
  const r = interpretarRobots('User-agent: *\nDisallow: /*.pdf$\nDisallow: /tienda*/carrito\n');
  assert.equal(r.permitido('/carta.pdf'), false);
  assert.equal(r.permitido('/carta.pdf?v=2'), true);
  assert.equal(r.permitido('/tienda-online/carrito'), false);
});

prueba('robots: el grupo con nuestro nombre manda sobre el de «*»', () => {
  const r = interpretarRobots('User-agent: OtroBot\nUser-agent: empresaDeWebs\nDisallow: /\nCrawl-delay: 4\n\nUser-agent: *\nAllow: /\n', 'empresaDeWebs/0.2');
  assert.equal(r.permitido('/cualquier-cosa'), false);
  assert.equal(r.retardo, 4);
});

prueba('robots: Disallow vacío permite todo y se leen los sitemaps', () => {
  const r = interpretarRobots('User-agent: *\nDisallow:\n\nSitemap: https://ejemplo.es/sitemap.xml\n');
  assert.equal(r.permitido('/lo-que-sea'), true);
  assert.deepEqual(r.sitemaps, ['https://ejemplo.es/sitemap.xml']);
});

// ───────────────────────────── captura

prueba('captura: ordenador, página completa y sin aviso de cookies', () => conWebDePrueba(async (web) => {
  const png = path.join(SALIDA, 'captura-ordenador.png');
  await ejecutar(path.join(HERRAMIENTAS, 'captura.sh'), [`${web.url}/servicios.html`, png]);
  const p = await pixeles(png);
  assert.equal(p.ancho, 1366);
  assert.ok(p.alto > 3200, `la captura debería ser de página completa y mide ${p.alto} px`);
  assert.ok(p.verde, 'no se ve la franja verde del final de la página');
  assert.equal(p.magenta, false, 'se ve el aviso de cookies (magenta)');
}));

prueba('captura: móvil (ancho < 768 → emulación de móvil) sin aviso', () => conWebDePrueba(async (web) => {
  const png = path.join(SALIDA, 'captura-movil.png');
  const { stdout } = await ejecutar(path.join(HERRAMIENTAS, 'captura.sh'), [`${web.url}/`, png, '390']);
  const p = await pixeles(png);
  assert.equal(p.ancho, 780, 'el móvil se captura a doble densidad (390 × 2)');
  assert.equal(p.magenta, false, 'se ve el aviso de cookies (magenta)');
  assert.match(stdout, /avisos de cookies ocultados/);
}));

prueba('captura: avisa de una web sin adaptar al móvil', () => conWebDePrueba(async (web) => {
  const { stdout } = await ejecutar('node', [path.join(HERRAMIENTAS, 'captura.mjs'), `${web.url}/sin-movil.html`, path.join(SALIDA, 'sin-movil.png'), '--movil']);
  assert.match(stdout, /NO está adaptada al móvil: no tiene la etiqueta viewport/);
}));

prueba('captura: con --con-avisos el aviso se queda', () => conWebDePrueba(async (web) => {
  const png = path.join(SALIDA, 'con-avisos.png');
  await ejecutar(path.join(HERRAMIENTAS, 'captura.sh'), [`${web.url}/`, png, '1366', '900', '--solo-pantalla', '--con-avisos']);
  const p = await pixeles(png);
  assert.equal(p.alto, 900);
  assert.ok(p.magenta, 'el aviso debería verse');
}));

// ───────────────────────────── extraer_web

let extraccion = null;
async function extraerUnaVez() {
  if (extraccion) return extraccion;
  extraccion = await conWebDePrueba(async (web, otra) => {
    const carpeta = path.join(SALIDA, 'web-actual');
    const { stdout } = await ejecutar('node', [path.join(HERRAMIENTAS, 'extraer_web.mjs'), `${web.url}/`, carpeta, '--espera', '0.1'], { maxBuffer: 1e7 });
    return {
      carpeta, stdout, base: web.url,
      datos: JSON.parse(readFileSync(path.join(carpeta, 'datos.json'), 'utf8')),
      resumen: readFileSync(path.join(carpeta, 'resumen.md'), 'utf8'),
      pedidas: web.pedidas, visitas: web.visitas, visitasOtra: otra.visitas.length,
    };
  });
  return extraccion;
}

prueba('extraer: no pide nunca lo que robots.txt prohíbe', async () => {
  const x = await extraerUnaVez();
  assert.equal(x.pedidas('/privado/secreto.html'), 0, 'ha pedido /privado/secreto.html');
  assert.ok(x.pedidas('/privado/publico.html') > 0, 'no ha visitado la excepción permitida');
  assert.ok(x.pedidas('/robots.txt') > 0);
});

prueba('extraer: no sale del sitio ni entra en administración', async () => {
  const x = await extraerUnaVez();
  assert.equal(x.visitasOtra, 0, 'ha visitado la otra web');
  assert.equal(x.pedidas('/wp-admin/'), 0, 'ha entrado en /wp-admin/');
});

prueba('extraer: encuentra la página que solo está en el sitemap y anota la rota', async () => {
  const x = await extraerUnaVez();
  assert.ok(x.datos.paginas.some((p) => p.url.endsWith('/oculta.html')));
  assert.ok(x.datos.rotas.some((r) => r.url.endsWith('/no-existe.html') && r.estado === 404));
});

prueba('extraer: se identifica en el User-Agent', async () => {
  const x = await extraerUnaVez();
  const paginas = x.visitas.filter((v) => v.ruta.endsWith('.html'));
  assert.ok(paginas.length && paginas.every((v) => v.agente.includes('empresaDeWebs/')));
});

prueba('extraer: textos, menú y precios (también los que pinta JavaScript)', async () => {
  const { datos, carpeta } = await extraerUnaVez();
  assert.deepEqual(datos.menu.map((m) => m.texto), ['Inicio', 'Servicios', 'Precios', 'Contacto']);
  const precios = datos.contacto.precios.map((p) => p.valor).join('\n');
  assert.match(precios, /Corte de caballero: 12 €/, 'falta el precio que pinta JavaScript');
  assert.match(precios, /Peinado \| 15,00 €/);
  const texto = readFileSync(path.join(carpeta, 'paginas', readdirSync(path.join(carpeta, 'paginas')).find((f) => f.includes('servicios'))), 'utf8');
  assert.match(texto, /^# Servicios$/m);
  assert.match(texto, /^- Tinte y mechas$/m);
  assert.doesNotMatch(texto, /Aceptar todas/, 'el texto del aviso de cookies se ha colado en la página');
});

prueba('extraer: contacto, horario y datos estructurados', async () => {
  const { datos } = await extraerUnaVez();
  const v = (k) => datos.contacto[k].map((x) => x.valor);
  assert.ok(v('telefonos').includes('967 000 111'));
  assert.ok(v('whatsapp').includes('600 000 222'));
  assert.ok(v('correos').includes('hola@peluqueria-la-prueba.invalid'));
  assert.ok(v('horarios').some((h) => h.startsWith('Lunes a viernes: 9:30')));
  assert.ok(v('direcciones').includes('C/ Inventada, 12'));
  assert.ok(v('redes').some((r) => r.startsWith('Instagram:')));
  assert.equal(datos.jsonld.negocio.tipo, 'HairSalon');
  assert.equal(datos.jsonld.negocio.direccion, 'C/ Inventada, 12, 02001, Albacete');
  assert.ok(datos.tecnologia.encontradas.includes('WordPress'));
});

prueba('extraer: imágenes a tamaño original, perezosas y con indicio de banco', async () => {
  const { datos, carpeta } = await extraerUnaVez();
  const por = (trozo) => datos.imagenes.find((i) => i.fichero?.includes(trozo));
  assert.deepEqual(por('foto-salon')?.medidas, [1200, 800], 'no ha sacado el original de la miniatura de WordPress');
  assert.ok(por('foto-perezosa'), 'falta la imagen perezosa');
  assert.match(por('shutterstock')?.posibleBanco ?? '', /nombre/);
  assert.match(por('equipo')?.posibleBanco ?? '', /metadatos/);
  for (const i of datos.imagenes.filter((x) => x.fichero)) assert.ok(existsSync(path.join(carpeta, i.fichero)));
});

prueba('extraer: capturas sin avisos y detección de web sin adaptar al móvil', async () => {
  const { datos, carpeta } = await extraerUnaVez();
  const servicios = datos.paginas.find((p) => p.url.endsWith('/servicios.html'));
  for (const tipo of ['ordenador', 'movil']) {
    const p = await pixeles(path.join(carpeta, servicios.capturas[tipo].fichero));
    assert.equal(p.magenta, false, `se ve el aviso en la captura de ${tipo}`);
    assert.ok(p.verde, `la captura de ${tipo} no llega al final de la página`);
  }
  const noAdaptadas = datos.paginas.filter((p) => p.capturas.movil?.adaptadaMovil === false).map((p) => p.url.split('/').pop());
  assert.deepEqual(noAdaptadas, ['sin-movil.html']);
  assert.equal(datos.avisosCookies.length >= 2, true);
});

prueba('extraer: descarga el PDF enlazado y escribe el resumen', async () => {
  const { datos, resumen, carpeta } = await extraerUnaVez();
  const carta = datos.documentos.find((d) => d.url.endsWith('/carta.pdf'));
  assert.ok(carta?.fichero && readFileSync(path.join(carpeta, carta.fichero)).toString('latin1').startsWith('%PDF'));
  assert.match(resumen, /Todo lo «detectado» es candidato/);
  assert.match(resumen, /robots\.txt no lo permite/);
});

// ───────────────────────────── html_a_pdf

prueba('html_a_pdf: avisa de la imagen rota y de la fuente que no carga', async () => {
  const pdf = path.join(SALIDA, 'prueba.pdf');
  const { stderr } = await ejecutar('node', [path.join(HERRAMIENTAS, 'html_a_pdf.mjs'), path.join(AQUI, 'pdf-prueba.html'), pdf]);
  assert.ok(readFileSync(pdf).toString('latin1').startsWith('%PDF'));
  // Se comprueban por separado las dos vías: el fallo de red y lo que no se ha dibujado.
  assert.match(stderr, /no ha cargado \S*imagen-que-no-existe\.png/, 'no avisa del fallo de red');
  assert.match(stderr, /imagen rota: imagen-que-no-existe\.png/, 'no avisa de la imagen sin dibujar');
  assert.match(stderr, /fuente sin cargar: Fuente Inexistente/);
  await assert.rejects(ejecutar('node', [path.join(HERRAMIENTAS, 'html_a_pdf.mjs'), path.join(AQUI, 'pdf-prueba.html'), pdf, '--estricto']));
});

prueba('html_a_pdf.sh: se sigue llamando igual que antes', async () => {
  const pdf = path.join(SALIDA, 'limpio.pdf');
  const { stdout } = await ejecutar(path.join(HERRAMIENTAS, 'html_a_pdf.sh'), [path.join(AQUI, 'web-prueba', 'sin-movil.html'), pdf]);
  assert.match(stdout, /limpio\.pdf/);
  assert.ok(statSync(pdf).size > 1000);
});

// ───────────────────────────── mapa.py (contra un servidor de teselas local)

prueba('mapa: guarda las teselas 7 días y al caducar pregunta si han cambiado', async () => {
  const tesela = readFileSync(path.join(AQUI, 'tesela.png'));
  const peticiones = [];
  const servidor = await servir(AQUI, {}, async (ruta, peticion, respuesta) => {
    if (!/^\/\d+\/\d+\/\d+\.png$/.test(ruta)) return false;
    const condicional = Boolean(peticion.headers['if-modified-since']);
    peticiones.push({ condicional, agente: peticion.headers['user-agent'] });
    if (condicional) respuesta.writeHead(304).end();
    else respuesta.writeHead(200, { 'content-type': 'image/png', 'last-modified': new Date(Date.now() - 864e5).toUTCString() }).end(tesela);
    return true;
  });
  const cache = path.join(SALIDA, 'cache-teselas');
  const entorno = { ...process.env, OSM_TESELAS: `${servidor.url}/{z}/{x}/{y}.png`, OSM_CACHE: cache };
  const mapa = (n) => ejecutar(PYTHON, [path.join(HERRAMIENTAS, 'mapa.py'), '38.99', '-1.85', path.join(SALIDA, `mapa-${n}.png`)], { env: entorno });
  try {
    await mapa(1);
    const primera = peticiones.length;
    assert.ok(primera > 0 && peticiones.every((p) => p.agente.startsWith('empresaDeWebs/')));
    await mapa(2);
    assert.equal(peticiones.length, primera, 'ha vuelto a pedir teselas que tenía en caché');
    const hace8dias = new Date(Date.now() - 8 * 864e5);
    const todas = (dir) => readdirSync(dir, { withFileTypes: true }).flatMap((e) => (e.isDirectory() ? todas(path.join(dir, e.name)) : [path.join(dir, e.name)]));
    for (const f of todas(cache)) utimesSync(f, hace8dias, hace8dias);
    await mapa(3);
    const nuevas = peticiones.slice(primera);
    assert.equal(nuevas.length, primera);
    assert.ok(nuevas.every((p) => p.condicional), 'al caducar debería preguntar con If-Modified-Since');
    const p = await pixeles(path.join(SALIDA, 'mapa-3.png'));
    assert.deepEqual([p.ancho, p.alto], [1200, 700]);
  } finally { await servidor.cerrar(); }
});

// ───────────────────────────── docx_util

prueba('docx_util: el Word sale con la estructura que exige Word', async () => {
  const docx = path.join(SALIDA, 'prueba.docx');
  await ejecutar(PYTHON, ['-c', `
import sys
sys.path.insert(0, ${JSON.stringify(HERRAMIENTAS)})
import docx_util as w
doc = w.nuevo_documento()
w.opciones(doc, ["Uno", "Dos", "Tres"], por_fila=2, marcadas=("Dos",))
w.opciones(doc, ["Sí", "No"])
w.hueco(doc, "Nombre", ayuda="como lo escribiríais")
w.tabla_respuestas(doc, ["Pregunta", "Sí", "Respuesta"], [["¿Abrís en agosto?", "[ ]", ""]], [8, 2, 6.6], columnas_respuesta=(2,), fondo_fila="EEF2F6")
w.recuadro(doc, "Lo que sabemos", ["Una línea", "Otra"])
w.propuesta_texto(doc, "Quiénes somos", "Texto propuesto")
w.imagen(doc, ${JSON.stringify(path.join(AQUI, 'tesela.png'))}, 4, pie="Una tesela de prueba")
w.pie_de_pagina(doc, "Prueba")
w.guardar(doc, ${JSON.stringify(docx)})`]);
  const { stdout } = await ejecutar(PYTHON, [path.join(AQUI, 'revisar_docx.py'), docx]).catch((e) => e);
  assert.match(stdout, /sin problemas de estructura ni de propiedades/, stdout);
});

prueba('docx_util: no guarda encima de un documento abierto en Word', async () => {
  const carpeta = path.join(SALIDA, 'abierto');
  const codigo = (nombre) => `
import sys
sys.path.insert(0, ${JSON.stringify(HERRAMIENTAS)})
import docx_util as w
w.guardar(w.nuevo_documento(), ${JSON.stringify(carpeta)} + "/" + ${JSON.stringify(nombre)})`;
  await ejecutar('mkdir', ['-p', carpeta]);
  // Word, con un nombre largo, cambia los dos primeros caracteres por «~$».
  writeFileSync(path.join(carpeta, '~$estionario de prueba.docx'), 'bloqueo');
  await assert.rejects(ejecutar(PYTHON, ['-c', codigo('Cuestionario de prueba.docx')]), /está abierto/);
  assert.equal(existsSync(path.join(carpeta, 'Cuestionario de prueba.docx')), false);
  await ejecutar(PYTHON, ['-c', codigo('Otro documento.docx')]);
  assert.ok(existsSync(path.join(carpeta, 'Otro documento.docx')));
});

// ───────────────────────────── ejecución

let fallos = 0;
for (const { nombre, fn } of pruebas.filter((p) => !filtro || p.nombre.includes(filtro))) {
  const inicio = Date.now();
  try {
    await fn();
    console.log(`✓ ${nombre}  (${((Date.now() - inicio) / 1000).toFixed(1)} s)`);
  } catch (e) {
    fallos += 1;
    console.log(`✗ ${nombre}\n    ${String(e.message).split('\n').join('\n    ')}`);
  }
}
if (conservar) console.log(`\nResultados en ${SALIDA}`);
else rmSync(SALIDA, { recursive: true, force: true });
console.log(fallos ? `\n${fallos} pruebas fallidas` : '\nTodas las pruebas pasan');
process.exit(fallos ? 1 : 0);
