#!/usr/bin/env python
"""Convertit le premier JSON 01_user_*.json en CSV (une ligne, colonnes aplaties)."""
import json
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE, "01_user_9800552_2026-02-04_13-55_9800552_00338243.json")
csv_path = os.path.join(BASE, "01_user_9800552_2026-02-04_13-55_9800552_00338243.csv")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Aplatir: champs racine + chaque clé de state en colonne
row = {}
for k, v in data.items():
    if k == "state":
        for sk, sv in (v or {}).items():
            row["state_" + sk] = sv if sv is None or isinstance(sv, str) else json.dumps(sv, ensure_ascii=False)
    else:
        row[k] = v if v is None or isinstance(v, (str, int, float, bool)) else json.dumps(v, ensure_ascii=False)

headers = list(row.keys())
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    w.writerow(headers)
    w.writerow([row[h] for h in headers])

print(f"CSV écrit: {csv_path}")
