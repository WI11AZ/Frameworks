#!/usr/bin/env python
"""
Script pour corriger les fichiers statiques (local et PythonAnywhere)
À exécuter localement ou sur PythonAnywhere
"""

import os
import sys
import shutil
from pathlib import Path

def fix_static_files():
    """Corrige la configuration des fichiers statiques"""
    
    print("🔧 Correction des fichiers statiques...")
    
    # Détection automatique de l'environnement
    if os.path.exists('/home/WILLAZ/Frameworks-master'):
        # PythonAnywhere
        project_root = Path('/home/WILLAZ/Frameworks-master')
        print("🌐 Environnement détecté: PythonAnywhere")
    else:
        # Local (Windows/Linux/Mac)
        project_root = Path(__file__).parent
        print("💻 Environnement détecté: Local")
    
    static_source = project_root / 'web_app' / 'static'
    static_dest = project_root / 'staticfiles'
    
    print(f"📁 Source: {static_source}")
    print(f"📁 Destination: {static_dest}")
    
    # Vérifier que le projet existe
    if not project_root.exists():
        print(f"❌ Erreur: Le projet n'existe pas dans {project_root}")
        return False
    
    # Vérifier que le dossier source existe
    if not static_source.exists():
        print(f"❌ Erreur: Le dossier source n'existe pas dans {static_source}")
        return False
    
    # Créer le dossier de destination
    static_dest.mkdir(exist_ok=True)
    
    # Copier tous les fichiers statiques
    print("📋 Copie des fichiers statiques...")
    try:
        if static_dest.exists():
            shutil.rmtree(static_dest)
        shutil.copytree(static_source, static_dest)
        print("✅ Fichiers statiques copiés avec succès")
    except Exception as e:
        print(f"❌ Erreur lors de la copie: {e}")
        return False
    
    # Vérifier les fichiers importants
    important_files = [
        'photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png',
        'photos_haute_qualite/CAB2.png',
        'photos_haute_qualite/bg1.png',
        'favicon.ico',
    ]
    
    print("\n🔍 Vérification des fichiers importants...")
    all_good = True
    for file_path in important_files:
        full_path = static_dest / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MANQUANT")
            all_good = False
    
    # Définir les permissions (Unix/Linux seulement)
    print("\n🔐 Configuration des permissions...")
    if os.name != 'nt':  # Pas Windows
        try:
            os.system(f"chmod -R 755 {static_dest}")
            print("✅ Permissions configurées")
        except Exception as e:
            print(f"⚠️  Erreur lors de la configuration des permissions: {e}")
    else:
        print("ℹ️  Windows détecté - permissions automatiques")
    
    if all_good:
        print("\n🎉 Configuration terminée avec succès!")
        print("📋 Prochaines étapes:")
        print("1. Redémarrez votre application web sur PythonAnywhere")
        print("2. Testez l'URL: https://willaz.pythonanywhere.com/static/photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png")
        return True
    else:
        print("\n⚠️  Certains fichiers sont manquants, mais la configuration de base est faite")
        return False

if __name__ == '__main__':
    fix_static_files()
