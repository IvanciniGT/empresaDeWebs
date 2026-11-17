/**
 * Servidor web local para las pruebas: sirve una carpeta en 127.0.0.1 y apunta
 * cada petición, para poder comprobar qué se ha pedido y qué no.
 *
 *   const web = await servir('pruebas/web-prueba', { '{{EXTERNO}}': otra.url });
 *   web.url              → http://127.0.0.1:PUERTO
 *   web.pedidas('/ruta') → cuántas veces se ha pedido
 *   await web.cerrar();
 *
 * En los ficheros de texto, {{BASE}} se cambia por la URL del propio servidor.
 * Si una ruta no existe, se llama a `otras(ruta, peticion)` (si se da) antes del 404.
 */
import { readFile, stat } from 'node:fs/promises';
import { createServer } from 'node:http';
import path from 'node:path';

const TIPOS = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml', '.json': 'application/json', '.pdf': 'application/pdf', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.md': 'text/markdown; charset=utf-8',
};

export async function servir(carpeta, sustituciones = {}, otras = null) {
  const visitas = [];
  const servidor = createServer(async (peticion, respuesta) => {
    const ruta = decodeURIComponent(new URL(peticion.url, 'http://x').pathname);
    visitas.push({ ruta, agente: peticion.headers['user-agent'] ?? '', cabeceras: peticion.headers });
    if (otras) {
      const hecho = await otras(ruta, peticion, respuesta);
      if (hecho) return;
    }
    let fichero = path.join(carpeta, ruta);
    if (!fichero.startsWith(path.resolve(carpeta))) { respuesta.writeHead(403).end(); return; }
    try {
      if ((await stat(fichero)).isDirectory()) fichero = path.join(fichero, 'index.html');
      let cuerpo = await readFile(fichero);
      const tipo = TIPOS[path.extname(fichero).toLowerCase()] ?? 'application/octet-stream';
      if (/^text|xml|json/.test(tipo)) {
        let texto = cuerpo.toString('utf8').replaceAll('{{BASE}}', base);
        for (const [clave, valor] of Object.entries(sustituciones)) texto = texto.replaceAll(clave, valor);
        cuerpo = Buffer.from(texto);
      }
      respuesta.writeHead(200, { 'content-type': tipo, 'server': 'servidor-de-pruebas' }).end(cuerpo);
    } catch {
      respuesta.writeHead(404, { 'content-type': 'text/html; charset=utf-8' }).end('<!doctype html><title>No existe</title><h1>404</h1>');
    }
  });
  await new Promise((r) => servidor.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${servidor.address().port}`;
  return {
    url: base,
    visitas,
    pedidas: (ruta) => visitas.filter((v) => v.ruta === ruta).length,
    cerrar: () => new Promise((r) => { servidor.closeAllConnections(); servidor.close(r); }),
  };
}
