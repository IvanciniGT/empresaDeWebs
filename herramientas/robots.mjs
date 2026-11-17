/**
 * Lector de robots.txt según la RFC 9309.
 *
 *   const robots = interpretarRobots(texto, 'empresaDeWebs');
 *   robots.permitido('/ruta?con=consulta')  → true / false
 *   robots.retardo                          → segundos de Crawl-delay o null
 *   robots.sitemaps                         → URLs de sitemaps declarados
 *
 * Reglas: manda el grupo que nombra a nuestro agente; si no hay, el de «*».
 * Gana la regla más larga que encaja y, si empatan, Allow.
 */

export function interpretarRobots(texto, agente = 'empresadewebs') {
  const grupos = [];
  const sitemaps = [];
  let actual = null;
  let leyendoAgentes = false;
  for (const bruta of texto.split(/\r\n|\r|\n/)) {
    const linea = bruta.replace(/#.*/, '').trim();
    const dos = linea.indexOf(':');
    if (dos < 0) continue;
    const clave = linea.slice(0, dos).trim().toLowerCase();
    const valor = linea.slice(dos + 1).trim();
    if (clave === 'user-agent') {
      if (!leyendoAgentes) { actual = { agentes: [], reglas: [], retardo: null }; grupos.push(actual); }
      actual.agentes.push(valor.toLowerCase());
      leyendoAgentes = true;
      continue;
    }
    leyendoAgentes = false;
    if (clave === 'sitemap') { if (valor) sitemaps.push(valor); continue; }
    if (!actual) continue;
    if ((clave === 'allow' || clave === 'disallow') && valor) {
      actual.reglas.push({ permitir: clave === 'allow', patron: valor, re: aExpresion(valor) });
    } else if (clave === 'crawl-delay' && !Number.isNaN(parseFloat(valor))) {
      actual.retardo = parseFloat(valor);
    }
  }
  const nombre = agente.toLowerCase();
  const propios = grupos.filter((g) => g.agentes.some((a) => a !== '*' && nombre.includes(a)));
  const elegidos = propios.length ? propios : grupos.filter((g) => g.agentes.includes('*'));
  const reglas = elegidos.flatMap((g) => g.reglas);
  const retardos = elegidos.map((g) => g.retardo).filter((r) => r !== null);
  return {
    sitemaps,
    retardo: retardos.length ? Math.max(...retardos) : null,
    reglas: reglas.map(({ permitir, patron }) => ({ permitir, patron })),
    permitido(ruta) {
      let mejor = null;
      for (const r of reglas) {
        if (!r.re.test(ruta)) continue;
        if (!mejor || r.patron.length > mejor.patron.length
          || (r.patron.length === mejor.patron.length && r.permitir)) mejor = r;
      }
      return mejor ? mejor.permitir : true;
    },
  };
}

/** Sin robots.txt (404) se puede todo; si el servidor falla (5xx), no se puede nada. */
export const TODO_PERMITIDO = interpretarRobots('');
export const NADA_PERMITIDO = interpretarRobots('User-agent: *\nDisallow: /');

function aExpresion(patron) {
  const anclado = patron.endsWith('$');
  const cuerpo = (anclado ? patron.slice(0, -1) : patron)
    .split('*').map((t) => t.replace(/[.+?^${}()|[\]\\]/g, '\\$&')).join('.*');
  return new RegExp('^' + cuerpo + (anclado ? '$' : ''));
}
