import pandas as pd
import json
import sys
import numpy as np

try:
    # Lire le fichier Excel
    df = pd.read_excel('2025-11-04__MEGA-BASELINE.xlsx')
    
    # Afficher les informations sur le DataFrame
    print(f"Nombre de lignes: {len(df)}", file=sys.stderr)
    print(f"Nombre de colonnes: {len(df.columns)}", file=sys.stderr)
    print(f"Colonnes: {list(df.columns)}", file=sys.stderr)
    
    # Remplacer les NaN par None (qui sera converti en null en JSON)
    df = df.replace({np.nan: None})
    
    # Convertir en liste de dictionnaires
    data = df.to_dict('records')
    
    # Traiter les cas dédoublés 631/632
    new_data = []
    for record in data:
        opm_id = str(record.get('OPM-ID', ''))
        
        # Si c'est "631 (632)", créer deux entrées : une pour 631 et une pour 632
        if opm_id == "631 (632)":
            # Créer l'entrée 631 avec les informations actuelles
            entry_631 = record.copy()
            entry_631['OPM-ID'] = "631"
            new_data.append(entry_631)
            
            # Créer l'entrée 632 avec les mêmes informations
            entry_632 = record.copy()
            entry_632['OPM-ID'] = "632"
            new_data.append(entry_632)
            
            print(f"Créé entrée 631: {entry_631['DCWF 2025 - Titre']}", file=sys.stderr)
            print(f"Créé entrée 632: {entry_632['DCWF 2025 - Titre']}", file=sys.stderr)
        
        # Si c'est "632 (631)", créer deux entrées : une pour 631 et une pour 632
        elif opm_id == "632 (631)":
            # Créer l'entrée 631 avec les informations actuelles
            entry_631 = record.copy()
            entry_631['OPM-ID'] = "631"
            new_data.append(entry_631)
            
            # Créer l'entrée 632 avec les mêmes informations
            entry_632 = record.copy()
            entry_632['OPM-ID'] = "632"
            new_data.append(entry_632)
            
            print(f"Créé entrée 631: {entry_631['DCWF 2025 - Titre']}", file=sys.stderr)
            print(f"Créé entrée 632: {entry_632['DCWF 2025 - Titre']}", file=sys.stderr)
        
        else:
            # Pour toutes les autres entrées, les garder telles quelles
            new_data.append(record)
    
    # Écrire dans un fichier JSON
    with open('mega_baseline.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)
    
    print(f"Fichier JSON créé avec succès! {len(new_data)} enregistrements.", file=sys.stderr)
    
except Exception as e:
    print(f"Erreur: {e}", file=sys.stderr)
    sys.exit(1)

