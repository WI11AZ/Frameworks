/**
 * serverStorage.js
 * 
 * Une alternative côté serveur au localStorage du navigateur.
 * Fournit une interface similaire mais stocke les données sur le serveur.
 * Utilisation :
 * - serverStorage.getItem(key) : récupère une valeur depuis le serveur
 * - serverStorage.setItem(key, value) : sauvegarde une valeur sur le serveur
 * - serverStorage.removeItem(key) : supprime une valeur du serveur
 * - serverStorage.keys() : liste toutes les clés disponibles
 */

const serverStorage = {
  // Cache local pour réduire les appels API
  _cache: {},
  
  // Renvoie le token CSRF
  _getCsrfToken() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  },
  
  // Détermine si l'utilisateur est connecté
  _isAuthenticated() {
    // Vérifie si l'élément avec l'ID 'user-authenticated' existe et a l'attribut data-authenticated="True"
    const authElem = document.getElementById('user-authenticated');
    return authElem && authElem.getAttribute('data-authenticated') === 'True';
  },
  
  // Si l'utilisateur n'est pas connecté, utilise le localStorage comme fallback
  async getItem(key) {
    if (!this._isAuthenticated()) {
      console.warn('Utilisateur non authentifié, utilisation du localStorage');
      return localStorage.getItem(key);
    }
    
    try {
      // Si dans le cache, renvoie directement
      if (this._cache[key] !== undefined) {
        return this._cache[key];
      }
      
      const response = await fetch(`/api/saved-data/${encodeURIComponent(key)}/`);
      
      if (!response.ok) {
        // Si 404, renvoie null comme le ferait localStorage
        if (response.status === 404) return null;
        throw new Error(`Erreur lors de la récupération des données: ${response.statusText}`);
      }
      
      const result = await response.json();
      // Mise en cache
      this._cache[key] = JSON.stringify(result.data);
      return JSON.stringify(result.data);
    } catch (error) {
      console.error('Erreur serverStorage.getItem:', error);
      // Fallback à localStorage en cas d'erreur
      return localStorage.getItem(key);
    }
  },
  
  async setItem(key, value) {
    if (!this._isAuthenticated()) {
      console.warn('Utilisateur non authentifié, utilisation du localStorage');
      return localStorage.setItem(key, value);
    }
    
    try {
      // Parse la valeur si c'est une chaîne JSON
      let parsedValue;
      try {
        parsedValue = JSON.parse(value);
      } catch (e) {
        // Si ce n'est pas du JSON valide, utilise la valeur telle quelle
        parsedValue = value;
      }
      
      const response = await fetch('/api/saved-data/save/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this._getCsrfToken()
        },
        body: JSON.stringify({
          key: key,
          value: parsedValue
        })
      });
      
      if (!response.ok) {
        throw new Error(`Erreur lors de la sauvegarde des données: ${response.statusText}`);
      }
      
      // Met à jour le cache
      this._cache[key] = value;
      
      return true;
    } catch (error) {
      console.error('Erreur serverStorage.setItem:', error);
      // Fallback à localStorage en cas d'erreur
      return localStorage.setItem(key, value);
    }
  },
  
  async removeItem(key) {
    if (!this._isAuthenticated()) {
      console.warn('Utilisateur non authentifié, utilisation du localStorage');
      return localStorage.removeItem(key);
    }
    
    try {
      const response = await fetch(`/api/saved-data/delete/${encodeURIComponent(key)}/`, {
        method: 'DELETE',
        headers: {
          'X-CSRFToken': this._getCsrfToken()
        }
      });
      
      if (!response.ok) {
        throw new Error(`Erreur lors de la suppression des données: ${response.statusText}`);
      }
      
      // Supprime du cache
      delete this._cache[key];
      
      return true;
    } catch (error) {
      console.error('Erreur serverStorage.removeItem:', error);
      // Fallback à localStorage en cas d'erreur
      return localStorage.removeItem(key);
    }
  },
  
  async keys() {
    if (!this._isAuthenticated()) {
      console.warn('Utilisateur non authentifié, utilisation du localStorage');
      return Object.keys(localStorage);
    }
    
    try {
      const response = await fetch('/api/saved-data/');
      
      if (!response.ok) {
        throw new Error(`Erreur lors de la récupération des clés: ${response.statusText}`);
      }
      
      const result = await response.json();
      return result.data.map(item => item.key);
    } catch (error) {
      console.error('Erreur serverStorage.keys:', error);
      // Fallback à localStorage en cas d'erreur
      return Object.keys(localStorage);
    }
  }
};

// Fonction d'initialisation à appeler dans chaque page
function initServerStorage() {
  // Ajoute un élément caché qui indique si l'utilisateur est authentifié
  // Cette fonction doit être appelée depuis les templates Django où
  // vous avez accès à la variable user.is_authenticated
  console.log('serverStorage initialisé');
} 