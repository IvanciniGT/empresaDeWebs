#!/usr/bin/env node
/**
 * Extrae la web actual de un cliente para reaprovecharla en la web nueva.
 *
 * Uso:
 *   node herramientas/extraer_web.mjs URL CARPETA_SALIDA [opciones]
 *
 *   CARPETA_SALIDA suele ser clientes/<negocio>/recopilado/web-actual
 *
 * Opciones:
 *   --max-paginas N     tope de páginas (por defecto 30; máximo 200)
 *   --espera S          segundos entre páginas (por defecto 1,5; o el Crawl-delay del sitio si es mayor)
 *   --sin-capturas      no hace capturas (más rápido)
 *   --sin-movil         solo capturas de ordenador
 *   --sin-dominio       no consulta DNS, whois ni certificado
 *   --prefijo /ruta     solo páginas bajo esa ruta (se pone solo en wixsite.com y similares)
 *   --ignorar-robots "MOTIVO"
 *                       no respeta robots.txt. SOLO con autorización escrita del
 *                       cliente; el motivo (p. ej. «correo de Ana, 12/03») queda
 *                       escrito en el resumen.
 *
 * Qué hace, y qué NO hace:
 *   - Solo visita páginas del dominio del cliente, con pausas y con un tope.
 *   - Respeta robots.txt (si el servidor no lo sirve por un error suyo, no visita nada).
 *   - Se identifica: añade «empresaDeWebs/…» al User-Agent de Chrome.
 *   - Bloquea los medidores de visitas (Analytics, píxel de Facebook…) para no
 *     inflar las estadísticas del cliente.
 *   - Oculta los avisos de cookies sin aceptarlos.
 *   - No inicia sesión, no envía formularios, no entra en carrito, login ni admin.
 *   - Las imágenes sí las descarga aunque estén en otro servidor (Wix, Squarespace
 *     y otros las sirven desde el suyo): son las de las páginas del cliente.
 *
 * Todo lo que detecta (teléfonos, horarios, precios…) es un CANDIDATO: la web del
 * cliente es fuente primaria, pero la detección automática se equivoca. Revisar.
 */
import { execFile } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import tls from 'node:tls';
import { promisify } from 'node:util';
import { abrirChrome, esComando, FIRMA, RASTREADORES } from './chrome.mjs';
import { interpretarRobots, NADA_PERMITIDO, TODO_PERMITIDO } from './robots.mjs';

const ejecutar = promisify(execFile);
const esperar = (ms) => new Promise((r) => setTimeout(r, ms));
const VERSION = '0.2';

// ───────────────────────────── opciones

export function leerOpciones(argv) {
  const o = { maxPaginas: 30, espera: 1.5, capturas: true, movil: true, dominio: true, prefijo: null, ignorarRobots: null };
  const libres = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--max-paginas') o.maxPaginas = Math.min(200, Math.max(1, parseInt(argv[++i], 10)));
    else if (a === '--espera') o.espera = Math.max(0, parseFloat(String(argv[++i]).replace(',', '.')));
    else if (a === '--sin-capturas') o.capturas = false;
    else if (a === '--sin-movil') o.movil = false;
    else if (a === '--sin-dominio') o.dominio = false;
    else if (a === '--prefijo') o.prefijo = argv[++i];
    else if (a === '--ignorar-robots') {
      o.ignorarRobots = argv[++i];
      if (!o.ignorarRobots || o.ignorarRobots.startsWith('--')) throw new Error('--ignorar-robots necesita el motivo: qué autorización escrita lo permite.');
    } else if (a.startsWith('--')) throw new Error(`Opción desconocida: ${a}`);
    else libres.push(a);
  }
  if (libres.length !== 2) throw new Error('Uso: extraer_web.mjs URL CARPETA_SALIDA [--max-paginas N] [--espera S] [--sin-capturas] [--sin-movil] [--sin-dominio] [--prefijo /ruta] [--ignorar-robots "MOTIVO"]');
  [o.url, o.salida] = libres;
  if (!/^https?:\/\//.test(o.url)) o.url = `https://${o.url}`;
  return o;
}

// ───────────────────────────── direcciones

const sinWww = (host) => host.replace(/^www\./, '');
const EXT_DOCUMENTO = /\.(pdf|docx?|xlsx?|odt|ods|pptx?)$/i;
const EXT_NO_PAGINA = /\.(jpe?g|png|gif|webp|avif|svg|ico|bmp|tiff?|mp4|webm|mov|mp3|wav|ogg|zip|rar|7z|gz|exe|dmg|css|js|json|xml|txt|rss|atom)$/i;
// Páginas que cambian cosas o no son contenido: ni se visitan.
const RUTA_EVITADA = /(wp-admin|wp-login|xmlrpc|\/login|\/logout|\/salir|\/acceder|\/cart|\/carrito|\/checkout|\/finalizar-compra|add-to-cart|\/my-account|\/mi-cuenta|replytocom|\/feed\/?$|[?&]s=|\/search|\/buscar|\/wp-json)/i;
// Plataformas que alojan muchas webs en el mismo dominio, cada una bajo su ruta.
const DOMINIOS_COMPARTIDOS = /(^|\.)(wixsite\.com|sites\.google\.com|weebly\.com|jimdofree\.com|webnode\.es|site123\.me)$/;
const ALOJAMIENTO_DE_FICHEROS = /(^|\.)(filesusr\.com|wixstatic\.com|squarespace-cdn\.com|squarespace\.com|shopify\.com|wp\.com|jimcdn\.com|webnode\.(es|com)|site123\.me)$/;

export function normalizar(href, base) {
  try {
    const u = new URL(href, base);
    if (!/^https?:$/.test(u.protocol)) return null;
    u.hash = '';
    for (const k of [...u.searchParams.keys()]) if (/^(utm_|fbclid|gclid|mc_|_ga)/i.test(k)) u.searchParams.delete(k);
    return u.href;
  } catch { return null; }
}

function slug(url, n) {
  const u = new URL(url);
  const partes = (u.pathname + (u.search ? '-' + u.search : '')).split(/[/?&=]+/).filter(Boolean)
    .map((p) => p.replace(/\.(html?|php|aspx?)$/i, ''));
  const base = (partes.join('-') || 'inicio').normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'pagina';
  return `${String(n).padStart(2, '0')}-${base}`;
}

// ───────────────────────────── red (para robots, sitemaps, imágenes y documentos)

async function pedir(url, { maxBytes = 5e6, tiempo = 20000 } = {}) {
  const r = await fetch(url, { headers: { 'user-agent': FIRMA, 'accept-language': 'es-ES,es' }, redirect: 'follow', signal: AbortSignal.timeout(tiempo) });
  const trozos = [];
  let total = 0;
  for await (const t of r.body ?? []) {
    total += t.length;
    if (total > maxBytes) throw new Error(`más de ${Math.round(maxBytes / 1e6)} MB`);
    trozos.push(t);
  }
  return { estado: r.status, tipo: r.headers.get('content-type') ?? '', cuerpo: Buffer.concat(trozos), urlFinal: r.url };
}

