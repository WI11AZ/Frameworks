# -*- coding: utf-8 -*-
"""
Améliore le JSON 04 pour qu'il suive la même structure que le template JSON 01 :
- Dé-sérialise les champs de state qui sont des chaînes JSON en vrais objets/tableaux.
- Aligne les types et clés manquantes sur le template 01.
"""
import json
import os

# Clés de state qui doivent être des objets ou tableaux (pas des chaînes)
STATE_JSON_KEYS = (
    "ksatLastSavedState",
    "step0_baseline_data",
    "currentJobSelection",
    "selectedNFDomains",
    "nfcomAttributeSelections",
    "posteAttributeSelections",
    "wizardLevelSelections",
    "wizardSummary",
    "summaryMilRoleCompetences",
)

def try_parse_json(value):
    if not isinstance(value, str):
        return value
    s = value.strip()
    if not s or (s[0] not in ("{", "[")):
        return value
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value

def improve_state(state):
    if not state:
        return state
    out = {}
    for k, v in state.items():
        if k in STATE_JSON_KEYS:
            out[k] = try_parse_json(v)
        else:
            out[k] = v
    # Aligner sur template 01 : null -> valeur par défaut si besoin
    if out.get("summaryMilSelectedSkills") is None:
        out["summaryMilSelectedSkills"] = {}
    # currentKsatSelection peut rester null
    return out

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    path_04 = os.path.join(base, "04_user_1504629_2026-02-04_11-24_1504629_111_APPATECH_NEWXXX.json")
    with open(path_04, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "state" in data:
        data["state"] = improve_state(data["state"])

    # Réécrire en JSON (format compact comme le 01 d'origine, ou indent=2 pour lisibilité)
    with open(path_04, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("JSON 04 mis à jour:", path_04)

if __name__ == "__main__":
    main()
