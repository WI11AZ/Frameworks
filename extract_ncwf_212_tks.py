"""Extrait les TKS du rôle 212 NCWF (PD-WRL-002) dans un fichier JSON."""
import json

with open('KSAT 2025 FINAL/NCWF 2025/nice_framework_2.1.0.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

tks_212 = [item for item in data if item.get('WRL-ID') == 'PD-WRL-002']

output = {
    'work_role': {
        'wrl_id': 'PD-WRL-002',
        'opm_id': '212',
        'title': 'Digital Forensics'
    },
    'tks_count': {
        'tasks': len([x for x in tks_212 if x.get('KSAT') == 'T']),
        'knowledge': len([x for x in tks_212 if x.get('KSAT') == 'K']),
        'skills': len([x for x in tks_212 if x.get('KSAT') == 'S'])
    },
    'tks': tks_212
}

with open('KSAT 2025 FINAL/NCWF 2025/ncwf_212_TKS.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f'Extrait {len(tks_212)} TKS pour PD-WRL-002 (212)')
print(f'  Tasks: {output["tks_count"]["tasks"]}')
print(f'  Knowledge: {output["tks_count"]["knowledge"]}')
print(f'  Skills: {output["tks_count"]["skills"]}')
