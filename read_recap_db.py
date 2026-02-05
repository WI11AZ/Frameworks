#!/usr/bin/env python
"""
Script pour lire le contenu des sauvegardes Project Recap dans la DB.
Usage: docker compose exec web python read_recap_db.py
       docker compose exec web python read_recap_db.py --full   # JSON complet de la dernière sauvegarde
"""
import os
import sys
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcwf.settings")
django.setup()

from web_app.models.user_saved_data import UserSavedData

recaps = UserSavedData.objects.filter(key__startswith="project_recap_").order_by("-updated_at")
count = recaps.count()
print(f"=== Nombre de sauvegardes Project Recap: {count} ===\n")

if count == 0:
    print("Aucune sauvegarde trouvée.")
    sys.exit(0)

# Mode --full : afficher le JSON complet de la dernière sauvegarde
if "--full" in sys.argv:
    r = recaps.first()
    print(f"--- Dernière sauvegarde (JSON complet) ---")
    print(f"Clé: {r.key} | User: {r.user.username} | Updated: {r.updated_at}\n")
    print(json.dumps(r.value, indent=2, ensure_ascii=False))
    sys.exit(0)

# Mode résumé par défaut
for i, r in enumerate(recaps[:5], 1):
    print(f"--- Sauvegarde {i} ---")
    print(f"  Clé: {r.key}")
    print(f"  User: {r.user.username}")
    print(f"  Updated: {r.updated_at}")
    v = r.value
    if isinstance(v, dict):
        print(f"  Keys dans value: {list(v.keys())}")
        if "state" in v:
            state = v["state"]
            print(f"  Keys dans state: {list(state.keys())}")
            for k, val in state.items():
                preview = str(val)[:80] + "..." if val and len(str(val)) > 80 else (val or "(vide)")
                print(f"    - {k}: {preview}")
    print()
