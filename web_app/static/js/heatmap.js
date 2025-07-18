// --- Constants ---
const MAX_RELEVANCE_VALUE = 5;

// Fonction pour obtenir la catégorie d'un OPM ID
function getOpmCategory(id) {
  // IT (Cyberspace)
  if (["421", "431", "441", "451", "411", "651", "632", "641", "671", "661"].includes(id)) {
    return "IT (Cyberspace)";
  }
  // Cybersecurity
  else if (["723", "612", "611", "722", "511", "212", "531", "521", "541", "652", "631", "622", "462"].includes(id)) {
    return "Cybersecurity";
  }
  // Cyberspace Effects
  else if (["332", "121", "131", "132", "341", "322", "122", "463", "443", "442", "133"].includes(id)) {
    return "Cyberspace Effects";
  }
  // Intelligence (Cyberspace)
  else if (["111", "311", "312", "331", "151"].includes(id)) {
    return "Intelligence (Cyberspace)";
  }
  // Cyberspace Enablers
  else if (["752", "751", "711", "712", "731", "901", "732", "803", "801", "802", "804", "805", "221", "211"].includes(id)) {
    return "Cyberspace Enablers";
  }
  // Software Engineering
  else if (["621", "461", "627", "625", "806", "626", "673", "628"].includes(id)) {
    return "Software Engineering";
  }
  // Data/AI
  else if (["422", "753", "902", "733", "672", "623", "653", "903", "624", "423", "424"].includes(id)) {
    return "Data/AI";
  }
  // Catégorie inconnue
  else {
    return "Autre";
  }
}

// Les 15 domaines de compétence du NCWF (mis à jour selon les spécifications)
const competencyAreas = [
  "Access Controls (NF-COM-001)",
  "Artificial Intelligence (AI) Security (NF-COM-002)",
  "Asset Management (NF-COM-003)",
  "Cloud Security (NF-COM-004)",
  "Communications Security (NF-COM-005)",
  "Cryptography (NF-COM-006)",
  "Cyber Resiliency (NF-COM-007)",
  "DevSecOps (NF-COM-008)",
  "Operating Systems (OS) Security (NF-COM-009)",
  "Operational Technology (OT) Security (NF-COM-010)",
  "Supply Chain Security (NF-COM-011)",
  "Cybersecurity Fundamentals (NF-COM-12)",
  "Cybersecurity Leadership (NF-COM-13)",
  "Data Security (NF-COM-14)",
  "Secure Programming (NF-COM-15)"
];

// Liste des OPM IDs identifiés dans la base de données
const opmIds = [
  "111", "112", "121", "122", "131", "132", "133", "141", "151", 
  "211", "212", "221", 
  "311", "312", "321", "322", "331", "332", "333", "341", 
  "411", "421", "422", "423", "424", "431", "441", "442", "443", "451", "461", "462", "463", 
  "511", "521", "531", "541", 
  "611", "612", "621", "622", "623", "624", "625", "626", "627", "628", "631", "632", "641", "651", "652", "653", "661", "671", "672", "673", 
  "711", "712", "722", "723", "731", "732", "733", "751", "752", "753", 
  "801", "802", "803", "804", "805", "806", 
  "901", "902", "903"
];

// Mapping des OPM IDs vers leurs titres
const opmIdTitles = {
  "111": "All-Source Analyst",
  "121": "Exploitation Analyst",
  "122": "Digital Network Exploitation Analyst",
  "131": "Joint Targeting Analyst",
  "132": "Target Digital Network Analyst",
  "133": "Target Analyst Reporter",
  "151": "Multi-Disciplined Language Analyst",
  "211": "Forensics Analyst",
  "212": "Cyber Defense Forensics Analyst",
  "221": "Cyber Crime Investigator",
  "311": "All-Source Collection Manager",
  "312": "All-Source Collection Requirements Manager",
  "322": "Cyberspace Operator",
  "331": "Cyber Intelligence Planner",
  "332": "Cyber Operations Planner",
  "341": "Cyberspace Capability Developer",
  "411": "Technical Support Specialist",
  "421": "Database Administrator",
  "422": "Data Analyst",
  "423": "Data Scientist",
  "424": "Data Steward",
  "431": "Knowledge Manager",
  "441": "Network Operations Specialist",
  "442": "Network Technician",
  "443": "Network Analyst",
  "451": "System Administrator",
  "461": "Systems Security Analyst",
  "462": "Control Systems Security Specialist",
  "463": "Host Analyst",
  "511": "Cyber Defense Analyst",
  "521": "Cyber Defense Infrastructure Support Specialist",
  "531": "Cyber Defense Incident Responder",
  "541": "Vulnerability Assessment Analyst",
  "611": "Authorizing Official/Designated Representative",
  "612": "Security Control Assessor",
  "621": "Software Developer",
  "622": "Secure Software Assessor",
  "623": "AI/ML Specialist",
  "624": "Data Operations Specialist",
  "625": "Product Designer User Interface (UI)",
  "626": "Service Designer User Experience (UX)",
  "627": "DevSecOps Specialist",
  "628": "Software/Cloud Architect",
  "631": "Information Systems Security Developer",
  "632": "Systems Developer",
  "641": "Systems Requirements Planner",
  "651": "Enterprise Architect",
  "652": "Security Architect",
  "653": "Data Architect",
  "661": "Research & Development Specialist",
  "671": "System Testing and Evaluation Specialist",
  "672": "AI Test & Evaluation Specialist",
  "673": "Software Test & Evaluation Specialist",
  "711": "Cyber Instructional Curriculum Developer",
  "712": "Cyber Instructor",
  "722": "Information Systems Security Manager",
  "723": "COMSEC Manager",
  "731": "Cyber Legal Advisor",
  "732": "Privacy Compliance Manager",
  "733": "AI Risk & Ethics Specialist",
  "751": "Cyber Workforce Developer and Manager",
  "752": "Cyber Policy and Strategy Planner",
  "753": "AI Adoption Specialist",
  "801": "Program Manager",
  "802": "IT Project Manager",
  "803": "Product Support Manager",
  "804": "IT Investment/Portfolio Manager",
  "805": "IT Program Auditor",
  "806": "Product Manager",
  "901": "Executive Cyber Leader",
  "902": "AI Innovation Leader",
  "903": "Data Officer"
};

