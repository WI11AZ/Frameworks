#!/usr/bin/env python
"""
Script de déploiement pour PythonAnywhere avec WILLAZ
"""

import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcwf.settings')
django.setup()

from django.core.management import execute_from_command_line

def deploy():
    print("🚀 Déploiement des fichiers statiques sur PythonAnywhere...")
    print("📁 Chemin de déploiement : /home/WILLAZ/Frameworks-master/staticfiles")
    
    # Exécuter collectstatic
    print("🔄 Collecte des fichiers statiques...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("✅ Déploiement terminé !")
    print("\n📋 Instructions :")
    print("1. ✅ Fichiers collectés dans /home/WILLAZ/Frameworks-master/staticfiles/")
    print("2. 🔄 Redémarrez votre application web dans l'onglet 'Web'")
    print("3. 🧪 Testez vos images sur :")
    print("   - https://willaz.pythonanywhere.com/static/photos_haute_qualite/RealBG.png")
    print("   - https://willaz.pythonanywhere.com/static/photos_haute_qualite/E1.png")
    
    print("\n⚠️  Si les images ne s'affichent toujours pas :")
    print("   Vérifiez dans l'onglet 'Web' de PythonAnywhere que le chemin statique est :")
    print("   /home/WILLAZ/Frameworks-master/staticfiles/")

if __name__ == '__main__':
    deploy()
