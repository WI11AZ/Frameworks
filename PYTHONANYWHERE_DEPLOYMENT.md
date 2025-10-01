# 🚀 Guide de Déploiement PythonAnywhere - Images

## ✅ Configuration mise à jour

### 1. **Fichiers modifiés :**
- `dcwf/settings.py` - Configuration des fichiers statiques corrigée
- `deploy_pythonanywhere.py` - Script de déploiement automatique

### 2. **Améliorations apportées :**
- ✅ Correction du chemin utilisateur (`willaz` au lieu de `WILLAZ`)
- ✅ Ajout de `pythonanywhere.com` dans la détection d'environnement
- ✅ Inclusion des deux dossiers statiques (`web_app/static` et `static`)
- ✅ Script automatique de copie vers `mysite/static`

## 🔧 Instructions de déploiement

### **Étape 1 : Préparer localement**
```bash
# Collecter les fichiers statiques localement
python manage.py collectstatic --noinput

# Vérifier que les images sont présentes
ls staticfiles/photos_haute_qualite/
```

### **Étape 2 : Déployer sur PythonAnywhere**

#### **2.1 Télécharger les fichiers modifiés :**
- `dcwf/settings.py`
- `deploy_pythonanywhere.py`

#### **2.2 Exécuter le script de déploiement :**
```bash
# Dans la console Bash de PythonAnywhere
cd /home/willaz/Frameworks-master
python3.10 deploy_pythonanywhere.py
```

#### **2.3 Redémarrer l'application :**
- Allez dans l'onglet "Web" de PythonAnywhere
- Cliquez sur "Reload" pour redémarrer votre application

## 🧪 Tests de vérification

### **URLs à tester :**
1. **Image principale :** `https://willaz.pythonanywhere.com/static/photos_haute_qualite/RealBG.png`
2. **Images des étapes :** `https://willaz.pythonanywhere.com/static/photos_haute_qualite/E1.png`
3. **Favicon :** `https://willaz.pythonanywhere.com/static/favicon.ico`

### **Pages à vérifier :**
- Page d'accueil : Images de fond et étapes
- Page principale : Image RealBG.png
- Page étape 2 : Image CAB2.png

## 🔍 Dépannage

### **Si les images ne s'affichent toujours pas :**

#### **Vérification 1 : Structure des dossiers**
```bash
# Vérifier que les images existent
ls -la /home/willaz/Frameworks-master/web_app/static/photos_haute_qualite/
ls -la /home/willaz/mysite/static/photos_haute_qualite/
```

#### **Vérification 2 : Configuration Django**
```bash
# Dans la console PythonAnywhere
cd /home/willaz/Frameworks-master
python3.10 manage.py shell
>>> from django.conf import settings
>>> print(settings.STATIC_ROOT)
>>> print(settings.STATICFILES_DIRS)
```

#### **Vérification 3 : Permissions**
```bash
# Vérifier les permissions
ls -la /home/willaz/mysite/static/
chmod -R 755 /home/willaz/mysite/static/
```

## 📋 Checklist de déploiement

- [ ] Fichiers `dcwf/settings.py` et `deploy_pythonanywhere.py` téléchargés
- [ ] Script `deploy_pythonanywhere.py` exécuté avec succès
- [ ] Application redémarrée dans l'onglet "Web"
- [ ] Images testées sur les URLs directes
- [ ] Pages web vérifiées visuellement

## 🎯 Résultat attendu

Après le déploiement, toutes les images devraient s'afficher correctement :
- ✅ Images de fond sur toutes les pages
- ✅ Images des étapes (E1.png, E2.png, E3.png)
- ✅ Favicon dans l'onglet du navigateur
- ✅ Images dans les templates Django

---

**Cette configuration devrait résoudre définitivement le problème des images sur PythonAnywhere !** 🎉
