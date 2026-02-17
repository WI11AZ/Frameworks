# -*- coding: utf-8 -*-
"""Génère TestHt_04.html à partir du JSON 04 (sans section badges)."""
import json
import os
import html

def esc(s):
    return html.escape(str(s), quote=True)

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    path_json = os.path.join(base, "04_user_1504629_2026-02-04_11-24_1504629_111_APPATECH_NEWXXX.json")
    path_html = os.path.join(base, "TestHt_04.html")

    with open(path_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    root = data
    state = data.get("state") or {}
    ksat = state.get("ksatLastSavedState") or {}
    ksat_data = ksat.get("ksatData") or {}
    step0 = state.get("step0_baseline_data") or {}
    roles = step0.get("selectedWorkRoles") or []
    primary_id = step0.get("primaryRoleOpmId") or ""
    job_sel = state.get("currentJobSelection") or {}
    job_num = state.get("currentJobNumber") or job_sel.get("poste") or ""
    nf_domains = state.get("selectedNFDomains") or []
    nf_attrs = state.get("nfcomAttributeSelections") or {}
    poste_attrs = state.get("posteAttributeSelections") or {}
    wizard = state.get("wizardSummary") or {}
    mil_comp = state.get("summaryMilRoleCompetences") or {}
    mil_skills = state.get("summaryMilSelectedSkills") or {}
    ksat_sel = state.get("currentKsatSelection")

    # Poste id pour les attributs (ex: "111")
    poste_id = job_num if isinstance(job_num, str) else str(job_num)
    poste_attr = poste_attrs.get(poste_id) or poste_attrs.get(str(poste_id)) or {}
    radar_labels = ["AUTO", "INFL", "COMP", "KNGE", "COLL", "COMM", "IMPM", "CRTY", "DECM", "DIGI", "LEAD", "LADV", "PLAN", "PROB", "ADAP", "SCPE"]
    radar_data = [poste_attr.get(k, 0) for k in radar_labels]
    radar_meta = esc(", ".join(radar_labels))

    # KSAT counts (checked only)
    tasks = [t for t in (ksat_data.get("task") or []) if t.get("checked")]
    know = [k for k in (ksat_data.get("knowledge") or []) if k.get("checked")]
    skills = [s for s in (ksat_data.get("skill") or []) if s.get("checked")]
    abils = [a for a in (ksat_data.get("abilitie") or []) if a.get("checked")]
    n_t, n_k, n_s, n_a = len(tasks), len(know), len(skills), len(abils)

    # MIL counts for primary role
    primary_comp = mil_comp.get(primary_id) or mil_comp.get(str(primary_id)) or []
    mil_high = sum(1 for c in primary_comp if c.get("level") == "HIGH")
    mil_med = sum(1 for c in primary_comp if c.get("level") == "MEDIUM")
    mil_low = sum(1 for c in primary_comp if c.get("level") == "LOW")

    # Wizard: levelSelections for primary
    opm_ids = wizard.get("opmIds") or []
    level_sel = wizard.get("levelSelections") or {}
    primary_levels = level_sel.get(primary_id) or level_sel.get(str(primary_id)) or {}
    wizard_labels = list(primary_levels.keys())
    wizard_values = [int(primary_levels.get(k, 0)) for k in wizard_labels]
    opm_avg = (wizard.get("opmAverages") or {}).get(primary_id) or (wizard.get("opmAverages") or {}).get(str(primary_id)) or 0
    if not wizard_labels:
        wizard_labels = ["—"]
        wizard_values = [0]

    # NF-COM chart: domaines et moyenne par domaine (moyenne des 4 attributs)
    nf_labels = list(nf_attrs.keys())
    nf_avg = []
    for d in nf_labels:
        v = nf_attrs.get(d) or {}
        avg = (v.get("AUTO", 0) + v.get("INFL", 0) + v.get("COMP", 0) + v.get("KNGE", 0)) / 4
        nf_avg.append(round(avg, 1))
    if not nf_labels:
        nf_labels = ["—"]
        nf_avg = [0]

    # Build KSAT JS arrays (all items for "Lire les KSAT", with checked)
    def ksat_js(arr, key_id="id", key_desc="description"):
        out = []
        for x in (ksat_data.get(arr) or []):
            out.append({
                "id": x.get(key_id, x.get("id", "")),
                "desc": x.get(key_desc, x.get("description", "")),
                "checked": x.get("checked", False)
            })
        return json.dumps(out, ensure_ascii=False)

    tasks_js = ksat_js("task")
    knowledge_js = ksat_js("knowledge")
    skills_js = ksat_js("skill")
    abilitie_js = ksat_js("abilitie")

    # Work role lines (first role as main, or list all)
    role_lines = []
    for r in roles:
        role_lines.append({
            "name": r.get("dcwf_work_role", ""),
            "opm": r.get("opm_code", ""),
            "elem": r.get("dcwf_element", ""),
            "ncwf": r.get("ncwf_work_role", ""),
            "ncwf_id": r.get("ncwf_id", ""),
            "ncwf_elem": r.get("ncwf_element", "")
        })

    # currentKsatSelection roles (if any)
    ksat_sel_roles = (ksat_sel or {}).get("roles") or []

    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Project Recap — """ + esc(root.get("name", "")) + """</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    body { font-family: system-ui, sans-serif; background: #f6f8fa; color: #1f2328; margin: 0; padding: 24px; }
    h1 { color: #0969da; font-size: 1.5rem; margin: 0 0 8px 0; }
    .meta { color: #656d76; font-size: 0.9rem; }
    .card { background: #ffffff; border: 1px solid #d0d7de; border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }
    .card h2 { color: #0969da; font-size: 1rem; margin: 0 0 12px 0; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
    ul { margin: 0; padding: 0; list-style: none; }
    ul li { padding: 8px 0; border-bottom: 1px solid #d0d7de; }
    .job { display: flex; align-items: center; gap: 12px; padding: 12px; background: #ddf4ff; border: 1px solid #b6e3ff; border-radius: 8px; }
    .job-dot { width: 14px; height: 14px; border-radius: 50%; background: #0969da; }
    .nf span { display: inline-block; padding: 6px 12px; background: #eaeef2; color: #1f2328; border-radius: 6px; margin: 4px; font-size: 0.85rem; }
    .chart-box { height: 280px; position: relative; }
    .btn { background: #2da44e; color: #fff; border: none; padding: 10px 20px; border-radius: 8px; font-size: 1rem; cursor: pointer; }
    .btn:hover { background: #2c974b; }
    #ksat-list { display: none; margin-top: 16px; max-height: 70vh; overflow: auto; }
    #ksat-list.show { display: block; }
    .ksat-block { margin-bottom: 24px; }
    .ksat-block h3 { color: #0969da; font-size: 0.95rem; margin: 0 0 8px 0; }
    .ksat-item { padding: 8px 12px; margin: 4px 0; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; font-size: 0.9rem; color: #1f2328; }
    .ksat-item .id { color: #656d76; margin-right: 8px; }
  </style>
</head>
<body>

<div class="card">
  <h1>Recap — """ + esc(root.get("name", "")) + """</h1>
  <p class="meta">id: """ + esc(root.get("id", "")) + """ · """ + esc(root.get("timestamp", "")) + """</p>
</div>

<div class="grid">
  <div class="card">
    <h2>Work role (Step0)</h2>
    <ul>
""")
    for r in role_lines:
        html_parts.append("      <li><strong>" + esc(r["name"]) + "</strong></li>\n")
        html_parts.append("      <li class=\"meta\">opm_code: " + esc(r["opm"]) + " · " + esc(r["elem"]) + "</li>\n")
        html_parts.append("      <li class=\"meta\">NCWF: " + esc(r["ncwf"]) + " (" + esc(r["ncwf_id"]) + ") · " + esc(r["ncwf_elem"]) + "</li>\n")
    html_parts.append("    </ul>\n    <p class=\"meta\">primaryRoleOpmId: " + esc(primary_id) + "</p>\n  </div>\n")
    html_parts.append("""  <div class="card">
    <h2>Poste / Job</h2>
    <div class="job">
      <span class="job-dot"></span>
      <div>
        <strong>""" + esc(job_sel.get("nom", "")) + """</strong><br>
        <span class="meta">Poste """ + esc(str(job_num)) + """ · """ + esc(job_sel.get("couleur", "")) + """</span>
      </div>
    </div>
  </div>
  <div class="card">
    <h2>NF-COM domaines</h2>
    <div class="nf">
""")
    for d in nf_domains:
        html_parts.append("      <span>" + esc(d) + "</span>")
    html_parts.append("\n    </div>\n  </div>\n</div>\n\n")

    html_parts.append("""<div class="card">
  <h2>Tous les KSAT</h2>
  <button type="button" class="btn" id="btn-ksat">Lire les KSAT</button>
  <div id="ksat-list"></div>
</div>

<div class="grid">
  <div class="card">
    <h2>KSAT sélectionnés</h2>
    <p>Tasks: <strong>""" + str(n_t) + """</strong> · Knowledge: <strong>""" + str(n_k) + """</strong> · Skills: <strong>""" + str(n_s) + """</strong> · Abilities: <strong>""" + str(n_a) + """</strong></p>
    <div class="chart-box"><canvas id="c1"></canvas></div>
  </div>
  <div class="card">
    <h2>Compétences MIL (rôle """ + esc(primary_id) + """)</h2>
    <p>HIGH: <strong>""" + str(mil_high) + """</strong> · MEDIUM: """ + str(mil_med) + """ · LOW: """ + str(mil_low) + """</p>
    <div class="chart-box"><canvas id="c2"></canvas></div>
  </div>
</div>

<div class="grid">
  <div class="card">
    <h2>Attributs poste """ + esc(poste_id) + """ (radar)</h2>
    <p class="meta">""" + radar_meta + """</p>
    <div class="chart-box"><canvas id="c3"></canvas></div>
  </div>
  <div class="card">
    <h2>NF-COM moyenne par domaine</h2>
    <p class="meta">Moyenne AUTO, INFL, COMP, KNGE par domaine</p>
    <div class="chart-box"><canvas id="c4"></canvas></div>
  </div>
</div>

<div class="card">
  <h2>Wizard rôle """ + esc(primary_id) + """ — niveaux</h2>
  <p class="meta">Niveau moyen: """ + str(opm_avg) + """</p>
  <div class="chart-box"><canvas id="c5"></canvas></div>
</div>
""")

    # Pas de section badges

    if mil_skills:
        skills_str = ", ".join(k + ": " + str(v) for k, v in mil_skills.items())
        html_parts.append("""<div class="card">
  <h2>Skills MIL sélectionnés</h2>
  <p>""" + esc(skills_str) + """</p>
</div>
""")
    else:
        html_parts.append("""<div class="card">
  <h2>Skills MIL sélectionnés</h2>
  <p class="meta">Aucun</p>
</div>
""")

    if ksat_sel_roles:
        html_parts.append("""<div class="card">
  <h2>Rôles KSAT (currentKsatSelection)</h2>
  <ul>
""")
        for r in ksat_sel_roles:
            html_parts.append("    <li><strong>" + esc(r.get("dcwf_work_role", "")) + "</strong> · " + esc(r.get("dcwf_element", "")) + " · " + esc(r.get("ncwf_work_role", "")) + " (" + esc(r.get("ncwf_id", "")) + ")</li>\n")
        html_parts.append("  </ul>\n</div>\n")
    else:
        html_parts.append("""<div class="card">
  <h2>Rôles KSAT (currentKsatSelection)</h2>
  <p class="meta">Non renseigné</p>
</div>
""")

    # Script: data + renderKsat + Charts
    html_parts.append("""
<script>
var KSAT_TASKS = """ + tasks_js + """;
var KSAT_KNOWLEDGE = """ + knowledge_js + """;
var KSAT_SKILLS = """ + skills_js + """;
var KSAT_ABILITIES = """ + abilitie_js + """;

function renderKsat() {
  var el = document.getElementById("ksat-list");
  if (el.classList.contains("show")) {
    el.classList.remove("show");
    el.innerHTML = "";
    document.getElementById("btn-ksat").textContent = "Lire les KSAT";
    return;
  }
  var html = "";
  html += "<div class=\\"ksat-block\\"><h3>Tasks (" + KSAT_TASKS.length + ")</h3>";
  KSAT_TASKS.forEach(function(t) {
    html += "<div class=\\"ksat-item\\"><span class=\\"id\\">" + t.id + "</span>" + t.desc.replace(/</g, "&lt;") + (t.checked ? " ✓" : "") + "</div>";
  });
  html += "</div>";
  html += "<div class=\\"ksat-block\\"><h3>Knowledge (" + KSAT_KNOWLEDGE.length + ")</h3>";
  KSAT_KNOWLEDGE.forEach(function(t) {
    html += "<div class=\\"ksat-item\\"><span class=\\"id\\">" + t.id + "</span>" + t.desc.replace(/</g, "&lt;") + (t.checked ? " ✓" : "") + "</div>";
  });
  html += "</div>";
  html += "<div class=\\"ksat-block\\"><h3>Skills (" + KSAT_SKILLS.length + ")</h3>";
  KSAT_SKILLS.forEach(function(t) {
    html += "<div class=\\"ksat-item\\"><span class=\\"id\\">" + t.id + "</span>" + t.desc.replace(/</g, "&lt;") + (t.checked ? " ✓" : "") + "</div>";
  });
  html += "</div>";
  html += "<div class=\\"ksat-block\\"><h3>Abilities (" + KSAT_ABILITIES.length + ")</h3>";
  KSAT_ABILITIES.forEach(function(t) {
    html += "<div class=\\"ksat-item\\"><span class=\\"id\\">" + t.id + "</span>" + t.desc.replace(/</g, "&lt;") + (t.checked ? " ✓" : "") + "</div>";
  });
  html += "</div>";
  el.innerHTML = html;
  el.classList.add("show");
  document.getElementById("btn-ksat").textContent = "Masquer les KSAT";
}
document.getElementById("btn-ksat").onclick = renderKsat;

(function(){
  new Chart(document.getElementById("c1"), {
    type: "doughnut",
    data: {
      labels: ["Tasks", "Knowledge", "Skills", "Abilities"],
      datasets: [{ data: [""" + str(n_t) + "," + str(n_k) + "," + str(n_s) + "," + str(n_a) + """], backgroundColor: ["#58a6ff", "#3fb950", "#d29922", "#a371f7"], borderWidth: 0 }]
    },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: "bottom" } } }
  });

  new Chart(document.getElementById("c2"), {
    type: "bar",
    data: {
      labels: ["HIGH", "MEDIUM", "LOW"],
      datasets: [{ data: [""" + str(mil_high) + "," + str(mil_med) + "," + str(mil_low) + """], backgroundColor: ["#3fb950", "#d29922", "#f85149"] }]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { beginAtZero: true } }, plugins: { legend: { display: false } } }
  });

  new Chart(document.getElementById("c3"), {
    type: "radar",
    data: {
      labels: """ + json.dumps(radar_labels) + """,
      datasets: [{ label: "Poste """ + poste_id + """", data: """ + json.dumps(radar_data) + """, fill: true, backgroundColor: "rgba(88,166,255,0.2)", borderColor: "#58a6ff", pointBackgroundColor: "#58a6ff" }]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { r: { min: 0, max: 7 } } }
  });

  new Chart(document.getElementById("c4"), {
    type: "bar",
    data: {
      labels: """ + json.dumps(nf_labels) + """,
      datasets: [{ label: "Moyenne", data: """ + json.dumps(nf_avg) + """, backgroundColor: "#a371f7" }]
    },
    options: { responsive: true, maintainAspectRatio: false, indexAxis: "y", scales: { x: { max: 7, beginAtZero: true } }, plugins: { legend: { display: false } } }
  });

  new Chart(document.getElementById("c5"), {
    type: "bar",
    data: {
      labels: """ + json.dumps(wizard_labels) + """,
      datasets: [{ label: "Niveau", data: """ + json.dumps(wizard_values) + """, backgroundColor: "#3fb950" }]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { max: 7, beginAtZero: true } }, plugins: { legend: { display: false } } }
  });
})();
</script>
</body>
</html>
""")

    with open(path_html, "w", encoding="utf-8") as f:
        f.write("".join(html_parts))

    print("Généré:", path_html)

if __name__ == "__main__":
    main()
