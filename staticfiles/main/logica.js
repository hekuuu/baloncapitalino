// --- BÚSQUEDA DE JUGADORES ---
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
      const jugadores = data.results || data;
      if (!jugadores || jugadores.length === 0) {
        resultDiv.innerHTML = '<p>No se encontraron jugadores.</p>';
      } else {
        resultDiv.innerHTML = '<ul>' + jugadores.map(j => `<li>${j.nombre} (${j.posicion || ''})</li>`).join('') + '</ul>';
      }
    });
});

// --- LOGIN ---
async function login(username, password) {
  try {
    const response = await fetch('/api/token/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    if (response.ok) {
      localStorage.setItem('access', data.access);
      localStorage.setItem('refresh', data.refresh);
      alert('¡Login exitoso!');
      location.reload();
    } else {
      alert('Error: ' + (data.detail || 'Credenciales incorrectas'));
    }
  } catch (err) {
    alert('Error de conexión. Intenta de nuevo.');
  }
}

// --- USAR TOKEN EN PETICIONES PROTEGIDAS ---
async function getJugadores() {
  let token = localStorage.getItem('access');
  let response = await fetch('http://127.0.0.1:8000/api/jugadores/', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (response.status === 401) {
    const refreshed = await refreshToken();
    if (refreshed) {
      token = localStorage.getItem('access');
      response = await fetch('http://127.0.0.1:8000/api/jugadores/', {
        headers: { 'Authorization': 'Bearer ' + token }
      });
    } else {
      alert('Sesión expirada. Por favor inicia sesión de nuevo.');
      logout();
      return;
    }
  }
  const data = await response.json();
  console.log(data);
  // Aquí puedes mostrar los jugadores en el DOM
}

// --- REFRESCAR TOKEN ---
async function refreshToken() {
  const refresh = localStorage.getItem('refresh');
  if (!refresh) return false;
  const response = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh })
  });
  const data = await response.json();
  if (response.ok) {
    localStorage.setItem('access', data.access);
    return true;
  } else {
    return false;
  }
}

// --- CERRAR SESIÓN ---
function logout() {
  localStorage.removeItem('access');
  localStorage.removeItem('refresh');
  alert('Sesión cerrada.');
  location.reload();
}

// --- EVENTOS DEL DOM ---
document.addEventListener('DOMContentLoaded', function() {
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async function(e) {
      e.preventDefault();
      const username = document.getElementById('login-username').value;
      const password = document.getElementById('login-password').value;
      login(username, password);
    });
  }
});
document.getElementById('btn-jugadores').addEventListener('click', getJugadores);
// Si quieres un botón de cerrar sesión:
// document.getElementById('btn-logout').addEventListener('click', logout);