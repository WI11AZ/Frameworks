#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur HTML complet pour visualiser les données NCWF & DCWF 2025
"""

import json

# Lire les deux fichiers JSON
with open('ncwf_dcwf25.json', 'r', encoding='utf-8') as f:
    ncwf_dcwf_data = json.load(f)

with open('nice_framework_final.json', 'r', encoding='utf-8') as f:
    nice_data = json.load(f)

# Créer un dictionnaire pour accès rapide aux données NICE par ID
nice_lookup = {role['id']: role for role in nice_data['work_roles']}

# Générer les données JavaScript
js_roles = []

for mapping in ncwf_dcwf_data:
    dcwf_role = mapping.get('dcwf_role') or {}
    ncwf_id = mapping.get('ncwf_id')
    nice_role_meta = mapping.get('nice_role')

    # Bloc DCWF toujours présent
    dcwf_block = {
        'work_role': dcwf_role.get('work_role'),
        'code': dcwf_role.get('dcwf_code'),
        'element': (dcwf_role.get('element') or '').replace('\n', ' ').strip(),
        'definition': dcwf_role.get('work_role_definition')
    }

    role_data = {
        'ncwf_id': ncwf_id,
        'opm_code': dcwf_role.get('dcwf_code'),  # OPM-ID = dcwf_code
        'dcwf': dcwf_block,
        'nice': None
    }

    # Attacher NICE si disponible dans nice_framework_final.json
    if ncwf_id and ncwf_id in nice_lookup:
        nice_info = nice_lookup[ncwf_id]
        role_data['nice'] = {
            'work_role': (nice_role_meta or {}).get('work_role', nice_info.get('name')),
            'id': (nice_role_meta or {}).get('work_role_id', ncwf_id),
            'description': (nice_role_meta or {}).get('work_role_description', ''),
            'element': (nice_role_meta or {}).get('element', ''),
            'related_roles_tks': nice_info['common_relationships'].get('related_roles_by_tks', []),
            'on_ramps': [r['name'] for r in nice_info['common_relationships'].get('on_ramps', [])],
            'off_ramps': [r['name'] for r in nice_info['common_relationships'].get('off_ramps', [])],
            'top_5_secondary': nice_info.get('federal_data', {}).get('top_5_secondary_work_roles', [])
        }

    js_roles.append(role_data)

# Créer des lookups depuis nice_framework_final.json
nice_name_to_opm = {}
nice_name_to_wrl = {}
for role in nice_data['work_roles']:
    role_name = role.get('name', '').strip()
    role_number = role.get('number')
    role_id = role.get('id')
    if role_name and role_number:
        nice_name_to_opm[role_name] = role_number
    if role_name and role_id:
        nice_name_to_wrl[role_name] = role_id

# Générer le contenu JavaScript avec échappement approprié
def escape_js_string(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

js_data = "const allRolesData = " + json.dumps(js_roles, indent=2, ensure_ascii=False) + ";\n\n"
js_data += "const niceNameToOpmLookup = " + json.dumps(nice_name_to_opm, indent=2, ensure_ascii=False) + ";\n\n"
js_data += "const niceNameToWrlLookup = " + json.dumps(nice_name_to_wrl, indent=2, ensure_ascii=False) + ";"

# Générer le fichier HTML complet
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCWF & DCWF 2025 - Référentiel Complet des Rôles Cybersécurité</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }
        
        .main-container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        
        .selector-section {
            background: white;
            padding: 18px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        
        .selector-section h2 {
            font-size: 20px;
            color: #333;
            margin-bottom: 15px;
        }
        
        .selector-group {
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .selector-group label {
            font-size: 14px;
            font-weight: 600;
            color: #555;
        }
        
        .selector-group select, .selector-group input {
            flex: 1;
            min-width: 300px;
            padding: 12px;
            font-size: 14px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            background: white;
            cursor: pointer;
            transition: border-color 0.3s;
        }
        
        .selector-group select:hover, .selector-group input:focus {
            border-color: #0078d4;
        }
        
        .selector-group select:focus, .selector-group input:focus {
            outline: none;
            border-color: #0078d4;
        }
        
        .filter-group {
            display: flex;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
        }
        
        .filter-btn {
            padding: 8px 16px;
            border: 2px solid #e0e0e0;
            background: white;
            border-radius: 20px;
            cursor: pointer;
            font-size: 13px;
            transition: all 0.3s;
        }
        
        .filter-btn:hover {
            border-color: #0078d4;
            background: #e8f4fd;
        }
        
        .filter-btn.active {
            border-color: #0078d4;
            background: #0078d4;
            color: white;
        }
        
        /* Grille des rôles */
        .grid-section { margin-bottom: 28px; }
        .grid-title { font-weight: 800; color: #111827; margin-bottom: 10px; font-size: 18px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; }
        .tile {
            background: white;
            border: 1px solid #eaeaea;
            border-radius: 10px;
            padding: 16px;
            cursor: pointer;
            transition: box-shadow .2s, transform .2s;
        }
        .tile:hover { box-shadow: 0 8px 20px rgba(0,0,0,.12); transform: translateY(-2px); }
        .tile-title { font-weight: 700; color: #1f2937; font-size: 15px; margin-bottom: 6px; }
        .tile-sub { font-size: 12px; color: #6b7280; margin-bottom: 8px; }
        .chip { display:inline-block; font-size: 11px; font-weight:700; padding:4px 8px; border-radius: 999px; color:#fff; margin-right:6px; margin-bottom:4px; }
        /* Couleurs éléments DCWF */
        .el-it { background:#0ea5e9; }
        .el-cs { background:#10b981; }
        .el-en { background:#8b5cf6; }
        .el-ce { background:#8b5a2b; }
        .el-ci { background:#f59e0b; }
        .el-da { background:#14b8a6; }
        .el-se { background:#ef4444; }
        .tile.el-it, .tile.el-cs, .tile.el-en, .tile.el-ce, .tile.el-ci, .tile.el-da, .tile.el-se { color:#fff; border-color:transparent; }
        .tile.el-it .tile-title, .tile.el-cs .tile-title, .tile.el-en .tile-title, .tile.el-ce .tile-title, .tile.el-ci .tile-title, .tile.el-da .tile-title, .tile.el-se .tile-title { color:#fff; }
        /* Contours pour chips de même couleur que tuile */
        .chip.el-it { border: 1.5px solid #0369a1; }
        .chip.el-cs { border: 1.5px solid #047857; }
        .chip.el-en { border: 1.5px solid #6d28d9; }
        .chip.el-ce { border: 1.5px solid #6b4423; }
        .chip.el-ci { border: 1.5px solid #c2410c; }
        .chip.el-da { border: 1.5px solid #0f766e; }
        .chip.el-se { border: 1.5px solid #b91c1c; }
        /* Couleurs chips NICE (catégories) */
        .chip-og { background:#0ea5e9; }
        .chip-in { background:#8b5cf6; }
        .chip-dd { background:#ef4444; }
        .chip-pd { background:#ec4899; }
        .chip-io { background:#14b8a6; }
        
        /* Amélioration lisibilité pour tuiles sans couleur (TBD) */
        .tile:not(.el-it):not(.el-cs):not(.el-en):not(.el-ce):not(.el-ci):not(.el-da):not(.el-se) {
            border: 2px solid #d1d5db;
            background: #f9fafb;
        }
        .tile:not(.el-it):not(.el-cs):not(.el-en):not(.el-ce):not(.el-ci):not(.el-da):not(.el-se) .tile-title {
            color: #111827;
            font-size: 16px;
        }
        .tile:not(.el-it):not(.el-cs):not(.el-en):not(.el-ce):not(.el-ci):not(.el-da):not(.el-se) .tile-sub {
            color: #374151;
            font-weight: 600;
        }
        .tile:not(.el-it):not(.el-cs):not(.el-en):not(.el-ce):not(.el-ci):not(.el-da):not(.el-se) .chip {
            background: #6b7280;
            color: white;
        }
        
        .card {
            background: white;
            border-radius: 8px;
            padding: 30px;
            min-width: 380px;
            max-width: 380px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            position: relative;
            border-left: 5px solid;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }
        
        .card.dcwf {
            border-left-color: #0078d4;
        }
        
        .card.ncwf {
            border-left-color: #00a99d;
        }
        
        .framework-label {
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .dcwf .framework-label {
            color: #0078d4;
        }
        
        .ncwf .framework-label {
            color: #00a99d;
        }
        
        .role-title {
            font-size: 22px;
            font-weight: 700;
            color: #333;
            margin-bottom: 20px;
            line-height: 1.4;
        }
        
        .ids {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .id-item {
            font-size: 14px;
            padding: 8px 12px;
            border-radius: 6px;
            font-weight: 600;
        }
        
        .wrl-id {
            background: #e8f4fd;
            color: #0078d4;
        }
        
        .opm-id {
            background: #e1f5f3;
            color: #00a99d;
        }
        
        
        .description {
            font-size: 15px;
            color: #555;
            line-height: 1.7;
            margin-bottom: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 6px;
            max-height: 150px;
            overflow-y: auto;
        }
        
        .element-badge {
            display: inline-block;
            padding: 10px 16px;
            border-radius: 25px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .badge-it { background: #0078d4; color: white; }
        .badge-cs { background: #7c3aed; color: white; }
        .badge-en { background: #059669; color: white; }
        .badge-ce { background: #dc2626; color: white; }
        .badge-ci { background: #ea580c; color: white; }
        .badge-da { background: #8b5cf6; color: white; }
        .badge-se { background: #0891b2; color: white; }
        .badge-cx { background: #64748b; color: white; }
        .badge-og { background: #00a99d; color: white; }
        .badge-io { background: #10b981; color: white; }
        .badge-dd { background: #3b82f6; color: white; }
        .badge-pd { background: #ef4444; color: white; }
        .badge-in { background: #f59e0b; color: white; }
        
        .section {
            margin-top: 25px;
            padding-top: 25px;
            border-top: 2px solid #e0e0e0;
        }
        
        .section-title {
            font-size: 14px;
            font-weight: 800;
            color: #333;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }
        
        .list-container {
            max-height: 300px;
            overflow-y: auto;
        }
        
        .list-item {
            font-size: 14px;
            color: #666;
            padding: 10px;
            border-bottom: 1px solid #f0f0f0;
            transition: background 0.2s;
        }
        
        .list-item:hover {
            background: #f9f9f9;
        }
        
        .list-item:last-child {
            border-bottom: none;
        }
        
        .list-item-with-percentage {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
        }
        
        .percentage {
            font-weight: 700;
            color: #0078d4;
            font-size: 13px;
            background: #e8f4fd;
            padding: 4px 10px;
            border-radius: 12px;
            flex-shrink: 0;
        }
        
        .arrow {
            color: #00a99d;
            font-size: 36px;
            display: flex;
            align-items: center;
            padding: 0 15px;
            font-weight: bold;
        }

        /* Modal centrée */
        .modal-backdrop { position: fixed; inset: 0; background: rgba(0,0,0,.45); display:none; }
        .modal { position: fixed; top:50%; left:50%; transform: translate(-50%, -50%) scale(.98); width: min(1100px, 96vw); max-height: 90vh; background:#fff; border-radius:12px; box-shadow:0 20px 60px rgba(0,0,0,.2); opacity:0; pointer-events:none; transition: .2s ease; overflow:auto; }
        .modal.open { opacity:1; transform: translate(-50%, -50%) scale(1); pointer-events:auto; }
        .modal-header { position: sticky; top:0; background:#fff; padding:14px 18px; border-bottom:1px solid #eee; display:flex; justify-content:space-between; align-items:center; }
        .close-btn { border:none; background:#f3f4f6; border-radius:8px; padding:6px 10px; cursor:pointer; }
        
        .no-data-message {
            color: #999;
            font-style: italic;
            padding: 10px;
        }
        
        .stats-box {
            background: linear-gradient(135deg, #e8f4fd, #f0f9ff);
            padding: 15px;
            border-radius: 6px;
            margin-top: 20px;
            border-left: 4px solid #0078d4;
        }
        
        .stats-title {
            font-size: 13px;
            font-weight: 700;
            color: #0078d4;
            margin-bottom: 10px;
        }
        
        .stats-content {
            font-size: 14px;
            color: #555;
        }
        
        .search-box {
            padding: 12px;
            font-size: 14px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            width: 100%;
            margin-top: 15px;
        }
        
        .roles-list {
            background: white;
            max-height: 400px;
            overflow-y: auto;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            margin-top: 10px;
            display: none;
        }
        
        .roles-list.active {
            display: block;
        }
        
        .role-item {
            padding: 12px 15px;
            border-bottom: 1px solid #f0f0f0;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .role-item:hover {
            background: #f9f9f9;
        }
        
        .role-item:last-child {
            border-bottom: none;
        }
        
        .role-item-title {
            font-weight: 600;
            color: #333;
            margin-bottom: 5px;
        }
        
        .role-item-meta {
            font-size: 12px;
            color: #666;
        }
        
        .opm-badge {
            display: inline-block;
            background-color: #0ea5e9;
            color: #000;
            padding: 4px 10px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 12px;
            margin-right: 8px;
            white-space: nowrap;
        }
        
        .wrl-badge {
            display: inline-block;
            border: 2px solid #0ea5e9;
            color: #0ea5e9;
            background: transparent;
            padding: 3px 9px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 12px;
            margin-left: 8px;
            white-space: nowrap;
        }
        
        .list-item {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 4px;
        }
        
        .list-item-with-percentage {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="selector-section">
            <h2>📋 Sélectionner un rôle</h2>
            <div class="selector-group">
                <label for="roleSelector">Choisir un rôle :</label>
                <select id="roleSelector" onchange="displayRole()">
                    <option value="">-- Sélectionnez un rôle --</option>
                </select>
            </div>
            
            <input type="text" id="searchBox" class="search-box" placeholder="🔍 Rechercher un rôle par nom, ID OPM, ou WRL ID..." oninput="searchRoles()">
            
            <div id="rolesList" class="roles-list"></div>
            
            <div class="filter-group">
                <button class="filter-btn active" onclick="filterByElement('all')">Tous</button>
                <button class="filter-btn" onclick="filterByElement('Implementation & Operation')">Implementation & Operation</button>
                <button class="filter-btn" onclick="filterByElement('Oversight & Governance')">Oversight & Governance</button>
                <button class="filter-btn" onclick="filterByElement('Design & Development')">Design & Development</button>
                <button class="filter-btn" onclick="filterByElement('Protection & Defense')">Protection & Defense</button>
                <button class="filter-btn" onclick="filterByElement('Investigation')">Investigation</button>
            </div>
        </div>
        
        <div id="contentArea"></div>

        <!-- Modal de détails -->
        <div id="modalBackdrop" class="modal-backdrop" onclick="closeModal()"></div>
        <div id="detailsModal" class="modal" aria-hidden="true">
            <div class="modal-header">
                <div id="modalTitle" style="font-weight:800;color:#111827;"></div>
                <button class="close-btn" onclick="closeModal()">Fermer</button>
            </div>
            <div id="modalBody" style="padding:18px 20px 30px 20px;"></div>
        </div>
    </div>

    <script>
        """ + js_data + """

        let currentFilter = 'all';
        
        function getElementBadgeClass(element) {
            const normalized = element.replace(/\\s+/g, ' ').trim();
            const map = {
                'Information Technology (IT)': 'badge-it',
                'Information Technology  (IT)': 'badge-it',
                'Cybersecurity (CS)': 'badge-cs',
                'Cyber Enablers (EN)': 'badge-en',
                'Cyber Effects (CE)': 'badge-ce',
                'Intel (Cyber) (CI)': 'badge-ci',
                'Data/AI (DA)': 'badge-da',
                'Software Engineering (SE)': 'badge-se',
                'Sans Communauté (CX)': 'badge-cx',
                'Oversight & Governance': 'badge-og',
                'Implementation & Operation': 'badge-io',
                'Design & Development': 'badge-dd',
                'Protection & Defense': 'badge-pd',
                'Protection and Defense': 'badge-pd',
                'Investigation': 'badge-in'
            };
            return map[normalized] || 'badge-it';
        }

        function populateSelector() {
            const selector = document.getElementById('roleSelector');
            allRolesData.forEach((role, index) => {
                const option = document.createElement('option');
                option.value = index;
                const niceName = role.nice ? role.nice.work_role : role.dcwf.work_role;
                const opmDisplay = role.opm_code !== null ? role.opm_code : '—';
                option.text = `${niceName} (OPM-ID: ${opmDisplay})`;
                selector.appendChild(option);
            });
        }

        function searchRoles() {
            const searchTerm = document.getElementById('searchBox').value.toLowerCase();
            const rolesList = document.getElementById('rolesList');
            
            if (searchTerm.length < 2) {
                rolesList.classList.remove('active');
                return;
            }
            
            const filtered = allRolesData.filter((role, index) => {
                const niceName = (role.nice?.work_role || '').toLowerCase();
                const dcwfName = (role.dcwf?.work_role || '').toLowerCase();
                const opmCode = String(role.opm_code).toLowerCase();
                const wrlId = (role.nice?.id || '').toLowerCase();
                
                return niceName.includes(searchTerm) || 
                       dcwfName.includes(searchTerm) || 
                       opmCode.includes(searchTerm) ||
                       wrlId.includes(searchTerm);
            }).map((role, originalIndex) => ({role, originalIndex: allRolesData.indexOf(role)}));
            
            if (filtered.length > 0) {
                rolesList.innerHTML = filtered.map(({role, originalIndex}) => `
                    <div class="role-item" onclick="selectRoleFromSearch(${originalIndex})">
                        <div class="role-item-title">${role.nice?.work_role || role.dcwf.work_role}</div>
                        <div class="role-item-meta">
                            OPM-ID: ${role.opm_code !== null ? role.opm_code : '—'} | 
                            ${role.nice ? 'WRL-ID: ' + role.nice.id : 'Pas de correspondance NCWF'} | 
                            ${role.nice ? role.nice.element : role.dcwf.element}
                        </div>
                    </div>
                `).join('');
                rolesList.classList.add('active');
            } else {
                rolesList.innerHTML = '<div class="no-data-message">Aucun rôle trouvé</div>';
                rolesList.classList.add('active');
            }
        }

        function selectRoleFromSearch(index) {
            document.getElementById('roleSelector').value = index;
            document.getElementById('rolesList').classList.remove('active');
            document.getElementById('searchBox').value = '';
            displayRole();
        }

        function filterByElement(element) {
            currentFilter = element;
            
            // Update button states
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // Filter dropdown
            const selector = document.getElementById('roleSelector');
            selector.innerHTML = '<option value="">-- Sélectionnez un rôle --</option>';
            
            allRolesData.forEach((role, index) => {
                if (element === 'all' || role.nice?.element === element) {
                    const option = document.createElement('option');
                    option.value = index;
                    const niceName = role.nice ? role.nice.work_role : role.dcwf.work_role;
                    const opmDisplay = role.opm_code !== null ? role.opm_code : '—';
                    option.text = `${niceName} (OPM-ID: ${opmDisplay})`;
                    selector.appendChild(option);
                }
            });
        }

        function dcwfKey(role){
            const code = role.opm_code;
            if (code === 'TBD-A' || code === 'TBD-B') return 'tbd';
            const s = (role.dcwf.element || '').replace(/\\n/g,' ').toLowerCase();
            if (s.includes('information technology')) return 'it';
            if (s.includes('cybersecurity') && !s.includes('enablers')) return 'cs';
            if (s.includes('cyber enablers')) return 'en';
            if (s.includes('cyber effects')) return 'ce';
            if (s.includes('intel')) return 'ci';
            if (s.includes('data/ai')) return 'da';
            if (s.includes('software engineering')) return 'se';
            return 'tbd';
        }

        function sectionTitleForKey(k){
            return {it:'Information Technology (IT)', cs:'Cybersecurity (CS)', en:'Cyber Enablers (EN)', ce:'Cyber Effects (CE)', ci:'Intel (Cyber) (CI)', da:'Data/AI (DA)', se:'Software Engineering (SE)', tbd:'Autres / TBD'}[k];
        }

        function tileClassForKey(k){
            return {it:'el-it', cs:'el-cs', en:'el-en', ce:'el-ce', ci:'el-ci', da:'el-da', se:'el-se'}[k] || '';
        }

        function chipClassForNice(element){
            const s = (element||'').toLowerCase();
            if (s.includes('oversight')) return 'chip-og';
            if (s.includes('investigation')) return 'chip-in';
            if (s.includes('design') || s.includes('development')) return 'chip-dd';
            if (s.includes('protection')) return 'chip-pd';
            if (s.includes('implementation') || s.includes('operation')) return 'chip-io';
            return '';
        }

        function renderAllRoles() {
            const container = document.getElementById('contentArea');
            const order = ['it','cs','en','ce','ci','da','se','tbd'];
            const groups = { it:[], cs:[], en:[], ce:[], ci:[], da:[], se:[], tbd:[] };
            allRolesData.forEach((role, idx) => { groups[dcwfKey(role)].push({role, idx}); });
            let html = '';
            order.forEach(k => {
                if (groups[k].length === 0) return;
                const tiles = groups[k].sort((a,b)=> (a.role.nice?.work_role||a.role.dcwf.work_role).localeCompare(b.role.nice?.work_role||b.role.dcwf.work_role)).map(({role, idx}) => `
                    <div class="tile ${tileClassForKey(k)}" onclick="openModal(${idx})" title="Voir les détails">
                        <div class="tile-title">${role.nice?.work_role || role.dcwf.work_role}</div>
                        <div class="tile-sub">OPM-ID: ${role.opm_code !== null ? role.opm_code : '—'} ${role.nice ? ' • WRL-ID: ' + role.nice.id : ''}</div>
                        <div>
                            <span class="chip ${tileClassForKey(k)}">${(role.dcwf.element||'').replace(/\\n/g,' ') || '—'}</span>
                            ${role.nice ? `<span class=\"chip ${chipClassForNice(role.nice.element)}\">${role.nice.element}</span>` : ''}
                        </div>
                    </div>
                `).join('');
                html += `<div class=\"grid-section\"><div class=\"grid-title\">${sectionTitleForKey(k)}</div><div class=\"grid\">${tiles}</div></div>`;
            });
            container.innerHTML = html;
        }

        function findOpmIdByRoleName(roleName) {
            // D'abord chercher dans le lookup NICE complet
            if (niceNameToOpmLookup[roleName]) {
                return niceNameToOpmLookup[roleName];
            }
            
            // Sinon chercher dans allRolesData (fallback)
            const role = allRolesData.find(r => 
                (r.nice && r.nice.work_role === roleName) || 
                (r.dcwf && r.dcwf.work_role === roleName)
            );
            return role && role.opm_code !== null ? role.opm_code : null;
        }

        function getElementFromWrlId(wrlId) {
            if (!wrlId) return '';
            const prefix = wrlId.split('-')[0];
            const elementMap = {
                'OG': 'Oversight & Governance',
                'IO': 'Implementation & Operation',
                'DD': 'Design & Development',
                'PD': 'Protection & Defense',
                'IN': 'Investigation'
            };
            return elementMap[prefix] || '';
        }

        function getElementColorForOpmId(element) {
            const normalized = element.replace(/\\s+/g, ' ').trim();
            const colorMap = {
                'Information Technology (IT)': '#0ea5e9',
                'Information Technology  (IT)': '#0ea5e9',
                'Cybersecurity (CS)': '#10b981',
                'Cyber Enablers (EN)': '#8b5cf6',
                'Cyber Effects (CE)': '#8b5a2b',
                'Intel (Cyber) (CI)': '#f59e0b',
                'Data/AI (DA)': '#14b8a6',
                'Software Engineering (SE)': '#ef4444',
                'Oversight & Governance': '#00a99d',
                'Implementation & Operation': '#14b8a6',
                'Design & Development': '#ef4444',
                'Protection & Defense': '#ec4899',
                'Protection and Defense': '#ec4899',
                'Investigation': '#f59e0b'
            };
            return colorMap[normalized] || '#6b7280';
        }

        function findFullRoleInfo(roleName) {
            const cleanRoleName = roleName.trim();
            
            // D'abord chercher dans allRolesData pour avoir DCWF + NICE
            let roleInfo = allRolesData.find(r => 
                (r.nice && r.nice.work_role.trim() === cleanRoleName) || 
                (r.dcwf && r.dcwf.work_role.trim() === cleanRoleName)
            );
            
            if (roleInfo) {
                return {
                    opmId: roleInfo.opm_code,
                    dcwfName: roleInfo.dcwf?.work_role || '',
                    ncwfName: roleInfo.nice?.work_role || '',
                    wrlId: roleInfo.nice?.id || '',
                    dcwfElement: roleInfo.dcwf?.element || '',
                    niceElement: roleInfo.nice?.element || ''
                };
            }
            
            // Sinon chercher dans les lookups NICE (avec et sans espaces)
            let opmId = niceNameToOpmLookup[cleanRoleName] || niceNameToOpmLookup[roleName] || null;
            let wrlId = niceNameToWrlLookup[cleanRoleName] || niceNameToWrlLookup[roleName] || '';
            const niceElement = getElementFromWrlId(wrlId);
            
            return {
                opmId: opmId,
                dcwfName: '',
                ncwfName: cleanRoleName,
                wrlId: wrlId,
                dcwfElement: '',
                niceElement: niceElement
            };
        }

        function sectionList(items, emptyText, currentElement) {
            if (!items || items.length === 0) return `<div class=\"no-data-message\">${emptyText}</div>`;
            return items.map((t) => {
                const roleName = typeof t === 'string' ? t : t.name;
                const percentage = typeof t === 'object' ? t.percentage : null;
                const roleInfo = findFullRoleInfo(roleName);
                
                const opmId = roleInfo.opmId;
                const dcwfName = roleInfo.dcwfName;
                const ncwfName = roleInfo.ncwfName;
                const wrlId = roleInfo.wrlId;
                const dcwfElement = roleInfo.dcwfElement;
                const niceElement = roleInfo.niceElement;
                
                // Couleur pour OPM-ID basée sur l'élément DCWF
                const opmColor = getElementColorForOpmId(dcwfElement);
                // Couleur pour WRL-ID basée sur l'élément NICE
                const wrlColor = getElementColorForOpmId(niceElement);
                
                const opmDisplay = opmId ? `<span class=\"opm-badge\" style=\"background-color: ${opmColor};\">${opmId}</span>` : '';
                const wrlDisplay = wrlId ? `<span class=\"wrl-badge\" style=\"border-color: ${wrlColor}; color: ${wrlColor};\">${wrlId}</span>` : '';
                const names = dcwfName && ncwfName ? `${dcwfName} / ${ncwfName}` : ncwfName;
                
                if (!percentage) {
                    return `<div class=\"list-item\">${opmDisplay}<span>${names}</span>${wrlDisplay}</div>`;
                } else {
                    return `
                        <div class=\"list-item list-item-with-percentage\">
                            <span style=\"display: flex; align-items: center; gap: 8px; flex: 1;\">${opmDisplay}<span>${names}</span>${wrlDisplay}</span>
                            <span class=\"percentage\">${percentage}</span>
                        </div>
                    `;
                }
            }).join('');
        }

        function openModal(index) {
            const role = allRolesData[index];
            
            // Si pas de données NICE, ne pas ouvrir la modal
            if (!role.nice) {
                alert('Aucune donnée NCWF disponible pour ce rôle.');
                return;
            }
            
            document.getElementById('modalTitle').textContent = role.nice.work_role;
            
            let html = `
                <div class=\"card ncwf\" style=\"max-width:100%;min-width:auto;margin:0 auto;\">
                    <div class=\"framework-label\">NCWF 2025</div>
                    <div class=\"role-title\">${role.nice.work_role}</div>
                    <div class=\"ids\">
                        <div class=\"id-item wrl-id\">WRL-ID: ${role.nice.id}</div>
                        <div class=\"id-item opm-id\">OPM-ID: ${role.opm_code !== null ? role.opm_code : '—'}</div>
                    </div>
                    <div class=\"description\">${role.nice.description || '—'}</div>
                    <span class=\"element-badge ${getElementBadgeClass(role.nice.element)}\">${role.nice.element || '—'}</span>
                    
                    <div class=\"section\">
                        <div class=\"section-title\">🔗 Related Roles by TKS (Top 5)</div>
                        <div class=\"list-container\">${sectionList(role.nice.related_roles_tks, 'Aucune relation TKS', role.nice.element)}</div>
                    </div>
                    
                    <div class=\"section\">
                        <div class=\"section-title\">📊 Top 5 Secondary Work Roles (Federal Data)</div>
                        <div class=\"list-container\">${sectionList(role.nice.top_5_secondary, 'Pas de données fédérales', role.nice.element)}</div>
                    </div>
                    
                    <div class=\"section\">
                        <div class=\"section-title\">📥 On Ramps (${(role.nice.on_ramps||[]).length})</div>
                        <div class=\"list-container\">${sectionList(role.nice.on_ramps, 'Aucun on-ramp', role.nice.element)}</div>
                    </div>
                    
                    <div class=\"section\">
                        <div class=\"section-title\">📤 Off Ramps (${(role.nice.off_ramps||[]).length})</div>
                        <div class=\"list-container\">${sectionList(role.nice.off_ramps, 'Aucun off-ramp', role.nice.element)}</div>
                    </div>
                    
                    <div class=\"stats-box\">
                        <div class=\"stats-title\">📈 Résumé des Statistiques</div>
                        <div class=\"stats-content\">
                            <strong>On-Ramps:</strong> ${role.nice.on_ramps.length} | 
                            <strong>Off-Ramps:</strong> ${role.nice.off_ramps.length} | 
                            <strong>Related TKS:</strong> ${role.nice.related_roles_tks.length}
                        </div>
                    </div>
                </div>
            `;
            
            document.getElementById('modalBody').innerHTML = html;
            document.getElementById('modalBackdrop').style.display = 'block';
            document.getElementById('detailsModal').classList.add('open');
        }

        function closeModal() {
            document.getElementById('modalBackdrop').style.display = 'none';
            document.getElementById('detailsModal').classList.remove('open');
        }

        function displayRole() {
            const selector = document.getElementById('roleSelector');
            const selectedIndex = selector.value;
            
            if (selectedIndex === '') {
                renderAllRoles();
                return;
            }
            
            // Si un rôle est sélectionné, ouvrir la modal
            openModal(parseInt(selectedIndex));
        }

        // Initialiser
        try {
            populateSelector();
            displayRole();
        } catch (e) {
            const c = document.getElementById('contentArea');
            if (c) { c.innerHTML = '<div class="no-data-message">Erreur d\\'initialisation. Chargement de la grille…</div>'; }
            try { renderAllRoles(); } catch (_) {}
        }
    </script>
</body>
</html>
"""

# Écrire le fichier HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[OK] Fichier HTML genere avec succes !")
print(f"[INFO] Total de {len(js_roles)} roles avec correspondance NCWF/DCWF")
print(f"[FILE] Fichier: index.html")
