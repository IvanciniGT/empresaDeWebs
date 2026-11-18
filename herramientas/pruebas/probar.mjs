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
  // La que no lleva alt avisa; la decorativa (alt="") no: solo un aviso de alt.
  assert.equal((stderr.match(/imagen sin texto alternativo \(alt\): tesela\.png/g) ?? []).length, 1, 'el aviso de alt no distingue alt vacío de alt ausente');
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

// ───────────────────────────── captura de una zona (R57 de Puri)

prueba('captura: --elemento recorta a ese elemento y --recorte a esa caja', () => conWebDePrueba(async (web) => {
  const png = path.join(SALIDA, 'zona.png');
  await ejecutar('node', [path.join(HERRAMIENTAS, 'captura.mjs'), `${web.url}/servicios.html`, png, '--elemento', '#final']);
  const p = await pixeles(png);
  assert.deepEqual([p.ancho, p.alto], [1366, 40]);
  assert.deepEqual(p.abajo, [0, 255, 0], 'el recorte no es la franja verde del final');
  await ejecutar('node', [path.join(HERRAMIENTAS, 'captura.mjs'), `${web.url}/`, png, '--recorte', '10,20,300,100']);
  const q = await pixeles(png);
  assert.deepEqual([q.ancho, q.alto], [300, 100]);
  await assert.rejects(ejecutar('node', [path.join(HERRAMIENTAS, 'captura.mjs'), `${web.url}/`, png, '--elemento', '#no-existe']), /No hay ningún elemento/);
}));

// ───────────────────────────── números de página (para informe.css, R56 de Puri y Lola)

prueba('html_a_pdf: Chrome imprime «Página X de Y» con @page y sin número en la portada', async () => {
  const html = path.join(SALIDA, 'numeros.html');
  writeFileSync(html, `<!doctype html><html lang="es"><meta charset="utf-8"><style>
    @page { size: A5; margin: 15mm 12mm 18mm; @bottom-center { content: "Página " counter(page) " de " counter(pages); font: 8pt sans-serif; } }
    @page :first { @bottom-center { content: none; } }
    section { break-after: page; }</style>
    <section><h1>Portada</h1></section><section><h2>Uno</h2></section><section><h2>Dos</h2></section></html>`);
  const pdf = path.join(SALIDA, 'numeros.pdf');
  await ejecutar('node', [path.join(HERRAMIENTAS, 'html_a_pdf.mjs'), html, pdf]);
  const pagina = async (n) => (await ejecutar('pdftotext', ['-f', String(n), '-l', String(n), pdf, '-'])).stdout;
  assert.doesNotMatch(await pagina(1), /Página/);
  assert.match(await pagina(2), /Página 2 de 3/);
  assert.match(await pagina(3), /Página 3 de 3/);
});

// ───────────────────────────── lo instalado (A-008)

prueba('instalado: fuentes con su licencia, iconos con la suya y Lighthouse 13.6.0', async () => {
  for (const [carpeta, minimo] of [['fuentes/inter', 18], ['fuentes/fraunces', 24]]) {
    const ttf = readdirSync(path.join(HERRAMIENTAS, carpeta)).filter((f) => f.endsWith('.ttf'));
    assert.ok(ttf.length >= minimo, `${carpeta}: ${ttf.length} fuentes`);
    assert.match(readFileSync(path.join(HERRAMIENTAS, carpeta, 'OFL.txt'), 'utf8'), /SIL OPEN FONT LICENSE/i);
  }
  assert.match(readFileSync(path.join(HERRAMIENTAS, 'iconos/phone.svg'), 'utf8'), /<svg/);
  assert.match(readFileSync(path.join(HERRAMIENTAS, 'iconos/LICENSE.txt'), 'utf8'), /ISC License/);
  const { stdout } = await ejecutar(path.join(HERRAMIENTAS, 'node_modules/.bin/lighthouse'), ['--version']);
  assert.equal(stdout.trim(), '13.6.0');
});

