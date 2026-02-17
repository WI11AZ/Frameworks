# -*- coding: utf-8 -*-
"""Génère TestHt.html avec données 100% en dur (variables JS) et beaux graphiques."""
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE, "01_user_9800552_2026-02-04_13-55_9800552_00338243.json")
OUT_PATH = os.path.join(BASE, "TestHt.html")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

state = data.get("state") or {}
ksat = state.get("ksatLastSavedState") or {}
ksat_data = ksat.get("ksatData") or {}
step0 = state.get("step0_baseline_data") or {}
job = state.get("currentJobSelection") or {}
nf_domains = state.get("selectedNFDomains") or []
nfcom = state.get("nfcomAttributeSelections") or {}
poste = state.get("posteAttributeSelections") or {}
wizard_summary = state.get("wizardSummary") or {}
summary_mil = state.get("summaryMilRoleCompetences") or {}
summary_mil_skills = state.get("summaryMilSelectedSkills") or {}
current_ksat = state.get("currentKsatSelection") or {}
wizard_levels = state.get("wizardLevelSelections") or {}

def js_quote(s):
    return json.dumps(s, ensure_ascii=False)

# Données pour les graphiques (comptages)
tasks_checked = sum(1 for t in (ksat_data.get("task") or []) if t.get("checked"))
knowledge_checked = sum(1 for k in (ksat_data.get("knowledge") or []) if k.get("checked"))
knowledge_unchecked = sum(1 for k in (ksat_data.get("knowledge") or []) if not k.get("checked"))
skills_checked = sum(1 for s in (ksat_data.get("skill") or []) if s.get("checked"))
abilities_checked = sum(1 for a in (ksat_data.get("abilitie") or []) if a.get("checked"))

mil_high = 0
mil_medium = 0
mil_low = 0
for opm, arr in summary_mil.items():
    for c in arr or []:
        lvl = (c.get("level") or "").upper()
        if lvl == "HIGH": mil_high += 1
        elif lvl == "MEDIUM": mil_medium += 1
        else: mil_low += 1

# Rôle 802 compétences MIL (pour badges)
mil_802 = summary_mil.get("802") or []
# Wizard 802 level selections (pour radar)
wizard_802 = (wizard_summary.get("levelSelections") or {}).get("802") or {}
# Poste 305
poste_305 = (list(poste.values())[0] if poste else {}) or {}
poste_keys = list(poste_305.keys())
poste_vals = [int(poste_305.get(k, 0)) for k in poste_keys]

# NF-COM: moyenne par domaine (labels = domaines)
nfcom_labels = list(nfcom.keys())[:6]  # max 6 pour lisibilité
nfcom_avg = []
for d in nfcom_labels:
    v = nfcom[d] or {}
    avg = (int(v.get("AUTO",0)) + int(v.get("INFL",0)) + int(v.get("COMP",0)) + int(v.get("KNGE",0))) / 4
    nfcom_avg.append(round(avg, 1))

# Wizard levels: tous les OPM qui ont des sélections, avec nombre de compétences
wizard_opm_ids = [k for k, v in wizard_levels.items() if v and isinstance(v, dict)]
wizard_opm_counts = [len(wizard_levels.get(k) or {}) for k in wizard_opm_ids]

# Génération du HTML avec données en dur
html_parts = []

