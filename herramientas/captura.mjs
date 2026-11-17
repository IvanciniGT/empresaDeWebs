#!/usr/bin/env node
/**
 * Captura una web con Chrome sin ventana: página completa y sin avisos de cookies.
 *
 * Uso:
 *   node herramientas/captura.mjs URL salida.png [opciones]
 *
 * Opciones:
 *   --movil            como un móvil (390×844, pantalla de doble densidad)
 *   --ancho N          ancho de la ventana en px (por defecto 1366; 390 en móvil)
 *   --alto N           alto de la ventana en px (por defecto 900; 844 en móvil)
 *   --solo-pantalla    solo lo que se ve al abrir, sin bajar
 *   --con-avisos       deja los avisos de cookies (para enseñar cómo son)
 *   --escala N         densidad de píxeles (1 en ordenador, 2 en móvil)
 *   --json             imprime el resultado en JSON
 *
 * Los avisos de cookies se OCULTAN, no se aceptan: no damos consentimiento en
 * nombre de nadie. Lo que se ha ocultado se dice en la salida, porque que una
 * web tenga o no aviso también es un dato.
 */
import { abrirChrome, esComando, RASTREADORES } from './chrome.mjs';

export function leerOpciones(argv) {
  const libres = [];
  const o = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--movil') o.movil = true;
    else if (a === '--solo-pantalla') o.soloPantalla = true;
    else if (a === '--con-avisos') o.conAvisos = true;
    else if (a === '--json') o.json = true;
    else if (['--ancho', '--alto', '--escala'].includes(a)) o[a.slice(2)] = Number(argv[++i]);
    else if (a.startsWith('--')) throw new Error(`Opción desconocida: ${a}`);
    else libres.push(a);
  }
  if (libres.length !== 2) throw new Error('Uso: captura.mjs URL salida.png [--movil] [--ancho N] [--alto N] [--solo-pantalla] [--con-avisos]');
  [o.url, o.salida] = libres;
  if (!/^(https?|file):/.test(o.url)) o.url = `https://${o.url}`;
  return o;
}

async function main() {
  let o;
  try { o = leerOpciones(process.argv.slice(2)); } catch (e) { console.error(e.message); process.exit(2); }
  const chrome = await abrirChrome();
  try {
    const pestana = await chrome.nuevaPestana({
      movil: o.movil, ancho: o.ancho, alto: o.alto, escala: o.escala, bloquear: RASTREADORES,
    });
    const pagina = await pestana.ir(o.url);
    let ocultos = [];
    if (!o.conAvisos) ocultos = await pestana.ocultarAvisosCookies();
    if (!o.soloPantalla) await pestana.recorrerHastaElFinal();
    // Algunos avisos aparecen con retraso: segunda pasada justo antes de capturar.
    if (!o.conAvisos) ocultos.push(...await pestana.ocultarAvisosCookies());
    const captura = await pestana.capturar(o.salida, { completa: !o.soloPantalla });
    const resultado = { url: o.url, urlFinal: pagina.urlFinal, estado: pagina.estado, salida: o.salida, ...captura, avisosOcultados: ocultos };
    if (o.json) console.log(JSON.stringify(resultado, null, 2));
    else {
      console.log(`${o.salida}  ${captura.ancho}×${captura.alto} px  (HTTP ${pagina.estado ?? '?'})`);
      if (pagina.urlFinal !== o.url) console.log(`  redirige a: ${pagina.urlFinal}`);
      if (ocultos.length) console.log(`  avisos de cookies ocultados: ${ocultos.join(', ')}`);
      if (captura.recortada) console.log('  ⚠️ página muy larga: la captura está cortada por abajo');
      if (captura.adaptadaMovil === false) console.log(`  ⚠️ la web NO está adaptada al móvil: ${captura.motivo}`);
    }
    if (pagina.estado && pagina.estado >= 400) process.exitCode = 1;
  } finally {
    await chrome.cerrar();
  }
}

if (esComando(import.meta.url)) {
  main().catch((e) => { console.error(e.message); process.exit(1); });
}
