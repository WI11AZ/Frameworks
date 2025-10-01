#!/usr/bin/env python
"""
Script de déploiement complet pour PythonAnywhere
Gère les migrations, les utilisateurs et les fichiers statiques
À exécuter sur le serveur PythonAnywhere après chaque déploiement
"""

import os
import sys
import django
import shutil
from pathlib import Path

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcwf.settings')
django.setup()

from django.conf import settings
from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model

User = get_user_model()

def run_migrations():
    """Exécute les migrations de base de données"""
    print("🔄 Exécution des migrations de base de données...")
    
    try:
        # Appliquer toutes les migrations
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        print("✅ Migrations appliquées avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur lors des migrations: {e}")
        return False

def fix_user_roles():
    """Corrige les rôles des utilisateurs existants"""
    print("👥 Correction des rôles utilisateurs...")
    
    try:
        from web_app.helpers.user_roles import get_role_from_matricule
        
        # Trouver les utilisateurs qui ont des problèmes potentiels
        users_without_role = User.objects.filter(
            role__isnull=True
        ) | User.objects.filter(role='')
        
        users_without_matricule = User.objects.filter(
            matricule__isnull=True
        ) | User.objects.filter(matricule='')
        
        total_fixed = 0
        
        # Corriger les utilisateurs sans rôle
        for user in users_without_role:
            if user.matricule:
                new_role = get_role_from_matricule(user.matricule)
                user.role = new_role
                user.save()
                print(f"✅ User {user.username} (matricule: {user.matricule}) -> role: {new_role}")
                total_fixed += 1
            else:
                user.role = 'normal_user'
                user.save()
                print(f"✅ User {user.username} (no matricule) -> role: normal_user")
                total_fixed += 1
        
        # Corriger les utilisateurs sans matricule
        for user in users_without_matricule:
            user.role = 'normal_user'
            user.save()
            print(f"✅ User {user.username} (no matricule) -> role: normal_user")
            total_fixed += 1
        
        if total_fixed > 0:
            print(f"✅ {total_fixed} utilisateurs corrigés")
        else:
            print("✅ Aucun utilisateur à corriger")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la correction des utilisateurs: {e}")
        return False

def deploy_static_files():
    """Collecte tous les fichiers statiques dans STATIC_ROOT"""
    print("📁 Déploiement des fichiers statiques...")
    
    try:
        # Créer le répertoire STATIC_ROOT s'il n'existe pas
        static_root = Path(settings.STATIC_ROOT)
        static_root.mkdir(exist_ok=True)
        
        print(f"📁 STATIC_ROOT: {static_root}")
        
        # Exécuter collectstatic
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
        
        print(f"✅ Fichiers statiques collectés dans : {static_root}")
        
        # Vérifier que les images importantes sont présentes
        important_files = [
            'photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png',
            'photos_haute_qualite/CAB2.png',
            'photos_haute_qualite/bg1.png',
            'photos_haute_qualite/RealBG.png',
            'photos_haute_qualite/E1.png',
            'photos_haute_qualite/E2.png',
            'photos_haute_qualite/E3.png',
            'favicon.ico',
            'favicon-16x16.png',
            'favicon-32x32.png',
        ]
        
        print("\n🔍 Vérification des fichiers importants...")
        missing_files = []
        for file_path in important_files:
            full_path = static_root / file_path
            if full_path.exists():
                print(f"✅ {file_path}")
            else:
                print(f"❌ {file_path} - MANQUANT")
                missing_files.append(file_path)
        
        if missing_files:
            print(f"\n⚠️  Fichiers manquants ({len(missing_files)}):")
            for file in missing_files:
                print(f"   - {file}")
            print("\n💡 Vérifiez que ces fichiers existent dans web_app/static/")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors du déploiement des fichiers statiques: {e}")
        return False

def check_database_connection():
    """Vérifie la connexion à la base de données"""
    print("🗄️  Vérification de la connexion à la base de données...")
    
    try:
        # Tenter de compter les utilisateurs
        user_count = User.objects.count()
        print(f"✅ Connexion DB OK - {user_count} utilisateurs trouvés")
        return True
    except Exception as e:
        print(f"❌ Erreur de connexion à la base de données: {e}")
        return False

def main():
    """Fonction principale de déploiement"""
    print("🚀 Déploiement complet PythonAnywhere - Cyber Align")
    print("=" * 60)
    
    success_steps = []
    
    # Étape 1: Vérifier la connexion DB
    if check_database_connection():
        success_steps.append("DB Connection")
    else:
        print("❌ Impossible de continuer sans connexion DB")
        return False
    
    # Étape 2: Exécuter les migrations
    if run_migrations():
        success_steps.append("Migrations")
    else:
        print("❌ Échec des migrations")
        return False
    
    # Étape 3: Corriger les utilisateurs
    if fix_user_roles():
        success_steps.append("User Roles")
    else:
        print("❌ Échec de la correction des utilisateurs")
        return False
    
    # Étape 4: Déployer les fichiers statiques
    if deploy_static_files():
        success_steps.append("Static Files")
    else:
        print("❌ Échec du déploiement des fichiers statiques")
        return False
    
    # Résumé
    print("\n" + "=" * 60)
    print("📋 RÉSUMÉ DU DÉPLOIEMENT")
    print("=" * 60)
    
    for step in success_steps:
        print(f"✅ {step}")
    
    if len(success_steps) == 4:
        print("\n🎉 DÉPLOIEMENT RÉUSSI !")
        print("\n📋 Prochaines étapes:")
        print("1. 🔄 Redémarrez votre application web dans l'onglet 'Web' de PythonAnywhere")
        print("2. 🧪 Testez la connexion des utilisateurs existants")
        print("3. 🧪 Testez l'inscription de nouveaux utilisateurs")
        print("4. 🧪 Vérifiez que les images s'affichent correctement")
        print("\n💡 Le message d'avertissement peut maintenant être retiré du template main.html")
        return True
    else:
        print(f"\n⚠️  DÉPLOIEMENT PARTIEL - {len(success_steps)}/4 étapes réussies")
        return False

if __name__ == '__main__':
    success = main()
    if not success:
        sys.exit(1)
