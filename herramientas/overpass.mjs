#!/usr/bin/env node
/**
 * Consulta Overpass (OpenStreetMap) y guarda la consulta y la respuesta juntas,
 * para que cualquier cifra que salga de ellas se pueda recalcular y revisar (A-015).
 *
 * Uso:
 *   node herramientas/overpass.mjs consulta.overpassql carpeta_salida [--nombre NOMBRE]
 *
 * Deja en carpeta_salida:
 *   NOMBRE.overpassql   la consulta exacta que se ha enviado
 *   NOMBRE.json         la respuesta, tal cual
 *   NOMBRE.meta.json    servidor, fecha, fecha de los datos de OSM, elementos y licencia
 * (NOMBRE, por defecto, el de la consulta.)
 *
 * Servidor: overpass.private.coffee. Sus condiciones admiten cualquier proyecto y
 * no ponen límites; el principal (overpass-api.de) pide que el uso comercial vaya
 * por otro. Para cambiarlo: variable OVERPASS_URL, solo tras leer sus condiciones.
 *
 * Cómo usamos el servicio (política de la wiki de OSM y del servidor):
 *   - User-Agent que nos identifica; una consulta cada vez, nunca en paralelo;
 *   - ante un 429 o un 504 (saturado), esperar 30 s antes de reintentar (3 veces como mucho);
 *   - sin datos personales en la consulta;
 *   - si la misma consulta ya está guardada, NO se repite (--repetir para forzarlo).
 * Los datos son de OpenStreetMap (ODbL): cualquier cifra o mapa que salga de aquí
 * lleva «© colaboradores de OpenStreetMap · openstreetmap.org/copyright».
 */
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { esComando, FIRMA } from './chrome.mjs';

export const SERVIDOR = 'https://overpass.private.coffee/api/interpreter';
export const CONDICIONES = 'https://overpass.private.coffee/ · https://private.coffee/terms.html';
const REINTENTOS = 3;
const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

export async function consultar(consulta, carpeta, { nombre, repetir = false, servidor = process.env.OVERPASS_URL ?? SERVIDOR, espera = 30000, avisar = console.error } = {}) {
  const texto = consulta.trim() + '\n';
  if (!/\[out:json/.test(texto)) throw new Error('La consulta tiene que pedir JSON: empieza con [out:json][timeout:…];');
  // Un correo o un teléfono no tienen nada que hacer en una consulta de mapas.
  // (Un número suelto de 9 cifras no se mira: puede ser el identificador de un nodo de OSM.)
  if (/[\w.+-]+@[\w-]+\.[\w.]+|(?:\+34|0034)[\s.-]?\d|\b[6789]\d{2}[\s.-]\d{2,3}[\s.-]\d{2,3}\b/.test(texto)) throw new Error('La consulta parece llevar un correo o un teléfono: no se envían datos personales.');
  mkdirSync(carpeta, { recursive: true });
  const rutas = { consulta: path.join(carpeta, `${nombre}.overpassql`), respuesta: path.join(carpeta, `${nombre}.json`), meta: path.join(carpeta, `${nombre}.meta.json`) };
  const huella = createHash('sha256').update(texto).digest('hex');
  if (!repetir && existsSync(rutas.meta) && existsSync(rutas.respuesta)) {
    const previa = JSON.parse(readFileSync(rutas.meta, 'utf8'));
    if (previa.huellaConsulta === huella) {
      avisar(`Ya está guardada (${previa.consultada}); no se repite. Para repetirla: --repetir`);
      return { ...previa, repetida: false };
    }
  }
  let respuesta;
  for (let intento = 1; ; intento++) {
    respuesta = await fetch(servidor, {
      method: 'POST',
      headers: { 'user-agent': FIRMA, 'content-type': 'application/x-www-form-urlencoded', accept: 'application/json' },
      body: new URLSearchParams({ data: texto }),
      signal: AbortSignal.timeout(200000),
    });
    if (![429, 504].includes(respuesta.status) || intento > REINTENTOS) break;
    avisar(`El servidor está ocupado (HTTP ${respuesta.status}). Espero ${espera / 1000} s (intento ${intento} de ${REINTENTOS})…`);
    await respuesta.body?.cancel();
    await esperar(espera);
  }
  const cuerpo = await respuesta.text();
  if (!respuesta.ok) throw new Error(`Overpass ha respondido HTTP ${respuesta.status}: ${cuerpo.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').slice(0, 300)}`);
  let datos;
  try { datos = JSON.parse(cuerpo); } catch { throw new Error('La respuesta no es JSON: ¿la consulta pide [out:json]?'); }
  // Overpass responde 200 aunque la consulta se corte por tiempo o memoria: lo dice en «remark».
  if (datos.remark && /runtime error|timed out|out of memory/i.test(datos.remark)) throw new Error(`Overpass no ha terminado la consulta: ${datos.remark}`);
  const meta = {
    servidor, condiciones: servidor === SERVIDOR ? CONDICIONES : 'servidor cambiado con OVERPASS_URL: anota aquí dónde están sus condiciones',
    consultada: new Date().toISOString(),
    datosOsmDe: datos.osm3s?.timestamp_osm_base ?? null,
    elementos: datos.elements?.length ?? 0,
    porTipo: (datos.elements ?? []).reduce((t, e) => ({ ...t, [e.type]: (t[e.type] ?? 0) + 1 }), {}),
    huellaConsulta: huella,
    licencia: 'Datos © colaboradores de OpenStreetMap, ODbL 1.0 · openstreetmap.org/copyright',
    herramienta: 'herramientas/overpass.mjs 0.3',
  };
  writeFileSync(rutas.consulta, texto);
  writeFileSync(rutas.respuesta, cuerpo);
  writeFileSync(rutas.meta, JSON.stringify(meta, null, 2) + '\n');
  return { ...meta, repetida: true };
}

async function main() {
  const argumentos = process.argv.slice(2);
  const repetir = argumentos.includes('--repetir');
  const i = argumentos.indexOf('--nombre');
  const nombreDado = i >= 0 ? argumentos[i + 1] : null;
  const libres = argumentos.filter((a, n) => !a.startsWith('--') && (i < 0 || n !== i + 1));
  if (libres.length !== 2) {
    console.error('Uso: overpass.mjs consulta.overpassql carpeta_salida [--nombre NOMBRE] [--repetir]');
    process.exit(2);
  }
  const [ficheroConsulta, carpeta] = libres;
  const nombre = nombreDado ?? path.basename(ficheroConsulta).replace(/\.[^.]+$/, '');
  const m = await consultar(readFileSync(ficheroConsulta, 'utf8'), carpeta, { nombre, repetir });
  console.log(`${path.join(carpeta, `${nombre}.json`)}  ${m.elementos} elementos (${Object.entries(m.porTipo).map(([k, v]) => `${v} ${k}`).join(', ') || 'ninguno'}) · datos de OSM del ${m.datosOsmDe ?? '?'}`);
}

if (esComando(import.meta.url)) {
  main().catch((e) => { console.error(e.message); process.exit(1); });
}
