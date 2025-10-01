# 🛡️ ETAPE2PLUS - Déploiement PythonAnywhere

## 📋 Vue d'ensemble

Le programme **etape2plus** est un explorateur interactif des domaines de compétence NICE Framework (NF-COM) qui s'intègre parfaitement dans votre application Django.

## 🚀 Déploiement sur PythonAnywhere

### 1. Fichiers à déployer

Le dossier `staticfiles/etape2plus/` contient tous les fichiers nécessaires :

```
staticfiles/etape2plus/
├── index_1.html          # Page principale (28,384 bytes)
├── style_1.css           # Styles CSS complets (38,376 bytes)
├── app_3.js              # Logique JavaScript principale (39,335 bytes)
├── app_4.js              # Fichier JS supplémentaire (39,335 bytes)
├── app_5.js              # Fichier JS supplémentaire (39,335 bytes)
└── nice-competency-explorer-final.zip.zip  # Archive supplémentaire
```

### 2. Instructions de déploiement

#### Étape 1: Upload des fichiers
1. Connectez-vous à votre console PythonAnywhere
2. Naviguez vers le dossier `static/` de votre application
3. Créez un dossier `etape2plus/`
4. Uploadez tous les fichiers du dossier `staticfiles/etape2plus/`

#### Étape 2: Vérification des permissions
Assurez-vous que tous les fichiers sont accessibles en lecture :
```bash
chmod 644 /home/votreusername/mysite/static/etape2plus/*
```

#### Étape 3: Test de l'accès
Testez l'accès direct à votre fichier :
```
https://votreusername.pythonanywhere.com/static/etape2plus/index_1.html
```

### 3. Intégration dans l'application

Le bouton "Learn more about the Competency Areas" dans `etape2_first_step.html` est déjà configuré pour ouvrir le programme :

```html
<button onclick="window.open('/static/etape2plus/index_1.html', '_blank')">
  <span>Learn more about the Competency Areas</span>
  <span>+</span>
</button>
```

## 🔧 Fonctionnalités du programme

### Interface utilisateur
- **Navigation par onglets** : Competency Areas, Career Pathways, About
- **Recherche interactive** : Par nom ou mot-clé
- **Filtres avancés** : Par catégorie, niveau de progression
- **Vues multiples** : Grille et liste
- **Modal détaillé** : Informations complètes sur chaque domaine

### Données incluses
- **15 domaines de compétence** NF-COM (NF-COM-001 à NF-COM-015)
- **Descriptions détaillées** de chaque domaine
- **Applications réelles** et exemples pratiques
- **Pertinence carrière** pour différents rôles
- **Statut officiel** (officiel vs proposé)

### Catégories de domaines
- **Technique** : Access Controls, Asset Management, Cloud Security, etc.
- **Management** : Cybersecurity Leadership
- **Technologie émergente** : Artificial Intelligence Security
- **Stratégique** : Cyber Resiliency, Supply Chain Security
- **Spécialisé** : Operational Technology Security

## 🎯 Utilisation

1. **Accès direct** : Via le bouton dans `etape2_first_step.html`
2. **Navigation** : Utilisez les onglets pour explorer différents aspects
3. **Recherche** : Tapez des mots-clés pour filtrer les domaines
4. **Détails** : Cliquez sur une carte pour voir les informations complètes
5. **Filtres** : Utilisez les menus déroulants pour affiner les résultats

## 🔍 Dépannage

### Problèmes courants

#### Le CSS ne se charge pas
- Vérifiez que `style_1.css` est bien uploadé
- Vérifiez les permissions du fichier
- Vérifiez le chemin dans `index_1.html`

#### Le JavaScript ne fonctionne pas
- Vérifiez que `app_3.js` est bien uploadé
- Ouvrez la console du navigateur pour voir les erreurs
- Vérifiez le chemin dans `index_1.html`

#### Le lien ne s'ouvre pas
- Vérifiez que le chemin `/static/etape2plus/index_1.html` est correct
- Testez l'accès direct au fichier
- Vérifiez que le fichier `index_1.html` existe

### Commandes de vérification

```bash
# Vérifier que les fichiers existent
ls -la /home/votreusername/mysite/static/etape2plus/

# Vérifier les permissions
ls -la /home/votreusername/mysite/static/etape2plus/*.css
ls -la /home/votreusername/mysite/static/etape2plus/*.js
ls -la /home/votreusername/mysite/static/etape2plus/*.html
```

## 📞 Support

Si vous rencontrez des problèmes :
1. Vérifiez que tous les fichiers sont uploadés
2. Vérifiez les permissions des fichiers
3. Testez l'accès direct au fichier HTML
4. Consultez la console du navigateur pour les erreurs JavaScript

---

**Note** : Ce programme est entièrement autonome et ne nécessite aucune configuration supplémentaire une fois les fichiers uploadés correctement.
