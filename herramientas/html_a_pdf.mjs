#!/usr/bin/env node
/**
 * Convierte un HTML en PDF con Chrome sin ventana.
 *
 * Maquetamos en HTML+CSS porque da un control del diseño que no da ningún
 * generador de PDF de Python, y Chrome ya está instalado.
 *
 * Uso:
 *   node herramientas/html_a_pdf.mjs entrada.html salida.pdf [--estricto]
 *
 * Antes de imprimir espera a que carguen las fuentes y las imágenes, y AVISA de
 * lo que no ha cargado (una imagen con la ruta mal, una fuente web sin conexión)
 * y de las imágenes sin texto alternativo (`alt`; `alt=""` vale si es decorativa):
 * con la orden de Chrome de antes, eso salía en el PDF sin que nadie se enterase.
 * Con --estricto, cualquier aviso hace que termine con error.
 */
import { existsSync } from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { abrirChrome, esComando } from './chrome.mjs';

export async function htmlAPdf(entrada, salida) {
  const chrome = await abrirChrome();
  try {
    const pestana = await chrome.nuevaPestana();
    await pestana.ir(pathToFileURL(path.resolve(entrada)).href);
    await pestana.recorrerHastaElFinal();
    const avisos = pestana.registro.fallos.map((f) => `no ha cargado ${f.url} (${f.error})`);
    for (const r of pestana.registro.respuestas) {
      if (r.estado >= 400) avisos.push(`HTTP ${r.estado} en ${r.url}`);
    }
    const sinCargar = await pestana.evaluar(() => ({
      fuentes: [...document.fonts].filter((f) => f.status === 'error').map((f) => f.family),
      imagenes: [...document.images].filter((i) => !i.naturalWidth).map((i) => i.getAttribute('src')),
      // alt="" es válido (imagen decorativa); lo que falla es no ponerlo (AGENTS.md §11, WCAG 1.1.1).
      sinAlt: [...document.images].filter((i) => !i.hasAttribute('alt')).map((i) => i.getAttribute('src')),
    }));
    for (const f of new Set(sinCargar.fuentes)) avisos.push(`fuente sin cargar: ${f} (saldrá otra en su lugar)`);
    for (const i of sinCargar.imagenes) avisos.push(`imagen rota: ${i}`);
    for (const i of sinCargar.sinAlt) avisos.push(`imagen sin texto alternativo (alt): ${i}`);
    await pestana.pdf(salida);
    return [...new Set(avisos)];
  } finally {
    await chrome.cerrar();
  }
}

async function main() {
  const argumentos = process.argv.slice(2);
  const estricto = argumentos.includes('--estricto');
  const [entrada, salida] = argumentos.filter((a) => a !== '--estricto');
  if (!entrada || !salida) { console.error('Uso: html_a_pdf.mjs entrada.html salida.pdf [--estricto]'); process.exit(2); }
  if (!existsSync(entrada)) { console.error(`No existe ${entrada}`); process.exit(2); }
  const avisos = await htmlAPdf(entrada, salida);
  console.log(salida);
  for (const a of avisos) console.error(`⚠️  ${a}`);
  if (estricto && avisos.length) process.exit(1);
}

if (esComando(import.meta.url)) {
  main().catch((e) => { console.error(e.message); process.exit(1); });
}
