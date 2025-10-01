#!/usr/bin/env python
"""
Script de test pour vérifier que les fichiers statiques fonctionnent en local
"""

import os
import sys
from pathlib import Path

def test_local_static():
    """Teste la configuration des fichiers statiques en local"""
    
    print("🧪 Test de la configuration des fichiers statiques en local...")
    
    # Vérifier que le dossier staticfiles existe
    staticfiles_dir = Path('staticfiles')
    if not staticfiles_dir.exists():
        print("❌ Le dossier 'staticfiles' n'existe pas")
        print("💡 Exécutez d'abord: python fix_pythonanywhere.py")
        return False
    
    # Vérifier les fichiers importants
    important_files = [
        'photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png',
        'photos_haute_qualite/CAB2.png',
        'photos_haute_qualite/bg1.png',
        'favicon.ico',
    ]
    
    print("\n🔍 Vérification des fichiers...")
    all_good = True
    for file_path in important_files:
        full_path = staticfiles_dir / file_path
        if full_path.exists():
            size = full_path.stat().st_size
            print(f"✅ {file_path} ({size} bytes)")
        else:
            print(f"❌ {file_path} - MANQUANT")
            all_good = False
    
    # Test de l'URL statique
    print("\n🌐 Test de l'URL statique...")
    print("💡 Pour tester en local, démarrez le serveur Django :")
    print("   python manage.py runserver")
    print("   Puis visitez: http://127.0.0.1:8000/static/photos_haute_qualite/Capture_d_écran_2025-09-08_151818-removebg-preview.png")
    
    if all_good:
        print("\n🎉 Configuration locale OK !")
        return True
    else:
        print("\n⚠️  Certains fichiers sont manquants")
        return False

if __name__ == '__main__':
    test_local_static()
