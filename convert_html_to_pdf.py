#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script pour convertir le HTML en PDF en utilisant le navigateur
"""

import subprocess
import os
import sys
import webbrowser
from pathlib import Path

def convert_html_to_pdf():
    """Ouvre le fichier HTML dans le navigateur pour conversion en PDF"""
    
    html_file = "SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.html"
    pdf_file = "SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.pdf"
    
    if not os.path.exists(html_file):
        print(f"Erreur : Le fichier {html_file} n'existe pas.")
        return False
    
    # Chemin absolu du fichier HTML
    html_path = os.path.abspath(html_file)
    
    print("=" * 60)
    print("CONVERSION HTML VERS PDF")
    print("=" * 60)
    print(f"\nFichier HTML : {html_path}")
    print(f"Fichier PDF cible : {pdf_file}")
    print("\nInstructions :")
    print("1. Le fichier HTML va s'ouvrir dans votre navigateur")
    print("2. Utilisez Ctrl+P (ou Cmd+P sur Mac) pour ouvrir la boîte d'impression")
    print("3. Sélectionnez 'Enregistrer en PDF' comme destination")
    print("4. Enregistrez le fichier sous le nom : SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.pdf")
    print("\nOu utilisez un outil en ligne comme :")
    print("  - https://www.ilovepdf.com/html-to-pdf")
    print("  - https://www.freeconvert.com/html-to-pdf")
    print("\nAppuyez sur Entrée pour ouvrir le fichier HTML...")
    input()
    
    # Ouvrir le fichier HTML dans le navigateur par défaut
    try:
        webbrowser.open(f"file://{html_path}")
        print(f"\n✓ Fichier HTML ouvert dans le navigateur.")
        print(f"\nUne fois le PDF créé, il sera disponible dans le répertoire : {os.getcwd()}")
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier : {e}")
        print(f"\nVous pouvez ouvrir manuellement le fichier : {html_path}")
        return False
    
    return True

if __name__ == "__main__":
    convert_html_to_pdf()

