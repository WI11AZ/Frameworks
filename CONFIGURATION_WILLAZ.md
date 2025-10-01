# 🔧 Configuration PythonAnywhere - WILLAZ

## ✅ Configuration corrigée

### **Problème identifié :**
Le site cherche dans `/home/WILLAZ/Frameworks-master` (avec WILLAZ en majuscules)

### **Solution appliquée :**
1. **`dcwf/settings.py`** : `STATIC_ROOT = '/home/WILLAZ/Frameworks-master/staticfiles'`
2. **`dcwf/urls.py`** : Configuration pour servir les fichiers statiques sur PythonAnywhere

## 🚀 Instructions de déploiement

### **Étape 1 : Télécharger les fichiers modifiés**
- `dcwf/settings.py`
- `dcwf/urls.py`
- `deploy_willaz.py`

### **Étape 2 : Exécuter le script de déploiement**
```bash
# Dans la console Bash de PythonAnywhere
cd /home/WILLAZ/Frameworks-master
python3.10 deploy_willaz.py
```

### **Étape 3 : Configuration dans l'onglet "Web"**
1. Allez dans l'onglet "Web" de PythonAnywhere
2. Dans la section "Static files", ajoutez :
   - **URL** : `/static/`
   - **Directory** : `/home/WILLAZ/Frameworks-master/staticfiles/`
3. Cliquez sur "Reload" pour redémarrer l'application

## 🧪 Tests de vérification

### **URLs à tester :**
- `https://willaz.pythonanywhere.com/static/photos_haute_qualite/RealBG.png`
- `https://willaz.pythonanywhere.com/static/photos_haute_qualite/E1.png`
- `https://willaz.pythonanywhere.com/static/favicon.ico`

### **Vérification des fichiers :**
```bash
# Vérifier que les fichiers existent
ls -la /home/WILLAZ/Frameworks-master/staticfiles/photos_haute_qualite/
```

## 🔍 Dépannage

### **Si les images ne s'affichent toujours pas :**

1. **Vérifiez la configuration Web :**
   - URL : `/static/`
   - Directory : `/home/WILLAZ/Frameworks-master/staticfiles/`

2. **Vérifiez les permissions :**
   ```bash
   chmod -R 755 /home/WILLAZ/Frameworks-master/staticfiles/
   ```

3. **Vérifiez que les fichiers existent :**
   ```bash
   ls -la /home/WILLAZ/Frameworks-master/web_app/static/photos_haute_qualite/
   ```

## 📋 Checklist finale

- [ ] Fichiers `dcwf/settings.py` et `dcwf/urls.py` téléchargés
- [ ] Script `deploy_willaz.py` exécuté avec succès
- [ ] Configuration Web mise à jour avec le bon chemin
- [ ] Application redémarrée
- [ ] Images testées sur les URLs directes

---

**Cette configuration devrait résoudre le problème des images sur PythonAnywhere !** 🎉
