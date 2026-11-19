// Marca el día de hoy en el horario y dice si ahora está abierto.
// Sin este script la web funciona igual: solo no se destaca el día.
// El horario es PROVISIONAL (OpenStreetMap): cuando el cliente lo confirme, se cambia aquí y en el HTML.
(function () {
  // 0 = domingo … 6 = sábado. Tramos en minutos desde las 0:00.
  var HORARIO = {
    1: [[540, 825], [990, 1245]], 2: [[540, 825], [990, 1245]], 3: [[540, 825], [990, 1245]],
    4: [[540, 825], [990, 1245]], 5: [[540, 825], [990, 1245]], 6: [[510, 840]], 0: []
  };
  var ahora = new Date();
  var dia = ahora.getDay();
  var minuto = ahora.getHours() * 60 + ahora.getMinutes();
  var abierto = HORARIO[dia].some(function (t) { return minuto >= t[0] && minuto < t[1]; });
  document.querySelectorAll('[data-dias]').forEach(function (fila) {
    if (fila.getAttribute('data-dias').split(',').indexOf(String(dia)) >= 0) fila.classList.add('es-hoy');
  });
  document.querySelectorAll('[data-estado-hoy]').forEach(function (el) {
    el.textContent = abierto ? 'Abierto ahora' : 'Cerrado ahora';
    el.className = 'estado-hoy ' + (abierto ? 'abierto' : 'cerrado');
  });
})();
