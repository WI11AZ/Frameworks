import pandas as pd
import re
import json


def classify_ksat_item(item):
    """Retourne la catégorie cible ('tasks','knowledge','skills','abilities')
    en se basant d'abord sur le premier mot de la description (Knowledge/Skill/Ability/Task)
    puis, en secours, sur la première lettre de l'ID (K/S/A/T) et enfin sur la
    présence de ces lettres dans l'ID si besoin.
    """
    id_ = (item.get("id") or "").strip()
    desc = (item.get("description") or "").strip()

    # Extraire le premier mot de la description (gestion des accents / mots FR/EN)
    m = re.match(r"\s*([A-Za-zÀ-ÖØ-öø-ÿ]+)", desc)
    first = m.group(1).lower() if m else ""

    # Correspondances possibles (anglais + français minimal)
    if first.startswith("knowledge") or first.startswith("connaiss"):
        return "knowledge"
    if first.startswith("skill") or first.startswith("compet"):
        return "skills"
    if first.startswith("ability") or first.startswith("capacit"):
        return "abilities"
    if first.startswith("task") or first.startswith("tache") or first.startswith("tâche"):
        return "tasks"

    # Secours: regarder la première lettre de l'ID
    if id_:
        id_up = id_.upper()
        first_char = id_up[0]
        if first_char == 'K':
            return "knowledge"
        if first_char == 'S':
            return "skills"
        if first_char == 'A':
            return "abilities"
        if first_char == 'T':
            return "tasks"

        # Si l'ID contient plusieurs lettres (ex: 'KSA'), choisir la première lettre présente
        for ch, cat in (('K', 'knowledge'), ('S', 'skills'), ('A', 'abilities'), ('T', 'tasks')):
            if ch in id_up:
                return cat

    # Dernier recours
    return "knowledge"


def extract_ncwf_role(sheet_name):
    df = pd.read_excel("NCWF2025.xlsx", sheet_name=sheet_name, header=None)

    # Nom du Work Role (premières lignes, recherche ":")
    role_name = None
    for i in range(min(10, len(df))):
        if isinstance(df.iloc[i, 1], str) and ":" in df.iloc[i, 1]:
            role_name = df.iloc[i, 1].split(":")[0].strip()
            break
    if not role_name:
        role_name = sheet_name

    # Extraire KSAT (ID + description)
    ksat_list = []
    for i in range(2, len(df)):
        if pd.notna(df.iloc[i, 0]) and pd.notna(df.iloc[i, 1]):
            ksat_list.append({
                "id": str(df.iloc[i, 0]).strip(),
                "description": str(df.iloc[i, 1]).strip()
            })

    # Trier par type en utilisant la fonction de classification
    tasks, knowledge, skills, abilities = [], [], [], []
    for k in ksat_list:
        cat = classify_ksat_item(k)
        if cat == 'knowledge':
            knowledge.append(k)
        elif cat == 'skills':
            skills.append(k)
        elif cat == 'abilities':
            abilities.append(k)
        else:
            tasks.append(k)

    return {
        "framework": "NCWF",
        "work_role_code": sheet_name,
        "name": role_name,
        "tasks": tasks,
        "knowledge": knowledge,
        "skills": skills,
        "abilities": abilities
    }


def extract_dcwf_role(sheet_name):
    df = pd.read_excel("DCWF2025.xlsx", sheet_name=sheet_name, header=None)

    # Trouver ligne contenant (CAT-ID) Nom
    role_line = None
    for i in range(min(10, len(df))):
        for j in range(min(5, df.shape[1])):
            cell = str(df.iloc[i, j])
            if re.match(r"\([A-Z]+-\d+\)", cell):
                role_line = cell
                break
        if role_line:
            break

    if role_line:
        match = re.match(r"\(([A-Z]+)-(\d+)\)\s*(.*)", role_line)
        if match:
            categorie, opm_id, role_name = match.groups()
        else:
            match = re.match(r"\(([A-Z]+)-(\d+)\)", sheet_name)
            if match:
                categorie, opm_id = match.groups()
                role_name = role_line
            else:
                categorie, opm_id, role_name = None, None, role_line
    else:
        match = re.match(r"\(([A-Z]+)-(\d+)\)", sheet_name)
        if match:
            categorie, opm_id = match.groups()
            role_name = sheet_name
        else:
            categorie, opm_id, role_name = None, None, sheet_name

    # Extraire KSAT (ID + description + core/additional si présent)
    tasks_raw = []
    for i in range(4, len(df)):
        if df.shape[1] > 2 and pd.notna(df.iloc[i, 1]) and pd.notna(df.iloc[i, 2]):
            tasks_raw.append({
                "id": str(df.iloc[i, 1]).strip(),
                "description": str(df.iloc[i, 2]).strip(),
                "core_or_additional": str(df.iloc[i, 3]).strip() if df.shape[1] > 3 and pd.notna(df.iloc[i, 3]) else None
            })

    # Trier par type en utilisant la même logique que pour NCWF
    tasks, knowledge, skills, abilities = [], [], [], []
    for t in tasks_raw:
        cat = classify_ksat_item(t)
        if cat == 'knowledge':
            knowledge.append(t)
        elif cat == 'skills':
            skills.append(t)
        elif cat == 'abilities':
            abilities.append(t)
        else:
            tasks.append(t)

    return {
        "framework": "DCWF",
        "categorie": categorie,
        "opm_id": opm_id,
        "name": role_name.strip(),
        "tasks": tasks,
        "knowledge": knowledge,
        "skills": skills,
        "abilities": abilities
    }


# Extraction globale
def extract_all():
    roles = []

    # Charger les onglets
    ncwf_sheets = pd.ExcelFile("NCWF2025.xlsx").sheet_names
    dcwf_sheets = pd.ExcelFile("DCWF2025.xlsx").sheet_names

    # NCWF
    ncwf_work_roles = [sheet for sheet in ncwf_sheets if "-WRL-" in sheet]
    for sheet in ncwf_work_roles:
        try:
            roles.append(extract_ncwf_role(sheet))
        except Exception as e:
            print(f"Erreur NCWF {sheet}: {e}")

    # DCWF
    dcwf_work_roles = [sheet for sheet in dcwf_sheets if sheet.startswith("(")]
    for sheet in dcwf_work_roles:
        try:
            roles.append(extract_dcwf_role(sheet))
        except Exception as e:
            print(f"Erreur DCWF {sheet}: {e}")

    return {"work_roles": roles}


# Main
if __name__ == "__main__":
    print("Début extraction...")
    data = extract_all()
    print(f"Extraction terminée: {len(data['work_roles'])} work roles")

    with open("work_roles.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Fichier JSON généré: work_roles.json")