# 1) Données en dur (variables JS)
html_parts.append('''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Project Recap — Contenu du JSON</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0c0f14;
      --surface: #151922;
      --surface2: #1c2129;
      --border: #2a3140;
      --text: #e8ecf1;
      --muted: #7d8a9a;
      --blue: #5b9cf5;
      --green: #4ade80;
      --amber: #fbbf24;
      --red: #f87171;
      --violet: #a78bfa;
    }
    * { box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 1.5rem 2rem; line-height: 1.55; }
    .header {
      background: linear-gradient(145deg, var(--surface) 0%, #12171f 100%);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.75rem 2rem;
      margin-bottom: 1.75rem;
      box-shadow: 0 4px 24px rgba(0,0,0,0.25);
    }
    .header h1 { margin: 0 0 0.25rem; font-size: 1.85rem; font-weight: 700; color: var(--blue); }
    .header .meta { color: var(--muted); font-size: 0.95rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1.5rem; margin-bottom: 1.5rem; }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1.35rem;
      box-shadow: 0 2px 12px rgba(0,0,0,0.15);
    }
    .card h3 { margin: 0 0 1rem; font-size: 0.95rem; font-weight: 600; color: var(--blue); letter-spacing: 0.02em; }
    .chart-wrap { position: relative; height: 280px; }
    .chart-wrap.tall { height: 320px; }
    .badge { display: inline-block; padding: 0.25rem 0.6rem; border-radius: 8px; font-size: 0.75rem; font-weight: 600; margin: 0.2rem; }
    .badge-high { background: rgba(74,222,128,0.2); color: var(--green); }
    .badge-medium { background: rgba(251,191,36,0.2); color: var(--amber); }
    .badge-low { background: rgba(248,113,113,0.2); color: var(--red); }
    .job-card { display: flex; align-items: center; gap: 1rem; padding: 1rem 1.2rem; background: rgba(91,156,245,0.08); border-radius: 12px; border: 1px solid rgba(91,156,245,0.2); }
    .job-card .dot { width: 14px; height: 14px; border-radius: 50%; }
    .nf-list { display: flex; flex-wrap: wrap; gap: 0.5rem; }
    .nf-list span { padding: 0.4rem 0.8rem; background: var(--surface2); border-radius: 8px; font-size: 0.8rem; color: var(--muted); }
    ul.roles { list-style: none; padding: 0; margin: 0; }
    ul.roles li { padding: 0.55rem 0; border-bottom: 1px solid var(--border); font-size: 0.9rem; }
    ul.roles li:last-child { border-bottom: none; }
    .data-summary { font-size: 0.85rem; color: var(--muted); margin-top: 0.5rem; }
  </style>
</head>
<body>
  <div class="header">
    <h1 id="title">Recap — </h1>
    <p class="meta" id="meta"></p>
  </div>
  <script>
// ========== DONNÉES EN DUR (contenu du JSON) ==========
var RECAP_ID = ''' + js_quote(data.get("id", "")) + ''';
var RECAP_NAME = ''' + js_quote(data.get("name", "")) + ''';
var RECAP_TIMESTAMP = ''' + js_quote(data.get("timestamp", "")) + ''';

// step0_baseline_data — Work roles sélectionnés
var STEP0_WORK_ROLES = ''' + json.dumps(step0.get("selectedWorkRoles") or [], ensure_ascii=False) + ''';
var STEP0_PRIMARY_OPM = ''' + js_quote(step0.get("primaryRoleOpmId", "")) + ''';

// currentJobSelection
var JOB_NOM = ''' + js_quote(job.get("nom", "")) + ''';
var JOB_COULEUR = ''' + js_quote(job.get("couleur", "")) + ''';
var JOB_POSTE = ''' + js_quote(str(job.get("poste", ""))) + ''';

// selectedNFDomains
var NF_DOMAINS = ''' + json.dumps(nf_domains, ensure_ascii=False) + ''';

// KSAT comptages (checked)
var KSAT_TASKS_COUNT = ''' + str(tasks_checked) + ''';
var KSAT_KNOWLEDGE_COUNT = ''' + str(knowledge_checked) + ''';
var KSAT_KNOWLEDGE_UNCHECKED = ''' + str(knowledge_unchecked) + ''';
var KSAT_SKILLS_COUNT = ''' + str(skills_checked) + ''';
var KSAT_ABILITIES_COUNT = ''' + str(abilities_checked) + ''';

// summaryMilRoleCompetences (par niveau)
var MIL_HIGH = ''' + str(mil_high) + ''';
var MIL_MEDIUM = ''' + str(mil_medium) + ''';
var MIL_LOW = ''' + str(mil_low) + ''';

// Compétences MIL détaillées rôle 802
var MIL_802 = ''' + json.dumps(mil_802, ensure_ascii=False) + ''';

// summaryMilSelectedSkills
var MIL_SKILLS = ''' + json.dumps(summary_mil_skills, ensure_ascii=False) + ''';

// posteAttributeSelections (poste 305)
var POSTE_LABELS = ''' + json.dumps(poste_keys, ensure_ascii=False) + ''';
var POSTE_VALUES = ''' + json.dumps(poste_vals, ensure_ascii=False) + ''';

// nfcomAttributeSelections (moyenne par domaine)
var NFCOM_LABELS = ''' + json.dumps(nfcom_labels, ensure_ascii=False) + ''';
var NFCOM_AVG = ''' + json.dumps(nfcom_avg, ensure_ascii=False) + ''';

// wizardSummary — levelSelections pour rôle 802
var WIZARD_802_LABELS = ''' + json.dumps(list(wizard_802.keys()), ensure_ascii=False) + ''';
var WIZARD_802_VALUES = ''' + json.dumps([int(wizard_802.get(k, 0)) for k in wizard_802], ensure_ascii=False) + ''';

// wizardLevelSelections — nombre de compétences par OPM
var WIZARD_OPM_IDS = ''' + json.dumps(wizard_opm_ids[:12], ensure_ascii=False) + ''';
var WIZARD_OPM_COUNTS = ''' + json.dumps(wizard_opm_counts[:12], ensure_ascii=False) + ''';

// currentKsatSelection — rôles
var KSAT_SELECTION_ROLES = ''' + json.dumps(current_ksat.get("roles") or [], ensure_ascii=False) + ''';

// wizardSummary opmAverages
var OPM_AVERAGES_IDS = ''' + json.dumps(list((wizard_summary.get("opmAverages") or {}).keys()), ensure_ascii=False) + ''';
var OPM_AVERAGES_VALS = ''' + json.dumps(list((wizard_summary.get("opmAverages") or {}).values()), ensure_ascii=False) + ''';
  </script>
''')

