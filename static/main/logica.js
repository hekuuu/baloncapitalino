document.getElementById('search-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const equipo = document.getElementById('equipo').value;
  const torneo = document.getElementById('torneo').value;
  let url = `/api/jugadores/?`;
  if (equipo) url += `equipo=${encodeURIComponent(equipo)}&`;
  if (torneo) url += `torneo=${encodeURIComponent(torneo)}`;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const resultDiv = document.getElementById('jugadores-result');
      if (data.length === 0) {
        resultDiv.innerHTML = '<p>No se encontraron jugadores.</p>';
      } else {
        resultDiv.innerHTML = '<ul>' + data.map(j => `<li>${j.nombre} (${j.posicion || ''})</li>`).join('') + '</ul>';
      }
    });
});