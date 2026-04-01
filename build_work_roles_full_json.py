#!/usr/bin/env python3
"""
Génère work_roles_full.json : un enregistrement par OPM-ID (DCWF/NCWF 2025 uniquement).
- T, K, S, A : comptés depuis KSAT 2025 FINAL / DCWF 2025 / dcwf_data.json (même source que compare_ksat).
- on_ramps, off_ramps, related_roles_by_tks, top_5_secondary_work_role : UNIQUEMENT depuis NCWF
  (nice_framework_final.json via ncwf_dcwf25), pas inventés si absents.
"""
import json
import os
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    # 1) Base: 79 rôles DCWF (titre, description, catégories)
    dcwf79 = load_json(os.path.join(BASE, "dcwf_complete_79_roles.json"))
    by_opm = {r["omp_id"]: r for r in dcwf79["work_roles"]}

    # 2) Mega baseline (titres NCWF/DCWF 2025, définition si dispo)
    mega_path = os.path.join(BASE, "Step0", "mega_baseline.json")
    mega = load_json(mega_path) if os.path.exists(mega_path) else []
    mega_by_opm = {str(r.get("OPM-ID") or r.get("opm_id")): r for r in mega if r.get("OPM-ID") or r.get("opm_id")}

    # 3) ncwf_dcwf25 (titres/descriptions NCWF, et mapping opm_code -> ncwf_id)
    ncwf25_path = os.path.join(BASE, "Step0", "ncwf_dcwf25.json")
    ncwf25 = load_json(ncwf25_path) if os.path.exists(ncwf25_path) else []
    ncwf25_by_opm = {}
    for entry in ncwf25:
        code = entry.get("opm_code") or entry.get("dcwf_code")
        if code is not None:
            ncwf25_by_opm[str(code)] = entry

    # 4) T, K, S, A : depuis DCWF 2025 KSAT (même source que compare_ksat)
    dcwf_data_path = os.path.join(BASE, "KSAT 2025 FINAL", "DCWF 2025", "dcwf_data.json")
    tksa_counts = defaultdict(lambda: {"T": 0, "K": 0, "S": 0, "A": 0})
    if os.path.exists(dcwf_data_path):
        dcwf_ksat = load_json(dcwf_data_path)
        for row in dcwf_ksat:
            opm = str(row.get("opm_id", ""))
            if not opm:
                continue
            k = (row.get("ksat") or "").strip().upper()
            if k.startswith("T"):
                tksa_counts[opm]["T"] += 1
            elif k.startswith("K"):
                tksa_counts[opm]["K"] += 1
            elif k.startswith("S"):
                tksa_counts[opm]["S"] += 1
            elif k.startswith("A"):
                tksa_counts[opm]["A"] += 1

    # 5) NCWF : on_ramps, off_ramps, related_roles_by_tks, top_5_secondary (uniquement si dispo)
    nice_path = os.path.join(BASE, "Step0", "nice_framework_final.json")
    nice_by_wrl_id = {}
    if os.path.exists(nice_path):
        nice_data = load_json(nice_path)
        for role in nice_data.get("work_roles", []):
            rid = role.get("id")
            if rid:
                nice_by_wrl_id[rid] = role

    out_roles = []
    for opm_id in sorted(by_opm.keys(), key=lambda x: (len(x), x)):
        r79 = by_opm[opm_id]
        mega_r = mega_by_opm.get(opm_id) or {}
        ncwf_r = ncwf25_by_opm.get(opm_id) or {}

        # Titres
        titre_dcwf = (
            mega_r.get("DCWF 2025 - Titre")
            or r79.get("title")
            or (ncwf_r.get("dcwf_role") or {}).get("work_role")
        )
        titre_ncwf = (
            mega_r.get("NCWF 2025 - Titre")
            or (ncwf_r.get("nice_role") or {}).get("work_role")
        )
        # Descriptions
        desc_dcwf = (
            mega_r.get("definition")
            or r79.get("description")
            or (ncwf_r.get("dcwf_role") or {}).get("work_role_definition")
        )
        desc_ncwf = (ncwf_r.get("nice_role") or {}).get("work_role_description")

        # T, K, S, A depuis dcwf_data.json (DCWF 2025)
        counts = tksa_counts.get(opm_id, {})
        T = counts.get("T")
        K = counts.get("K")
        S = counts.get("S")
        A = counts.get("A")

        # Catégories
        categorie_dcwf = r79.get("dcwf_community") or mega_r.get("Community DCWF")
        categorie_ncwf = r79.get("ncwf_category") or (ncwf_r.get("nice_role") or {}).get("element")

        # NCWF uniquement : on_ramps, off_ramps, related_roles_by_tks, top_5_secondary (Step0 card.ncwf)
        ncwf_id = ncwf_r.get("ncwf_id") or (r79.get("wrl_id") if r79.get("wrl_id") and str(r79.get("wrl_id")).upper() != "N/A" else None)
        nice_role = nice_by_wrl_id.get(ncwf_id) if ncwf_id else None
        if nice_role:
            common = nice_role.get("common_relationships") or {}
            on_ramps = [r.get("name") for r in common.get("on_ramps", []) if r.get("name")]
            off_ramps = [r.get("name") for r in common.get("off_ramps", []) if r.get("name")]
            related_roles_by_tks = list(common.get("related_roles_by_tks", []))
            federal = nice_role.get("federal_data") or {}
            top_5_raw = federal.get("top_5_secondary_work_roles", [])
            top_5_secondary_work_role = [{"name": r.get("name"), "percentage": r.get("percentage")} for r in top_5_raw if r.get("name")]
        else:
            on_ramps = []
            off_ramps = []
            related_roles_by_tks = []
            top_5_secondary_work_role = []

        wrl_id = r79.get("wrl_id") or mega_r.get("WRL-ID") or (ncwf_r.get("nice_role") or {}).get("work_role_id")
        out_roles.append({
            "OPM-ID": opm_id,
            "WRL-ID": wrl_id,
            "titre_dcwf": titre_dcwf,
            "titre_ncwf": titre_ncwf or None,
            "description_dcwf": desc_dcwf,
            "description_ncwf": desc_ncwf or None,
            "T": T,
            "K": K,
            "S": S,
            "A": A,
            "categorie_dcwf": categorie_dcwf,
            "categorie_ncwf": categorie_ncwf,
            "on_ramps": on_ramps,
            "off_ramps": off_ramps,
            "related_roles_by_tks": related_roles_by_tks,
            "top_5_secondary_work_role": top_5_secondary_work_role,
        })

    out_path = os.path.join(BASE, "work_roles_full.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_roles, f, indent=2, ensure_ascii=False)

    print(f"Écrit {len(out_roles)} rôles dans {out_path}")

if __name__ == "__main__":
    main()