# 2) Markup des cartes et canvas
html_parts.append('''
  <div class="grid">
    <div class="card">
      <h3>Work role (Step0)</h3>
      <ul class="roles" id="step0-list"></ul>
      <p class="data-summary">primaryRoleOpmId: <span id="step0-primary"></span></p>
    </div>
    <div class="card">
      <h3>Poste / Job</h3>
      <div id="job-box"></div>
    </div>
    <div class="card">
      <h3>NF-COM domaines</h3>
      <div id="nf-box" class="nf-list"></div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Répartition KSAT (sélectionnés)</h3>
      <div class="chart-wrap"><canvas id="chart-ksat"></canvas></div>
      <p class="data-summary">Tasks: ''' + str(tasks_checked) + ''' · Knowledge: ''' + str(knowledge_checked) + ''' · Skills: ''' + str(skills_checked) + ''' · Abilities: ''' + str(abilities_checked) + '''</p>
    </div>
    <div class="card">
      <h3>Compétences MIL par niveau</h3>
      <div class="chart-wrap"><canvas id="chart-mil"></canvas></div>
      <p class="data-summary">HIGH: ''' + str(mil_high) + ''' · MEDIUM: ''' + str(mil_medium) + ''' · LOW: ''' + str(mil_low) + '''</p>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Attributs poste (radar)</h3>
      <div class="chart-wrap tall"><canvas id="chart-poste"></canvas></div>
    </div>
    <div class="card">
      <h3>Moyenne NF-COM par domaine</h3>
      <div class="chart-wrap"><canvas id="chart-nfcom"></canvas></div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Wizard — compétences rôle 802 (niveaux)</h3>
      <div class="chart-wrap"><canvas id="chart-wizard802"></canvas></div>
    </div>
    <div class="card">
      <h3>Niveau moyen par OPM (wizardSummary)</h3>
      <div class="chart-wrap"><canvas id="chart-opm-avg"></canvas></div>
    </div>
    <div class="card">
      <h3>Nombre de compétences wizard par OPM</h3>
      <div class="chart-wrap tall"><canvas id="chart-wizard-counts"></canvas></div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Compétences MIL rôle 802 (badges)</h3>
      <div id="mil-badges"></div>
    </div>
    <div class="card">
      <h3>Skills MIL sélectionnés</h3>
      <div id="mil-skills-box"></div>
    </div>
  </div>

  <div class="card" style="margin-top: 1rem;">
    <h3>Rôles KSAT (currentKsatSelection)</h3>
    <ul class="roles" id="ksat-roles-list"></ul>
  </div>

  <script>
(function() {
  // Remplir header
  document.getElementById("title").textContent = "Recap — " + RECAP_NAME;
  document.getElementById("meta").textContent = RECAP_TIMESTAMP + " · id: " + RECAP_ID;

  // Step0
  var step0Html = "";
  STEP0_WORK_ROLES.forEach(function(r) {
    step0Html += "<li><strong>" + (r.dcwf_work_role || r.opm_code) + "</strong><br><span class=\"data-summary\">" + (r.dcwf_element || "") + " · " + (r.ncwf_work_role || "") + " (" + (r.ncwf_id || "") + ")</span></li>";
  });
  document.getElementById("step0-list").innerHTML = step0Html || "<li class=\"data-summary\">—</li>";
  document.getElementById("step0-primary").textContent = STEP0_PRIMARY_OPM || "—";

  // Job
  var colorHex = { BLUE: "#5b9cf5", GREEN: "#4ade80", YELLOW: "#fbbf24", RED: "#f87171" }[JOB_COULEUR] || "#7d8a9a";
  document.getElementById("job-box").innerHTML = JOB_NOM ? "<div class=\"job-card\"><span class=\"dot\" style=\"background:" + colorHex + "\"></span><div><strong>" + JOB_NOM + "</strong><br><span class=\"data-summary\">Poste " + JOB_POSTE + " · " + JOB_COULEUR + "</span></div></div>" : "<p class=\"data-summary\">—</p>";

  // NF domains
  document.getElementById("nf-box").innerHTML = NF_DOMAINS.map(function(d) { return "<span>" + d + "</span>"; }).join("") || "<span>—</span>";

  // Chart.js options communes
  var chartOptions = { responsive: true, maintainAspectRatio: false };

  // Donut KSAT
  new Chart(document.getElementById("chart-ksat"), {
    type: "doughnut",
    data: {
      labels: ["Tasks", "Knowledge", "Skills", "Abilities"],
      datasets: [{
        data: [KSAT_TASKS_COUNT, KSAT_KNOWLEDGE_COUNT, KSAT_SKILLS_COUNT, KSAT_ABILITIES_COUNT],
        backgroundColor: ["#5b9cf5", "#4ade80", "#fbbf24", "#a78bfa"],
        borderWidth: 0
      }]
    },
    options: Object.assign({}, chartOptions, { plugins: { legend: { position: "bottom" } } })
  });

  // Barres MIL
  new Chart(document.getElementById("chart-mil"), {
    type: "bar",
    data: {
      labels: ["HIGH", "MEDIUM", "LOW"],
      datasets: [{
        label: "Compétences",
        data: [MIL_HIGH, MIL_MEDIUM, MIL_LOW],
        backgroundColor: ["#4ade80", "#fbbf24", "#f87171"]
      }]
    },
    options: Object.assign({}, chartOptions, { scales: { y: { beginAtZero: true } }, plugins: { legend: { display: false } } })
  });

  // Radar poste
  new Chart(document.getElementById("chart-poste"), {
    type: "radar",
    data: {
      labels: POSTE_LABELS,
      datasets: [{
        label: "Poste",
        data: POSTE_VALUES,
        fill: true,
        backgroundColor: "rgba(91,156,245,0.2)",
        borderColor: "#5b9cf5",
        pointBackgroundColor: "#5b9cf5"
      }]
    },
    options: Object.assign({}, chartOptions, { scales: { r: { min: 0, max: 7 } } })
  });

  // Barres NF-COM moyennes
  new Chart(document.getElementById("chart-nfcom"), {
    type: "bar",
    data: {
      labels: NFCOM_LABELS,
      datasets: [{ label: "Moyenne", data: NFCOM_AVG, backgroundColor: "#a78bfa" }]
    },
    options: Object.assign({}, chartOptions, { indexAxis: "y", scales: { x: { max: 7, beginAtZero: true } }, plugins: { legend: { display: false } } })
  });

  // Wizard 802 (barres des compétences)
  new Chart(document.getElementById("chart-wizard802"), {
    type: "bar",
    data: {
      labels: WIZARD_802_LABELS,
      datasets: [{ label: "Niveau", data: WIZARD_802_VALUES, backgroundColor: "#4ade80" }]
    },
    options: Object.assign({}, chartOptions, { scales: { y: { max: 7, beginAtZero: true } }, plugins: { legend: { display: false } } })
  });

  // OPM averages
  new Chart(document.getElementById("chart-opm-avg"), {
    type: "bar",
    data: {
      labels: OPM_AVERAGES_IDS.map(function(id) { return "OPM " + id; }),
      datasets: [{ label: "Niveau moyen", data: OPM_AVERAGES_VALS, backgroundColor: "#5b9cf5" }]
    },
    options: Object.assign({}, chartOptions, { scales: { y: { max: 7, beginAtZero: true } }, plugins: { legend: { display: false } } })
  });

  // Wizard: nombre de compétences par OPM
  new Chart(document.getElementById("chart-wizard-counts"), {
    type: "bar",
    data: {
      labels: WIZARD_OPM_IDS.map(function(id) { return "OPM " + id; }),
      datasets: [{ label: "Nb compétences", data: WIZARD_OPM_COUNTS, backgroundColor: "#a78bfa" }]
    },
    options: Object.assign({}, chartOptions, { indexAxis: "y", scales: { x: { beginAtZero: true } }, plugins: { legend: { display: false } } })
  });

  // Badges MIL 802
  var badgesHtml = MIL_802.map(function(c) {
    var cls = "badge-" + (c.level || "").toLowerCase();
    return "<span class=\"badge " + cls + "\">" + (c.code || "") + " " + (c.level || "") + "</span>";
  }).join(" ");
  document.getElementById("mil-badges").innerHTML = badgesHtml || "<span class=\"data-summary\">—</span>";

  // MIL skills
  var skillsArr = Object.keys(MIL_SKILLS).map(function(k) { return k + " (" + MIL_SKILLS[k] + ")"; });
  document.getElementById("mil-skills-box").innerHTML = skillsArr.length ? "<p>" + skillsArr.join(", ") + "</p>" : "<p class=\"data-summary\">—</p>";

  // KSAT selection roles
  var rolesHtml = KSAT_SELECTION_ROLES.map(function(r) {
    return "<li><strong>" + (r.dcwf_work_role || r.opm_code) + "</strong><br><span class=\"data-summary\">" + (r.dcwf_element || "") + " · " + (r.ncwf_work_role || "") + "</span></li>";
  }).join("");
  document.getElementById("ksat-roles-list").innerHTML = rolesHtml || "<li class=\"data-summary\">—</li>";
})();
  </script>
</body>
</html>
''')

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print("OK:", OUT_PATH)