async function leerRobots(origen) {
  try {
    const r = await pedir(new URL('/robots.txt', origen).href, { maxBytes: 5e5 });
    if (r.estado >= 200 && r.estado < 300) return { robots: interpretarRobots(r.cuerpo.toString('utf8'), 'empresaDeWebs'), estado: `encontrado (HTTP ${r.estado})` };
    if (r.estado >= 400 && r.estado < 500) return { robots: TODO_PERMITIDO, estado: `no tiene (HTTP ${r.estado}): se puede visitar todo` };
    return { robots: NADA_PERMITIDO, estado: `el servidor falla (HTTP ${r.estado}): no se visita nada` };
  } catch (e) {
    return { robots: NADA_PERMITIDO, estado: `no se ha podido leer (${e.message}): no se visita nada` };
  }
}

async function leerSitemaps(origen, declarados, esDelSitio) {
  const pendientes = [...new Set([...declarados, ...['/sitemap.xml', '/sitemap_index.xml', '/wp-sitemap.xml'].map((p) => new URL(p, origen).href)])];
  const vistos = new Set();
  const paginas = new Set();
  while (pendientes.length && vistos.size < 12) {
    const url = pendientes.shift();
    if (vistos.has(url)) continue;
    vistos.add(url);
    try {
      const r = await pedir(url, { maxBytes: 1e7 });
      if (r.estado !== 200) continue;
      const xml = r.cuerpo.toString('utf8');
      const locs = [...xml.matchAll(/<loc>\s*(?:<!\[CDATA\[)?\s*([^<\]]+?)\s*(?:\]\]>)?\s*<\/loc>/gi)].map((m) => m[1].replace(/&amp;/g, '&'));
      if (/<sitemapindex/i.test(xml)) pendientes.push(...locs.filter((l) => !vistos.has(l)));
      else for (const l of locs) { const n = normalizar(l); if (n && esDelSitio(n)) paginas.add(n); }
    } catch { /* un sitemap que falla no para la extracción */ }
    await esperar(300);
  }
  return [...paginas].slice(0, 500);
}

// ───────────────────────────── lo que se lee DENTRO de cada página

