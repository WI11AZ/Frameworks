#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Améliore la lisibilité d'un JSON Project Recap :
- Parse les chaînes JSON imbriquées dans state (ksatLastSavedState, step0_baseline_data, etc.)
- Formate avec indentation (sans supprimer aucune donnée)
"""
import json
import os
import sys

def try_parse_json(val):
    """Si val est une chaîne JSON valide, retourne l'objet parsé ; sinon val inchangé."""
    if isinstance(val, str) and val.strip():
        s = val.strip()
        if (s.startswith('{') and s.endswith('}')) or (s.startswith('[') and s.endswith(']')):
            try:
                return json.loads(val)
            except (json.JSONDecodeError, TypeError):
                pass
    return val

def deep_pretty(obj, max_depth=10, depth=0):
    """Parse récursivement les chaînes JSON dans les dict/list (limite la profondeur)."""
    if depth > max_depth:
        return obj
    if isinstance(obj, dict):
        return {k: deep_pretty(try_parse_json(v), max_depth, depth + 1) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deep_pretty(try_parse_json(item), max_depth, depth + 1) for item in obj]
    return obj

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    filename = "01_user_9800552_2026-02-04_13-55_9800552_00338243.json"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    path = os.path.join(base, filename)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Parser les chaînes JSON dans state et formater
    data = deep_pretty(data)

    out_path = path  # écraser le fichier
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"JSON mis à jour (lisible) : {out_path}")

if __name__ == "__main__":
    main()
