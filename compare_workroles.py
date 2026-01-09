#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour comparer les work roles entre t1.html et viz2_workroles_to_ecsf_REV+.html
"""

import re
import json
from pathlib import Path

def extract_opm_ids_from_t1(t1_path):
    """Extrait tous les OPM-ID (dcwf_code) de t1.html"""
    opm_ids = set()
    
    with open(t1_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher les patterns: dcwf_code: 111, dcwf_code: "TBD-A", etc.
    patterns = [
        r'dcwf_code:\s*(\d+)',  # Codes numériques
        r'dcwf_code:\s*"([^"]+)"',  # Codes avec guillemets (TBD-A, TBD-B)
        r'opm_code:\s*(\d+)',  # opm_code dans ncwf2017Data
        r'opm_code:\s*"([^"]+)"',  # opm_code avec guillemets
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            opm_ids.add(match)
    
    return sorted(opm_ids, key=lambda x: (0 if x.isdigit() else 1, x))

def extract_opm_ids_from_carl(carl_path):
    """Extrait tous les OPM-ID du fichier Carl"""
    opm_ids = set()
    
    with open(carl_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher dans le JavaScript: "OPM-ID": "111"
    pattern = r'"OPM-ID":\s*"([^"]+)"'
    matches = re.findall(pattern, content)
    for match in matches:
        opm_ids.add(match)
    
    return sorted(opm_ids, key=lambda x: (0 if x.isdigit() else 1, x))

def main():
    # Chemins des fichiers
    t1_path = Path('web_app/templates/web_app/main/t1.html')
    carl_path = Path('Carl 7 Jan 2026/viz2_workroles_to_ecsf_REV+.html')
    
    if not t1_path.exists():
        print(f"ERREUR: {t1_path} n'existe pas")
        return
    
    if not carl_path.exists():
        print(f"ERREUR: {carl_path} n'existe pas")
        return
    
    # Extraire les OPM-ID
    print("Extraction des OPM-ID de t1.html...")
    t1_opm_ids = extract_opm_ids_from_t1(t1_path)
    print(f"  -> {len(t1_opm_ids)} OPM-ID trouves dans t1.html")
    
    print("\nExtraction des OPM-ID du fichier Carl...")
    carl_opm_ids = extract_opm_ids_from_carl(carl_path)
    print(f"  -> {len(carl_opm_ids)} OPM-ID trouves dans le fichier Carl")
    
    # Convertir en sets pour la comparaison
    t1_set = set(t1_opm_ids)
    carl_set = set(carl_opm_ids)
    
    # Trouver les manquants
    missing_in_carl = sorted(t1_set - carl_set, key=lambda x: (0 if x.isdigit() else 1, x))
    extra_in_carl = sorted(carl_set - t1_set, key=lambda x: (0 if x.isdigit() else 1, x))
    
    # Afficher les résultats
    print("\n" + "="*70)
    print("RÉSULTATS DE LA COMPARAISON")
    print("="*70)
    
    print(f"\nStatistiques:")
    print(f"  - OPM-ID dans t1.html: {len(t1_opm_ids)}")
    print(f"  - OPM-ID dans fichier Carl: {len(carl_opm_ids)}")
    print(f"  - OPM-ID communs: {len(t1_set & carl_set)}")
    print(f"  - OPM-ID manquants dans Carl: {len(missing_in_carl)}")
    print(f"  - OPM-ID en plus dans Carl: {len(extra_in_carl)}")
    
    if missing_in_carl:
        print(f"\nOPM-ID MANQUANTS dans le fichier Carl ({len(missing_in_carl)}):")
        print("-" * 70)
        for opm_id in missing_in_carl:
            print(f"  - {opm_id}")
    else:
        print("\nOK: Tous les OPM-ID de t1.html sont presents dans le fichier Carl!")
    
    if extra_in_carl:
        print(f"\nOPM-ID en PLUS dans le fichier Carl ({len(extra_in_carl)}):")
        print("-" * 70)
        for opm_id in extra_in_carl:
            print(f"  - {opm_id}")
    
    # Sauvegarder dans un fichier
    output_file = Path('workroles_comparison_result.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("COMPARAISON DES WORK ROLES\n")
        f.write("="*70 + "\n\n")
        f.write(f"Fichier 1: {t1_path}\n")
        f.write(f"Fichier 2: {carl_path}\n\n")
        f.write(f"OPM-ID dans t1.html: {len(t1_opm_ids)}\n")
        f.write(f"OPM-ID dans fichier Carl: {len(carl_opm_ids)}\n")
        f.write(f"OPM-ID communs: {len(t1_set & carl_set)}\n\n")
        
        if missing_in_carl:
            f.write(f"OPM-ID MANQUANTS dans le fichier Carl ({len(missing_in_carl)}):\n")
            f.write("-" * 70 + "\n")
            for opm_id in missing_in_carl:
                f.write(f"  - {opm_id}\n")
        else:
            f.write("OK: Tous les OPM-ID de t1.html sont presents dans le fichier Carl!\n")
        
        if extra_in_carl:
            f.write(f"\nOPM-ID en PLUS dans le fichier Carl ({len(extra_in_carl)}):\n")
            f.write("-" * 70 + "\n")
            for opm_id in extra_in_carl:
                f.write(f"  - {opm_id}\n")
    
    print(f"\nResultats sauvegardes dans: {output_file}")

if __name__ == '__main__':
    main()
