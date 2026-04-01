"""
Génère work_roles_ncwf_dcwf_by_opm.json à partir de mega_baseline.json
(OPM-ID, titres NCWF/DCWF) enrichi avec :
- sfia_skills_summary_chart : Primaires / Secondaires depuis FORSAPINNOEL/output_merged (++).json
  (noms SFIA 9 depuis SKILLS_SFIA/sfia_skills.json quand le code existe)
- military_skills_summary_mil : entrées depuis SUMAARYMIL/military_skills_data.json
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
SRC = os.path.join(BASE, "mega_baseline.json")
OUT = os.path.join(BASE, "work_roles_ncwf_dcwf_by_opm.json")
OUTPUT_MERGED = os.path.join(ROOT, "FORSAPINNOEL", "output_merged (++).json")
MILITARY = os.path.join(ROOT, "SUMAARYMIL", "military_skills_data.json")
SFIA_SKILLS = os.path.join(ROOT, "SKILLS_SFIA", "sfia_skills.json")


def load_sfia_name_map():
    with open(SFIA_SKILLS, encoding="utf-8") as f:
        data = json.load(f)
    m = {}
    for x in data:
        code = (x.get("code") or "").strip().upper()
        if not code:
            continue
        m[code] = (x.get("name") or "").strip()
    return m


def normalize_chart_skill(entry, name_map):
    if isinstance(entry, str):
        c = entry.strip().upper()
        return {"code": c, "sfia_name": name_map.get(c)}
    code = (entry.get("code") or "").strip().upper()
    out = {"code": code, "sfia_name": name_map.get(code)}
    for k in ("levels", "domain"):
        if k in entry:
            out[k] = entry[k]
    return out


def chart_block_for_opm(row, name_map):
    if not row:
        return {"primary": [], "secondary": []}
    prim = row.get("Primaires") or []
    sec = row.get("Secondaires") or []
    return {
        "primary": [normalize_chart_skill(x, name_map) for x in prim],
        "secondary": [normalize_chart_skill(x, name_map) for x in sec],
    }


def military_list_for_opm(rows):
    seen = set()
    out = []
    for x in rows:
        code = x.get("Skill-code") or ""
        lvl = x.get("Skill-lvl") or ""
        key = (code, lvl)
        if key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "code": code,
                "level_band": lvl,
                "name": (x.get("Skill-name") or "").strip(),
                "category": (x.get("Skill-cat") or "").strip(),
            }
        )
    out.sort(key=lambda r: (r["level_band"], r["code"]))
    return out


def main():
    for path in (SRC, OUTPUT_MERGED, MILITARY, SFIA_SKILLS):
        if not os.path.isfile(path):
            raise FileNotFoundError(path)

    with open(SRC, encoding="utf-8") as f:
        baseline = json.load(f)
    with open(OUTPUT_MERGED, encoding="utf-8") as f:
        output_rows = json.load(f)
    with open(MILITARY, encoding="utf-8") as f:
        military_rows = json.load(f)

    chart_by_opm = {str(x["OPM_ID"]).strip(): x for x in output_rows}
    military_by_opm = {}
    for x in military_rows:
        oid = str(x.get("OPM-ID", "")).strip()
        if not oid:
            continue
        military_by_opm.setdefault(oid, []).append(x)

    name_map = load_sfia_name_map()

    rows = []
    for x in baseline:
        opm = str(x.get("OPM-ID", "")).strip()
        if not opm:
            continue
        chart_row = chart_by_opm.get(opm)
        rows.append(
            {
                "opm_id": opm,
                "ncwf_title": (x.get("NCWF 2025 - Titre") or "").strip(),
                "dcwf_title": (x.get("DCWF 2025 - Titre") or "").strip(),
                "sfia_skills_summary_chart": chart_block_for_opm(chart_row, name_map),
                "military_skills_summary_mil": military_list_for_opm(
                    military_by_opm.get(opm, [])
                ),
            }
        )

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"{len(rows)} lignes écrites -> {OUT}")


if __name__ == "__main__":
    main()
