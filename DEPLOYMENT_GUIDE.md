# Guide de Déploiement - PythonAnywhere

## Problème des Images qui ne s'affichent pas

### Cause du problème
Les images ne s'affichent pas sur PythonAnywhere car :
1. La configuration `STATIC_ROOT` était manquante
2. Les fichiers statiques n'étaient pas collectés correctement
3. Certains chemins d'images utilisaient des chemins absolus au lieu des chemins Django

### Solutions appliquées

#### 1. Configuration Django (settings.py)
```python
# Ajout de STATIC_ROOT pour la production
STATIC_ROOT = BASE_DIR / "staticfiles"
```

#### 2. Configuration des URLs (urls.py)
```python
# Ajout du service des fichiers statiques
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

#### 3. Correction des chemins dans les templates
- Remplacement des chemins absolus `/static/` par `{% static '...' %}`
- Correction dans `etape2_first_step.html` et `summary_chart_full.html`

### Instructions de déploiement

#### Étape 1 : Préparer les fichiers statiques
```bash
# Sur votre machine locale
python manage.py collectstatic --noinput
```

#### Étape 2 : Déployer sur PythonAnywhere
1. **Téléchargez tous les fichiers modifiés** :
   - `dcwf/settings.py`
   - `dcwf/urls.py`
   - `web_app/templates/web_app/ksat/etape2_first_step.html`
   - `web_app/templates/web_app/main/summary_chart_full.html`

2. **Sur PythonAnywhere** :
   ```bash
   # Dans la console Bash
   cd /home/willaz/Frameworks-master
   python3.10 manage.py collectstatic --noinput
   ```

3. **Copier les fichiers statiques** :
   - Naviguez vers `/home/willaz/Frameworks-master/staticfiles/`
   - Copiez tout le contenu vers `/home/willaz/mysite/static/`

#### Étape 3 : Configuration WSGI
Remplacez le contenu de votre fichier WSGI par le contenu de `pythonanywhere_wsgi.py`

#### Étape 4 : Redémarrer l'application
- Allez dans l'onglet "Web" de PythonAnywhere
- Cliquez sur "Reload" pour redémarrer votre application

### Vérification
1. Visitez `https://willaz.pythonanywhere.com/`
2. Vérifiez que l'image principale s'affiche correctement
3. Testez les autres pages avec des images

### Fichiers importants à vérifier
- `static/photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png`
- `static/photos_haute_qualite/CAB2.png`
- `static/photos_haute_qualite/bg1.png`
- `static/favicon.ico`

### En cas de problème
1. Vérifiez les logs d'erreur dans l'onglet "Web" de PythonAnywhere
2. Assurez-vous que tous les fichiers statiques sont copiés
3. Vérifiez que les permissions sont correctes (755 pour les dossiers, 644 pour les fichiers)
