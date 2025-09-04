# Gestion des Rôles Utilisateur

Ce document explique comment gérer le système de rôles utilisateur basé sur les matricules dans l'application DCWF.

## Rôles Disponibles

### 1. Super User
- **Accès complet** à toutes les étapes du processus
- **Accès direct** aux étapes 2 et 3 sans progression normale
- **Interface spéciale** avec indicateurs visuels

### 2. Bêta testeur
- **Accès étendu** aux fonctionnalités
- **Interface spéciale** avec indicateurs visuels
- **Fonctionnalités avancées** disponibles

### 3. User Normal
- **Accès standard** aux fonctionnalités
- **Progression normale** à travers les étapes
- **Interface standard**

## Matricules Configurés

### Super Users
- `2351882`
- `8742647`

### Bêta testeurs
- `8640426`

## Détection Automatique

Le système détecte automatiquement le rôle lors de l'inscription basé sur le matricule. Aucune action manuelle n'est requise.

## Gestion des Rôles

### Commandes Disponibles

#### 1. Lister tous les rôles
```bash
python manage.py manage_user_roles list
```

#### 2. Ajouter un Super User
```bash
python manage.py manage_user_roles add-super --matricule 1234567
```

#### 3. Supprimer un Super User
```bash
python manage.py manage_user_roles remove-super --matricule 1234567
```

#### 4. Ajouter un Bêta testeur
```bash
python manage.py manage_user_roles add-beta --matricule 1234567
```

#### 5. Supprimer un Bêta testeur
```bash
python manage.py manage_user_roles remove-beta --matricule 1234567
```

#### 6. Mettre à jour tous les utilisateurs
```bash
python manage.py manage_user_roles update-all
```

## Configuration Manuelle

### Ajouter un nouveau Super User

1. **Modifier le fichier** `web_app/helpers/user_roles.py`
2. **Ajouter le matricule** dans la liste `SUPER_USER_MATRICULES`
3. **Exécuter la commande** de mise à jour :
   ```bash
   python manage.py manage_user_roles update-all
   ```

### Ajouter un nouveau Bêta testeur

1. **Modifier le fichier** `web_app/helpers/user_roles.py`
2. **Ajouter le matricule** dans la liste `BETA_TESTER_MATRICULES`
3. **Exécuter la commande** de mise à jour :
   ```bash
   python manage.py manage_user_roles update-all
   ```

## Exemples d'Utilisation

### Ajouter un Super User
```bash
# Ajouter le matricule 9999999 comme Super User
python manage.py manage_user_roles add-super --matricule 9999999
```

### Supprimer un Bêta testeur
```bash
# Supprimer le matricule 8640426 des Bêta testeurs
python manage.py manage_user_roles remove-beta --matricule 8640426
```

### Vérifier la configuration
```bash
# Voir tous les rôles configurés
python manage.py manage_user_roles list
```

## Interface Utilisateur

### Super User
- **Bordure violette** sur la carte utilisateur
- **Badge violet** "Super User"
- **Accès direct** aux étapes 2 et 3
- **Message spécial** "Accès complet à toutes les étapes"

### Bêta testeur
- **Bordure orange** sur la carte utilisateur
- **Badge orange** "Bêta testeur"
- **Message spécial** "Accès étendu aux fonctionnalités"

### User Normal
- **Bordure bleue** sur la carte utilisateur
- **Badge bleu** "User Normal"
- **Accès standard** aux fonctionnalités

## Fichiers de Configuration

### `web_app/helpers/user_roles.py`
Contient les listes des matricules par rôle et les fonctions de gestion.

### `web_app/models/user.py`
Modèle User avec le champ `role` et les méthodes de détection.

### `web_app/management/commands/manage_user_roles.py`
Commande Django pour gérer les rôles via la ligne de commande.

## Sécurité

- Les rôles sont **déterminés automatiquement** lors de l'inscription
- **Aucune modification manuelle** du rôle n'est possible via l'interface
- Les **matricules sont validés** (7 chiffres exactement)
- Les **rôles sont persistants** en base de données

## Dépannage

### Problème : Rôle non détecté
1. Vérifier que le matricule est dans la bonne liste
2. Exécuter `python manage.py manage_user_roles update-all`
3. Vérifier avec `python manage.py manage_user_roles list`

### Problème : Accès refusé
1. Vérifier que l'utilisateur est connecté
2. Vérifier le rôle de l'utilisateur
3. Vérifier les permissions dans l'interface

### Problème : Interface incorrecte
1. Vérifier que le template affiche le bon rôle
2. Vérifier les classes CSS pour le rôle
3. Vérifier le JavaScript pour les accès spéciaux
