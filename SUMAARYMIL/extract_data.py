import pandas as pd
import json
import re

# Lire le fichier Excel, onglet Matrice_Complete
file_path = 'military_skills_relevance.xlsx'
df = pd.read_excel(file_path, sheet_name='Matrice_Complete', header=None)

# Initialiser la liste des résultats
results = []

# Extraire les OPM-ID de la ligne 1 (index 0), colonnes G à CG
# Colonne G = index 6, Colonne CG = index 84 (G=7ème colonne=index 6, CG=85ème colonne=index 84)
# En pandas, les colonnes sont indexées à partir de 0
# G = 7ème colonne = index 6
# CG = 85ème colonne = index 84

start_col = 6  # Colonne G (index 6)
end_col = 84   # Colonne CG (index 84)

# Extraire les OPM-ID de la première ligne
opm_ids = []
for col_idx in range(start_col, end_col + 1):
    cell_value = df.iloc[0, col_idx]
    if pd.notna(cell_value):
        cell_str = str(cell_value).strip()
        # Colonnes CF et CG (index 83 et 84) : 5 premiers digits
        # Sinon : 3 premiers digits
        if col_idx in [83, 84]:  # CF et CG
            # Prendre les 5 premiers digits
            digits = re.findall(r'\d+', cell_str)
            if digits:
                opm_id = digits[0][:5] if len(digits[0]) >= 5 else digits[0]
            else:
                opm_id = cell_str[:5] if len(cell_str) >= 5 else cell_str
        else:
            # Prendre les 3 premiers digits
            digits = re.findall(r'\d+', cell_str)
            if digits:
                opm_id = digits[0][:3] if len(digits[0]) >= 3 else digits[0]
            else:
                opm_id = cell_str[:3] if len(cell_str) >= 3 else cell_str
        
        if opm_id:
            opm_ids.append((col_idx, opm_id))

print(f"Nombre d'OPM-ID trouvés: {len(opm_ids)}")

# Parcourir les lignes 2 à 130 (index 1 à 129)
for row_idx in range(1, min(130, len(df))):  # Lignes 2 à 130 (index 1 à 129)
    skill_code = df.iloc[row_idx, 0]  # Colonne A (index 0)
    skill_name = df.iloc[row_idx, 1]  # Colonne B (index 1)
    skill_cat = df.iloc[row_idx, 2]   # Colonne C (index 2)
    source = df.iloc[row_idx, 4]      # Colonne E (index 4)
    
    # Vérifier si le skill_code existe
    if pd.isna(skill_code):
        continue
    
    skill_code = str(skill_code).strip()
    
    # Pour chaque OPM-ID, vérifier le niveau
    for col_idx, opm_id in opm_ids:
        skill_lvl = df.iloc[row_idx, col_idx]
        
        # Si le niveau existe et n'est pas N (none)
        if pd.notna(skill_lvl):
            skill_lvl_str = str(skill_lvl).strip().upper()
            
            # Ignorer si c'est N (none) ou vide
            if skill_lvl_str in ['L', 'M', 'H']:
                result = {
                    "OPM-ID": opm_id,
                    "Skill-code": skill_code,
                    "Skill-lvl": skill_lvl_str,
                    "Skill-name": str(skill_name).strip() if pd.notna(skill_name) else "",
                    "Skill-cat": str(skill_cat).strip() if pd.notna(skill_cat) else "",
                    "Source": str(source).strip() if pd.notna(source) else ""
                }
                results.append(result)

# Sauvegarder en JSON
output_file = 'military_skills_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Données extraites: {len(results)} entrées")
print(f"Fichier JSON créé: {output_file}")

