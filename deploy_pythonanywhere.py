#!/usr/bin/env python
"""
Script de déploiement des fichiers statiques pour PythonAnywhere
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

def deploy_static_files():
    """Collecte tous les fichiers statiques dans STATIC_ROOT"""
    print("🚀 Déploiement des fichiers statiques pour PythonAnywhere...")
    
    # Créer le répertoire STATIC_ROOT s'il n'existe pas
    static_root = Path(settings.STATIC_ROOT)
    static_root.mkdir(exist_ok=True)
    
    print(f"📁 STATIC_ROOT: {static_root}")
    print(f"📁 STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    # Exécuter collectstatic
    print("🔄 Collecte des fichiers statiques...")
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
    
    # Sur PythonAnywhere, STATIC_ROOT pointe déjà vers mysite/static
    # Donc pas besoin de copier, les fichiers sont déjà au bon endroit
    print(f"\n✅ Fichiers statiques prêts dans : {static_root}")
    print("📋 Sur PythonAnywhere, STATIC_ROOT pointe directement vers mysite/static")
    
    print("\n📋 Instructions pour PythonAnywhere :")
    print("1. ✅ Script exécuté avec succès")
    print("2. 🔄 Redémarrez votre application web dans l'onglet 'Web'")
    print("3. 🧪 Testez les images sur votre site")
    
    if missing_files:
        print(f"\n⚠️  Fichiers manquants ({len(missing_files)}):")
        for file in missing_files:
            print(f"   - {file}")
        print("\n💡 Vérifiez que ces fichiers existent dans web_app/static/")
    
    return len(missing_files) == 0

if __name__ == '__main__':
    success = deploy_static_files()
    if success:
        print("\n🎉 Déploiement réussi ! Les images devraient maintenant fonctionner.")
    else:
        print("\n⚠️  Déploiement terminé avec des avertissements.")
