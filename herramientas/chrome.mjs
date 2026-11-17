/**
 * Chrome sin ventana, manejado por su protocolo de depuración (CDP).
 *
 * Es la base de captura.mjs, html_a_pdf.mjs y extraer_web.mjs. No necesita
 * instalar nada: Node 24 y Chrome ya están en la máquina. Hablamos con Chrome
 * por una tubería (--remote-debugging-pipe) y no por un puerto, para que ningún
 * otro programa de la máquina pueda conectarse a él mientras trabaja.
 *
 * Uso desde otro script:
 *   import { abrirChrome } from './chrome.mjs';
 *   const chrome = await abrirChrome();
 *   const pestana = await chrome.nuevaPestana({ movil: true });
 *   await pestana.ir('https://…');
 *   await pestana.capturar('salida.png');
 *   await chrome.cerrar();
 */
import { spawn } from 'node:child_process';
import { mkdtempSync, realpathSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

/** ¿Se está ejecutando este fichero como comando (y no importado)? */
export function esComando(metaUrl) {
  try { return realpathSync(fileURLToPath(metaUrl)) === realpathSync(process.argv[1]); } catch { return false; }
}

export const RUTA_CHROME = process.env.CHROME
  ?? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

// Se añade al User-Agent de Chrome para que el dueño de la web pueda saber quién
// le visita. Cuando la empresa tenga web y correo propios, cambiarlos aquí y en mapa.py.
export const FIRMA = 'empresaDeWebs/0.2 (+mailto:ivan.osuna.ayuste@gmail.com)';

// Medidores y anuncios: si los cargáramos, cada visita nuestra contaría como una
// visita real en las estadísticas del cliente o de la competencia.
export const RASTREADORES = [
  '*google-analytics.com*', '*googletagmanager.com*', '*doubleclick.net*',
  '*googleadservices.com*', '*googlesyndication.com*', '*connect.facebook.net*',
  '*facebook.com/tr*', '*hotjar.com*', '*clarity.ms*', '*matomo.cloud*',
  '*plausible.io*', '*stats.wp.com*', '*pixel.wp.com*', '*analytics.tiktok.com*',
  '*snap.licdn.com*', '*bat.bing.com*', '*frog.wix.com*', '*panorama.wixapps.net*',
];

export const MOVIL = { ancho: 390, alto: 844, escala: 2 };
export const ORDENADOR = { ancho: 1366, alto: 900, escala: 1 };

const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

class Conexion {
  constructor(entrada, salida) {
    this.entrada = entrada;
    this.siguienteId = 0;
    this.pendientes = new Map();
    this.oyentes = new Set();
    let resto = '';
    salida.setEncoding('utf8');
    salida.on('data', (trozo) => {
      resto += trozo;
      let fin;
      while ((fin = resto.indexOf('\0')) >= 0) {
        const mensaje = JSON.parse(resto.slice(0, fin));
        resto = resto.slice(fin + 1);
        this.recibir(mensaje);
      }
    });
  }

  recibir(mensaje) {
    if (mensaje.id !== undefined) {
      const p = this.pendientes.get(mensaje.id);
      if (!p) return;
      this.pendientes.delete(mensaje.id);
      if (mensaje.error) p.rechazar(new Error(`${p.metodo}: ${mensaje.error.message}`));
      else p.resolver(mensaje.result);
      return;
    }
    for (const oyente of this.oyentes) oyente(mensaje);
  }

  enviar(metodo, params = {}, sessionId) {
    const id = ++this.siguienteId;
    return new Promise((resolver, rechazar) => {
      this.pendientes.set(id, { resolver, rechazar, metodo });
      this.entrada.write(JSON.stringify({ id, method: metodo, params, sessionId }) + '\0');
    });
  }

  fallarTodo(error) {
    for (const p of this.pendientes.values()) p.rechazar(error);
    this.pendientes.clear();
  }
}

/** Arranca Chrome sin ventana con un perfil temporal y vacío. */
export async function abrirChrome({ idioma = 'es-ES' } = {}) {
  const perfil = mkdtempSync(path.join(tmpdir(), 'chrome-edw-'));
  const proceso = spawn(RUTA_CHROME, [
    '--headless', '--remote-debugging-pipe', `--user-data-dir=${perfil}`,
    '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--hide-scrollbars',
    '--mute-audio', '--disable-extensions', '--disable-sync', '--disable-default-apps',
    '--disable-background-networking', '--disable-component-update',
    // Sin esto, macOS puede pedir acceso al llavero: una ventana que interrumpe a Iván.
    '--use-mock-keychain', '--password-store=basic',
    '--force-color-profile=srgb', `--lang=${idioma}`, `--accept-lang=${idioma},es`,
    'about:blank',
  ], { stdio: ['ignore', 'ignore', 'pipe', 'pipe', 'pipe'] });

  let errores = '';
  proceso.stderr.on('data', (d) => { errores = (errores + d).slice(-4000); });
  const conexion = new Conexion(proceso.stdio[3], proceso.stdio[4]);
  let cerrado = false;
  const limpiar = () => { try { rmSync(perfil, { recursive: true, force: true }); } catch { /* ya no está */ } };
  proceso.on('exit', () => {
    cerrado = true;
    conexion.fallarTodo(new Error(`Chrome se ha cerrado.\n${errores}`));
    limpiar();
  });
  proceso.on('error', (e) => conexion.fallarTodo(new Error(`No se pudo arrancar Chrome (${RUTA_CHROME}): ${e.message}`)));

  const version = await conexion.enviar('Browser.getVersion');

  return {
    version,
    async nuevaPestana(opciones = {}) {
      const { targetId } = await conexion.enviar('Target.createTarget', { url: 'about:blank' });
      const { sessionId } = await conexion.enviar('Target.attachToTarget', { targetId, flatten: true });
      const pestana = new Pestana(conexion, sessionId, version.userAgent, opciones);
      await pestana.preparar();
      return pestana;
    },
    async cerrar() {
      if (cerrado) return;
      try { await Promise.race([conexion.enviar('Browser.close'), esperar(3000)]); } catch { /* se cierra igual */ }
      if (!cerrado) proceso.kill();
      await Promise.race([new Promise((r) => proceso.once('exit', r)), esperar(3000)]);
      limpiar();
    },
  };
}

export class Pestana {
  constructor(conexion, sessionId, agenteChrome, opciones) {
    this.conexion = conexion;
    this.sessionId = sessionId;
    this.agenteChrome = agenteChrome;
    const base = opciones.movil ? MOVIL : ORDENADOR;
    this.opciones = { ...base, firma: false, bloquear: [], ...quitarIndefinidos(opciones) };
    this.enVuelo = new Map();
    this.ultimaActividad = Date.now();
    this.registro = { fallos: [], respuestas: [] };
    conexion.oyentes.add((m) => { if (m.sessionId === sessionId) this.alEvento(m); });
    this.esperas = new Set();
  }

  enviar(metodo, params) { return this.conexion.enviar(metodo, params, this.sessionId); }

  async preparar() {
    const o = this.opciones;
    await Promise.all([this.enviar('Page.enable'), this.enviar('Network.enable'), this.enviar('Runtime.enable')]);
    await this.enviar('Emulation.setDeviceMetricsOverride', {
      width: o.ancho, height: o.alto, deviceScaleFactor: o.escala, mobile: Boolean(o.movil),
    });
    let agente = this.agenteChrome;
    if (o.movil) {
      // El mismo Chrome, pero diciendo que es un móvil, como hace el modo
      // dispositivo de las herramientas de desarrollo. Sin hacernos pasar por nadie.
      agente = agente.replace(/\([^)]*\)/, '(Linux; Android 10; K)').replace(/ Safari\//, ' Mobile Safari/');
      await this.enviar('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 5 });
    }
    if (o.firma) agente += ` ${FIRMA}`;
    if (agente !== this.agenteChrome) await this.enviar('Network.setUserAgentOverride', { userAgent: agente, acceptLanguage: 'es-ES,es' });
    if (o.bloquear.length) await this.enviar('Network.setBlockedURLs', { urls: o.bloquear });
  }

  alEvento({ method, params }) {
    this.ultimaActividad = Date.now();
    if (method === 'Network.requestWillBeSent') this.enVuelo.set(params.requestId, params.request.url);
    else if (method === 'Network.loadingFinished') this.enVuelo.delete(params.requestId);
    else if (method === 'Network.loadingFailed') {
      const url = this.enVuelo.get(params.requestId);
      this.enVuelo.delete(params.requestId);
      if (!params.canceled) this.registro.fallos.push({ url, error: params.blockedReason ? `bloqueado (${params.blockedReason})` : params.errorText, tipo: params.type });
    } else if (method === 'Network.responseReceived') {
      const r = params.response;
      this.registro.respuestas.push({ url: r.url, estado: r.status, tipo: params.type, mime: r.mimeType, cabeceras: params.type === 'Document' ? r.headers : undefined, loaderId: params.loaderId });
    }
    for (const espera of this.esperas) espera({ method, params });
  }

  esperarEvento(nombre, ms = 30000, condicion = () => true) {
    return new Promise((resolver, rechazar) => {
      const oyente = (m) => {
        if (m.method === nombre && condicion(m.params)) { this.esperas.delete(oyente); clearTimeout(t); resolver(m.params); }
      };
      const t = setTimeout(() => { this.esperas.delete(oyente); rechazar(new Error(`Tiempo agotado esperando ${nombre}`)); }, ms);
      this.esperas.add(oyente);
    });
  }

  /** Espera a que no haya peticiones de red durante `quieto` ms (máximo `maximo` ms). */
  async esperarRedQuieta({ quieto = 600, maximo = 10000 } = {}) {
    const limite = Date.now() + maximo;
    while (Date.now() < limite) {
      if (this.enVuelo.size === 0 && Date.now() - this.ultimaActividad >= quieto) return true;
      await esperar(100);
    }
    return false;
  }

  /**
   * Chrome no dibuja las pestañas de fondo: sin esto, las cargas perezosas no se
   * disparan cuando hay más de una pestaña abierta (ordenador y móvil).
   * Comprobado: 0 de 5 cargas sin traerla al frente, 5 de 5 trayéndola.
   */
  alFrente() { return this.enviar('Page.bringToFront'); }

  /** Abre una URL y espera a que termine de cargar. Devuelve el estado HTTP y la URL final. */
  async ir(url, { maximo = 30000 } = {}) {
    await this.alFrente();
    this.registro = { fallos: [], respuestas: [] };
    this.enVuelo.clear();
    const carga = this.esperarEvento('Page.loadEventFired', maximo).catch(() => null);
    const r = await this.enviar('Page.navigate', { url });
    if (r.errorText) throw new Error(`No se pudo abrir ${url}: ${r.errorText}`);
    const cargada = await carga;
    await this.esperarRedQuieta();
    await this.evaluar(() => document.fonts.ready.then(() => true)).catch(() => null);
    const principal = this.registro.respuestas.find((x) => x.tipo === 'Document' && x.loaderId === r.loaderId);
    const urlFinal = await this.evaluar(() => location.href);
    return { estado: principal?.estado ?? null, cabeceras: principal?.cabeceras ?? {}, urlFinal, cargaCompleta: Boolean(cargada) };
  }

  /** Ejecuta una función dentro de la página y devuelve su resultado (debe ser serializable). */
  async evaluar(funcion, ...argumentos) {
    const expression = `(${funcion.toString()})(...${JSON.stringify(argumentos)})`;
    const r = await this.enviar('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (r.exceptionDetails) {
      throw new Error(`Error en la página: ${r.exceptionDetails.exception?.description ?? r.exceptionDetails.text}`);
    }
    return r.result.value;
  }

  /** Baja poco a poco hasta el final para que carguen las imágenes «perezosas», y vuelve arriba. */
  async recorrerHastaElFinal() {
    await this.alFrente();
    await this.evaluar(async () => {
      const pausa = (ms) => new Promise((r) => setTimeout(r, ms));
      const paso = Math.max(200, Math.floor(innerHeight * 0.8));
      for (let y = 0, i = 0; i < 80; i++, y += paso) {
        scrollTo(0, y);
        await pausa(120);
        if (y + innerHeight >= document.documentElement.scrollHeight) break;
      }
      scrollTo(0, document.documentElement.scrollHeight);
      // Las cargas perezosas con JavaScript reaccionan en el siguiente fotograma:
      // si se vuelve arriba enseguida, a veces no llegan a pedir la imagen.
      await Promise.race([new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))), pausa(1000)]);
      await pausa(300);
    });
    await this.esperarRedQuieta({ quieto: 500, maximo: 8000 });
    await this.evaluar(() => Promise.all([...document.images].filter((i) => !i.complete)
      .map((i) => new Promise((r) => { i.addEventListener('load', r); i.addEventListener('error', r); setTimeout(r, 4000); }))).then(() => true));
    await this.evaluar(() => { scrollTo(0, 0); return true; });
  }

  /** Oculta (no acepta) los avisos de cookies. Devuelve qué ha ocultado. */
  ocultarAvisosCookies() {
    return this.evaluar(ocultarAvisosCookiesEnPagina);
  }

  /**
   * Captura en PNG. Por defecto, la página completa (con un tope de alto en
   * píxeles de pantalla). Devuelve también si la web está adaptada al móvil.
   */
  async capturar(ruta, { completa = true, altoMaximo = 16000 } = {}) {
    const m = await this.enviar('Page.getLayoutMetrics');
    // Una web sin <meta name="viewport"> se dibuja a 980 px y el móvil la encoge
    // para que quepa: capturamos lo mismo que vería la persona, no un recorte.
    const zoom = m.cssVisualViewport.scale || 1;
    const anchoCss = m.cssLayoutViewport.clientWidth;
    const altoPantalla = Math.ceil((completa ? m.cssContentSize.height : m.cssLayoutViewport.clientHeight) * zoom);
    const alto = Math.min(altoPantalla, altoMaximo);
    const { data } = await this.enviar('Page.captureScreenshot', {
      format: 'png', captureBeyondViewport: completa,
      clip: { x: 0, y: 0, width: anchoCss, height: alto / zoom, scale: zoom },
    });
    writeFileSync(ruta, Buffer.from(data, 'base64'));
    let adaptadaMovil;
    let motivo;
    if (this.opciones.movil) {
      adaptadaMovil = zoom === 1 && anchoCss <= this.opciones.ancho;
      if (!adaptadaMovil) {
        const tieneViewport = await this.evaluar(() => Boolean(document.querySelector('meta[name="viewport"]')));
        motivo = tieneViewport ? 'hay contenido más ancho que la pantalla: se ve encogida o se mueve de lado'
          : 'no tiene la etiqueta viewport: el móvil la dibuja como en un ordenador y la encoge';
      }
    }
    return {
      ancho: Math.round(anchoCss * zoom * this.opciones.escala),
      alto: Math.round(alto * this.opciones.escala),
      recortada: altoPantalla > altoMaximo,
      adaptadaMovil,
      motivo,
    };
  }

  async pdf(ruta) {
    const { data } = await this.enviar('Page.printToPDF', {
      printBackground: true, preferCSSPageSize: true, displayHeaderFooter: false,
      generateTaggedPDF: true, generateDocumentOutline: true,
    });
    writeFileSync(ruta, Buffer.from(data, 'base64'));
  }

  async html() {
    return this.evaluar(() => '<!doctype html>\n' + document.documentElement.outerHTML);
  }
}