function leerPagina() {
  const visible = (el) => { const e = getComputedStyle(el); return e.display !== 'none' && e.visibility !== 'hidden'; };
  const texto = (el) => (el?.innerText ?? '').replace(/\s+/g, ' ').trim();
  // Conserva los saltos de línea: en el pie, cada línea suele ser un dato distinto.
  const textoEnLineas = (el) => (el?.innerText ?? '').split('\n').map((l) => l.replace(/\s+/g, ' ').trim()).filter(Boolean).join('\n');
  const meta = (sel) => document.querySelector(sel)?.getAttribute('content')?.trim() ?? null;

  // Texto en Markdown sencillo. Se salta menú y pie (van aparte) y lo oculto.
  const SALTAR = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'SVG', 'TEMPLATE', 'IFRAME', 'NAV', 'FOOTER', 'BUTTON', 'SELECT', 'OPTION', 'TEXTAREA', 'INPUT', 'CANVAS', 'VIDEO', 'AUDIO']);
  const lineas = [];
  let linea = '';
  const cortar = () => { const l = linea.replace(/\s+/g, ' ').trim(); if (l && l !== '-') lineas.push(l); linea = ''; };
  const visitar = (n) => {
    if (n.nodeType === Node.TEXT_NODE) { linea += n.textContent; return; }
    if (n.nodeType !== Node.ELEMENT_NODE || SALTAR.has(n.tagName)) return;
    if (n.getAttribute('role') === 'navigation' || n.getAttribute('aria-hidden') === 'true' || !visible(n)) return;
    const t = n.tagName;
    if (t === 'BR') { cortar(); return; }
    if (t === 'IMG') { const alt = n.getAttribute('alt')?.trim(); if (alt) linea += ` [imagen: ${alt}] `; return; }
    if (/^H[1-6]$/.test(t)) { cortar(); lineas.push(''); linea = '#'.repeat(Number(t[1])) + ' '; n.childNodes.forEach(visitar); cortar(); lineas.push(''); return; }
    if (t === 'LI') { cortar(); linea = '- '; n.childNodes.forEach(visitar); cortar(); return; }
    if (t === 'TR') { cortar(); lineas.push('| ' + [...n.cells].map((c) => texto(c)).join(' | ') + ' |'); return; }
    const pantalla = getComputedStyle(n).display;
    const bloque = !pantalla.startsWith('inline') && pantalla !== 'contents';
    if (bloque) cortar();
    n.childNodes.forEach(visitar);
    if (n.shadowRoot) n.shadowRoot.childNodes.forEach(visitar);
    if (bloque) { cortar(); if (['P', 'SECTION', 'ARTICLE', 'TABLE', 'UL', 'OL', 'BLOCKQUOTE'].includes(t)) lineas.push(''); }
  };
  visitar(document.body);
  const markdown = lineas.join('\n').replace(/\n{3,}/g, '\n\n').trim();

  const enlaces = [...document.querySelectorAll('a[href]')].map((a) => ({ texto: texto(a) || a.getAttribute('aria-label') || a.getAttribute('title') || '', url: a.href }));
  const nav = document.querySelector('header nav, nav, [role=navigation]');
  const menu = nav ? [...nav.querySelectorAll('a[href]')].map((a) => ({ texto: texto(a), url: a.href })).filter((m) => m.texto) : [];

  const imagenes = [];
  for (const i of document.images) {
    const url = i.currentSrc || i.src;
    if (!url || url.startsWith('data:')) continue;
    imagenes.push({ url, srcset: i.srcset || i.closest('picture')?.querySelector('source[srcset]')?.srcset || '', alt: i.getAttribute('alt'), natural: [i.naturalWidth, i.naturalHeight], mostrada: [i.clientWidth, i.clientHeight], tipo: 'img' });
  }
  for (const el of document.querySelectorAll('body *')) {
    const fondo = getComputedStyle(el).backgroundImage;
    if (!fondo || !fondo.includes('url(')) continue;
    const caja = el.getBoundingClientRect();
    if (caja.width < 150 || caja.height < 100) continue;
    for (const m of fondo.matchAll(/url\(["']?([^"')]+)["']?\)/g)) {
      if (!m[1].startsWith('data:')) imagenes.push({ url: new URL(m[1], location.href).href, srcset: '', alt: el.getAttribute('aria-label') ?? '', natural: [0, 0], mostrada: [Math.round(caja.width), Math.round(caja.height)], tipo: 'fondo' });
    }
  }
  const og = meta('meta[property="og:image"]');
  if (og) imagenes.push({ url: new URL(og, location.href).href, srcset: '', alt: 'og:image (la que sale al compartir)', natural: [0, 0], mostrada: [0, 0], tipo: 'og' });

  const estilo = (sel) => { const el = document.querySelector(sel); if (!el) return null; const e = getComputedStyle(el); return { fuente: e.fontFamily, color: e.color, fondo: e.backgroundColor, tamano: e.fontSize }; };

  return {
    titulo: document.title.trim(),
    descripcion: meta('meta[name="description"]'),
    canonica: document.querySelector('link[rel="canonical"]')?.href ?? null,
    robotsMeta: meta('meta[name="robots"]'),
    idioma: document.documentElement.lang || null,
    viewport: meta('meta[name="viewport"]'),
    generador: [...document.querySelectorAll('meta[name="generator"]')].map((m) => m.content),
    og: { titulo: meta('meta[property="og:title"]'), descripcion: meta('meta[property="og:description"]'), imagen: og },
    encabezados: [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(visible).map((h) => ({ nivel: Number(h.tagName[1]), texto: texto(h) })).filter((h) => h.texto),
    jsonld: [...document.querySelectorAll('script[type="application/ld+json"]')].map((s) => s.textContent),
    markdown,
    pie: textoEnLineas(document.querySelector('footer, [role=contentinfo]')),
    cabecera: textoEnLineas(document.querySelector('header')),
    menu,
    enlaces,
    imagenes,
    iframes: [...document.querySelectorAll('iframe[src]')].map((f) => f.src),
    formularios: [...document.forms].map((f) => ({ accion: f.getAttribute('action'), metodo: (f.method || 'get').toLowerCase(), campos: [...f.elements].filter((e) => e.name && e.type !== 'hidden').map((e) => `${e.name}:${e.type}`) })),
    recursos: [...document.querySelectorAll('script[src], link[href]')].map((e) => e.src || e.href),
    estilo: {
      fuentesCargadas: [...new Set([...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family.replace(/["']/g, '')))],
      cuerpo: estilo('body'), h1: estilo('h1'), enlace: estilo('main a, a'), boton: estilo('button, .btn, .button, a[class*="button"], a[class*="boton"]'),
    },
  };
}

// ───────────────────────────── detectores (sobre el texto ya extraído)

const REDES = [
  ['Instagram', /(^|\.)instagram\.com$/], ['Facebook', /(^|\.)(facebook\.com|fb\.me|fb\.com)$/], ['TikTok', /(^|\.)tiktok\.com$/],
  ['YouTube', /(^|\.)(youtube\.com|youtu\.be)$/], ['X / Twitter', /(^|\.)(twitter\.com|x\.com)$/], ['LinkedIn', /(^|\.)linkedin\.com$/],
  ['Pinterest', /(^|\.)pinterest\.[a-z.]+$/], ['WhatsApp', /(^|\.)(wa\.me|whatsapp\.com)$/], ['Telegram', /(^|\.)t\.me$/],
  ['Google Maps', /(^|\.)(maps\.google\.[a-z.]+|maps\.app\.goo\.gl|goo\.gl)$|google\.[a-z.]+\/maps/],
  ['TripAdvisor', /(^|\.)tripadvisor\.[a-z.]+$/],
];
const RESERVAS = [
  ['Treatwell', /treatwell\./], ['Booksy', /booksy\.com/], ['Fresha', /fresha\.com/], ['TheFork / ElTenedor', /(thefork|eltenedor)\./],
  ['Bookitit', /bookitit\./], ['Reservio', /reservio\./], ['Calendly', /calendly\.com/], ['SimplyBook', /simplybook\./],
  ['CoverManager', /covermanager\./], ['Timify', /timify\./], ['Doctoralia', /doctoralia\./], ['Glovo', /glovoapp\./],
  ['Just Eat', /just-eat\.|justeat\./], ['Uber Eats', /ubereats\./], ['Wix Bookings', /bookings|book-online/],
];
const TECNOLOGIAS = [
  ['WordPress', /wp-content|wp-includes|wp-json|wordpress/i], ['Wix', /wixstatic\.com|parastorage\.com|\bwix\.com|x-wix-/i],
  ['Squarespace', /squarespace/i], ['Shopify', /cdn\.shopify\.com|myshopify\.com|shopify/i], ['Jimdo', /jimdo|jimstatic/i],
  ['Webnode', /webnode/i], ['GoDaddy (constructor)', /img1\.wsimg\.com|godaddysites/i], ['Joomla', /joomla|\/media\/jui\/|com_content/i],
  ['Drupal', /drupal|\/sites\/default\/files/i], ['PrestaShop', /prestashop/i], ['Weebly', /weebly|editmysite/i], ['Site123', /site123/i],
  ['Hostinger (constructor)', /zyrosite|zyro\.com/i], ['Webflow', /webflow|website-files\.com/i], ['Blogger', /blogger\.com|blogspot\./i],
  ['Google Sites', /sites\.google\.com/i], ['Strikingly', /strikingly/i], ['Duda', /multiscreensite|dudaone|dudamobile/i],
  ['IONOS (constructor)', /mywebsite-editor|ionos/i], ['Elementor', /elementor/i], ['Divi', /et_pb_|\/divi\//i],
  ['WooCommerce', /woocommerce/i], ['Yoast SEO', /yoast/i], ['Rank Math', /rank-math|rankmath/i], ['Cloudflare', /cloudflare/i],
];

const DIAS = /\b(lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bados?|domingos?|festivos?|lun|mar|mi[eé]|jue|vie|s[aá]b|dom|l\s?-\s?v|l\s?a\s?v)\b/i;
const HORA = /\b([01]?\d|2[0-3])([:.h]\s?[0-5]\d|\s?h\b)/i;
const VIA = /\b(c\/|calle|avda\.?|avenida|av\.|plaza|pza\.?|paseo|p[ºo]\.?|ctra\.?|carretera|camino|ronda|traves[ií]a|pol[ií]gono|urbanizaci[oó]n|glorieta|pasaje)\s/i;
const PRECIO = /(\d{1,4}(?:[.,]\d{1,2})?)\s?(?:€|eur\b|euros\b)|€\s?(\d{1,4}(?:[.,]\d{1,2})?)/i;
const TELEFONO = /(?<![\d])(?:\+34|0034)?[\s.-]?([6789](?:[\s.-]?\d){8})(?![\d])/g;
const CORREO = /[\w.+-]+@[\w-]+(?:\.[\w-]+)+/g;

const recortar = (s, n = 180) => (s.length > n ? s.slice(0, n - 1) + '…' : s);
const lineasDe = (texto) => texto.split('\n').map((l) => l.replace(/^[#\-|\s]+/, '').trim()).filter(Boolean);

export function detectar(pagina, url) {
  const texto = [pagina.cabecera, pagina.markdown, pagina.pie].filter(Boolean).join('\n');
  const d = { telefonos: [], correos: [], whatsapp: [], horarios: [], direcciones: [], precios: [], redes: [], reservas: [], mapas: [] };
  const anotar = (lista, valor, fuente) => { if (!lista.some((x) => x.valor === valor)) lista.push({ valor, fuente, pagina: url }); };

  for (const e of pagina.enlaces) {
    if (e.url.startsWith('tel:')) anotar(d.telefonos, normalizarTelefono(decodeURIComponent(e.url.slice(4))), 'enlace tel:');
    else if (e.url.startsWith('mailto:')) anotar(d.correos, decodeURIComponent(e.url.slice(7).split('?')[0]).toLowerCase(), 'enlace mailto:');
    let u;
    try { u = new URL(e.url); } catch { continue; }
    const host = u.hostname.toLowerCase();
    if (/(^|\.)(wa\.me|whatsapp\.com)$/.test(host)) {
      const numero = u.pathname.replace(/\D/g, '') || u.searchParams.get('phone')?.replace(/\D/g, '');
      if (numero) anotar(d.whatsapp, normalizarTelefono(numero), 'enlace de WhatsApp');
    }
    for (const [red, re] of REDES) if (re.test(host) || re.test(host + u.pathname)) anotar(d.redes, `${red}: ${u.href}`, 'enlace');
    for (const [plataforma, re] of RESERVAS) if (re.test(host + u.pathname) && (plataforma !== 'Wix Bookings' || /wix/.test(host))) anotar(d.reservas, `${plataforma}: ${u.href}`, 'enlace');
  }
  for (const f of pagina.iframes) {
    if (/google\.[a-z.]+\/maps|maps\.google/.test(f)) anotar(d.mapas, f, 'mapa incrustado');
    for (const [plataforma, re] of RESERVAS) if (plataforma !== 'Wix Bookings' && re.test(f)) anotar(d.reservas, `${plataforma}: ${f}`, 'widget incrustado');
  }
  for (const m of texto.matchAll(TELEFONO)) anotar(d.telefonos, normalizarTelefono(m[1]), 'texto');
  for (const m of texto.matchAll(CORREO)) anotar(d.correos, m[0].toLowerCase(), 'texto');
  for (const l of lineasDe(texto)) {
    if (l.length > 300) continue;
    if (DIAS.test(l) && HORA.test(l)) anotar(d.horarios, recortar(l), 'texto');
    if (VIA.test(l) || /\b\d{5}\b.*\b[A-ZÁÉÍÓÚ][a-záéíóúñ]+/.test(l) && /\b(0[1-9]|[1-4]\d|5[0-2])\d{3}\b/.test(l)) anotar(d.direcciones, recortar(l), 'texto');
    if (PRECIO.test(l)) anotar(d.precios, recortar(l), 'texto');
  }
  return d;
}

function normalizarTelefono(t) {
  let n = t.replace(/[^\d+]/g, '').replace(/^00/, '+');
  if (/^\+?34\d{9}$/.test(n)) n = n.replace(/^\+?34/, '');
  return /^\d{9}$/.test(n) ? `${n.slice(0, 3)} ${n.slice(3, 6)} ${n.slice(6)}` : n;
}

/** Lo útil de los datos estructurados (schema.org) de negocio local. */
export function leerJsonLd(bloques) {
  const objetos = [];
  const errores = [];
  const recorrer = (x) => {
    if (Array.isArray(x)) return x.forEach(recorrer);
    if (!x || typeof x !== 'object') return;
    if (x['@graph']) recorrer(x['@graph']);
    if (x['@type']) objetos.push(x);
  };
  for (const b of bloques) {
    try { recorrer(JSON.parse(b)); } catch (e) { errores.push(`JSON-LD mal formado: ${e.message}`); }
  }
  const tipos = [...new Set(objetos.flatMap((o) => [].concat(o['@type'])))];
  const negocio = objetos.find((o) => [].concat(o['@type']).some((t) => /LocalBusiness|Organization|Store|Salon|Shop|Restaurant|Cafe|Bar|Clinic|Dentist|Physician|Hotel|AutoRepair|Bakery|Beauty|Hair|Barber|Health|Professional|Service/i.test(t)));
  let resumen = null;
  if (negocio) {
    const dir = negocio.address && typeof negocio.address === 'object' ? negocio.address : null;
    resumen = {
      tipo: [].concat(negocio['@type']).join(', '),
      nombre: negocio.name ?? null,
      telefono: negocio.telephone ?? null,
      correo: negocio.email ?? null,
      direccion: dir ? [dir.streetAddress, dir.postalCode, dir.addressLocality, dir.addressRegion].filter(Boolean).join(', ') : (negocio.address ?? null),
      horario: negocio.openingHours ?? (negocio.openingHoursSpecification ? [].concat(negocio.openingHoursSpecification).map((h) => `${[].concat(h.dayOfWeek).map((x) => String(x).replace(/.*\//, '')).join(',')} ${h.opens}-${h.closes}`) : null),
      precios: negocio.priceRange ?? null,
      coordenadas: negocio.geo ? `${negocio.geo.latitude}, ${negocio.geo.longitude}` : null,
      redes: negocio.sameAs ?? null,
      valoracion: negocio.aggregateRating ? `${negocio.aggregateRating.ratingValue} (${negocio.aggregateRating.reviewCount ?? negocio.aggregateRating.ratingCount ?? '?'} opiniones)` : null,
    };
  }
  return { tipos, negocio: resumen, errores };
}

export function detectarTecnologia(paginas, cabeceras) {
  const pistas = [
    ...paginas.flatMap((p) => [...p.generador, ...p.recursos]),
    ...Object.entries(cabeceras).map(([k, v]) => `${k}: ${v}`),
  ].join('\n');
  const encontradas = TECNOLOGIAS.filter(([, re]) => re.test(pistas)).map(([n]) => n);
  return { encontradas, generador: [...new Set(paginas.flatMap((p) => p.generador))], servidor: cabeceras.server ?? cabeceras.Server ?? null };
}

// ───────────────────────────── imágenes

function mejorDelSrcset(srcset) {
  let mejor = null;
  for (const parte of srcset.split(/,\s+/)) {
    const [url, medida = '1x'] = parte.trim().split(/\s+/);
    const valor = parseFloat(medida) * (medida.endsWith('x') ? 1000 : 1);
    if (url && (!mejor || valor > mejor.valor)) mejor = { url, valor };
  }
  return mejor?.url ?? null;
}

/** Candidatas a la imagen a tamaño original, de más a menos grande. */
export function candidatasOriginal(imagen, base) {
  const lista = [];
  const poner = (u) => { const n = normalizar(u, base); if (n && !lista.includes(n)) lista.push(n); };
  const grande = imagen.srcset ? mejorDelSrcset(imagen.srcset) : null;
  for (const u of [grande, imagen.url].filter(Boolean)) {
    const abs = new URL(u, base).href;
    // Wix: …/media/ID~mv2.jpg/v1/fill/w_300,…/nombre.jpg → …/media/ID~mv2.jpg
    if (/wixstatic\.com\/media\//.test(abs)) poner(abs.replace(/(\/media\/[^/]+)\/v1\/.*$/, '$1'));
    // WordPress: foto-300x200.jpg → foto.jpg (y quitar -scaled)
    if (/\/wp-content\/uploads\//.test(abs)) poner(abs.replace(/-\d+x\d+(\.\w+)(\?.*)?$/, '$1').replace(/-scaled(\.\w+)$/, '$1'));
    // Squarespace y Shopify: piden el tamaño en la consulta.
    if (/squarespace-cdn\.com/.test(abs)) { const x = new URL(abs); x.searchParams.set('format', 'original'); poner(x.href); }
    if (/cdn\.shopify\.com/.test(abs)) { const x = new URL(abs); x.searchParams.delete('width'); x.searchParams.delete('height'); poner(x.href.replace(/_\d+x\d*(\.\w+)/, '$1')); }
    poner(abs);
  }
  return lista;
}

/** Ancho y alto leyendo la cabecera del fichero (PNG, JPEG, GIF, WebP). */
export function medidas(b) {
  if (b.length > 24 && b.readUInt32BE(0) === 0x89504e47) return [b.readUInt32BE(16), b.readUInt32BE(20)];
  if (b.length > 10 && b.toString('ascii', 0, 3) === 'GIF') return [b.readUInt16LE(6), b.readUInt16LE(8)];
  if (b.length > 30 && b.toString('ascii', 0, 4) === 'RIFF' && b.toString('ascii', 8, 12) === 'WEBP') {
    const tipo = b.toString('ascii', 12, 16);
    if (tipo === 'VP8X') return [1 + b.readUIntLE(24, 3), 1 + b.readUIntLE(27, 3)];
    if (tipo === 'VP8 ') return [b.readUInt16LE(26) & 0x3fff, b.readUInt16LE(28) & 0x3fff];
    if (tipo === 'VP8L') { const v = b.readUInt32LE(21); return [1 + (v & 0x3fff), 1 + ((v >> 14) & 0x3fff)]; }
  }
  if (b.length > 4 && b[0] === 0xff && b[1] === 0xd8) {
    let i = 2;
    while (i + 9 < b.length) {
      if (b[i] !== 0xff) { i++; continue; }
      const marca = b[i + 1];
      if (marca >= 0xc0 && marca <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(marca)) return [b.readUInt16BE(i + 7), b.readUInt16BE(i + 5)];
      i += 2 + b.readUInt16BE(i + 2);
    }
  }
  return null;
}

// Indicio, no prueba: el nombre del banco en la URL o en los metadatos del fichero.
const BANCOS = /shutterstock|istock(photo)?|gettyimages|getty images|adobe ?stock|depositphotos|dreamstime|123rf|freepik|pexels|unsplash|pixabay|alamy|fotolia|envato|stocksy/i;

// ───────────────────────────── dominio

function dominioRegistrable(host) {
  const partes = host.split('.');
  const segundo = partes.slice(-2).join('.');
  return /^(com|org|nom|gob|edu|co|net)\.(es|uk|ar|mx|co|br|pt)$/.test(segundo) ? partes.slice(-3).join('.') : segundo;
}

async function consultarDominio(host) {
  const dom = dominioRegistrable(host);
  const dig = async (tipo, nombre = dom) => {
    try { return (await ejecutar('dig', ['+short', '+time=5', tipo, nombre])).stdout.trim().split('\n').filter(Boolean); } catch { return []; }
  };
  const ip = await dig('A', host);
  const resultado = {
    dominio: dom, ns: await dig('NS'), mx: await dig('MX'), ip,
    inversa: ip[0] && /^\d+\.\d+\.\d+\.\d+$/.test(ip[0]) ? await dig('-x', ip[0]) : [],
    whois: null, certificado: null,
  };
  if (dom.endsWith('.es')) {
    resultado.whois = { nota: 'El whois de los .es no es público: la caducidad hay que pedírsela al cliente o verla en su panel.' };
  } else {
    try {
      const { stdout } = await ejecutar('whois', [dom], { timeout: 15000 });
      const campo = (re) => stdout.match(re)?.[1]?.trim() ?? null;
      resultado.whois = {
        registrador: campo(/Registrar:\s*(.+)/i),
        alta: campo(/Creation Date:\s*(.+)/i),
        caduca: campo(/(?:Registry Expiry Date|Registrar Registration Expiration Date|Expiry Date|Expiration Date):\s*(.+)/i),
      };
    } catch (e) { resultado.whois = { nota: `whois no ha respondido (${e.message.split('\n')[0]})` }; }
  }
  resultado.certificado = await new Promise((resolver) => {
    const s = tls.connect({ host, port: 443, servername: host, timeout: 10000 }, () => {
      const c = s.getPeerCertificate();
      resolver({ emisor: c.issuer?.O ?? c.issuer?.CN ?? null, desde: c.valid_from, hasta: c.valid_to, valido: s.authorized, error: s.authorizationError ?? null });
      s.end();
    });
    s.on('error', (e) => resolver({ error: e.message }));
    s.on('timeout', () => { s.destroy(); resolver({ error: 'sin respuesta en el puerto 443' }); });
  });
  return resultado;
}

// ───────────────────────────── extracción

export async function extraer(o, avisar = console.log) {
  const carpetas = Object.fromEntries(['paginas', 'imagenes', 'documentos', 'capturas', 'html'].map((c) => [c, path.join(o.salida, c)]));
  Object.values(carpetas).forEach((c) => mkdirSync(c, { recursive: true }));
  const datos = {
    herramienta: `extraer_web.mjs ${VERSION}`, fecha: new Date().toISOString(), inicio: o.url,
    sitio: null, robots: null, paginas: [], omitidas: [], rotas: [], imagenes: [], documentos: [],
    contacto: null, jsonld: null, tecnologia: null, dominio: null, avisosCookies: [], errores: [],
  };

  const chrome = await abrirChrome();
  try {
    const ordenador = await chrome.nuevaPestana({ firma: true, bloquear: RASTREADORES });
    const movil = o.capturas && o.movil ? await chrome.nuevaPestana({ movil: true, firma: true, bloquear: RASTREADORES }) : null;

    // robots.txt ANTES de la primera visita. La URL de inicio puede redirigir
    // (http→https, sin www→con www): si cambia de origen, se lee el del nuevo.
    const rutaDe = (u) => { const x = new URL(u); return x.pathname + x.search; };
    const noPermite = (url, estado) => new Error(`robots.txt (${estado}) no permite visitar ${url}. Si el cliente lo autoriza por escrito, repetir con --ignorar-robots "quién y cuándo lo autorizó".`);
    let { robots, estado } = o.ignorarRobots ? { robots: TODO_PERMITIDO, estado: 'IGNORADO' } : await leerRobots(new URL(o.url).origin);
    if (!robots.permitido(rutaDe(o.url))) throw noPermite(o.url, estado);
    avisar(`Abriendo ${o.url}`);
    const primera = await ordenador.ir(o.url);
    const inicio = new URL(primera.urlFinal);
    if (inicio.origin !== new URL(o.url).origin && !o.ignorarRobots) {
      ({ robots, estado } = await leerRobots(inicio.origin));
      if (!robots.permitido(rutaDe(primera.urlFinal))) throw noPermite(primera.urlFinal, estado);
    }
    const host = sinWww(inicio.host);
    let prefijo = o.prefijo ?? '/';
    if (!o.prefijo && DOMINIOS_COMPARTIDOS.test(inicio.hostname)) prefijo = `/${inicio.pathname.split('/')[1] ?? ''}`;
    prefijo = prefijo.replace(/\/+$/, '') || '/';
    datos.sitio = { origen: inicio.origin, host, prefijo, redirigeA: primera.urlFinal !== o.url ? primera.urlFinal : null };
    const esDelSitio = (url) => {
      try {
        const u = new URL(url);
        return sinWww(u.host) === host && (prefijo === '/' || u.pathname === prefijo || u.pathname.startsWith(`${prefijo}/`));
      } catch { return false; }
    };

    datos.robots = { estado, reglas: robots.reglas, retardo: robots.retardo, autorizacionParaIgnorar: o.ignorarRobots };
    avisar(`robots.txt: ${estado}`);
    const pausa = Math.max(o.espera, robots.retardo ?? 0) * 1000;
    const permitido = (url) => robots.permitido(rutaDe(url));

    const cola = [{ url: normalizar(primera.urlFinal), origen: '(inicio)' }];
    const enCola = new Set([cola[0].url]);
    const encolar = (url, origen) => {
      const n = normalizar(url);
      if (!n || enCola.has(n)) return;
      enCola.add(n);
      const { hostname, pathname } = new URL(n);
      if (EXT_DOCUMENTO.test(pathname)) {
        // Las cartas y tarifas en PDF de Wix, Squarespace… viven en el servidor de la plataforma.
        if (esDelSitio(n) || ALOJAMIENTO_DE_FICHEROS.test(hostname)) datos.documentos.push({ url: n, origen });
        return;
      }
      if (!esDelSitio(n) || EXT_NO_PAGINA.test(pathname)) return;
      if (RUTA_EVITADA.test(n)) { datos.omitidas.push({ url: n, motivo: 'login, carrito, búsqueda o administración' }); return; }
      cola.push({ url: n, origen });
    };
    for (const u of await leerSitemaps(inicio.origin, robots.sitemaps, esDelSitio)) encolar(u, '(sitemap)');

    const vistasFinales = new Set();
    let n = 0;
    let cabecerasPrincipal = primera.cabeceras;
    let yaEnPagina = true;
    while (cola.length && datos.paginas.length < o.maxPaginas) {
      const { url, origen } = cola.shift();
      if (!permitido(url)) { datos.omitidas.push({ url, motivo: 'robots.txt no lo permite' }); continue; }
      let visita;
      try {
        if (yaEnPagina) { visita = primera; yaEnPagina = false; } else { await esperar(pausa); visita = await ordenador.ir(url); }
      } catch (e) { datos.errores.push(`${url}: ${e.message}`); continue; }
      const final = normalizar(visita.urlFinal);
      if (visita.estado >= 400) { datos.rotas.push({ url, estado: visita.estado, enlazadaDesde: origen }); continue; }
      if (!esDelSitio(final)) { datos.omitidas.push({ url, motivo: `redirige fuera del sitio (${final})` }); continue; }
      if (vistasFinales.has(final)) continue;
      vistasFinales.add(final);
      const tipo = ordenador.registro.respuestas.find((r) => r.tipo === 'Document')?.mime ?? '';
      if (tipo && !/html/.test(tipo)) { datos.documentos.push({ url: final, origen }); continue; }

      n += 1;
      const nombre = slug(final, n);
      avisar(`[${n}] ${final}`);
      const ocultos = await ordenador.ocultarAvisosCookies();
      await ordenador.recorrerHastaElFinal();
      ocultos.push(...await ordenador.ocultarAvisosCookies());
      if (ocultos.length) datos.avisosCookies.push({ pagina: final, ocultados: [...new Set(ocultos)] });
      const pagina = await ordenador.evaluar(leerPagina);
      writeFileSync(path.join(carpetas.html, `${nombre}.html`), await ordenador.html());
      const registro = {
        n, url: final, nombre, estado: visita.estado, enlazadaDesde: origen,
        titulo: pagina.titulo, descripcion: pagina.descripcion, canonica: pagina.canonica, robotsMeta: pagina.robotsMeta,
        idioma: pagina.idioma, viewport: pagina.viewport, og: pagina.og, encabezados: pagina.encabezados,
        palabras: pagina.markdown.split(/\s+/).filter(Boolean).length, formularios: pagina.formularios,
        capturas: {},
      };
      if (n === 1) {
        datos.menu = pagina.menu;
        datos.pie = pagina.pie;
        datos.estilo = pagina.estilo;
        cabecerasPrincipal = visita.cabeceras;
      }
      if (o.capturas) {
        const c = await ordenador.capturar(path.join(carpetas.capturas, `${nombre}-ordenador.png`));
        registro.capturas.ordenador = { fichero: `capturas/${nombre}-ordenador.png`, ...c };
      }
      writeFileSync(path.join(carpetas.paginas, `${nombre}.md`), [
        '---', `url: ${final}`, `titulo: ${JSON.stringify(pagina.titulo)}`, `descripcion: ${JSON.stringify(pagina.descripcion ?? '')}`,
        `extraida: ${datos.fecha}`, '---', '', pagina.markdown, '',
      ].join('\n'));
      if (movil) {
        try {
          await esperar(pausa);
          await movil.ir(final);
          await movil.ocultarAvisosCookies();
          await movil.recorrerHastaElFinal();
          await movil.ocultarAvisosCookies();
          const c = await movil.capturar(path.join(carpetas.capturas, `${nombre}-movil.png`));
          registro.capturas.movil = { fichero: `capturas/${nombre}-movil.png`, ...c };
        } catch (e) { datos.errores.push(`captura móvil de ${final}: ${e.message}`); }
      }
      registro._datos = pagina;
      datos.paginas.push(registro);
      for (const e of pagina.enlaces) encolar(e.url, final);
    }
    if (cola.length) datos.omitidas.push(...cola.map(({ url }) => ({ url, motivo: `tope de ${o.maxPaginas} páginas` })));

    // Lo que se saca del conjunto de páginas.
    const leidas = datos.paginas.map((p) => p._datos);
    const juntar = (clave) => datos.paginas.flatMap((p) => detectar(p._datos, p.url)[clave]);
    const unicos = (lista) => lista.filter((x, i) => lista.findIndex((y) => y.valor === x.valor) === i);
    datos.contacto = Object.fromEntries(['telefonos', 'correos', 'whatsapp', 'horarios', 'direcciones', 'precios', 'redes', 'reservas', 'mapas'].map((k) => [k, unicos(juntar(k))]));
    datos.jsonld = leerJsonLd(leidas.flatMap((p) => p.jsonld));
    datos.tecnologia = detectarTecnologia(leidas, cabecerasPrincipal);

    avisar('Descargando imágenes…');
    await descargarImagenes(datos, carpetas.imagenes);
    avisar('Descargando documentos…');
    await descargarDocumentos(datos, carpetas.documentos, permitido, esDelSitio);
    if (o.dominio && !/^(localhost|127\.|\[::1\])/.test(inicio.hostname)) {
      avisar('Consultando dominio y certificado…');
      datos.dominio = await consultarDominio(inicio.hostname);
    }
  } finally {
    await chrome.cerrar();
  }

  for (const p of datos.paginas) delete p._datos;
  writeFileSync(path.join(o.salida, 'datos.json'), JSON.stringify(datos, null, 2));
  writeFileSync(path.join(o.salida, 'resumen.md'), resumen(datos));
  return datos;
}

async function descargarImagenes(datos, carpeta) {
  const porUrl = new Map();
  for (const p of datos.paginas) {
    for (const img of p._datos.imagenes) {
      const clave = normalizar(img.url, p.url);
      if (!clave) continue;
      const previa = porUrl.get(clave);
      if (previa) { if (!previa.paginas.includes(p.url)) previa.paginas.push(p.url); continue; }
      porUrl.set(clave, { ...img, url: clave, paginas: [p.url], candidatas: candidatasOriginal(img, p.url) });
    }
  }
  const porContenido = new Map();
  let n = 0;
  for (const img of [...porUrl.values()].slice(0, 300)) {
    let descarga = null;
    for (const candidata of img.candidatas) {
      try {
        const r = await pedir(candidata, { maxBytes: 2e7 });
        if (r.estado === 200 && /^image\//.test(r.tipo)) { descarga = { ...r, url: candidata }; break; }
      } catch { /* probar la siguiente */ }
      await esperar(150);
    }
    const registro = {
      url: img.url, alt: img.alt, tipo: img.tipo, paginas: img.paginas, mostrada: img.mostrada, fichero: null,
      medidas: null, bytes: null, origen: null, posibleBanco: BANCOS.test(img.url) ? 'el nombre lo sugiere' : null,
    };
    if (!descarga) { registro.error = 'no se ha podido descargar'; datos.imagenes.push(registro); continue; }
    const huella = createHash('sha1').update(descarga.cuerpo).digest('hex');
    const repetida = porContenido.get(huella);
    if (repetida) { repetida.paginas = [...new Set([...repetida.paginas, ...img.paginas])]; repetida.otrasUrls = [...(repetida.otrasUrls ?? []), img.url]; continue; }
    n += 1;
    const extension = (descarga.tipo.match(/image\/(jpeg|png|gif|webp|avif|svg)/)?.[1] ?? 'img').replace('jpeg', 'jpg').replace('svg', 'svg');
    const base = path.basename(new URL(descarga.url).pathname).replace(/\.[a-z0-9]+$/i, '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^\w-]+/g, '-').slice(0, 50) || 'imagen';
    registro.fichero = `imagenes/${String(n).padStart(3, '0')}-${base}.${extension}`;
    writeFileSync(path.join(carpeta, path.basename(registro.fichero)), descarga.cuerpo);
    registro.urlDescargada = descarga.url;
    registro.medidas = medidas(descarga.cuerpo);
    registro.bytes = descarga.cuerpo.length;
    registro.origen = new URL(descarga.url).host;
    const metadatos = descarga.cuerpo.subarray(0, 512 * 1024).toString('latin1');
    const banco = metadatos.match(BANCOS)?.[0];
    if (banco) registro.posibleBanco = `los metadatos del fichero citan «${banco}»`;
    else if (!registro.posibleBanco && BANCOS.test(descarga.url)) registro.posibleBanco = 'el nombre lo sugiere';
    porContenido.set(huella, registro);
    datos.imagenes.push(registro);
  }
  if (porUrl.size > 300) datos.errores.push(`Hay ${porUrl.size} imágenes; solo se han descargado 300.`);
}

async function descargarDocumentos(datos, carpeta, permitido, esDelSitio) {
  let n = 0;
  for (const d of datos.documentos.slice(0, 30)) {
    if (esDelSitio(d.url) && !permitido(d.url)) { d.error = 'robots.txt no lo permite'; continue; }
    try {
      const r = await pedir(d.url, { maxBytes: 2.5e7 });
      if (r.estado !== 200) { d.error = `HTTP ${r.estado}`; continue; }
      n += 1;
      const nombre = `${String(n).padStart(2, '0')}-${path.basename(new URL(d.url).pathname).replace(/[^\w.-]+/g, '-')}`;
      writeFileSync(path.join(carpeta, nombre), r.cuerpo);
      d.fichero = `documentos/${nombre}`;
      d.bytes = r.cuerpo.length;
    } catch (e) { d.error = e.message; }
    await esperar(500);
  }
}

// ───────────────────────────── resumen para las personas (y los agentes)

function resumen(d) {
  const L = [];
  const celda = (s) => String(s ?? '—').replace(/\|/g, '\\|').replace(/\n/g, ' ');
  const lista = (titulo, elementos, formato) => {
    L.push(`### ${titulo}`, '');
    if (!elementos?.length) L.push('_No se ha detectado nada. Eso no prueba que no exista._', '');
    else { elementos.forEach((x) => L.push(`- ${formato(x)}`)); L.push(''); }
  };
  L.push(`# Web actual · ${d.sitio?.host ?? d.inicio}`, '');
  L.push(`> Extraída con ${d.herramienta} el ${d.fecha.slice(0, 10)}. **Todo lo «detectado» es candidato**: la web`,
    '> del cliente es fuente primaria, pero la lectura automática se equivoca. Comprobar antes de usarlo y',
    '> pasarlo al expediente con su origen.', '');
  L.push('## Resumen', '');
  L.push(`| | |`, `|---|---|`);
  L.push(`| Dirección | ${d.sitio?.origen ?? d.inicio}${d.sitio?.redirigeA ? ` (redirige desde ${d.inicio})` : ''} |`);
  L.push(`| Páginas leídas | ${d.paginas.length} |`);
  L.push(`| Tecnología | ${celda(d.tecnologia?.encontradas.join(', ') || 'no identificada')}${d.tecnologia?.generador.length ? ` · generador: ${celda(d.tecnologia.generador.join(', '))}` : ''} |`);
  L.push(`| robots.txt | ${celda(d.robots?.estado)}${d.robots?.autorizacionParaIgnorar ? ` · **ignorado con autorización: ${celda(d.robots.autorizacionParaIgnorar)}**` : ''} |`);
  const movilNo = d.paginas.filter((p) => p.capturas.movil?.adaptadaMovil === false);
  L.push(`| Adaptada al móvil | ${d.paginas.some((p) => p.capturas.movil) ? (movilNo.length ? `**No** en ${movilNo.length} de ${d.paginas.length} páginas: ${movilNo.map((p) => `${p.n} (${p.capturas.movil.motivo})`).join('; ')}` : 'Sí, en todas las capturadas') : 'sin comprobar'} |`);
  L.push(`| Aviso de cookies | ${d.avisosCookies.length ? `se ha visto (y ocultado) en ${d.avisosCookies.length} páginas` : 'no se ha detectado ninguno (comprobar a mano: puede ser un tipo que no conocemos)'} |`);
  L.push(`| Imágenes | ${d.imagenes.filter((i) => i.fichero).length} descargadas${d.imagenes.some((i) => i.posibleBanco) ? `, ${d.imagenes.filter((i) => i.posibleBanco).length} con indicios de banco de imágenes` : ''} |`);
  L.push(`| Documentos | ${d.documentos.filter((x) => x.fichero).length} descargados |`);
  L.push(`| Enlaces internos rotos | ${d.rotas.length} |`, '');

  L.push('## Menú', '');
  if (d.menu?.length) d.menu.forEach((m) => L.push(`- ${m.texto} → ${m.url}`)); else L.push('_No se ha encontrado un menú (`<nav>`)._');
  L.push('');

  L.push('## Páginas', '', '| # | Título | Dirección | H1 | Palabras | Capturas |', '|---|---|---|---|---|---|');
  for (const p of d.paginas) {
    const h1 = p.encabezados.filter((h) => h.nivel === 1).map((h) => h.texto);
    L.push(`| ${p.n} | ${celda(p.titulo)} | ${p.url} | ${celda(h1.join(' / ') || '(sin H1)')} | ${p.palabras} | ${[p.capturas.ordenador && `[ordenador](${p.capturas.ordenador.fichero})`, p.capturas.movil && `[móvil](${p.capturas.movil.fichero})`].filter(Boolean).join(' · ')} |`);
  }
  L.push('', `El texto de cada página está en [paginas/](paginas/) y el HTML tal como lo dibuja el navegador, en [html/](html/).`, '');

  L.push('## Datos del negocio detectados', '');
  if (d.jsonld?.negocio) {
    L.push('### En los datos estructurados (schema.org)', '');
    for (const [k, v] of Object.entries(d.jsonld.negocio)) if (v) L.push(`- **${k}:** ${celda([].concat(v).join(' · '))}`);
    L.push('');
  }
  const conFuente = (x) => `${x.valor}  _(${x.fuente}; ${x.pagina})_`;
  lista('Teléfonos', d.contacto?.telefonos, conFuente);
  lista('WhatsApp', d.contacto?.whatsapp, conFuente);
  lista('Correos', d.contacto?.correos, conFuente);
  lista('Direcciones (candidatas)', d.contacto?.direcciones, conFuente);
  lista('Horarios (líneas candidatas)', d.contacto?.horarios, conFuente);
  lista('Precios (líneas con €)', d.contacto?.precios, conFuente);
  lista('Redes sociales y mapas', [...(d.contacto?.redes ?? []), ...(d.contacto?.mapas ?? []).map((m) => ({ ...m, valor: `Mapa: ${m.valor}` }))], conFuente);
  lista('Reservas y pedidos en plataformas', d.contacto?.reservas, conFuente);

  L.push('## SEO por página', '', '| # | Título (caracteres) | Descripción | H1 | Canónica | Indexable |', '|---|---|---|---|---|---|');
  for (const p of d.paginas) {
    const h1 = p.encabezados.filter((h) => h.nivel === 1).length;
    L.push(`| ${p.n} | ${p.titulo ? p.titulo.length : '**falta**'} | ${p.descripcion ? `${p.descripcion.length} car.` : '**falta**'} | ${h1 === 1 ? '1' : `**${h1}**`} | ${p.canonica ? (normalizar(p.canonica) === p.url ? 'sí' : `otra: ${p.canonica}`) : 'no'} | ${/noindex/i.test(p.robotsMeta ?? '') ? '**no (noindex)**' : 'sí'} |`);
  }
  L.push('', `Datos estructurados: ${d.jsonld?.tipos.length ? d.jsonld.tipos.join(', ') : 'ninguno'}${d.jsonld?.errores.length ? ` · **${d.jsonld.errores.length} bloques mal formados**` : ''}.`, '');

  L.push('## Imágenes', '', 'Las fotos de la web son del cliente **salvo que no lo sean**: antes de reutilizar una, confirmarlo con él.', '');
  L.push('| Fichero | Medidas | Texto alternativo | Indicio de banco | Dónde sale |', '|---|---|---|---|---|');
  for (const i of d.imagenes) {
    const alt = i.tipo === 'fondo' ? '(imagen de fondo: no tiene)' : i.tipo === 'og' ? '(imagen para redes sociales)' : (i.alt || (i.alt === '' ? '(vacío)' : '(no tiene)'));
    L.push(`| ${i.fichero ? `[${path.basename(i.fichero)}](${i.fichero})` : `no descargada: ${i.url}`} | ${i.medidas ? i.medidas.join('×') : '?'} | ${celda(alt)} | ${celda(i.posibleBanco ?? '')} | ${i.paginas.length} pág. |`);
  }
  L.push('');

  L.push('## Estilo actual (para Lola)', '');
  if (d.estilo) {
    L.push(`- Fuentes cargadas: ${d.estilo.fuentesCargadas.join(', ') || 'ninguna web (las del sistema)'}`);
    for (const k of ['cuerpo', 'h1', 'enlace', 'boton']) if (d.estilo[k]) L.push(`- ${k}: ${d.estilo[k].fuente} · color ${d.estilo[k].color} · fondo ${d.estilo[k].fondo} · ${d.estilo[k].tamano}`);
  }
  L.push('');

  if (d.dominio) {
    const x = d.dominio;
    L.push('## Dominio y alojamiento (para Paco y Reme)', '');
    L.push(`- Dominio: ${x.dominio}`, `- Servidores DNS: ${x.ns.join(', ') || '?'}`, `- Correo (MX): ${x.mx.join(', ') || 'ninguno'}`, `- IP: ${x.ip.join(', ') || '?'}${x.inversa.length ? ` (${x.inversa.join(', ')})` : ''}`);
    if (x.whois) L.push(`- Whois: ${x.whois.nota ?? `registrador ${x.whois.registrador ?? '?'}, alta ${x.whois.alta ?? '?'}, **caduca ${x.whois.caduca ?? '?'}**`}`);
    if (x.certificado) L.push(`- Certificado: ${x.certificado.error ? `**problema: ${x.certificado.error}**` : `${x.certificado.emisor}, válido hasta ${x.certificado.hasta}`}`);
    L.push(`- Servidor web: ${d.tecnologia?.servidor ?? '?'}`, '');
  }

  if (d.documentos.length) {
    L.push('## Documentos enlazados', '');
    d.documentos.forEach((x) => L.push(`- ${x.fichero ? `[${path.basename(x.fichero)}](${x.fichero})` : `**no descargado (${x.error ?? '?'})**`} ← ${x.url}`));
    L.push('');
  }
  if (d.rotas.length || d.omitidas.length || d.errores.length) {
    L.push('## Lo que no se ha leído', '');
    d.rotas.forEach((x) => L.push(`- **Rota (HTTP ${x.estado}):** ${x.url} ← enlazada desde ${x.enlazadaDesde}`));
    d.omitidas.forEach((x) => L.push(`- Omitida: ${x.url} — ${x.motivo}`));
    d.errores.forEach((x) => L.push(`- Error: ${x}`));
    L.push('');
  }
  return L.join('\n');
}

async function main() {
  let o;
  try { o = leerOpciones(process.argv.slice(2)); } catch (e) { console.error(e.message); process.exit(2); }
  const d = await extraer(o);
  console.log(`\n${d.paginas.length} páginas, ${d.imagenes.filter((i) => i.fichero).length} imágenes, ${d.documentos.filter((x) => x.fichero).length} documentos → ${path.join(o.salida, 'resumen.md')}`);
  if (!d.paginas.length) process.exitCode = 1;
}

if (esComando(import.meta.url)) {
  main().catch((e) => { console.error(e.stack ?? e.message); process.exit(1); });
}
