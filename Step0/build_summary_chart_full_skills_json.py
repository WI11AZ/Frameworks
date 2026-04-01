"""
Extrait depuis web_app/templates/web_app/main/summary_chart_full.html la constante
JavaScript `sfiaData` : toutes les compétences SFIA affichées dans la grille,
avec les niveaux SFIA 9 définis pour chacune (même liste que l’UI).

Sortie : Step0/summary_chart_full_sfia_skills.json
"""
import ast
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
HTML = os.path.join(
    ROOT,
    "web_app",
    "templates",
    "web_app",
    "main",
    "summary_chart_full.html",
)
OUT = os.path.join(BASE, "summary_chart_full_sfia_skills.json")
SFIA_SKILLS_JSON = os.path.join(ROOT, "SKILLS_SFIA", "sfia_skills.json")

SKILL_RE = re.compile(
    r'\{\s*name:\s*"((?:[^"\\]|\\.)*)",\s*code:\s*"([A-Z]{4})",\s*levels:\s*(\[[^\]]*\])\s*\}'
)
NAME_ONLY = re.compile(r'name:\s*"((?:[^"\\]|\\.)*)",\s*$')


def parse_sfia_data_block(block: str) -> list[dict]:
    skills: list[dict] = []
    current_cat = None
    current_sub = None
    for line in block.splitlines():
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if (
            stripped.startswith('name: "')
            and stripped.endswith(",")
            and "code:" not in stripped
        ):
            m = NAME_ONLY.match(stripped)
            if m:
                name_val = m.group(1)
                if indent == 12:
                    current_cat = name_val
                    current_sub = None
                elif indent == 20:
                    current_sub = name_val
        m = SKILL_RE.search(line)
        if m:
            if current_cat is None or current_sub is None:
                raise ValueError(f"Skill sans catégorie: {line.strip()}")
            name, code, levels_s = m.group(1), m.group(2), m.group(3)
            levels = ast.literal_eval(levels_s)
            skills.append(
                {
                    "category": current_cat,
                    "subcategory": current_sub,
                    "name": name,
                    "code": code,
                    "levels_defined": levels,
                }
            )
    return skills


def load_sfia_skills_by_code():
    with open(SFIA_SKILLS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    by_code = {}
    for x in data:
        c = (x.get("code") or "").strip().upper()
        if c:
            by_code[c] = x
    return by_code


def level_definitions_for(code: str, levels_defined: list, by_code: dict) -> list[dict]:
    """Textes SFIA 9 par niveau (sfia_skills.json), filtrés sur levels_defined du chart."""
    upper = code.strip().upper()
    meta = by_code.get(upper)
    if not meta and upper == "DNAN":
        meta = by_code.get("DAAN")
    if not meta:
        return []
    lvl_map = {L["level"]: L for L in (meta.get("levels") or [])}
    out = []
    for n in levels_defined:
        L = lvl_map.get(n)
        if L:
            out.append(
                {
                    "level": n,
                    "title": L.get("title") or "",
                    "definition": L.get("definition") or "",
                }
            )
    return out


def main():
    if not os.path.isfile(HTML):
        raise FileNotFoundError(HTML)

    with open(HTML, encoding="utf-8") as f:
        text = f.read()

    marker = "const sfiaData = ["
    idx = text.find(marker)
    if idx < 0:
        raise ValueError("const sfiaData introuvable dans summary_chart_full.html")

    sub = text[idx + len(marker) - 1 :]
    end = sub.find("\n    ];\n\n    document.addEventListener")
    if end < 0:
        raise ValueError("Fin de sfiaData introuvable (document.addEventListener)")

    block = sub[:end]
    skills = parse_sfia_data_block(block)

    if not os.path.isfile(SFIA_SKILLS_JSON):
        raise FileNotFoundError(SFIA_SKILLS_JSON)
    by_code = load_sfia_skills_by_code()

    for s in skills:
        s["level_definitions"] = level_definitions_for(
            s["code"], s["levels_defined"], by_code
        )

    payload = {
        "source": "summary_chart_full.html — constante sfiaData",
        "sfia_reference": "SKILLS_SFIA/sfia_skills.json (textes par niveau)",
        "skill_count": len(skills),
        "skills": skills,
    }

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"{len(skills)} compétences -> {OUT}")


if __name__ == "__main__":
    main()