prueba('instalado: si una descarga no cuadra con su suma, instalar.sh no instala nada', async () => {
  const copia = path.join(SALIDA, 'instalar-copia');
  await ejecutar('mkdir', ['-p', path.join(copia, 'vendor/descargas'), path.join(copia, 'iconos')]);
  await ejecutar('cp', [path.join(HERRAMIENTAS, 'instalar.sh'), copia]);
  writeFileSync(path.join(copia, 'iconos/testigo.svg'), 'lo que había antes');
  writeFileSync(path.join(copia, 'vendor/descargas/lucide-icons-1.75.0.zip'), 'esto no es el zip de Lucide');
  await assert.rejects(ejecutar(path.join(copia, 'instalar.sh'), ['iconos']), /no coincide/);
  assert.equal(readFileSync(path.join(copia, 'iconos/testigo.svg'), 'utf8'), 'lo que había antes', 'ha tocado los iconos con una descarga mala');
});

// ───────────────────────────── ortografia.py (hunspell)

prueba('ortografía: señala las erratas y no lo que es de la empresa, del cliente, siglas o unidades', async () => {
  const codigo = `
import sys, json
sys.path.insert(0, ${JSON.stringify(HERRAMIENTAS)})
import ortografia
print(json.dumps(ortografia.palabras_dudosas(
  "¿Prefierís hablarlo por WhatsApp? Abrimos a las 9 h, a 200 m de la Plaza. Hay una herrata. La RGPD manda. Peluquería Cotillas.",
  extra=["Cotillas"])))`;
  const dudosas = JSON.parse((await ejecutar('/usr/bin/python3', ['-c', codigo])).stdout);
  assert.deepEqual(Object.keys(dudosas).sort(), ['Prefierís', 'herrata']);
});

// ───────────────────────────── transcribir.sh (whisper.cpp)

async function notaDeVoz() {
  // Voz sintética de macOS con un texto inventado, en Ogg/Opus como WhatsApp.
  // Mónica: con la voz «Eddy» whisper falla cifras (comprobado), y no es lo que se prueba.
  const aiff = path.join(SALIDA, 'nota.aiff');
  const opus = path.join(SALIDA, 'nota.opus');
  if (existsSync(opus)) return opus;
  await ejecutar('say', ['-v', 'Mónica', '-o', aiff, 'Abrimos de martes a sábado. El corte de caballero cuesta doce euros.']);
  await ejecutar('ffmpeg', ['-loglevel', 'error', '-y', '-i', aiff, '-c:a', 'libopus', '-b:a', '24k', '-ar', '48000', '-ac', '1', opus]);
  return opus;
}

prueba('transcribir: nota de voz de WhatsApp (Ogg/Opus) a texto, en local', async () => {
  const opus = await notaDeVoz();
  await ejecutar(path.join(HERRAMIENTAS, 'transcribir.sh'), [opus]);
  const texto = readFileSync(`${opus}.txt`, 'utf8');
  assert.match(texto, /Transcripción automática/);
  assert.match(texto, /martes a sábado/i);
  assert.match(texto, /12 euros|doce euros/i);
});

prueba('transcribir: no deja la transcripción donde iría a git', async () => {
  const opus = await notaDeVoz();
  const carpeta = path.join(RAIZ, 'clientes', `prueba-paco-${process.pid}`);
  await ejecutar('mkdir', ['-p', path.join(carpeta, 'privado')]);
  try {
    await assert.rejects(ejecutar(path.join(HERRAMIENTAS, 'transcribir.sh'), [opus, '--salida', carpeta]), /entraría en git/);
    assert.equal(existsSync(path.join(carpeta, 'nota.opus.txt')), false);
    await ejecutar(path.join(HERRAMIENTAS, 'transcribir.sh'), [opus, '--salida', path.join(carpeta, 'privado')]);
    assert.ok(existsSync(path.join(carpeta, 'privado', 'nota.opus.txt')));
  } finally { rmSync(carpeta, { recursive: true, force: true }); }
});

