#!/usr/bin/env python
"""
Génère des fichiers HTML lisibles à partir des JSON dans Save4Fev.
Chaque HTML affiche les infos comme project_recap.html (Job, Work Roles, KSAT, NF-COM, etc.)
Usage: python json_to_readable_html.py
"""
import os
import json
import re
from html import escape

OUTPUT_DIR = "Save4Fev"

def safe(s):
    return escape(str(s)) if s is not None else ""

def parse_state_val(v):
    """Parse une valeur du state (peut être une string JSON)."""
    if v is None or v == "":
        return None
    if isinstance(v, (dict, list)):
        return v
    try:
        return json.loads(v)
    except (json.JSONDecodeError, TypeError):
        return v

def render_job_info(state):
    job_sel = parse_state_val(state.get("currentJobSelection"))
    job_num = state.get("currentJobNumber") or (job_sel.get("poste") if isinstance(job_sel, dict) else None)
    if not job_sel and not job_num:
        return "<p class='text-gray-500 italic'>Aucune info poste</p>"
    html = "<div class='grid grid-cols-1 md:grid-cols-3 gap-4'>"
    if isinstance(job_sel, dict):
        html += f"""
        <div class='bg-indigo-50 p-4 rounded-lg border border-indigo-200'>
            <div class='text-sm font-medium text-indigo-700 mb-1'>Job Number</div>
            <div class='text-2xl font-bold text-indigo-900'>{safe(job_sel.get('poste') or job_num)}</div>
        </div>
        <div class='bg-blue-50 p-4 rounded-lg border border-blue-200'>
            <div class='text-sm font-medium text-blue-700 mb-1'>Job Name</div>
            <div class='text-xl font-semibold text-blue-900'>{safe(job_sel.get('nom', 'N/A'))}</div>
        </div>
        <div class='bg-purple-50 p-4 rounded-lg border border-purple-200'>
            <div class='text-sm font-medium text-purple-700 mb-1'>Color</div>
            <div class='text-xl font-semibold text-purple-900'>{safe(job_sel.get('couleur', 'N/A'))}</div>
        </div>
        """
    else:
        html += f"""
        <div class='bg-indigo-50 p-4 rounded-lg border border-indigo-200'>
            <div class='text-sm font-medium text-indigo-700 mb-1'>Job Number</div>
            <div class='text-2xl font-bold text-indigo-900'>{safe(job_num)}</div>
        </div>
        """
    html += "</div>"
    return html

def render_work_roles(state):
    step0 = parse_state_val(state.get("step0_baseline_data"))
    if not step0 or not isinstance(step0, dict):
        return "<p class='text-gray-500 italic'>Aucun work role sélectionné</p>"
    roles = step0.get("selectedWorkRoles") or []
    if not roles:
        return "<p class='text-gray-500 italic'>Aucun work role sélectionné</p>"
    html = "<div class='space-y-3'>"
    for r in roles:
        opm = r.get("opm_code", "")
        dcwf = r.get("dcwf_work_role", "")
        ncwf = r.get("ncwf_work_role", "")
        elem = r.get("dcwf_element", "")
        html += f"""
        <div class='bg-gray-50 p-4 rounded-lg border border-gray-200'>
            <div class='font-bold text-indigo-700'>OPM {opm}</div>
            <div class='text-gray-800'>{safe(dcwf)}</div>
            <div class='text-sm text-gray-600'>{safe(elem)}</div>
            {f"<div class='text-sm text-blue-600'>NCWF: {safe(ncwf)}</div>" if ncwf else ""}
        </div>
        """
    html += "</div>"
    return html

def render_nfcom(state):
    domains = parse_state_val(state.get("selectedNFDomains"))
    attrs = parse_state_val(state.get("nfcomAttributeSelections"))
    if not domains and not attrs:
        return "<p class='text-gray-500 italic'>Aucun domaine NF-COM sélectionné</p>"
    html = "<div class='space-y-4'>"
    if isinstance(domains, list) and domains:
        html += "<div class='flex flex-wrap gap-2 mb-2'>"
        for d in domains:
            html += f"<span class='badge bg-indigo-100 text-indigo-800'>{safe(d)}</span>"
        html += "</div>"
    if isinstance(attrs, dict) and attrs:
        html += "<div class='space-y-2'>"
        for domain, levels in attrs.items():
            if isinstance(levels, dict):
                lvls = ", ".join(f"{k}:{v}" for k, v in levels.items())
                html += f"<div class='text-sm'><strong>{safe(domain)}</strong>: {safe(lvls)}</div>"
        html += "</div>"
    html += "</div>"
    return html

def render_poste_attributes(state):
    poste = parse_state_val(state.get("posteAttributeSelections"))
    if not poste or not isinstance(poste, dict):
        return "<p class='text-gray-500 italic'>Aucun attribut poste</p>"
    html = "<div class='space-y-2'>"
    for poste_id, levels in poste.items():
        if isinstance(levels, dict):
            lvls = ", ".join(f"{k}:{v}" for k, v in levels.items())
            html += f"<div class='bg-gray-50 p-3 rounded'><strong>Poste {safe(poste_id)}</strong>: {safe(lvls)}</div>"
    html += "</div>"
    return html

CAT_LABELS = {
    "task": "Tasks (K-T)",
    "knowledge": "Knowledge (K)",
    "skill": "Skills (S)",
    "abilitie": "Abilities (A)",
}

