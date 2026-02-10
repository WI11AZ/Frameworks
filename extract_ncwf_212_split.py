"""Extrait les TASKS et KS du rôle 212 NCWF dans des fichiers séparés."""
import json

with open('KSAT 2025 FINAL/NCWF 2025/ncwf_212_TKS.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

work_role = data['work_role']
tks = data['tks']

tasks = [x for x in tks if x.get('KSAT') == 'T']
ks = [x for x in tks if x.get('KSAT') in ('K', 'S')]
knowledge = [x for x in ks if x.get('KSAT') == 'K']
skills = [x for x in ks if x.get('KSAT') == 'S']

# JSON Tasks uniquement
tasks_file = {
    'work_role': work_role,
    'count': len(tasks),
    'tasks': tasks
}
with open('KSAT 2025 FINAL/NCWF 2025/ncwf_212_TASKS.json', 'w', encoding='utf-8') as f:
    json.dump(tasks_file, f, indent=2, ensure_ascii=False)

# JSON Knowledge + Skills
ks_file = {
    'work_role': work_role,
    'count': {'knowledge': len(knowledge), 'skills': len(skills)},
    'knowledge': knowledge,
    'skills': skills
}
with open('KSAT 2025 FINAL/NCWF 2025/ncwf_212_KS.json', 'w', encoding='utf-8') as f:
    json.dump(ks_file, f, indent=2, ensure_ascii=False)

print('Fichiers créés:')
print(f'  ncwf_212_TASKS.json: {len(tasks)} tasks')
print(f'  ncwf_212_KS.json: {len(knowledge)} knowledge + {len(skills)} skills')
