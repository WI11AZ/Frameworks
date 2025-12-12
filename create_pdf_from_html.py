#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script pour convertir le HTML en PDF en utilisant Chrome/Edge en mode headless
"""

import subprocess
import os
import sys
from pathlib import Path

def find_chrome_executable():
    """Trouve l'exécutable Chrome ou Edge"""
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\Application\msedge.exe"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None

def convert_html_to_pdf_chrome():
    """Convertit le HTML en PDF en utilisant Chrome/Edge"""
    
    html_file = "SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.html"
    pdf_file = "SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.pdf"
    
    if not os.path.exists(html_file):
        print(f"Erreur : Le fichier {html_file} n'existe pas.")
        return False
    
    # Trouver Chrome ou Edge
    chrome_path = find_chrome_executable()
    
    if not chrome_path:
        print("Chrome ou Edge non trouvé. Utilisation de la méthode manuelle...")
        print("\nInstructions pour conversion manuelle :")
        print("1. Ouvrez le fichier HTML dans votre navigateur")
        print("2. Utilisez Ctrl+P pour imprimer")
        print("3. Sélectionnez 'Enregistrer en PDF'")
        print("4. Enregistrez sous : SYNTHESE_COMPLETE_PROJET_FRAMEWORKS.pdf")
        return False
    
    # Chemin absolu des fichiers
    html_path = os.path.abspath(html_file)
    pdf_path = os.path.abspath(pdf_file)
    
    print(f"Conversion de {html_file} en {pdf_file}...")
    print(f"Utilisation de : {chrome_path}")
    
    try:
        # Commande pour convertir HTML en PDF avec Chrome/Edge
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--print-to-pdf=" + pdf_path,
            "file:///" + html_path.replace("\\", "/")
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and os.path.exists(pdf_path):
            print(f"\n✓ PDF généré avec succès : {pdf_path}")
            return True
        else:
            print(f"\n✗ Erreur lors de la conversion.")
            if result.stderr:
                print(f"Erreur : {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("✗ Timeout lors de la conversion.")
        return False
    except Exception as e:
        print(f"✗ Erreur : {e}")
        return False

if __name__ == "__main__":
    success = convert_html_to_pdf_chrome()
    if not success:
        print("\nAlternative : Ouvrez le fichier HTML dans votre navigateur et utilisez 'Imprimer' > 'Enregistrer en PDF'")

