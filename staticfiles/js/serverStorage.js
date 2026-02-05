/**
 * serverStorage.js
 *
 * Stockage côté serveur pour les données utilisateur.
 * Chaque utilisateur a accès à ses sauvegardes depuis n'importe quelle machine.
 *
 * userStorage : interface sync (après preload) - utilise le serveur si authentifié
 * serverStorage : interface async - pour les appels directs
 */

const serverStorage = {
  _cache: {},
  _preloadPromise: null,

  _getCsrfToken() {
    const input = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (input && input.value) return input.value;
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  },

  _isAuthenticated() {
    const authElem = document.getElementById('user-authenticated');
    return authElem && authElem.getAttribute('data-authenticated') === 'True';
  },

  /**
   * Précharge toutes les données utilisateur depuis le serveur.
   * À appeler au chargement de la page avant toute lecture.
   */
  async preload() {
    if (!this._isAuthenticated()) return;
    if (this._preloadPromise) return this._preloadPromise;
    this._preloadPromise = (async () => {
      try {
        const response = await fetch('/api/saved-data/all/');
        if (!response.ok) return;
        const result = await response.json();
        if (result.status === 'success' && result.data) {
          for (const [key, value] of Object.entries(result.data)) {
            this._cache[key] = typeof value === 'string' ? value : JSON.stringify(value);
          }
        }
      } catch (e) {
        console.error('serverStorage.preload:', e);
      }
    })();
    return this._preloadPromise;
  },

  async getItem(key) {
    if (!this._isAuthenticated()) return localStorage.getItem(key);
    if (this._cache[key] !== undefined) return this._cache[key];
    try {
      const response = await fetch(`/api/saved-data/${encodeURIComponent(key)}/`);
      if (!response.ok) {
        if (response.status === 404) return null;
        throw new Error(response.statusText);
      }
      const result = await response.json();
      this._cache[key] = JSON.stringify(result.data);
      return this._cache[key];
    } catch (e) {
      console.error('serverStorage.getItem:', e);
      return localStorage.getItem(key);
    }
  },

  async setItem(key, value) {
    if (!this._isAuthenticated()) {
      localStorage.setItem(key, value);
      return;
    }
    let parsedValue;
    try {
      parsedValue = typeof value === 'string' ? JSON.parse(value) : value;
    } catch (_) {
      parsedValue = value;
    }
    this._cache[key] = typeof value === 'string' ? value : JSON.stringify(value);
    try {
      const response = await fetch('/api/saved-data/save/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this._getCsrfToken()
        },
        body: JSON.stringify({ key, value: parsedValue })
      });
      if (!response.ok) throw new Error(response.statusText);
    } catch (e) {
      console.error('serverStorage.setItem:', e);
      localStorage.setItem(key, value);
    }
  },

  async removeItem(key) {
    if (!this._isAuthenticated()) {
      localStorage.removeItem(key);
      return;
    }
    delete this._cache[key];
    try {
      const response = await fetch(`/api/saved-data/delete/${encodeURIComponent(key)}/`, {
        method: 'DELETE',
        headers: { 'X-CSRFToken': this._getCsrfToken() }
      });
      if (!response.ok) throw new Error(response.statusText);
    } catch (e) {
      console.error('serverStorage.removeItem:', e);
      localStorage.removeItem(key);
    }
  },

  async keys() {
    if (!this._isAuthenticated()) return Object.keys(localStorage);
    try {
      const response = await fetch('/api/saved-data/');
      if (!response.ok) throw new Error(response.statusText);
      const result = await response.json();
      return result.data.map(item => item.key);
    } catch (e) {
      console.error('serverStorage.keys:', e);
      return Object.keys(localStorage);
    }
  }
};

/**
 * userStorage : interface sync pour les données utilisateur.
 * - Si authentifié : lit/écrit via le serveur (cache après preload)
 * - Sinon : localStorage
 *
 * IMPORTANT : appeler await userStorage.ready() au début du DOMContentLoaded
 * avant toute lecture des données utilisateur.
 */
const userStorage = {
  _ready: false,

  async ready() {
    if (this._ready) return;
    await serverStorage.preload();
    this._ready = true;
  },

  getItem(key) {
    if (serverStorage._isAuthenticated() && serverStorage._cache[key] !== undefined) {
      return serverStorage._cache[key];
    }
    return localStorage.getItem(key);
  },

  setItem(key, value) {
    const str = typeof value === 'string' ? value : JSON.stringify(value);
    if (serverStorage._isAuthenticated()) {
      serverStorage._cache[key] = str;
      serverStorage.setItem(key, str);
    } else {
      localStorage.setItem(key, str);
    }
  },

  removeItem(key) {
    if (serverStorage._isAuthenticated()) {
      delete serverStorage._cache[key];
      serverStorage.removeItem(key);
    } else {
      localStorage.removeItem(key);
    }
  }
};

/** Helper: retourne userStorage si dispo (données serveur), sinon localStorage */
function getStorage() {
  return typeof userStorage !== 'undefined' ? userStorage : localStorage;
}