// ───────────────────────────── medir_web.mjs (Lighthouse)

prueba('medir: cuatro notas en móvil y ordenador, firmado y sin medidores de visitas', () => conWebDePrueba(async (web) => {
  const carpeta = path.join(SALIDA, 'medir');
  await ejecutar('node', [path.join(HERRAMIENTAS, 'medir_web.mjs'), `${web.url}/contacto.html`, carpeta, '--nombre', 'prueba']).catch((e) => e);
  const r = JSON.parse(readFileSync(path.join(carpeta, 'prueba-resumen.json'), 'utf8'));
  for (const d of ['movil', 'ordenador']) {
    assert.deepEqual(Object.keys(r.dispositivos[d].notas).sort(), ['accessibility', 'best-practices', 'performance', 'seo']);
    assert.ok(Object.values(r.dispositivos[d].notas).every((n) => n > 0 && n <= 100));
  }
  const ajustes = JSON.parse(readFileSync(path.join(carpeta, 'prueba-movil.json'), 'utf8')).configSettings;
  assert.ok(ajustes.blockedUrlPatterns.includes('*google-analytics.com*'), 'no bloquea los medidores de visitas');
  const agentes = web.visitas.filter((v) => v.ruta === '/contacto.html').map((v) => v.agente);
  assert.ok(agentes.length >= 2 && agentes.every((a) => a.includes('empresaDeWebs/')), 'Lighthouse no se identifica');
}));

// ───────────────────────────── overpass.mjs (contra un Overpass falso)

prueba('overpass: guarda consulta, respuesta y metadatos; no repite; espera ante un 429', async () => {
  const { consultar } = await import('../overpass.mjs');
  const recibidas = [];
  let ocupado = 1;
  const falso = await servir(AQUI, {}, async (ruta, peticion, respuesta) => {
    if (ruta !== '/api/interpreter') return false;
    let cuerpo = '';
    for await (const t of peticion) cuerpo += t;
    recibidas.push({ agente: peticion.headers['user-agent'], consulta: new URLSearchParams(cuerpo).get('data'), hora: Date.now() });
    if (ocupado-- > 0) { respuesta.writeHead(429).end('Too Many Requests'); return true; }
    respuesta.writeHead(200, { 'content-type': 'application/json' }).end(JSON.stringify({
      osm3s: { timestamp_osm_base: '2026-11-18T10:00:00Z' },
      elements: [{ type: 'node', id: 1 }, { type: 'node', id: 2 }, { type: 'way', id: 3 }],
    }));
    return true;
  });
  const carpeta = path.join(SALIDA, 'overpass');
  const consulta = '[out:json][timeout:60];\nnode["shop"="hairdresser"](around:1500,38.99,-1.85);\nout;';
  const opciones = { nombre: 'censo', servidor: `${falso.url}/api/interpreter`, espera: 200, avisar: () => {} };
  try {
    const m = await consultar(consulta, carpeta, opciones);
    assert.equal(recibidas.length, 2, 'tras el 429 debería reintentar una vez');
    assert.ok(recibidas[1].hora - recibidas[0].hora >= 200, 'no ha esperado antes de reintentar');
    assert.ok(recibidas.every((r) => r.agente.startsWith('empresaDeWebs/')));
    assert.equal(m.elementos, 3);
    assert.deepEqual(m.porTipo, { node: 2, way: 1 });
    assert.equal(readFileSync(path.join(carpeta, 'censo.overpassql'), 'utf8'), consulta + '\n');
    const meta = JSON.parse(readFileSync(path.join(carpeta, 'censo.meta.json'), 'utf8'));
    assert.equal(meta.datosOsmDe, '2026-11-18T10:00:00Z');
    assert.match(meta.licencia, /openstreetmap\.org\/copyright/);
    await consultar(consulta, carpeta, opciones);
    assert.equal(recibidas.length, 2, 'ha repetido una consulta que ya estaba guardada');
    await assert.rejects(consultar('[out:json];\nnode["email"="ana@ejemplo.es"];\nout;', carpeta, { ...opciones, nombre: 'mal' }), /datos personales/);
    assert.equal(recibidas.length, 2, 'ha enviado una consulta con un correo');
  } finally { await falso.cerrar(); }
});

