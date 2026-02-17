"""Génère dcwf_2025_opm_titles.json : tous les OPM-ID et titres DCWF 2025."""
import json
import os

base = os.path.dirname(os.path.abspath(__file__))
repo = os.path.dirname(base)
path_in = os.path.join(repo, 'dcwf_complete_79_roles.json')
path_out = os.path.join(repo, 'dcwf_2025_opm_titles.json')

with open(path_in, 'r', encoding='utf-8') as f:
    data = json.load(f)

out = [{'OPM-ID': r['omp_id'], 'title': r['title']} for r in data['work_roles']]

with open(path_out, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f'{len(out)} rôles écrits dans {path_out}')
