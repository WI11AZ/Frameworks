#!/usr/bin/env python
"""
Script de déploiement des fichiers statiques pour PythonAnywhere
À exécuter sur le serveur PythonAnywhere après chaque déploiement
"""

import os
import sys
import django
from pathlib import Path

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcwf.settings')
django.setup()

from django.conf import settings
from django.core.management import execute_from_command_line

def deploy_static_files():
    """Collecte tous les fichiers statiques dans STATIC_ROOT"""
    print("🔄 Collecte des fichiers statiques...")
    
    # Créer le répertoire STATIC_ROOT s'il n'existe pas
    static_root = Path(settings.STATIC_ROOT)
    static_root.mkdir(exist_ok=True)
    
    # Exécuter collectstatic
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print(f"✅ Fichiers statiques collectés dans : {static_root}")
    
    # Vérifier que les images importantes sont présentes
    important_files = [
        'photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png',
        'photos_haute_qualite/CAB2.png',
        'photos_haute_qualite/bg1.png',
        'favicon.ico',
        'favicon-16x16.png',
        'favicon-32x32.png',
    ]
    
    print("\n🔍 Vérification des fichiers importants...")
    for file_path in important_files:
        full_path = static_root / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MANQUANT")
    
    print("\n📋 Instructions pour PythonAnywhere :")
    print("1. Exécutez ce script sur votre serveur PythonAnywhere")
    print("2. Dans l'onglet 'Files', naviguez vers le dossier 'staticfiles'")
    print("3. Copiez tout le contenu vers votre dossier '/home/willaz/mysite/static/'")
    print("4. Redémarrez votre application web")

if __name__ == '__main__':
    deploy_static_files()
