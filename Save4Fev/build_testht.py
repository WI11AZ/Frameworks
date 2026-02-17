# -*- coding: utf-8 -*-
"""Génère TestHt.html à partir du JSON recap (données en dur + graphiques)."""
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE, "01_user_9800552_2026-02-04_13-55_9800552_00338243.json")
OUT_PATH = os.path.join(BASE, "TestHt.html")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    json_str = f.read()

# Échapper pour inclusion dans <script type="application/json">
json_escaped = json_str.replace("</", "<\\/")

html = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Project Recap — Visualisation</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0f1419;
      --card: #1a2332;
      --border: #2d3a4f;
      --text: #e6edf3;
      --muted: #8b9cb3;
      --accent: #58a6ff;
      --green: #3fb950;
      --amber: #d29922;
      --red: #f85149;
    }
    * { box-sizing: border-box; }
    body {
      font-family: 'DM Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 1.5rem;
      line-height: 1.5;
    }
    h1 { font-size: 1.75rem; margin: 0 0 0.5rem; color: var(--accent); }
    h2 { font-size: 1.15rem; margin: 0 0 1rem; color: var(--muted); font-weight: 600; }
    .header {
      background: linear-gradient(135deg, var(--card) 0%, #162238 100%);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem 2rem;
      margin-bottom: 1.5rem;
    }
    .header .meta { color: var(--muted); font-size: 0.9rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-bottom: 1.5rem; }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
      overflow: hidden;
    }
    .card h3 { margin: 0 0 1rem; font-size: 1rem; color: var(--accent); }
    .chart-wrap { position: relative; height: 260px; }
    .chart-wrap.wide { height: 300px; }
    .badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.8rem; margin: 0.15rem; }
    .badge-high { background: rgba(63,185,80,0.25); color: var(--green); }
    .badge-medium { background: rgba(210,153,34,0.25); color: var(--amber); }
    .badge-low { background: rgba(248,81,73,0.2); color: var(--red); }
    ul.roles { list-style: none; padding: 0; margin: 0; }
    ul.roles li { padding: 0.5rem 0; border-bottom: 1px solid var(--border); }
    ul.roles li:last-child { border-bottom: none; }
    .job-card { display: flex; align-items: center; gap: 1rem; padding: 1rem; background: rgba(88,166,255,0.08); border-radius: 8px; }
    .job-card .couleur { width: 12px; height: 12px; border-radius: 50%; }
    .nf-list { display: flex; flex-wrap: wrap; gap: 0.5rem; }
    .nf-list span { padding: 0.35rem 0.75rem; background: var(--border); border-radius: 6px; font-size: 0.85rem; }
    table.attrs { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    table.attrs th, table.attrs td { padding: 0.4rem 0.6rem; text-align: left; border-bottom: 1px solid var(--border); }
    table.attrs th { color: var(--muted); font-weight: 600; }
  </style>
</head>
<body>
  <div class="header">
    <h1 id="recap-title">Project Recap</h1>
    <p class="meta" id="recap-meta">—</p>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Work role (Step0)</h3>
      <div id="step0-roles"></div>
    </div>
    <div class="card">
      <h3>Poste / Job</h3>
      <div id="job-selection"></div>
    </div>
    <div class="card">
      <h3>NF-COM domaines sélectionnés</h3>
      <div id="nf-domains" class="nf-list"></div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Répartition KSAT (Tasks, Knowledge, Skills, Abilities)</h3>
      <div class="chart-wrap"><canvas id="chart-ksat"></canvas></div>
    </div>
    <div class="card">
      <h3>Compétences MIL par niveau (rôle principal)</h3>
      <div class="chart-wrap"><canvas id="chart-mil"></canvas></div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Attributs poste (radar)</h3>
      <div class="chart-wrap wide"><canvas id="chart-poste"></canvas></div>
    </div>
    <div class="card">
      <h3>Moyenne NF-COM (AUTO, INFL, COMP, KNGE)</h3>
      <div class="chart-wrap"><canvas id="chart-nfcom"></canvas></div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>Wizard — niveau moyen par rôle (OPM)</h3>
      <div class="chart-wrap wide"><canvas id="chart-wizard"></canvas></div>
    </div>
    <div class="card">
      <h3>Skills MIL sélectionnés</h3>
      <div id="mil-skills"></div>
    </div>
  </div>

  <div class="card" style="margin-top: 1rem;">
    <h3>Rôles KSAT (sélection Step0)</h3>
    <div id="ksat-roles"></div>
  </div>

  <script type="application/json" id="recap-data">''' + json_escaped + '''</script>
  <script>
(function() {
  const raw = document.getElementById("recap-data").textContent;
  const data = JSON.parse(raw);
  const state = data.state || {};
  const ksat = state.ksatLastSavedState || {};
  const ksatData = ksat.ksatData || {};
  const step0 = state.step0_baseline_data || {};
  const job = state.currentJobSelection || {};
  const nfDomains = state.selectedNFDomains || [];
  const nfcomAttrs = state.nfcomAttributeSelections || {};
  const posteAttrs = state.posteAttributeSelections || {};
  const wizardSummary = state.wizardSummary || {};
  const summaryMil = state.summaryMilRoleCompetences || {};
  const summaryMilSkills = state.summaryMilSelectedSkills || {};
  const currentKsat = state.currentKsatSelection || {};
  const wizardLevels = state.wizardLevelSelections || {};

  // Header
  document.getElementById("recap-title").textContent = "Recap — " + (data.name || data.id || "Project Recap");
  document.getElementById("recap-meta").textContent = data.timestamp || "";

  // Step0 roles
  const rolesHtml = (step0.selectedWorkRoles || []).map(function(r) {
    return "<li><strong>" + (r.dcwf_work_role || r.opm_code) + "</strong><br><span class=\"meta\">" + (r.dcwf_element || "") + " · " + (r.ncwf_work_role || "") + " (" + (r.ncwf_id || "") + ")</span></li>";
  }).join("");
  document.getElementById("step0-roles").innerHTML = rolesHtml ? "<ul class=\"roles\">" + rolesHtml + "</ul>" : "<p class=\"meta\">—</p>";

  // Job
  const jobColor = (job.couleur || "").toLowerCase();
  const colorHex = { blue: "#58a6ff", green: "#3fb950", yellow: "#d29922", red: "#f85149" }[jobColor] || "#8b9cb3";
  document.getElementById("job-selection").innerHTML = job.nom ? "<div class=\"job-card\"><span class=\"couleur\" style=\"background:" + colorHex + "\"></span><div><strong>" + job.nom + "</strong><br>Poste " + (job.poste || state.currentJobNumber || "") + "</div></div>" : "<p class=\"meta\">—</p>";

  // NF domains
  document.getElementById("nf-domains").innerHTML = nfDomains.map(function(d) { return "<span>" + d + "</span>"; }).join("") || "<span class=\"meta\">—</span>";

  // KSAT counts → pie
  const taskCount = (ksatData.task || []).filter(function(t) { return t.checked; }).length;
  const knowCount = (ksatData.knowledge || []).filter(function(k) { return k.checked; }).length;
  const skillCount = (ksatData.skill || []).filter(function(s) { return s.checked; }).length;
  const abilCount = (ksatData.abilitie || []).filter(function(a) { return a.checked; }).length;
  const ksatLabels = ["Tasks", "Knowledge", "Skills", "Abilities"];
  const ksatValues = [taskCount, knowCount, skillCount, abilCount];
  const ksatColors = ["#58a6ff", "#3fb950", "#d29922", "#a371f7"];

  new Chart(document.getElementById("chart-ksat"), {
    type: "doughnut",
    data: {
      labels: ksatLabels,
      datasets: [{ data: ksatValues, backgroundColor: ksatColors, borderWidth: 0 }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { position: "bottom" } }
    }
  });

  // MIL competences by level → bar
  let milByLevel = { HIGH: 0, MEDIUM: 0, LOW: 0 };
  Object.keys(summaryMil).forEach(function(opm) {
    (summaryMil[opm] || []).forEach(function(c) {
      const l = (c.level || "").toUpperCase();
      if (milByLevel[l] !== undefined) milByLevel[l]++;
    });
  });
  new Chart(document.getElementById("chart-mil"), {
    type: "bar",
    data: {
      labels: ["HIGH", "MEDIUM", "LOW"],
      datasets: [{
        label: "Compétences",
        data: [milByLevel.HIGH, milByLevel.MEDIUM, milByLevel.LOW],
        backgroundColor: ["#3fb950", "#d29922", "#f85149"]
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: { y: { beginAtZero: true } },
      plugins: { legend: { display: false } }
    }
  });

  // Poste attributes → radar (first poste key)
  const posteKey = Object.keys(posteAttrs)[0];
  const posteV = posteAttrs[posteKey] || {};
  const posteLabels = Object.keys(posteV);
  const posteValues = posteLabels.map(function(k) { return Number(posteV[k]) || 0; });
  new Chart(document.getElementById("chart-poste"), {
    type: "radar",
    data: {
      labels: posteLabels,
      datasets: [{ label: "Poste " + (posteKey || ""), data: posteValues, fill: true, backgroundColor: "rgba(88,166,255,0.2)", borderColor: "#58a6ff", pointBackgroundColor: "#58a6ff" }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: { r: { min: 0, max: 7 } }
    }
  });

  // NF-COM average (first domain)
  const nfKey = Object.keys(nfcomAttrs)[0];
  const nfV = nfcomAttrs[nfKey] || {};
  const nfLabels = Object.keys(nfV);
  const nfValues = nfLabels.map(function(k) { return Number(nfV[k]) || 0; });
  new Chart(document.getElementById("chart-nfcom"), {
    type: "bar",
    data: {
      labels: nfLabels,
      datasets: [{ label: nfKey || "NF-COM", data: nfValues, backgroundColor: "#a371f7" }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      indexAxis: "y",
      scales: { x: { max: 7, beginAtZero: true } },
      plugins: { legend: { display: false } }
    }
  });

  // Wizard averages (opmAverages)
  const opmAverages = wizardSummary.opmAverages || {};
  const opmIds = Object.keys(opmAverages);
  const opmVals = opmIds.map(function(id) { return opmAverages[id] || 0; });
  new Chart(document.getElementById("chart-wizard"), {
    type: "bar",
    data: {
      labels: opmIds.map(function(id) { return "OPM " + id; }),
      datasets: [{ label: "Niveau moyen", data: opmVals, backgroundColor: "#3fb950" }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: { y: { max: 7, beginAtZero: true } },
      plugins: { legend: { display: false } }
    }
  });

  // MIL selected skills (object key → value)
  const milSkillsArr = Object.keys(summaryMilSkills || {}).map(function(k) { return k + " (" + summaryMilSkills[k] + ")"; });
  document.getElementById("mil-skills").innerHTML = milSkillsArr.length ? "<p>" + milSkillsArr.join(", ") + "</p>" : "<p class=\"meta\">—</p>";

  // Current KSAT selection roles
  const ksatRoles = (currentKsat.roles || []).map(function(r) {
    return "<li><strong>" + (r.dcwf_work_role || r.opm_code) + "</strong> — " + (r.dcwf_element || "") + "</li>";
  }).join("");
  document.getElementById("ksat-roles").innerHTML = ksatRoles ? "<ul class=\"roles\">" + ksatRoles + "</ul>" : "<p class=\"meta\">—</p>";
})();
  </script>
</body>
</html>
'''

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("OK: " + OUT_PATH)