prueba('overpass: por defecto, la instancia que admite uso comercial (A-015)', async () => {
  const { SERVIDOR } = await import('../overpass.mjs');
  assert.equal(SERVIDOR, 'https://overpass.private.coffee/api/interpreter');
});

// ───────────────────────────── cuestionario con ID (Reme) y lector

async function cuestionarioConIds(nombre) {
  const docx = path.join(SALIDA, `${nombre}.docx`);
  await ejecutar(PYTHON, ['-c', `
import sys
sys.path.insert(0, ${JSON.stringify(HERRAMIENTAS)})
import docx_util as w
doc = w.nuevo_documento(titulo="Prueba", autor="Paco")
w.opciones(doc, ["Clientes nuevos", "Horario y cómo llegar", "Reservas"], id="A 4.1")
w.opciones(doc, ["Mañanas", "Tardes", "Sábados", "Domingos"], por_fila=2, id="A 4.4")
w.hueco(doc, "¿Para cuándo?", lineas=3, id="A 4.5")
w.tabla_respuestas(doc, ["Lo que hemos visto", "¿Bien?", "Si no, lo bueno"],
    [["Horario", "[ ]", ""], ["Teléfono", "[ ]", ""]], [8, 2.5, 6.1], columnas_respuesta=(2,), ids=["A 1.4", "A 1.3"])
w.propuesta_texto(doc, "Quiénes somos", "Texto propuesto", id="B 6.3")
w.guardar(doc, ${JSON.stringify(docx)})`]);
  return docx;
}

async function rellenar(entrada, salida, respuestas) {
  const json = path.join(SALIDA, `${path.basename(salida)}.json`);
  writeFileSync(json, JSON.stringify(respuestas));
  await ejecutar(PYTHON, [path.join(AQUI, 'rellenar_docx.py'), entrada, salida, json]);
}

async function leer(docx, ...mas) {
  return (await ejecutar('/usr/bin/python3', [path.join(HERRAMIENTAS, 'leer_cuestionario.py'), docx, ...mas])).stdout;
}

const RESPUESTAS = {
  'A 4.1|1': true, 'A 4.1|3': true, 'A 4.4|2': true, 'A 4.5': 'Para marzo (inventado)',
  'A 1.4|¿Bien?': false, 'A 1.4|Si no, lo bueno': 'L-V 10-19', 'A 1.3|¿Bien?': true,
  'B 6.3|Cambiadlo así': true, 'B 6.3|cambio': 'Somos tres hermanos', __fuera__: ['Nota escrita fuera de los recuadros'],
};

function comprobarLectura(md) {
  const fila = (id) => md.split('\n').find((l) => l.startsWith(`| ${id} |`)) ?? '';
  assert.match(fila('A 4.1'), /Clientes nuevos, Reservas \|$/);
  assert.match(fila('A 4.4'), /Tardes \|$/);
  assert.match(fila('A 4.5'), /Para marzo \(inventado\) \|$/);
  assert.match(fila('A 1.4'), /¿Bien\?: ☐ · Si no, lo bueno: L-V 10-19/);
  assert.match(fila('A 1.3'), /¿Bien\?: ☒ · Si no, lo bueno: \(vacío\)/);
  assert.match(fila('B 6.3'), /Me gusta así: ☐ · Cambiadlo así: ☒ · cambio: Somos tres hermanos/);
}

