#!/usr/bin/env node
/**
 * Mide una web con Lighthouse 13.6.0 (A-008), en local y sin ventana: rendimiento,
 * accesibilidad, buenas prácticas y SEO, en móvil y en ordenador.
 *
 * Uso:
 *   node herramientas/medir_web.mjs URL CARPETA_SALIDA [--solo-movil] [--con-medidores] [--nombre NOMBRE]
 *
 * Deja en CARPETA_SALIDA, por cada dispositivo:
 *   NOMBRE-movil.html / NOMBRE-ordenador.html   informe de Lighthouse (se abre en el navegador)
 *   NOMBRE-movil.json / NOMBRE-ordenador.json   datos completos
 *   NOMBRE-resumen.json                          las cuatro notas, la fecha y cómo se ha medido
 * y escribe las notas en pantalla, marcando si llegan al 90 que exige §11.
 *
 * Por defecto bloquea los medidores de visitas (Analytics, píxel de Facebook…),
 * como el resto de herramientas: no contamos como visita en las estadísticas de
 * nadie. Eso hace que la nota de rendimiento salga algo MEJOR de lo que ve un
 * visitante (sin medidores la web pesa menos). Para nuestras webs, que es donde
 * la cifra decide si se publica (§11), usar --con-medidores.
 *
 * Una medición son una o dos visitas a una página, como una captura: no recorre
 * la web. Para la web de un competidor, solo su página de inicio.
 */
import { mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import * as chromeLauncher from 'chrome-launcher';
import lighthouse, { desktopConfig } from 'lighthouse';
import { userAgents } from 'lighthouse/core/config/constants.js';
import { esComando, FIRMA, RASTREADORES, RUTA_CHROME } from './chrome.mjs';

const CATEGORIAS = { performance: 'Rendimiento', accessibility: 'Accesibilidad', 'best-practices': 'Buenas prácticas', seo: 'SEO' };
export const MINIMO = 90; // AGENTS.md §11

export async function medir(url, carpeta, { nombre = 'medicion', soloMovil = false, conMedidores = false } = {}) {
  mkdirSync(carpeta, { recursive: true });
  const chrome = await chromeLauncher.launch({
    chromePath: RUTA_CHROME,
    // Sin ventana, perfil temporal y sin pedir el llavero de macOS.
    chromeFlags: ['--headless=new', '--no-first-run', '--no-default-browser-check', '--disable-extensions',
      '--use-mock-keychain', '--password-store=basic', '--mute-audio', '--lang=es-ES'],
    logLevel: 'silent',
  });
  const resumen = { url, medida: new Date().toISOString(), herramienta: 'Lighthouse 13.6.0', medidoresBloqueados: !conMedidores, dispositivos: {} };
  try {
    for (const dispositivo of soloMovil ? ['movil'] : ['movil', 'ordenador']) {
      const ordenador = dispositivo === 'ordenador';
      const ajustes = {
        logLevel: 'error', output: ['html', 'json'], locale: 'es',
        onlyCategories: Object.keys(CATEGORIAS),
        emulatedUserAgent: `${ordenador ? userAgents.desktop : userAgents.mobile} ${FIRMA}`,
        blockedUrlPatterns: conMedidores ? [] : RASTREADORES,
      };
      const r = await lighthouse(url, { port: chrome.port, ...ajustes }, ordenador ? desktopConfig : undefined);
      if (!r?.lhr) throw new Error(`Lighthouse no ha devuelto resultado para ${url}`);
      if (r.lhr.runtimeError) throw new Error(`Lighthouse no ha podido medir ${url}: ${r.lhr.runtimeError.message}`);
      const [informe, datos] = r.report;
      writeFileSync(path.join(carpeta, `${nombre}-${dispositivo}.html`), informe);
      writeFileSync(path.join(carpeta, `${nombre}-${dispositivo}.json`), datos);
      resumen.dispositivos[dispositivo] = {
        notas: Object.fromEntries(Object.keys(CATEGORIAS).map((c) => [c, Math.round((r.lhr.categories[c]?.score ?? 0) * 100)])),
        urlFinal: r.lhr.finalDisplayedUrl,
        avisos: r.lhr.runWarnings,
      };
    }
  } finally {
    await chrome.kill();
  }
  writeFileSync(path.join(carpeta, `${nombre}-resumen.json`), JSON.stringify(resumen, null, 2) + '\n');
  return resumen;
}

async function main() {
  const a = process.argv.slice(2);
  const i = a.indexOf('--nombre');
  const nombre = i >= 0 ? a[i + 1] : 'medicion';
  const libres = a.filter((x, n) => !x.startsWith('--') && (i < 0 || n !== i + 1));
  if (libres.length !== 2) { console.error('Uso: medir_web.mjs URL CARPETA_SALIDA [--solo-movil] [--con-medidores] [--nombre NOMBRE]'); process.exit(2); }
  const [url, carpeta] = libres;
  const r = await medir(/^(https?|file):/.test(url) ? url : `https://${url}`, carpeta, { nombre, soloMovil: a.includes('--solo-movil'), conMedidores: a.includes('--con-medidores') });
  let todoBien = true;
  for (const [dispositivo, d] of Object.entries(r.dispositivos)) {
    console.log(`${dispositivo === 'movil' ? 'Móvil    ' : 'Ordenador'}  ${Object.entries(d.notas).map(([c, n]) => { if (n < MINIMO) todoBien = false; return `${CATEGORIAS[c]} ${n}${n >= MINIMO ? ' ✓' : ' ✗'}`; }).join(' · ')}`);
    for (const aviso of d.avisos) console.log(`  ⚠️ ${aviso}`);
  }
  if (r.medidoresBloqueados) console.log('(medida sin medidores de visitas: el rendimiento real puede ser algo peor)');
  console.log(`Informes en ${carpeta}`);
  process.exitCode = todoBien ? 0 : 1;
}

if (esComando(import.meta.url)) {
  main().catch((e) => { console.error(e.message); process.exit(2); });
}
