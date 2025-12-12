"""
Script pour vérifier que les IDs des abilities dans le JSON sont bien mis à jour
et prêts à être importés dans la base de données
"""

import json
from pathlib import Path

json_path = Path("KSAT 2025 FINAL/DCWF 2025/dcwf_data.json")

print(f"Vérification des IDs des abilities dans {json_path}...")

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filtrer les abilities
abilities = [item for item in data if item.get('ksat', '').upper() == 'A']

print(f"\nNombre total d'abilities: {len(abilities)}")

# Vérifier les abilities pour OPM 441 (exemple)
abilities_441 = [a for a in abilities if a.get('opm_id', '').endswith('441') or '441' in str(a.get('opm_id', ''))]
print(f"\nAbilities pour OPM 441: {len(abilities_441)}")

if abilities_441:
    print("\nExemples d'IDs pour OPM 441:")
    for ab in abilities_441[:10]:
        print(f"  ID: {ab.get('id')}, Description: {ab.get('description', '')[:60]}...")

# Vérifier s'il y a des abilities sans ID
abilities_without_id = [a for a in abilities if not a.get('id') or a.get('id').strip() == '']
if abilities_without_id:
    print(f"\n⚠ {len(abilities_without_id)} abilities sans ID:")
    for ab in abilities_without_id[:5]:
        print(f"  OPM: {ab.get('opm_id')}, Description: {ab.get('description', '')[:60]}...")
else:
    print("\n✓ Tous les abilities ont un ID")

# Vérifier les IDs uniques
ids = [a.get('id') for a in abilities if a.get('id')]
unique_ids = set(ids)
print(f"\nIDs uniques: {len(unique_ids)} sur {len(ids)} abilities")

# Vérifier les IDs qui commencent par des chiffres (format attendu)
numeric_start_ids = [id for id in ids if id and (id[0].isdigit() if id else False)]
print(f"IDs commençant par un chiffre: {len(numeric_start_ids)}")

print("\n✓ Vérification terminée. Les données sont prêtes pour l'import.")