function quitarIndefinidos(objeto) {
  return Object.fromEntries(Object.entries(objeto).filter(([, v]) => v !== undefined));
}

// Se ejecuta DENTRO de la página: no puede usar nada de fuera de la función.
function ocultarAvisosCookiesEnPagina() {
  const conocidos = [
    '#onetrust-consent-sdk', '#onetrust-banner-sdk', '#CybotCookiebotDialog', '#CybotCookiebotDialogBodyUnderlay',
    '#cmplz-cookiebanner-container', '.cmplz-cookiebanner', '#cookie-law-info-bar', '.cli-modal-backdrop',
    '.cky-consent-container', '.cky-overlay', '#didomi-host', '#qc-cmp2-container', '#iubenda-cs-banner',
    '#usercentrics-root', '#usercentrics-cmp-ui', '[id^="sp_message_container"]', '#cookie-notice', '#cookieConsent',
    '.cc-window', '.cc-banner', '#moove_gdpr_cookie_info_bar', '#BorlabsCookieBox', '#cookiescript_injected',
    '.fc-consent-root', '#truste-consent-track', '#tarteaucitronRoot', '#axeptio_overlay', '#gdpr-cookie-message',
    '#cookie-banner', '.cookie-banner', '#cookies-banner', '.cookies-banner', '#cookie-consent', '.cookie-consent',
    '#aviso-cookies', '.aviso-cookies', '#cookieNotice', '#cookie-bar', '.cookie-bar', '#ckyBanner',
  ];
  const ocultos = [];
  const esconder = (el, motivo) => {
    el.style.setProperty('display', 'none', 'important');
    el.dataset.edwOculto = '1';
    ocultos.push(motivo);
  };
  const describir = (el) => el.tagName.toLowerCase() + (el.id ? `#${el.id}` : '')
    + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
  for (const selector of conocidos) {
    for (const el of document.querySelectorAll(selector)) {
      if (getComputedStyle(el).display !== 'none') esconder(el, selector);
    }
  }
  // Para los que no conocemos: capas fijas que hablan de cookies o de consentimiento.
  const habla = /cookie|consentimiento|consent|galletas|rgpd|gdpr/i;
  for (const el of document.querySelectorAll('body *')) {
    if (el.dataset.edwOculto || ['HEADER', 'NAV', 'FOOTER', 'MAIN'].includes(el.tagName)) continue;
    const estilo = getComputedStyle(el);
    if (!['fixed', 'sticky'].includes(estilo.position) || estilo.display === 'none' || estilo.visibility === 'hidden') continue;
    const caja = el.getBoundingClientRect();
    if (caja.width * caja.height < 2000) continue;
    const texto = (el.innerText || '') + ' ' + (el.shadowRoot?.textContent || '');
    if (texto.length < 4000 && (habla.test(texto) || habla.test(el.id) || habla.test(String(el.className)))) {
      esconder(el, `parecido: ${describir(el)}`);
    }
  }
  for (const d of document.querySelectorAll('dialog[open]')) {
    if (habla.test(d.innerText)) esconder(d, 'dialog');
  }
  if (ocultos.length) {
    // Muchos avisos bloquean el desplazamiento mientras están abiertos.
    for (const el of [document.documentElement, document.body]) {
      el.style.setProperty('overflow', 'visible', 'important');
    }
  }
  return ocultos;
}