// Filtrer les OPM IDs pour ne garder que ceux qui ont une description
const filteredOpmIds = opmIds.filter(id => opmIdTitles[id] && opmIdTitles[id].trim() !== "");

// Rendre les variables accessibles globalement pour le débogage
window.competencyAreas = competencyAreas;
window.opmIds = filteredOpmIds; // Utiliser les OPM IDs filtrés

// Données pour les rôles et la heatmap
let roleData = [];
let heatmapData = [];

// Fonction pour normaliser un ID à partir d'un titre
function normalizeId(title) {
  return title
    .replace(/[^a-zA-Z0-9]/g, '_')  // Remplacer les caractères spéciaux par des underscores
    .replace(/_+/g, '_')            // Remplacer les underscores multiples par un seul
    .replace(/^_|_$/g, '')          // Supprimer les underscores au début et à la fin
    .toLowerCase();                 // Tout en minuscules
}

// Structure des mappings entre domaines de compétence et OPM IDs
// Basée sur l'analyse des documents NICE Framework et DCWF
const mappings = {
  // Access Controls (NF-COM-001): Contrôle d'accès et gestion des identités
  access_controls: {
    critical: ["611", "612", "631", "632", "652", "722"], // Authorizing Official, Security Control Assessor, Security Developers, Security Architects
    high: ["421", "451", "511", "521", "541", "651"],     // Database Admin, System Admin, Cyber Defense, Vulnerability Assessment
    medium: ["411", "441", "461", "621", "622", "641"],   // Tech Support, Network Ops, Systems Security, Software Dev
    low: ["211", "221", "331", "531", "671", "712"],      // Forensics, Investigation, Planning, Incident Response
    minimal: ["111", "131", "151", "751", "801", "803"]   // Management, Leadership roles
  },
  
  // Artificial Intelligence Security (NF-COM-002): Sécurité de l'IA
  ai_security: {
    critical: ["623", "672", "673", "733", "902", "903"], // AI/ML Specialist, AI Test & Eval, AI Risk & Ethics, AI Leadership
    high: ["422", "423", "424", "653", "661", "753"],     // Data Analyst, Data Scientist, Data Steward, Research
    medium: ["421", "461", "541", "611", "631", "641"],   // Database, Security, Development
    low: ["451", "511", "521", "612", "622", "652"],      // Admin, Defense, Security Architecture
    minimal: ["711", "712", "731", "732", "751", "801"]   // Training, Legal, Management
  },
  
  // Asset Management (NF-COM-003): Gestion des actifs
  asset_management: {
    critical: ["411", "421", "451", "511", "521", "803"], // Admin, Operations, Management
    high: ["441", "461", "541", "611", "612", "651"],     // Network Ops, Security, Architecture
    medium: ["431", "531", "631", "641", "652", "722"],   // Knowledge Management, Security
    low: ["621", "622", "632", "671", "712", "732"],      // Development, Testing
    minimal: ["111", "151", "331", "751", "801", "901"]   // Intelligence, Leadership
  },
  
  // Cloud Security (NF-COM-004): Sécurité du cloud
  cloud_security: {
    critical: ["421", "451", "611", "628", "631", "652"], // Admin, Cloud Architect, Security
    high: ["441", "511", "521", "612", "622", "651"],     // Network, Defense, Architecture
    medium: ["411", "431", "461", "541", "621", "641"],   // Support, Development
    low: ["531", "671", "722", "732", "752", "802"],      // Incident Response, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Communications Security (NF-COM-005): Sécurité des communications
  communications_security: {
    critical: ["441", "511", "521", "631", "632", "723"], // Network, Defense, COMSEC
    high: ["421", "451", "531", "611", "612", "652"],     // Admin, Security
    medium: ["411", "431", "461", "541", "621", "641"],   // Support, Development
    low: ["422", "622", "651", "671", "722", "732"],      // Data, Testing, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Cryptography (NF-COM-006): Cryptographie
  cryptography: {
    critical: ["511", "521", "611", "612", "631", "723"], // Security, Defense, COMSEC
    high: ["421", "441", "451", "521", "622", "652"],     // Admin, Network, Security
    medium: ["411", "431", "461", "541", "621", "641"],   // Support, Development
    low: ["422", "531", "651", "671", "722", "732"],      // Data, Incident Response, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Cyber Resiliency (NF-COM-007): Résilience cyber
  cyber_resiliency: {
    critical: ["511", "521", "531", "611", "612", "722"], // Security, Defense, Incident Response
    high: ["421", "441", "451", "461", "541", "651"],     // Admin, Network, Vulnerability Assessment
    medium: ["411", "431", "631", "641", "652", "732"],   // Support, Security Development
    low: ["422", "621", "622", "671", "751", "752"],      // Data, Development, Workforce
    minimal: ["711", "712", "731", "801", "803", "901"]   // Training, Legal, Leadership
  },
  
  // DevSecOps (NF-COM-008): DevSecOps
  devsecops: {
    critical: ["621", "622", "623", "627", "628", "673"], // Development, DevSecOps, Testing
    high: ["451", "461", "511", "611", "631", "652"],     // Admin, Security, Architecture
    medium: ["421", "441", "521", "541", "612", "641"],   // Database, Network, Defense
    low: ["411", "431", "531", "671", "722", "732"],      // Support, Incident Response, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Operating Systems Security (NF-COM-009): Sécurité des systèmes d'exploitation
  os_security: {
    critical: ["411", "421", "451", "511", "521", "631"], // Admin, Security
    high: ["441", "461", "541", "611", "612", "652"],     // Network, Security Assessment
    medium: ["431", "531", "621", "622", "641", "722"],   // Knowledge, Incident Response, Development
    low: ["422", "632", "651", "671", "732", "752"],      // Data, Architecture, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Operational Technology Security (NF-COM-010): Sécurité des technologies opérationnelles
  ot_security: {
    critical: ["462", "511", "521", "531", "611", "631"], // Control Systems, Security, Defense
    high: ["421", "441", "451", "461", "541", "652"],     // Admin, Network, Vulnerability
    medium: ["411", "431", "621", "622", "641", "722"],   // Support, Development, Management
    low: ["422", "532", "651", "671", "732", "752"],      // Data, Architecture, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Supply Chain Security (NF-COM-011): Sécurité de la chaîne d'approvisionnement
  supply_chain_security: {
    critical: ["211", "212", "221", "611", "612", "803"], // Forensics, Investigation, Security Assessment
    high: ["421", "451", "511", "521", "541", "722"],     // Admin, Security, Defense
    medium: ["441", "461", "631", "641", "651", "652"],   // Network, Security Development, Architecture
    low: ["411", "431", "621", "622", "671", "732"],      // Support, Development, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Cybersecurity Fundamentals (NF-COM-012): Fondamentaux de la cybersécurité
  cybersecurity_fundamentals: {
    critical: ["411", "421", "451", "511", "521", "611"], // Admin, Security, Defense
    high: ["441", "461", "531", "541", "612", "631"],     // Network, Incident Response, Security Dev
    medium: ["431", "621", "622", "641", "651", "652"],   // Knowledge, Development, Architecture
    low: ["422", "632", "671", "722", "732", "752"],      // Data, Testing, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Cybersecurity Leadership (NF-COM-013): Leadership en cybersécurité
  cybersecurity_leadership: {
    critical: ["751", "752", "801", "802", "803", "901"], // Workforce, Policy, Management, Leadership
    high: ["611", "612", "722", "731", "732", "902"],     // Security, Legal, AI Leadership
    medium: ["511", "521", "531", "541", "651", "652"],   // Security, Defense, Architecture
    low: ["421", "441", "451", "461", "631", "641"],      // Admin, Network, Security Development
    minimal: ["411", "422", "431", "621", "622", "671"]   // Support, Data, Development
  },
  
  // Data Security (NF-COM-014): Sécurité des données
  data_security: {
    critical: ["421", "422", "423", "511", "611", "631"], // Database, Data Analysis, Security
    high: ["424", "451", "521", "541", "612", "652"],     // Data Steward, Admin, Defense
    medium: ["411", "441", "461", "621", "622", "641"],   // Support, Network, Development
    low: ["431", "531", "651", "671", "722", "732"],      // Knowledge, Incident Response, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  },
  
  // Secure Programming (NF-COM-015): Programmation sécurisée
  secure_programming: {
    critical: ["621", "622", "623", "627", "628", "631"], // Development, DevSecOps, Security Dev
    high: ["461", "511", "541", "611", "612", "652"],     // Security Analysis, Security Assessment
    medium: ["421", "441", "451", "521", "641", "673"],   // Admin, Network, Testing
    low: ["411", "431", "531", "651", "671", "722"],      // Support, Incident Response, Management
    minimal: ["711", "712", "731", "751", "801", "901"]   // Training, Legal, Leadership
  }
};

// Fonction pour dessiner la heatmap
function drawHeatmap(opmIdList) {
  // Si une liste d'OPM IDs est fournie, on l'utilise, sinon on prend tous les OPM IDs filtrés
  const opmIdsToUse = Array.isArray(opmIdList) && opmIdList.length > 0 ? opmIdList : filteredOpmIds;
  console.log("Dessin de la heatmap avec", opmIdsToUse.length, "OPM IDs et", competencyAreas.length, "domaines de compétence");
  
  // Générer les données pour la heatmap
  heatmapData = buildHeatmapDataset(opmIdsToUse);
  console.log("Dataset généré avec", heatmapData.length, "lignes");
  
  // Calculer la largeur nécessaire en fonction du nombre d'OPM IDs
  const cellMinWidth = 40; // Largeur minimale pour chaque cellule en pixels
  const requiredWidth = opmIdsToUse.length * cellMinWidth;
  
  // Augmenter les marges pour éviter la coupure
  const margin = { top: 120, right: 150, bottom: 300, left: 350 };
  
  // Dimensions ajustées
  const width = Math.max(2800, requiredWidth) - margin.left - margin.right;
  const height = 1400 - margin.top - margin.bottom;
  
  // Nettoyage du SVG existant (reset complet du SVG)
  d3.select("#heatmap-svg-element").html("");
  
  // Échelles de couleur
  const colorScale = d3.scaleLinear()
    .domain([0, 1, 2, 3, 4, 5])
    .range(["#ffffff", "#e6eeff", "#99bbff", "#4d88ff", "#0044cc", "#002266"]);
    
  // Préparation du SVG
  const svg = d3.select("#heatmap-svg-element")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);
    
  // Créer un groupe pour le tooltip SVG - le placer en dernier pour qu'il soit au-dessus
  let tooltipGroup;
  
  // Fonction pour créer le tooltip après tout le reste
  function createTooltip() {
    // Supprimer l'ancien tooltip s'il existe
    svg.selectAll(".tooltip-group").remove();
    
    // Créer un nouveau groupe pour le tooltip
    tooltipGroup = svg.append("g")
      .attr("class", "tooltip-group")
      .style("opacity", 0)
      .attr("pointer-events", "none"); // Ignorer les événements de souris sur le tooltip
      
    // Rectangle de fond pour le tooltip
    tooltipGroup.append("rect")
      .attr("class", "tooltip-bg")
      .attr("rx", 5)
      .attr("ry", 5)
      .attr("fill", "white")
      .attr("stroke", "#ccc")
      .attr("stroke-width", 1)
      .attr("width", 250)
      .attr("height", 60);
      
    // Texte du tooltip
    tooltipGroup.append("text")
      .attr("class", "tooltip-title")
      .attr("x", 10)
      .attr("y", 20)
      .style("font-weight", "bold")
      .style("font-size", "12px");
      
    tooltipGroup.append("text")
      .attr("class", "tooltip-category")
      .attr("x", 10)
      .attr("y", 40)
      .style("font-size", "11px")
      .style("font-style", "italic");
      
    tooltipGroup.append("text")
      .attr("class", "tooltip-desc")
      .attr("x", 10)
      .attr("y", 60)
      .style("font-size", "12px");
  }
  
  // Échelles
  const xScale = d3.scaleBand()
    .domain(opmIdsToUse)
    .range([0, width])
    .padding(0.12);
    
  const yScale = d3.scaleBand()
    .domain(competencyAreas)
    .range([0, height])
    .padding(0.1);
    
  // Fond gris moyen pour les OPM IDs
  svg.append("g")
    .selectAll("rect")
    .data(opmIdsToUse)
    .enter()
    .append("rect")
    .attr("x", d => xScale(d))
    .attr("y", height + 1)
    .attr("width", xScale.bandwidth())
    .attr("height", 50)
    .attr("fill", "#6b7280")
    .attr("class", "opm-header-rect")
    .attr("data-opmid", d => d)
    .style("cursor", "pointer")
    .on("mouseover", function(event, d) {
      // Obtenir la position de la case
      const x = xScale(d);
      const y = height + 1;
      const width = xScale.bandwidth();
      
      // Obtenir la catégorie OPM basée sur les nouvelles classifications fournies
      const categoryText = `Catégorie: ${getOpmCategory(d)}`;
      const desc = opmIdTitles[d];
      
      // Préparer le contenu du tooltip
      const title = `OPM ID: ${d}`;
      
      // Créer le tooltip s'il n'existe pas
      createTooltip();
      
      // Mettre à jour le texte du tooltip
      tooltipGroup.select(".tooltip-title").text(title);
      
      // Ajouter un élément pour la catégorie
      tooltipGroup.select(".tooltip-category").remove(); // Supprimer l'ancien s'il existe
      tooltipGroup.append("text")
        .attr("class", "tooltip-category")
        .attr("x", 10)
        .attr("y", 40)
        .style("font-size", "11px")
        .style("font-style", "italic")
        .text(categoryText);
      
      // Gérer le texte long avec du wrapping
      const words = desc.split(/\s+/);
      let line = '';
      let lineNumber = 0;
      const lineHeight = 15;
      const tooltipDesc = tooltipGroup.select(".tooltip-desc").text('');
      
      for (let i = 0; i < words.length; i++) {
        const testLine = line + words[i] + ' ';
        if (testLine.length * 6 > 180) { // Approximation simple de la largeur du texte
          tooltipDesc.append("tspan")
            .attr("x", 10)
            .attr("y", 60 + (lineNumber * lineHeight)) // Décalé pour laisser de la place à la catégorie
            .text(line);
          line = words[i] + ' ';
          lineNumber++;
        } else {
          line = testLine;
        }
      }
      
      tooltipDesc.append("tspan")
        .attr("x", 10)
        .attr("y", 60 + (lineNumber * lineHeight)) // Décalé pour laisser de la place à la catégorie
        .text(line);
      
      // Ajuster la hauteur du fond en fonction du nombre de lignes
      const tooltipHeight = 50 + ((lineNumber + 1) * lineHeight); // Augmenté pour la ligne de catégorie
      tooltipGroup.select(".tooltip-bg")
        .attr("height", tooltipHeight);
      
      // Positionner le tooltip sous la case
      tooltipGroup.attr("transform", `translate(${x + width/2 - 100}, ${y + 50})`);
      
      // Afficher le tooltip
      tooltipGroup.style("opacity", 1);
      
      // Déplacer le tooltip à la fin du SVG pour qu'il soit au-dessus de tout
      tooltipGroup.raise();
    })
    .on("mouseout", function() {
      // Masquer le tooltip
      if (tooltipGroup) tooltipGroup.style("opacity", 0);
    });
    
  // Textes des OPM IDs - Afficher uniquement le numéro
  svg.append("g")
    .selectAll("text")
    .data(opmIdsToUse)
    .enter()
    .append("text")
    .attr("class", "opm-id-label")
    .attr("x", d => xScale(d) + xScale.bandwidth() / 2)
    .attr("y", height + 25)
    .attr("text-anchor", "middle")
    .style("font-size", "14px")
    .style("font-weight", "bold")
    .style("fill", "white")
    .style("pointer-events", "none")
    .text(d => d);
  
  // Axe Y - Domaines de compétence
  svg.append("g")
    .call(d3.axisLeft(yScale))
    .selectAll("text")
    .style("font-size", "14px")
    .style("font-weight", "bold")
    .call(wrap, margin.left - 30);
    
  // Fonction pour wrap le texte long
  function wrap(text, width) {
    text.each(function() {
      const text = d3.select(this);
      const words = text.text().split(/\s+/).reverse();
      let word, line = [], lineNumber = 0, lineHeight = 1.1;
      const y = text.attr("y");
      const dy = parseFloat(text.attr("dy") || 0);
      let tspan = text.text(null).append("tspan").attr("x", -15).attr("y", y).attr("dy", dy + "em");
      
      while (word = words.pop()) {
        line.push(word);
        tspan.text(line.join(" "));
        if (tspan.node().getComputedTextLength() > width) {
          line.pop();
          tspan.text(line.join(" "));
          line = [word];
          tspan = text.append("tspan").attr("x", -15).attr("y", y).attr("dy", `${++lineNumber * lineHeight + dy}em`).text(word);
        }
      }
    });
  }
   
  // Fonction pour obtenir la justification du niveau de pertinence
  function getRelationJustification(domain, opmId, value) {
    // Base des justifications pour chaque niveau de valeur
    if (value === 0) {
      return "Aucune relation significative identifiée entre ce domaine de compétence et ce rôle professionnel selon le NICE Framework et le DCWF.";
    } else if (value === 1) {
      return "Relation minimale: Ce rôle a une compréhension basique ou une implication périphérique dans ce domaine de compétence, selon les définitions du NICE Framework.";
    } else if (value === 2) {
      return "Relation faible: Ce rôle nécessite une connaissance fonctionnelle de base de ce domaine, sans en faire un aspect central des responsabilités quotidiennes.";
    } else if (value === 3) {
      return "Relation modérée: Ce rôle implique une utilisation régulière des compétences de ce domaine, qui constituent une partie importante mais non principale des fonctions.";
    } else if (value === 4) {
      return "Relation forte: Ce domaine représente une compétence essentielle pour ce rôle, avec une application fréquente et approfondie dans les tâches quotidiennes.";
    } else if (value === 5) {
      return "Relation critique: Ce domaine est fondamental pour ce rôle professionnel, qui exige une maîtrise complète et une expertise avancée dans ce domaine de compétence.";
    }
    
    // Identifier quel mapping utiliser basé sur le domaine de compétence
    let mappingKey = "";
    if (domain.includes("Access Controls")) mappingKey = "access_controls";
    else if (domain.includes("Artificial Intelligence")) mappingKey = "ai_security";
    else if (domain.includes("Asset Management")) mappingKey = "asset_management";
    else if (domain.includes("Cloud Security")) mappingKey = "cloud_security";
    else if (domain.includes("Communications Security")) mappingKey = "communications_security";
    else if (domain.includes("Cryptography")) mappingKey = "cryptography";
    else if (domain.includes("Cyber Resiliency")) mappingKey = "cyber_resiliency";
    else if (domain.includes("DevSecOps")) mappingKey = "devsecops";
    else if (domain.includes("Operating Systems")) mappingKey = "os_security";
    else if (domain.includes("Operational Technology")) mappingKey = "ot_security";
    else if (domain.includes("Supply Chain")) mappingKey = "supply_chain_security";
    else if (domain.includes("Fundamentals")) mappingKey = "cybersecurity_fundamentals";
    else if (domain.includes("Leadership")) mappingKey = "cybersecurity_leadership";
    else if (domain.includes("Data Security")) mappingKey = "data_security";
    else if (domain.includes("Secure Programming")) mappingKey = "secure_programming";
    else mappingKey = "cybersecurity_fundamentals"; // Valeur par défaut
    
    console.log(`Domaine: ${domain} => Mapping: ${mappingKey}`);
    
    const mapping = mappings[mappingKey];
    if (!mapping) {
      console.error(`Aucun mapping trouvé pour la clé: ${mappingKey}`);
    }
    
    // Vérifier s'il existe une justification spécifique
    const specificKey = `${mappingKey}_${opmId}`;
    if (specificJustifications[specificKey]) {
      return specificJustifications[specificKey];
    }
    
    // Si aucune justification spécifique n'est trouvée, retourner la justification générale
    return getGeneralJustification(domain, opmId, value, mappingKey);
  }
  
  // Créer les cellules de la heatmap
  for (let i = 0; i < competencyAreas.length; i++) {
    const domain = competencyAreas[i];
    for (let j = 0; j < opmIdsToUse.length; j++) {
      const opmId = opmIdsToUse[j];
      const value = heatmapData[i][j].value;
      
      console.log(`Cellule [${i},${j}]: domaine=${domain}, opmId=${opmId}, valeur=${value}`);
      
      // Obtenir la justification pour cette relation
      const justification = getRelationJustification(domain, opmId, value);
      
      // Créer la cellule
      svg.append("rect")
        .attr("class", "heatmap-cell")
        .attr("data-domain", domain)
        .attr("data-opmid", opmId)
        .attr("data-value", value)
        .attr("data-justification", justification)
        .attr("x", xScale(opmId))
        .attr("y", yScale(domain))
        .attr("width", xScale.bandwidth())
        .attr("height", yScale.bandwidth())
        .attr("fill", colorScale(value))
        .style("cursor", "default") // Curseur normal (flèche) au survol des cellules
        .on("mouseover", function(event) {
          // Obtenir la position de la cellule
          const rect = d3.select(this);
          const domain = rect.attr("data-domain");
          const opmId = rect.attr("data-opmid");
          const value = parseInt(rect.attr("data-value"));
          const x = parseFloat(rect.attr("x"));
          const y = parseFloat(rect.attr("y"));
          const width = parseFloat(rect.attr("width"));
          const height = parseFloat(rect.attr("height"));
          
          // Obtenir la justification pour cette relation
          const justification = rect.attr("data-justification");
          
          // Préparer le contenu du tooltip
          const title = `${domain} - OPM ID: ${opmId} - Niveau: ${value}/5`;
          
          // Créer le tooltip s'il n'existe pas
          createTooltip();
          
          // Mettre à jour le texte du tooltip
          tooltipGroup.select(".tooltip-title").text(title);
          
          // Gérer le texte long avec du wrapping
          const words = justification.split(/\s+/);
          let line = '';
          let lineNumber = 0;
          const lineHeight = 15;
          const tooltipDesc = tooltipGroup.select(".tooltip-desc").text('');
          
          for (let i = 0; i < words.length; i++) {
            const testLine = line + words[i] + ' ';
            if (testLine.length * 6 > 230) { // Approximation simple de la largeur du texte
              tooltipDesc.append("tspan")
                .attr("x", 10)
                .attr("y", 40 + (lineNumber * lineHeight))
                .text(line);
              line = words[i] + ' ';
              lineNumber++;
            } else {
              line = testLine;
            }
          }
          
          tooltipDesc.append("tspan")
            .attr("x", 10)
            .attr("y", 40 + (lineNumber * lineHeight))
            .text(line);
          
          // Ajuster la hauteur du fond en fonction du nombre de lignes
          const tooltipHeight = 30 + ((lineNumber + 1) * lineHeight);
          tooltipGroup.select(".tooltip-bg")
            .attr("height", tooltipHeight)
            .attr("width", 250); // Élargir pour les justifications
          
          // Positionner le tooltip au-dessus de la cellule pour éviter qu'il soit caché
          tooltipGroup.attr("transform", `translate(${x + width/2 - 125}, ${y - tooltipHeight - 10})`);
          
          // Afficher le tooltip
          tooltipGroup.style("opacity", 1);
          
          // Déplacer le tooltip à la fin du SVG pour qu'il soit au-dessus de tout
          tooltipGroup.raise();
        })
        .on("mouseout", function() {
          // Masquer le tooltip
          if (tooltipGroup) tooltipGroup.style("opacity", 0);
        })
        .on("click", function(event) {
          // Afficher le popup d'édition
          const cell = d3.select(this);
          const domain = cell.attr("data-domain");
          const opmId = cell.attr("data-opmid");
          const value = cell.attr("data-value");
          
          const popup = d3.select("#edit-value-popup");
          popup.classed("active", true);
          popup.style("left", (event.pageX - 50) + "px")
               .style("top", (event.pageY - 100) + "px");
          
          d3.select("#edit-popup-title").html(`
            Modifier la valeur<br>
            <span class="text-sm font-normal">${domain}<br>OPM ID: ${opmId}</span>
          `);
          
          d3.select("#current-value").text(value);
          
          // Stocker les données pour le bouton "Appliquer"
          popup.attr("data-domain", domain)
               .attr("data-opmid", opmId)
               .attr("data-cell-index-i", i)
               .attr("data-cell-index-j", j);
        });
        
      // Ajouter le texte de valeur dans chaque cellule
      svg.append("text")
        .attr("x", xScale(opmId) + xScale.bandwidth() / 2)
        .attr("y", yScale(domain) + yScale.bandwidth() / 2)
        .attr("dy", "0.35em")
        .attr("text-anchor", "middle")
        .style("font-size", "12px")
        .style("font-weight", "bold")
        .style("fill", value > 2.5 ? "white" : "black")
        .style("cursor", "default") // Conserver le curseur par défaut
        .style("pointer-events", "none") // Ignorer les événements de souris sur le texte
        .text(value);
    }
  }
  
  // Titre de la heatmap
  svg.append("text")
    .attr("x", width / 2)
    .attr("y", -40)
    .attr("text-anchor", "middle")
    .style("font-size", "20px")
    .style("font-weight", "bold")
    .text("Heatmap des 15 Domaines de Compétence NICE par OPM ID");
    
  svg.append("text")
    .attr("x", width / 2)
    .attr("y", -15)
    .attr("text-anchor", "middle")
    .style("font-size", "14px")
    .text("Intensité de la relation entre les domaines de compétence et les OPM IDs (0-5)");
    
  // Légende
  const legendWidth = 300;
  const legendHeight = 20;
  
  const legendScale = d3.scaleLinear()
    .domain([0, 5])
    .range([0, legendWidth]);
    
  const legendAxis = d3.axisBottom(legendScale)
    .tickValues([0, 1, 2, 3, 4, 5])
    .tickFormat(d => d);
    
  const legend = svg.append("g")
    .attr("transform", `translate(${width - legendWidth - 50},${height + 100})`);
    
  // Gradient pour la légende
  legend.append("defs")
    .append("linearGradient")
    .attr("id", "legend-gradient")
    .attr("x1", "0%").attr("y1", "0%")
    .attr("x2", "100%").attr("y2", "0%")
    .selectAll("stop")
    .data([
      {offset: "0%", color: colorScale(0)},
      {offset: "20%", color: colorScale(1)},
      {offset: "40%", color: colorScale(2)},
      {offset: "60%", color: colorScale(3)},
      {offset: "80%", color: colorScale(4)},
      {offset: "100%", color: colorScale(5)}
    ])
    .enter().append("stop")
    .attr("offset", d => d.offset)
    .attr("stop-color", d => d.color);
    
  legend.append("rect")
    .attr("width", legendWidth)
    .attr("height", legendHeight)
    .style("fill", "url(#legend-gradient)");
    
  legend.append("g")
    .attr("transform", `translate(0,${legendHeight})`)
    .call(legendAxis);
    
  legend.append("text")
    .attr("x", 0)
    .attr("y", -10)
    .style("font-size", "14px")
    .text("Échelle d'intensité");
}

// Lorsque le document est chargé
document.addEventListener("DOMContentLoaded", function() {
  // Event handlers pour les boutons de contrôle de valeur
  document.getElementById("increase-value").addEventListener("click", function() {
    const valueDisplay = document.getElementById("current-value");
    let currentValue = parseInt(valueDisplay.textContent);
    if (currentValue < MAX_RELEVANCE_VALUE) {
      currentValue++;
      valueDisplay.textContent = currentValue;
    }
  });
  
  document.getElementById("decrease-value").addEventListener("click", function() {
    const valueDisplay = document.getElementById("current-value");
    let currentValue = parseInt(valueDisplay.textContent);
    if (currentValue > 0) {
      currentValue--;
      valueDisplay.textContent = currentValue;
    }
  });
  
  document.getElementById("save-value-btn").addEventListener("click", function() {
    const popup = document.getElementById("edit-value-popup");
    const domain = popup.getAttribute("data-domain");
    const opmId = popup.getAttribute("data-opmid");
    const i = parseInt(popup.getAttribute("data-cell-index-i"));
    const j = parseInt(popup.getAttribute("data-cell-index-j"));
    const newValue = parseInt(document.getElementById("current-value").textContent);
    
    // Mettre à jour la valeur dans le dataset
    heatmapData[i][j].value = newValue;
    
    // Mettre à jour la cellule dans le SVG
    const cell = d3.select(`rect.heatmap-cell[data-domain="${domain}"][data-opmid="${opmId}"]`);
    cell.attr("data-value", newValue)
        .attr("fill", colorScale(newValue));
    
    // Mettre à jour le texte de la valeur
    d3.selectAll("text")
      .filter(function() {
        const x = parseFloat(d3.select(this).attr("x"));
        const y = parseFloat(d3.select(this).attr("y"));
        const cellX = parseFloat(cell.attr("x")) + parseFloat(cell.attr("width")) / 2;
        const cellY = parseFloat(cell.attr("y")) + parseFloat(cell.attr("height")) / 2;
        return Math.abs(x - cellX) < 1 && Math.abs(y - cellY) < 1;
      })
      .text(newValue)
      .style("fill", newValue > 2.5 ? "white" : "black");
    
    // Fermer le popup
    popup.classList.remove("active");
  });
  
  // Afficher la heatmap
  document.getElementById("heatmap-main").classList.remove("hidden");
  
  // Dessiner la heatmap
  drawHeatmap();
});

// Fournit une justification générale basée sur la catégorie et la valeur
function getGeneralJustification(domain, opmId, value, domainKey) {
  // Obtenir la catégorie OPM basée sur les nouvelles classifications
  const category = getOpmCategory(opmId);
  
  // Base de justification selon le niveau de la relation et la catégorie OPM
  let baseJustification = "";
  
  if (value >= 4) {
    baseJustification = `Ce rôle de la catégorie "${category}" est très fortement lié au domaine ${domain}.`;
  } else if (value >= 2) {
    baseJustification = `Ce rôle de la catégorie "${category}" présente une relation modérée avec le domaine ${domain}.`;
  } else {
    baseJustification = `Ce rôle de la catégorie "${category}" a une faible interaction avec le domaine ${domain}.`;
  }
  
  return baseJustification;
}

// Fonction pour appliquer une nouvelle valeur
function applyNewValue() {
  const popup = d3.select("#edit-value-popup");
  const domain = popup.attr("data-domain");
  const opmId = popup.attr("data-opmid");
  const i = parseInt(popup.attr("data-cell-index-i"));
  const j = parseInt(popup.attr("data-cell-index-j"));
  const newValue = parseInt(d3.select("#new-value").property("value"));
  
  // Mettre à jour les données
  heatmapData[i][j].value = newValue;
  
  // Mettre à jour la cellule
  const cell = d3.select(`rect.heatmap-cell[data-domain="${domain}"][data-opmid="${opmId}"]`);
  cell.attr("data-value", newValue)
       .attr("fill", colorScale(newValue));
  
  // Mettre à jour le texte de la valeur
  const text = d3.select(`text[x="${parseFloat(cell.attr("x")) + parseFloat(cell.attr("width"))/2}"][y="${parseFloat(cell.attr("y")) + parseFloat(cell.attr("height"))/2}"]`);
  text.text(newValue)
       .style("fill", newValue > 2.5 ? "white" : "black");
  
  // Fermer le popup
  popup.classed("active", false);
}

// Données d'intensité de relation entre domaines de compétence et OPM IDs
function buildHeatmapDataset(opmIdsToUse) {
  const opmIds = Array.isArray(opmIdsToUse) && opmIdsToUse.length > 0 ? opmIdsToUse : filteredOpmIds;
  console.log("Construction du dataset de la heatmap avec des valeurs précises");
  
  // Créer un dataset vide
  const dataset = [];
  
  // Pour chaque domaine de compétence
  for (let i = 0; i < competencyAreas.length; i++) {
    let row = [];
    const domain = competencyAreas[i];
    
    // Identifier quel mapping utiliser basé sur le domaine de compétence
    let mappingKey = "";
    if (domain.includes("Access Controls")) mappingKey = "access_controls";
    else if (domain.includes("Artificial Intelligence")) mappingKey = "ai_security";
    else if (domain.includes("Asset Management")) mappingKey = "asset_management";
    else if (domain.includes("Cloud Security")) mappingKey = "cloud_security";
    else if (domain.includes("Communications Security")) mappingKey = "communications_security";
    else if (domain.includes("Cryptography")) mappingKey = "cryptography";
    else if (domain.includes("Cyber Resiliency")) mappingKey = "cyber_resiliency";
    else if (domain.includes("DevSecOps")) mappingKey = "devsecops";
    else if (domain.includes("Operating Systems")) mappingKey = "os_security";
    else if (domain.includes("Operational Technology")) mappingKey = "ot_security";
    else if (domain.includes("Supply Chain")) mappingKey = "supply_chain_security";
    else if (domain.includes("Fundamentals")) mappingKey = "cybersecurity_fundamentals";
    else if (domain.includes("Leadership")) mappingKey = "cybersecurity_leadership";
    else if (domain.includes("Data Security")) mappingKey = "data_security";
    else if (domain.includes("Secure Programming")) mappingKey = "secure_programming";
    else mappingKey = "cybersecurity_fundamentals"; // Valeur par défaut
    
    console.log(`Domaine: ${domain} => Mapping: ${mappingKey}`);
    
    const mapping = mappings[mappingKey];
    if (!mapping) {
      console.error(`Aucun mapping trouvé pour la clé: ${mappingKey}`);
    }
    
    // Pour chaque OPM ID filtré
    for (let j = 0; j < opmIds.length; j++) {
      const opmId = opmIds[j];
      let value = 0;
      
      // Attribuer une valeur basée sur la relation du mapping
      if (mapping && mapping.critical && mapping.critical.includes(opmId)) {
        value = 5; // Relation critique/essentielle
      } else if (mapping && mapping.high && mapping.high.includes(opmId)) {
        value = 4; // Relation forte
      } else if (mapping && mapping.medium && mapping.medium.includes(opmId)) {
        value = 3; // Relation modérée
      } else if (mapping && mapping.low && mapping.low.includes(opmId)) {
        value = 2; // Relation faible
      } else if (mapping && mapping.minimal && mapping.minimal.includes(opmId)) {
        value = 1; // Relation minimale
      }
      
      row.push({
        domain: domain,
        opmId: opmId,
        value: value
      });
    }
    dataset.push(row);
  }
  
  console.log(`Dataset généré avec ${dataset.length} lignes et ${dataset[0]?.length || 0} colonnes`);
  return dataset;
} 

// Fonction utilitaire pour redessiner la heatmap avec une liste filtrée d'OPM IDs
window.drawHeatmapWithOpmIds = function(opmIdList) {
  drawHeatmap(opmIdList);
}; 