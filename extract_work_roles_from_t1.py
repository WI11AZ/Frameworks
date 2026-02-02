#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour extraire tous les work roles depuis t1.html
avec leur nom, OPM-ID et family header
"""

import re
import json

# Lire le fichier t1.html
with open('web_app/templates/web_app/main/t1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Charger les WRL-ID depuis dcwf_complete_79_roles.json
wrl_id_from_json = {}
try:
    with open('dcwf_complete_79_roles.json', 'r', encoding='utf-8') as f:
        dcwf_data = json.load(f)
        for role in dcwf_data.get('work_roles', []):
            opm_id = role.get('omp_id', '')
            wrl_id = role.get('wrl_id', '')
            if opm_id and wrl_id:
                wrl_id_from_json[opm_id] = wrl_id
except:
    pass

# Extraire dcwf2025Data
dcwf2025_match = re.search(r'const dcwf2025Data = \[(.*?)\];', content, re.DOTALL)
if not dcwf2025_match:
    print("Erreur: dcwf2025Data non trouvé")
    exit(1)

dcwf2025_text = dcwf2025_match.group(1)

# Parser les données dcwf2025Data
dcwf2025_roles = []
# Pattern pour extraire dcwf_code, work_role, element et wrl_id si présent
pattern = r'\{dcwf_code:\s*([^,]+),\s*work_role:\s*"([^"]+)",\s*element:\s*"([^"]+)"(?:[^}]*wrl_id:\s*"([^"]+)")?'
for match in re.finditer(pattern, dcwf2025_text):
    code = match.group(1).strip().strip('"')
    work_role = match.group(2)
    element = match.group(3)
    wrl_id = match.group(4) if match.group(4) else None
    
    # Extraire le code de famille depuis element
    family_match = re.search(r'\(([A-Z]{2})\)', element)
    family = family_match.group(1) if family_match else ''
    
    dcwf2025_roles.append({
        'code': code,
        'work_role': work_role,
        'element': element,
        'family': family,
        'wrl_id': wrl_id
    })

# Extraire ncwf2025Data pour les rôles manquants dans dcwf2025Data
ncwf2025_match = re.search(r'const ncwf2025Data = \[(.*?)\];', content, re.DOTALL)
ncwf2025_roles = []
if ncwf2025_match:
    ncwf2025_text = ncwf2025_match.group(1)
    # Pattern pour extraire work_role, work_role_id, opm_code, element
    pattern = r'\{work_role:\s*"([^"]+)",[^}]*work_role_id:\s*"([^"]+)",[^}]*opm_code:\s*([^,}]+),\s*element:\s*"([^"]+)"'
    for match in re.finditer(pattern, ncwf2025_text):
        work_role = match.group(1)
        wrl_id = match.group(2)
        opm_code = match.group(3).strip().strip('"')
        element = match.group(4)
        
        # Mapping NCWF vers DCWF
        ncwf_to_dcwf = {
            'PD': 'CS',
            'IO': 'IT',
            'OG': 'EN',
            'DD': 'IT',
            'IN': 'EN',
            'CI': 'CI',
            'CE': 'CE'
        }
        
        element_match = re.search(r'\(([A-Z]+)\)', element)
        if element_match:
            ncwf_category = element_match.group(1)
            family = ncwf_to_dcwf.get(ncwf_category, 'IT')
        else:
            family = 'IT'
        
        # Vérifier si ce code existe déjà dans dcwf2025_roles
        if not any(r['code'] == opm_code for r in dcwf2025_roles):
            ncwf2025_roles.append({
                'code': opm_code,
                'work_role': work_role,
                'element': element,
                'family': family,
                'wrl_id': wrl_id
            })

# Créer un mapping des WRL-ID depuis ncwf2025Data
wrl_id_map = {}
for role in ncwf2025_roles:
    code = role['code']
    if role.get('wrl_id'):
        wrl_id_map[code] = role['wrl_id']

# Enrichir les rôles dcwf2025Data avec les WRL-ID depuis ncwf2025Data et dcwf_complete_79_roles.json
for role in dcwf2025_roles:
    code = role['code']
    # D'abord essayer depuis ncwf2025Data
    if not role.get('wrl_id') and code in wrl_id_map:
        role['wrl_id'] = wrl_id_map[code]
    # Sinon depuis dcwf_complete_79_roles.json
    elif not role.get('wrl_id') and code in wrl_id_from_json:
        role['wrl_id'] = wrl_id_from_json[code]

# Combiner les deux listes
all_roles = dcwf2025_roles + ncwf2025_roles

# Créer un dictionnaire par code pour éviter les doublons
roles_dict = {}
for role in all_roles:
    code = role['code']
    if code not in roles_dict:
        roles_dict[code] = role
    # Si existe déjà, préférer dcwf2025 mais garder le wrl_id si disponible
    elif role in dcwf2025_roles:
        # Si le nouveau rôle a un wrl_id et l'ancien non, mettre à jour
        if role.get('wrl_id') and not roles_dict[code].get('wrl_id'):
            roles_dict[code]['wrl_id'] = role['wrl_id']
        roles_dict[code] = role
    # Si le rôle existant n'a pas de wrl_id et le nouveau en a un, l'ajouter
    elif role.get('wrl_id') and not roles_dict[code].get('wrl_id'):
        roles_dict[code]['wrl_id'] = role['wrl_id']
    # Enrichir avec wrl_id_from_json si manquant
    if not roles_dict[code].get('wrl_id') and code in wrl_id_from_json:
        roles_dict[code]['wrl_id'] = wrl_id_from_json[code]

# Organiser par famille
family_order = ['IT', 'CS', 'EN', 'CE', 'CI', 'DA', 'SE', 'CX']
family_names = {
    'IT': 'Information Technology (IT)',
    'CS': 'Cybersecurity (CS)',
    'EN': 'Cyber Enablers (EN)',
    'CE': 'Cyber Effects (CE)',
    'CI': 'Intel (Cyber) (CI)',
    'DA': 'Data/AI (DA)',
    'SE': 'Software Engineering (SE)',
    'CX': 'Not in any DCWF Community / Workforce Element (CX)'
}

# Grouper par famille
roles_by_family = {fam: [] for fam in family_order}
for code, role in roles_dict.items():
    family = role['family']
    if family in roles_by_family:
        roles_by_family[family].append(role)
    else:
        roles_by_family['CX'].append(role)

# Trier chaque famille par code
for family in roles_by_family:
    roles_by_family[family].sort(key=lambda x: (
        1 if isinstance(x['code'], str) and x['code'].startswith('TBD') else 0,
        int(x['code']) if x['code'].isdigit() else float('inf') if not x['code'].startswith('TBD') else 999,
        x['code']
    ))

# Afficher les résultats
print("=" * 80)
print("LISTE DES 79 WORK ROLES DCWF PAR COMMUNAUTÉ")
print("=" * 80)
print()

total = 0
for family_code in family_order:
    roles = roles_by_family[family_code]
    if not roles:
        continue
    
    family_name = family_names[family_code]
    print(f"\n### {family_name} ({len(roles)} rôles)")
    print("-" * 80)
    
    for idx, role in enumerate(roles, 1):
        code = role['code']
        work_role = role['work_role']
        wrl_id = role.get('wrl_id', 'N/A')
        print(f"{total + idx}. {work_role} ({code}) - WRL-ID: {wrl_id}")
    
    total += len(roles)

print()
print("=" * 80)
print(f"TOTAL : {total} work roles")
print("=" * 80)

# Exporter en JSON
output = {
    'work_roles': [],
    'by_family': {}
}

for family_code in family_order:
    roles = roles_by_family[family_code]
    if not roles:
        continue
    
    family_name = family_names[family_code]
    output['by_family'][family_code] = {
        'name': family_name,
        'count': len(roles),
        'roles': []
    }
    
    for role in roles:
        role_data = {
            'opm_id': role['code'],
            'work_role': role['work_role'],
            'wrl_id': role.get('wrl_id', 'N/A'),
            'family': family_code,
            'family_name': family_name,
            'element': role['element']
        }
        output['work_roles'].append(role_data)
        output['by_family'][family_code]['roles'].append(role_data)

# Sauvegarder en JSON
with open('work_roles_extracted_from_t1.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\nDonnees exportees dans work_roles_extracted_from_t1.json")