prueba('cuestionario: cada respuesta llega con su ID, y lo escrito fuera también se ve', async () => {
  const enviado = await cuestionarioConIds('enviado');
  const { stdout } = await ejecutar(PYTHON, [path.join(AQUI, 'revisar_docx.py'), enviado]).catch((e) => e);
  assert.match(stdout, /sin problemas/, stdout);
  const recibido = path.join(SALIDA, 'recibido.docx');
  await rellenar(enviado, recibido, RESPUESTAS);
  const md = await leer(recibido, '--original', enviado, '--catalogo', path.join(AQUI, 'catalogo-prueba.md'));
  comprobarLectura(md);
  assert.match(md, /## Escrito fuera de los recuadros\n\n- Nota escrita fuera de los recuadros\n/);
  assert.match(md, /\| A 4\.1 \| ¿Para qué queréis la web\? \|/, 'no ha sacado la pregunta del catálogo');
});

prueba('cuestionario: sin contestar, sale vacío (no «Escribid aquí»)', async () => {
  const enviado = await cuestionarioConIds('vacio');
  const md = await leer(enviado);
  assert.doesNotMatch(md, /Escribid/);
  assert.match(md, /\| A 4\.5 \|  \| \(vacío\) \|/);
  assert.match(md, /\| A 4\.1 \|  \| \(ninguna marcada\) \|/);
});

prueba('cuestionario: las respuestas sobreviven a guardarlo con LibreOffice', async () => {
  const enviado = await cuestionarioConIds('lo-enviado');
  const recibido = path.join(SALIDA, 'lo-recibido.docx');
  await rellenar(enviado, recibido, RESPUESTAS);
  const salida = path.join(SALIDA, 'libreoffice');
  await ejecutar('soffice', [`-env:UserInstallation=file://${path.join(SALIDA, 'perfil-lo')}`, '--headless',
    '--convert-to', 'docx:MS Word 2007 XML', '--outdir', salida, recibido], { timeout: 120000 });
  const md = await leer(path.join(salida, 'lo-recibido.docx'), '--original', enviado);
  comprobarLectura(md);
  assert.doesNotMatch(md.split('## Escrito fuera')[1] ?? '', /Para marzo|L-V 10-19|tres hermanos/, 'las respuestas han salido de sus controles');
});

prueba('cuestionario: lee los dos formatos del catálogo y no los ID retirados', async () => {
  const codigo = `
import sys, json
sys.path.insert(0, ${JSON.stringify(HERRAMIENTAS)})
import leer_cuestionario as l
print(json.dumps(sorted(l.leer_catalogo(${JSON.stringify(path.join(AQUI, 'catalogo-prueba.md'))}))))`;
  const ids = JSON.parse((await ejecutar('/usr/bin/python3', ['-c', codigo])).stdout);
  assert.deepEqual(ids, ['A 1.1', 'A 1.2', 'A 1.3', 'A 4.1', 'B 6.9', 'B1 1.4']);
});

prueba('cuestionario: no escribe las respuestas donde irían a git; sin ID, avisa', async () => {
  const enviado = await cuestionarioConIds('git');
  const dentro = path.join(RAIZ, 'clientes', `prueba-paco-${process.pid}`, 'respuestas.md');
  try {
    await assert.rejects(leer(enviado, '-o', dentro), /entraría en git/);
    assert.equal(existsSync(dentro), false);
  } finally { rmSync(path.dirname(dentro), { recursive: true, force: true }); }
  const sinIds = path.join(SALIDA, 'sin-ids.docx');
  await ejecutar(PYTHON, ['-c', `
import sys
sys.path.insert(0, ${JSON.stringify(HERRAMIENTAS)})
import docx_util as w
doc = w.nuevo_documento(); w.hueco(doc, "Sin ID"); w.guardar(doc, ${JSON.stringify(sinIds)})`]);
  await assert.rejects(leer(sinIds), /no tiene controles con ID/);
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
