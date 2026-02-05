#!/usr/bin/env python
"""
Exporte toutes les sauvegardes Project Recap de la DB vers des fichiers JSON
dans le dossier Save4Fev (un fichier par sauvegarde).
Usage: docker compose exec web python export_recaps_to_files.py
"""
import os
import json
import re
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcwf.settings")
django.setup()

from web_app.models.user_saved_data import UserSavedData

OUTPUT_DIR = "Save4Fev"

def safe_filename(s):
    """Remplacer les caractères interdits dans les noms de fichiers."""
    return re.sub(r'[<>:"/\\|?*]', '_', str(s))[:80]

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base, OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)

    recaps = UserSavedData.objects.filter(key__startswith="project_recap_").order_by("-updated_at")
    count = recaps.count()

    print(f"Export de {count} sauvegarde(s) Project Recap vers {OUTPUT_DIR}/")

    for i, r in enumerate(recaps, 1):
        username = r.user.username
        ts = r.updated_at.strftime("%Y-%m-%d_%H-%M") if r.updated_at else "unknown"
        name = safe_filename(r.value.get("name", "recap")) if isinstance(r.value, dict) else "recap"
        filename = f"{i:02d}_{username}_{ts}_{name}.json"
        filepath = os.path.join(out_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(r.value, f, indent=2, ensure_ascii=False)

        print(f"  -> {filename}")

    print(f"\nTerminé. {count} fichier(s) dans {out_dir}")

if __name__ == "__main__":
    main()