def render_ksat_summary(state):
    ksat = parse_state_val(state.get("ksatLastSavedState"))
    if not ksat or not isinstance(ksat, dict):
        return "<p class='text-gray-500 italic'>Aucune sélection KSAT</p>"
    roles = ksat.get("roles") or []
    ksat_data = ksat.get("ksatData") or {}
    html = "<div class='space-y-6'>"
    # Work roles
    if roles:
        seen = set()
        opm_ids = []
        for r in roles:
            opm = r.get("opmId") or r.get("title", "")
            if opm and opm not in seen:
                seen.add(opm)
                opm_ids.append(opm)
        html += f"<div class='font-medium text-indigo-700'>Work Role(s): OPM {', '.join(opm_ids)}</div>"
    # Détail par catégorie
    for cat_key, cat_label in CAT_LABELS.items():
        items = ksat_data.get(cat_key) or []
        if not isinstance(items, list):
            continue
        checked_items = [x for x in items if x.get("checked")]
        if not checked_items:
            continue
        html += f"<div class='border-l-4 border-indigo-400 pl-4'>"
        html += f"<h3 class='font-bold text-gray-800 mb-2'>{cat_label} ({len(checked_items)} sélectionnés)</h3>"
        html += "<ul class='space-y-2'>"
        for i, item in enumerate(checked_items, 1):
            desc = item.get("description", "")
            kid = item.get("id", "")
            html += f"<li class='bg-gray-50 p-3 rounded'>"
            html += f"<span class='text-xs font-mono text-indigo-600'>#{kid}</span> "
            html += f"<span class='text-gray-800'>{safe(desc)}</span>"
            html += "</li>"
        html += "</ul></div>"
    html += "</div>"
    return html

def render_skill_levels(state):
    wizard = parse_state_val(state.get("wizardSummary"))
    if not wizard or not isinstance(wizard, dict):
        return "<p class='text-gray-500 italic'>Aucun niveau SFIA</p>"
    selections = wizard.get("levelSelections") or {}
    html = "<div class='space-y-3'>"
    for opm_id, skills in selections.items():
        if isinstance(skills, dict) and skills:
            sk = ", ".join(f"{c}:{l}" for c, l in skills.items())
            html += f"<div class='bg-gray-50 p-3 rounded'><strong>OPM {safe(opm_id)}</strong>: {safe(sk)}</div>"
    html += "</div>"
    return html

def render_summary_mil(state):
    competences = parse_state_val(state.get("summaryMilRoleCompetences"))
    skills = parse_state_val(state.get("summaryMilSelectedSkills"))
    html = "<div class='space-y-2'>"
    if isinstance(competences, dict) and competences:
        for opm_id, comps in competences.items():
            if isinstance(comps, list):
                cstr = ", ".join(f"{c.get('code', '')}({c.get('level', '')})" for c in comps)
                html += f"<div><strong>OPM {safe(opm_id)}</strong>: {safe(cstr)}</div>"
    if isinstance(skills, dict) and skills:
        sstr = ", ".join(f"{c}:{l}" for c, l in skills.items())
        html += f"<div><strong>Skills sélectionnés</strong>: {safe(sstr)}</div>"
    html += "</div>"
    return html

def generate_html(data, filename):
    state = data.get("state") or {}
    name = data.get("name", "Recap")
    ts = data.get("timestamp", "")

    job_html = render_job_info(state)
    work_html = render_work_roles(state)
    nfcom_html = render_nfcom(state)
    poste_html = render_poste_attributes(state)
    ksat_html = render_ksat_summary(state)
    skill_html = render_skill_levels(state)
    mil_html = render_summary_mil(state)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Recap - {safe(name)}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 p-6 font-sans">
    <div class="max-w-4xl mx-auto">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Complete Project Recap</h1>
        <p class="text-gray-600 mb-1">{safe(name)}</p>
        <p class="text-sm text-gray-500 mb-8">Exporté le {safe(ts)}</p>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">Job Position Information</h2>
            {job_html}
        </section>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">Selected Work Roles</h2>
            {work_html}
        </section>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">Selected KSAT (détail avec descriptions)</h2>
            {ksat_html}
        </section>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">NF-COM Competency Areas</h2>
            {nfcom_html}
        </section>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">Poste Attribute Levels</h2>
            {poste_html}
        </section>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">Skill Code Levels (SFIA)</h2>
            {skill_html}
        </section>

        <section class="bg-white rounded-lg shadow p-6 mb-6">
            <h2 class="text-xl font-bold text-indigo-700 mb-4">Summary MIL Competences</h2>
            {mil_html}
        </section>
    </div>
</body>
</html>"""

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base, OUTPUT_DIR)
    if not os.path.isdir(out_dir):
        print(f"Dossier {OUTPUT_DIR} introuvable.")
        return

    json_files = [f for f in os.listdir(out_dir) if f.endswith(".json")]
    count = 0
    for jf in sorted(json_files):
        path = os.path.join(out_dir, jf)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Erreur {jf}: {e}")
            continue
        html_name = jf.replace(".json", ".html")
        html_path = os.path.join(out_dir, html_name)
        html = generate_html(data, jf)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print(f"  -> {html_name}")

    print(f"\nTerminé. {count} fichier(s) HTML créé(s) dans {OUTPUT_DIR}/")
    print("Ouvrez les .html dans votre navigateur pour les lire.")

if __name__ == "__main__":
    main()
