"""
Construit le catalogue des compétences militières utilisées dans summary_mil
(SUMAARYMIL/military_skills_data.json) : une entrée par Skill-code (nom + catégorie).
Pas de définitions de niveau type SFIA ; les bandes L/M/H varient selon le rôle OPM.

Sortie : Step0/summary_mil_skills.json
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
MILITARY = os.path.join(ROOT, "SUMAARYMIL", "military_skills_data.json")
OUT = os.path.join(BASE, "summary_mil_skills.json")


def main():
    if not os.path.isfile(MILITARY):
        raise FileNotFoundError(MILITARY)

    with open(MILITARY, encoding="utf-8") as f:
        rows = json.load(f)

    by_code = {}
    for x in rows:
        code = (x.get("Skill-code") or "").strip()
        if not code:
            continue
        if code not in by_code:
            by_code[code] = {
                "code": code,
                "name": (x.get("Skill-name") or "").strip(),
                "category": (x.get("Skill-cat") or "").strip(),
            }

    skills = sorted(
        by_code.values(),
        key=lambda s: (s["category"].lower(), s["code"]),
    )

    payload = {
        "source": "SUMAARYMIL/military_skills_data.json — aligné summary_mil",
        "skill_count": len(skills),
        "skills": skills,
    }

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"{len(skills)} compétences -> {OUT}")


if __name__ == "__main__":
    main()
