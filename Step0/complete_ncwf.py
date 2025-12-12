import json
import sys

def get_element_from_wrl_id(wrl_id):
    """Convertit un WRL-ID en élément NCWF"""
    if not wrl_id:
        return None
    prefix = wrl_id.split('-')[0]
    element_map = {
        'OG': 'Oversight & Governance',
        'IO': 'Implementation & Operation',
        'DD': 'Design & Development',
        'PD': 'Protection & Defense',
        'IN': 'Investigation',
        'CE': None,  # Cyber Effects - à déterminer
        'CI': 'Investigation'
    }
    return element_map.get(prefix)

def normalize_opm_id(opm_id):
    """Normalise un OPM-ID (peut être string ou int)"""
    if opm_id is None:
        return None
    if isinstance(opm_id, str):
        # Enlever les références croisées comme "631 (632)"
        if ' ' in opm_id:
            return opm_id.split()[0]
        return opm_id
    return str(opm_id)

try:
    # Lire les fichiers JSON
    print("Lecture de mega_baseline.json...", file=sys.stderr)
    with open('mega_baseline.json', 'r', encoding='utf-8') as f:
        mega_baseline = json.load(f)
    
    print("Lecture de ncwf_dcwf25.json...", file=sys.stderr)
    with open('ncwf_dcwf25.json', 'r', encoding='utf-8') as f:
        ncwf_dcwf = json.load(f)
    
    # Créer un dictionnaire de lookup par OPM-ID et WRL-ID
    mega_lookup_by_opm = {}
    mega_lookup_by_wrl = {}
    
    for entry in mega_baseline:
        opm_id = normalize_opm_id(entry.get('OPM-ID'))
        wrl_id = entry.get('WRL-ID')
        
        if opm_id:
            # Créer une entrée pour chaque OPM-ID (peut être plusieurs pour 631/632)
            if opm_id not in mega_lookup_by_opm:
                mega_lookup_by_opm[opm_id] = []
            mega_lookup_by_opm[opm_id].append(entry)
        
        if wrl_id:
            mega_lookup_by_wrl[wrl_id] = entry
    
    print(f"Créé {len(mega_lookup_by_opm)} entrées par OPM-ID", file=sys.stderr)
    print(f"Créé {len(mega_lookup_by_wrl)} entrées par WRL-ID", file=sys.stderr)
    
    # Compléter les données ncwf_dcwf
    updated_count = 0
    
    for entry in ncwf_dcwf:
        dcwf_code = entry.get('dcwf_code')
        nice_role = entry.get('nice_role')
        
        # Si nice_role est null, essayer de le compléter
        if nice_role is None:
            # Chercher par dcwf_code (qui correspond à OPM-ID)
            if dcwf_code:
                dcwf_code_str = str(dcwf_code)
                matching_entries = mega_lookup_by_opm.get(dcwf_code_str, [])
                
                if matching_entries:
                    # Prendre la première correspondance
                    mega_entry = matching_entries[0]
                    
                    wrl_id = mega_entry.get('WRL-ID')
                    ncwf_title = mega_entry.get('NCWF 2025 - Titre')
                    
                    if ncwf_title:  # Si on a au moins un titre NCWF
                        # Créer l'objet nice_role
                        element = get_element_from_wrl_id(wrl_id) if wrl_id else None
                        
                        # Si pas d'élément trouvé via WRL-ID, essayer de le déterminer à partir de la communauté DCWF
                        if not element:
                            community = mega_entry.get('Community DCWF', '')
                            # Mapping approximatif communauté -> élément NCWF
                            community_to_element = {
                                'IT': 'Implementation & Operation',
                                'CS': 'Protection & Defense',  # Par défaut
                                'EN': 'Oversight & Governance',
                                'CE': None,  # Pas dans NCWF
                                'CI': 'Investigation',
                                'DA': 'Implementation & Operation',
                                'SE': 'Design & Development'
                            }
                            element = community_to_element.get(community)
                        
                        entry['nice_role'] = {
                            'work_role': ncwf_title,
                            'work_role_description': None,  # Pas disponible dans mega_baseline
                            'work_role_id': wrl_id if wrl_id else None,
                            'link_to_tks_list': f"Click to view {wrl_id} TKS List" if wrl_id else None,
                            'element': element
                        }
                        
                        # Mettre à jour ncwf_id et opm_code
                        entry['ncwf_id'] = wrl_id if wrl_id else None
                        entry['opm_code'] = dcwf_code
                        
                        updated_count += 1
                        print(f"Mis à jour OPM-ID {dcwf_code}: {ncwf_title} ({wrl_id if wrl_id else 'WRL-ID null'})", file=sys.stderr)
    
    print(f"\nTotal d'entrées mises à jour: {updated_count}", file=sys.stderr)
    
    # Sauvegarder le fichier mis à jour
    print("Sauvegarde de ncwf_dcwf25.json...", file=sys.stderr)
    with open('ncwf_dcwf25.json', 'w', encoding='utf-8') as f:
        json.dump(ncwf_dcwf, f, indent=2, ensure_ascii=False)
    
    print("Fichier mis à jour avec succès!", file=sys.stderr)
    
except Exception as e:
    print(f"Erreur: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit(1)

