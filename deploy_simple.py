#!/usr/bin/env python
"""
Script simple pour déployer les fichiers statiques sur PythonAnywhere
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
    
    # Exécuter collectstatic
    print("🔄 Collecte des fichiers statiques...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("✅ Déploiement terminé !")
    print("🔄 Redémarrez votre application web dans l'onglet 'Web' de PythonAnywhere")
    print("🧪 Testez vos images sur : https://willaz.pythonanywhere.com/static/photos_haute_qualite/RealBG.png")

if __name__ == '__main__':
    deploy()
