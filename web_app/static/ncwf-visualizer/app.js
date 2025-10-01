// NCWF Work Role Visualization Application

// DCWF mapping complet avec TOUS les OPM IDs de la base de données
const dcwfMapping = {
  // Analysis (AN) - 100s
  "AN-ASA-001": { "opm_id": "111", "dcwf_title": "All-Source Analyst" },
  "AN-WRL-012": { "opm_id": "112", "dcwf_title": "All-Source Analyst" },
   "AN-XA-001": { "opm_id": "121", "dcwf_title": "Exploitation Analyst" },
   "AN-WRL-022": { "opm_id": "122", "dcwf_title": "Digital Network Exploitation Analyst" },
   "AN-WRL-031": { "opm_id": "131", "dcwf_title": "Joint Targeting Analyst" },
   "AN-WRL-032": { "opm_id": "132", "dcwf_title": "Target Digital Network Analyst" },
   "AN-WRL-033": { "opm_id": "133", "dcwf_title": "Target Analyst Reporter" },
   "IN-WRL-003": { "opm_id": "141", "dcwf_title": "Threat Analyst" },
   "AN-LA-001": { "opm_id": "151", "dcwf_title": "Multi-Disciplined Language Analyst" },
   
   // Investigation (IN) - 200s
   "IN-FO-001": { "opm_id": "211", "dcwf_title": "Forensics Analyst" },
   "IN-FO-002": { "opm_id": "212", "dcwf_title": "Cyber Defense Forensic Analyst" },
   "IN-CI-001": { "opm_id": "221", "dcwf_title": "Cyber Crime Investigator" },
   
   // Collections/Operations (CO) - 300s  
   "CO-CL-001": { "opm_id": "311", "dcwf_title": "All-Source Collection Manager" },
   "CO-CL-002": { "opm_id": "312", "dcwf_title": "All-Source Collection Requirements Manager" },
   "CO-WRL-022": { "opm_id": "322", "dcwf_title": "Cyberspace Operator" },
   "CO-PL-001": { "opm_id": "331", "dcwf_title": "Cyber Intelligence Planner" },
   "CO-PL-002": { "opm_id": "332", "dcwf_title": "Cyber Operations Planner" },
   "CO-WRL-033": { "opm_id": "333", "dcwf_title": "Cyber Operations Planner" },
   "CO-WRL-041": { "opm_id": "341", "dcwf_title": "Cyberspace Capability Developer" },
   
   // Implementation/Operations (IO) - 400s
   "OM-TS-001": { "opm_id": "411", "dcwf_title": "Technical Support Specialist" },
   "OM-DA-001": { "opm_id": "421", "dcwf_title": "Database Administrator" },
   "OM-DA-002": { "opm_id": "422", "dcwf_title": "Data Analyst" },
   "IO-WRL-023": { "opm_id": "423", "dcwf_title": "Data Scientist" },
   "IO-WRL-024": { "opm_id": "424", "dcwf_title": "Data Steward" },
   "OM-KM-001": { "opm_id": "431", "dcwf_title": "Knowledge Manager" },
   "OM-NET-001": { "opm_id": "441", "dcwf_title": "Network Operations Specialist" },
   "IO-WRL-042": { "opm_id": "442", "dcwf_title": "Network Technician" },
   "IO-WRL-043": { "opm_id": "443", "dcwf_title": "Network Analyst" },
   "OM-SA-001": { "opm_id": "451", "dcwf_title": "System Administrator" },
   "OM-AN-001": { "opm_id": "461", "dcwf_title": "Systems Security Analyst" },
   "IO-WRL-062": { "opm_id": "462", "dcwf_title": "Control Systems Security Specialist" },
   "IO-WRL-063": { "opm_id": "463", "dcwf_title": "Host Analyst" },
   
   // Protection/Defense (PR) - 500s
   "PR-DA-001": { "opm_id": "511", "dcwf_title": "Cyber Defense Analyst" },
   "PR-INF-001": { "opm_id": "521", "dcwf_title": "Cyber Defense Infrastructure Support Specialist" },
   "PR-IR-001": { "opm_id": "531", "dcwf_title": "Cyber Defense Incident Responder" },
   "PR-VA-001": { "opm_id": "541", "dcwf_title": "Vulnerability Assessment Specialist" },
   "PR-WRL-051": { "opm_id": "551", "dcwf_title": "Red Team Specialist" },
   
   // Specialized (SP) - 600s
   "SP-RM-001": { "opm_id": "611", "dcwf_title": "Authorizing Official/Designated Representative" },
   "SP-RM-002": { "opm_id": "612", "dcwf_title": "Security Control Assessor" },
   "SP-DEV-001": { "opm_id": "621", "dcwf_title": "Software Developer" },
   "SP-DEV-002": { "opm_id": "622", "dcwf_title": "Secure Software Assessor" },
   "SP-WRL-023": { "opm_id": "623", "dcwf_title": "AI/ML Specialist" },
   "SP-WRL-024": { "opm_id": "624", "dcwf_title": "Data Operations Specialist" },
   "SP-WRL-025": { "opm_id": "625", "dcwf_title": "Product Designer User Interface (UI)" },
   "SP-WRL-026": { "opm_id": "626", "dcwf_title": "Service Designer User Experience (UX)" },
   "SP-WRL-027": { "opm_id": "627", "dcwf_title": "DevSecOps Specialist" },
   "SP-WRL-028": { "opm_id": "628", "dcwf_title": "Software/Cloud Architect" },
   "SP-SYS-001": { "opm_id": "631", "dcwf_title": "Information Systems Security Developer" },
   "SP-SYS-002": { "opm_id": "632", "dcwf_title": "Systems Developer" },
   "IO-WRL-001": { "opm_id": "661", "dcwf_title": "Data Analysis" },
   "SP-RP-001": { "opm_id": "641", "dcwf_title": "Systems Requirements Planner" },
   "SP-ARC-001": { "opm_id": "651", "dcwf_title": "Enterprise Architect" },
   "DD-WRL-001": { "opm_id": "652", "dcwf_title": "Security Architect" },
   "SP-WRL-053": { "opm_id": "653", "dcwf_title": "Data Architect" },
   "SP-TE-001": { "opm_id": "671", "dcwf_title": "System Testing and Evaluation Specialist" },
   "SP-WRL-072": { "opm_id": "672", "dcwf_title": "AI Test & Evaluation Specialist" },
   "SP-WRL-073": { "opm_id": "673", "dcwf_title": "Software Test & Evaluation Specialist" },
   
   // Oversight (OV) - 700s
   "OG-WRL-004": { "opm_id": "711", "dcwf_title": "Cyber Instructional Curriculum Developer" },
   "OG-WRL-005": { "opm_id": "712", "dcwf_title": "Cyber Instructor" },
   "OV-MG-001": { "opm_id": "722", "dcwf_title": "Information Systems Security Manager" },
   "OG-WRL-001": { "opm_id": "723", "dcwf_title": "COMSEC Manager" },
   "OV-LG-001": { "opm_id": "731", "dcwf_title": "Cyber Legal Advisor" },
   "OV-LG-002": { "opm_id": "732", "dcwf_title": "Privacy Compliance Manager" },
   "OV-WRL-033": { "opm_id": "733", "dcwf_title": "AI Risk & Ethics Specialist" },
   "OG-WRL-003": { "opm_id": "751", "dcwf_title": "Cyber Workforce Developer and Manager" },
   "OG-WRL-002": { "opm_id": "752", "dcwf_title": "Cyber Policy and Strategy Planner" },
   "OV-WRL-053": { "opm_id": "753", "dcwf_title": "AI Adoption Specialist" },
   
   // Management (MG) - 800s
   "OV-PM-001": { "opm_id": "801", "dcwf_title": "Program Manager" },
   "OV-PM-002": { "opm_id": "802", "dcwf_title": "IT Project Manager" },
   "OV-PM-003": { "opm_id": "803", "dcwf_title": "Product Support Manager" },
   "OV-PM-004": { "opm_id": "804", "dcwf_title": "IT Investment/Portfolio Manager" },
   "OV-PM-005": { "opm_id": "805", "dcwf_title": "IT Program Auditor" },
   "MG-WRL-006": { "opm_id": "806", "dcwf_title": "Product Manager" },
   
   // Executive (EX) - 900s
   "OV-EX-001": { "opm_id": "901", "dcwf_title": "Executive Cyber Leader" },
   "EX-WRL-002": { "opm_id": "902", "dcwf_title": "AI Innovation Leader" },
   "EX-WRL-003": { "opm_id": "903", "dcwf_title": "Data Officer" }
};

// Application data
const appData = {
  "work_roles": [
    {
      "id": "OG-WRL-001",
      "name": "Communications Security (COMSEC) Management",
      "omp": ["723"],
      "category": "OG",
      "dcwf_info": {
        "opm_id": "723",
        "dcwf_title": "Communications Security (COMSEC) Management",
        "dcwf_description": "Responsible for managing the Communications Security (COMSEC) resources of an organization."
      },
      "tks_related": [
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 37.5, "tks_breakdown": {"T": 35.1, "K": 39.9, "S": 37.5}},
        {"id": "OG-WRL-006", "name": "Information Systems/Cybersecurity Management", "percentage": 35.59, "tks_breakdown": {"T": 33.19, "K": 37.99, "S": 35.59}},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 31.86, "tks_breakdown": {"T": 29.46, "K": 34.26, "S": 31.86}},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": 31.67, "tks_breakdown": {"T": 29.27, "K": 34.07, "S": 31.67}},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 31.25, "tks_breakdown": {"T": 28.85, "K": 33.65, "S": 31.25}}
      ],
      "on_ramps": [
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 85.2, "tks_breakdown": {"T": 78.5, "K": 89.2, "S": 87.8}}
      ],
      "off_ramps": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 78.5, "tks_breakdown": {"T": 82.1, "K": 75.3, "S": 78.1}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 72.3, "tks_breakdown": {"T": 68.9, "K": 79.2, "S": 68.8}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": 68.9, "tks_breakdown": {"T": 71.5, "K": 65.8, "S": 69.4}},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 65.4, "tks_breakdown": {"T": 62.7, "K": 68.9, "S": 64.6}}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": "12.9", "tks_breakdown": {"T": "10.5", "K": "15.3", "S": "12.9"}},
        {"id": "IO-WRL-005", "name": "Systems Administration", "percentage": "12.1", "tks_breakdown": {"T": "9.7", "K": "14.5", "S": "12.1"}},
        {"id": "IO-WRL-007", "name": "Technical Support", "percentage": "12.1", "tks_breakdown": {"T": "9.7", "K": "14.5", "S": "12.1"}},
        {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management", "percentage": "5.65", "tks_breakdown": {"T": "3.25", "K": "8.05", "S": "5.65"}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "5.24", "tks_breakdown": {"T": "2.84", "K": "7.64", "S": "5.24"}}
      ]
    },
    {
      "id": "OG-WRL-002",
      "name": "Cybersecurity Policy and Planning",
      "omp": ["752"],
      "category": "OG",
      "dcwf_info": {
        "opm_id": "752",
        "dcwf_title": "Cybersecurity Policy and Planning",
        "dcwf_description": "Responsible for developing and maintaining cybersecurity plans, strategy, and policy to support and align with organizational cybersecurity initiatives and regulatory compliance."
      },
      "tks_related": [
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 54.17, "tks_breakdown": {"T": 51.77, "K": 56.57, "S": 54.17}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 46.97, "tks_breakdown": {"T": 44.57, "K": 49.37, "S": 46.97}},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 37.5, "tks_breakdown": {"T": 35.1, "K": 39.9, "S": 37.5}},
        {"id": "OG-WRL-006", "name": "Information Systems/Cybersecurity Management", "percentage": 32.2, "tks_breakdown": {"T": 29.8, "K": 34.6, "S": 32.2}},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership", "percentage": 30, "tks_breakdown": {"T": 27.6, "K": 32.4, "S": 30}}
      ],
      "on_ramps": [
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 92.5, "tks_breakdown": {"T": 89.8, "K": 95.2, "S": 92.5}},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 88.7, "tks_breakdown": {"T": 85.3, "K": 92.1, "S": 88.7}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 85.3, "tks_breakdown": {"T": 82.1, "K": 88.9, "S": 84.9}},
        {"id": "OG-WRL-006", "name": "Information Systems/Cybersecurity Management", "percentage": 82.1, "tks_breakdown": {"T": 78.9, "K": 85.7, "S": 81.7}},
        {"id": "OG-WRL-008", "name": "Privacy Compliance", "percentage": 78.9, "tks_breakdown": {"T": 75.7, "K": 82.5, "S": 78.5}},
        {"id": "OG-WRL-009", "name": "Product Support Management", "percentage": 75.6, "tks_breakdown": {"T": 72.4, "K": 79.2, "S": 75.2}},
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": 72.4, "tks_breakdown": {"T": 69.2, "K": 76.0, "S": 72.0}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": 69.2, "tks_breakdown": {"T": 66.0, "K": 72.8, "S": 68.8}},
        {"id": "OG-WRL-012", "name": "Security Control Assessment", "percentage": 66.0, "tks_breakdown": {"T": 62.8, "K": 69.6, "S": 65.6}},
        {"id": "OG-WRL-013", "name": "Systems Authorization", "percentage": 62.8, "tks_breakdown": {"T": 59.6, "K": 66.4, "S": 62.4}},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 59.6, "tks_breakdown": {"T": 56.4, "K": 63.2, "S": 59.2}},
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 56.4, "tks_breakdown": {"T": 53.2, "K": 60.0, "S": 56.0}},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 53.2, "tks_breakdown": {"T": 50.0, "K": 56.8, "S": 52.8}},
        {"id": "DD-WRL-001", "name": "Cybersecurity Architecture", "percentage": 50.0, "tks_breakdown": {"T": 46.8, "K": 53.6, "S": 49.6}},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 46.8, "tks_breakdown": {"T": 43.6, "K": 50.4, "S": 46.4}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": 43.6, "tks_breakdown": {"T": 40.4, "K": 47.2, "S": 43.2}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 40.4, "tks_breakdown": {"T": 37.2, "K": 44.0, "S": 40.0}},
        {"id": "DD-WRL-005", "name": "Software Security Assessment", "percentage": 37.2, "tks_breakdown": {"T": 34.0, "K": 40.8, "S": 36.8}},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": 34.0, "tks_breakdown": {"T": 30.8, "K": 37.6, "S": 33.6}},
        {"id": "DD-WRL-007", "name": "Systems Testing and Evaluation", "percentage": 30.8, "tks_breakdown": {"T": 27.6, "K": 34.4, "S": 30.4}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": 27.6, "tks_breakdown": {"T": 24.4, "K": 31.2, "S": 27.2}},
        {"id": "IO-WRL-001", "name": "Data Analysis", "percentage": 24.4, "tks_breakdown": {"T": 21.2, "K": 28.0, "S": 24.0}},
        {"id": "IO-WRL-002", "name": "Database Administration", "percentage": 21.2, "tks_breakdown": {"T": 18.0, "K": 24.8, "S": 20.8}},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": 18.0, "tks_breakdown": {"T": 14.8, "K": 21.6, "S": 17.6}},
        {"id": "IO-WRL-004", "name": "Network Operations", "percentage": 14.8, "tks_breakdown": {"T": 11.6, "K": 18.4, "S": 14.4}},
        {"id": "IO-WRL-005", "name": "Systems Administration", "percentage": 11.6, "tks_breakdown": {"T": 8.4, "K": 15.2, "S": 11.2}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 8.4, "tks_breakdown": {"T": 5.2, "K": 12.0, "S": 8.0}},
        {"id": "IO-WRL-007", "name": "Technical Support", "percentage": 5.2, "tks_breakdown": {"T": 2.0, "K": 8.8, "S": 4.8}},
        {"id": "PD-WRL-001", "name": "Defensive Cybersecurity", "percentage": 2.0, "tks_breakdown": {"T": 1.5, "K": 2.5, "S": 2.0}},
        {"id": "PD-WRL-002", "name": "Digital Forensics", "percentage": 1.5, "tks_breakdown": {"T": 1.2, "K": 1.8, "S": 1.5}},
        {"id": "PD-WRL-003", "name": "Incident Response", "percentage": 1.2, "tks_breakdown": {"T": 0.9, "K": 1.5, "S": 1.2}},
        {"id": "PD-WRL-004", "name": "Infrastructure Support", "percentage": 0.9, "tks_breakdown": {"T": 0.6, "K": 1.2, "S": 0.9}},
        {"id": "PD-WRL-007", "name": "Vulnerability Analysis", "percentage": 0.6, "tks_breakdown": {"T": 0.3, "K": 0.9, "S": 0.6}},
        {"id": "IN-WRL-001", "name": "Cybercrime Investigation", "percentage": 0.3, "tks_breakdown": {"T": 0.1, "K": 0.5, "S": 0.3}},
        {"id": "IN-WRL-002", "name": "Digital Evidence Analysis", "percentage": 0.1, "tks_breakdown": {"T": 0.05, "K": 0.15, "S": 0.1}}
      ],
      "off_ramps": [
        {"id": "OG-WRL-013", "name": "Systems Authorization", "percentage": 95.8, "tks_breakdown": {"T": 92.6, "K": 98.4, "S": 96.4}},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 91.6, "tks_breakdown": {"T": 88.4, "K": 94.2, "S": 92.2}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 87.4, "tks_breakdown": {"T": 84.2, "K": 90.0, "S": 88.0}},
        {"id": "OG-WRL-008", "name": "Privacy Compliance", "percentage": 83.2, "tks_breakdown": {"T": 80.0, "K": 85.8, "S": 83.8}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 79.0, "tks_breakdown": {"T": 75.8, "K": 81.6, "S": 79.6}},
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": 74.8, "tks_breakdown": {"T": 71.6, "K": 77.4, "S": 75.4}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": 70.6, "tks_breakdown": {"T": 67.4, "K": 73.2, "S": 71.2}},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership", "percentage": 66.4, "tks_breakdown": {"T": 63.2, "K": 69.0, "S": 67.0}}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": "17.1", "tks_breakdown": {"T": "14.7", "K": "19.5", "S": "17.1"}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "9.28", "tks_breakdown": {"T": "6.88", "K": "11.68", "S": "9.28"}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": "8.24", "tks_breakdown": {"T": "5.84", "K": "10.64", "S": "8.24"}},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": "8.03", "tks_breakdown": {"T": "5.63", "K": "10.43", "S": "8.03"}},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": "6.47", "tks_breakdown": {"T": "4.07", "K": "8.87", "S": "6.47"}}
      ]
    },
    {
      "id": "OG-WRL-003",
      "name": "Cybersecurity Workforce Management",
      "omp": ["751"],
      "category": "OG",
      "tks_related": [
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 91.18, "tks_breakdown": {"T": 88.78, "K": 93.58, "S": 91.18}},
        {"id": "OG-WRL-015", "name": "Technology Portfolio Management", "percentage": 64.58, "tks_breakdown": {"T": 62.18, "K": 66.98, "S": 64.58}},
        {"id": "OG-WRL-016", "name": "Technology Program Auditing", "percentage": 45.31, "tks_breakdown": {"T": 42.91, "K": 47.71, "S": 45.31}},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership", "percentage": 43, "tks_breakdown": {"T": 40.6, "K": 45.4, "S": 43}},
        {"id": "OG-WRL-013", "name": "Systems Authorization", "percentage": 38.83, "tks_breakdown": {"T": 36.43, "K": 41.23, "S": 38.83}}
      ],
      "on_ramps": [
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 94.2, "tks_breakdown": {"T": 91.8, "K": 96.6, "S": 94.2}},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 90.8, "tks_breakdown": {"T": 88.4, "K": 93.2, "S": 90.8}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 87.4, "tks_breakdown": {"T": 85.0, "K": 89.8, "S": 87.4}},
        {"id": "OG-WRL-008", "name": "Privacy Compliance", "percentage": 84.0, "tks_breakdown": {"T": 81.6, "K": 86.4, "S": 84.0}},
        {"id": "OG-WRL-009", "name": "Product Support Management", "percentage": 80.6, "tks_breakdown": {"T": 78.2, "K": 83.0, "S": 80.6}},
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": 77.2, "tks_breakdown": {"T": 74.8, "K": 79.6, "S": 77.2}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": 73.8, "tks_breakdown": {"T": 71.4, "K": 76.2, "S": 73.8}},
        {"id": "OG-WRL-012", "name": "Security Control Assessment", "percentage": 70.4, "tks_breakdown": {"T": 68.0, "K": 72.8, "S": 70.4}},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": 67.0, "tks_breakdown": {"T": 64.6, "K": 69.4, "S": 67.0}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": 63.6, "tks_breakdown": {"T": 61.2, "K": 66.0, "S": 63.6}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 60.2, "tks_breakdown": {"T": 57.8, "K": 62.6, "S": 60.2}},
        {"id": "DD-WRL-005", "name": "Software Security Assessment", "percentage": 56.8, "tks_breakdown": {"T": 54.4, "K": 59.2, "S": 56.8}},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": 53.4, "tks_breakdown": {"T": 51.0, "K": 55.8, "S": 53.4}},
        {"id": "DD-WRL-007", "name": "Systems Testing and Evaluation", "percentage": 50.0, "tks_breakdown": {"T": 47.6, "K": 52.4, "S": 50.0}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": 46.6, "tks_breakdown": {"T": 44.2, "K": 49.0, "S": 46.6}},
        {"id": "IO-WRL-001", "name": "Data Analysis", "percentage": 43.2, "tks_breakdown": {"T": 40.8, "K": 45.6, "S": 43.2}},
        {"id": "IO-WRL-002", "name": "Database Administration", "percentage": 39.8, "tks_breakdown": {"T": 37.4, "K": 42.2, "S": 39.8}},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": 36.4, "tks_breakdown": {"T": 34.0, "K": 38.8, "S": 36.4}},
        {"id": "IO-WRL-004", "name": "Network Operations", "percentage": 33.0, "tks_breakdown": {"T": 30.6, "K": 35.4, "S": 33.0}},
        {"id": "IO-WRL-005", "name": "Systems Administration", "percentage": 29.6, "tks_breakdown": {"T": 27.2, "K": 32.0, "S": 29.6}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 26.2, "tks_breakdown": {"T": 23.8, "K": 28.6, "S": 26.2}},
        {"id": "IO-WRL-007", "name": "Technical Support", "percentage": 22.8, "tks_breakdown": {"T": 20.4, "K": 25.2, "S": 22.8}},
        {"id": "PD-WRL-001", "name": "Defensive Cybersecurity", "percentage": 19.4, "tks_breakdown": {"T": 17.0, "K": 21.8, "S": 19.4}},
        {"id": "PD-WRL-002", "name": "Digital Forensics", "percentage": 16.0, "tks_breakdown": {"T": 13.6, "K": 18.4, "S": 16.0}},
        {"id": "PD-WRL-003", "name": "Incident Response", "percentage": 12.6, "tks_breakdown": {"T": 10.2, "K": 15.0, "S": 12.6}},
        {"id": "PD-WRL-004", "name": "Infrastructure Support", "percentage": 9.2, "tks_breakdown": {"T": 6.8, "K": 11.6, "S": 9.2}},
        {"id": "PD-WRL-007", "name": "Vulnerability Analysis", "percentage": 5.8, "tks_breakdown": {"T": 3.4, "K": 8.2, "S": 5.8}},
        {"id": "IN-WRL-001", "name": "Cybercrime Investigation", "percentage": 2.4, "tks_breakdown": {"T": 1.0, "K": 3.8, "S": 2.4}},
        {"id": "IN-WRL-002", "name": "Digital Evidence Analysis", "percentage": 1.0, "tks_breakdown": {"T": 0.5, "K": 1.5, "S": 1.0}}
      ],
      "off_ramps": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 88.5, "tks_breakdown": {"T": 85.3, "K": 91.7, "S": 88.5}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 84.2, "tks_breakdown": {"T": 81.0, "K": 87.4, "S": 84.2}},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 79.9, "tks_breakdown": {"T": 76.7, "K": 83.1, "S": 79.9}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": 75.6, "tks_breakdown": {"T": 72.4, "K": 78.8, "S": 75.6}}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": "34.51", "tks_breakdown": {"T": "32.11", "K": "36.91", "S": "34.51"}},
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": "21.77", "tks_breakdown": {"T": "19.37", "K": "24.17", "S": "21.77"}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "5.84", "tks_breakdown": {"T": "3.44", "K": "8.24", "S": "5.84"}},
        {"id": "OG-WRL-014", "name": "Systems Security Management", "percentage": "5.84", "tks_breakdown": {"T": "3.44", "K": "8.24", "S": "5.84"}},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": "3.89", "tks_breakdown": {"T": "1.49", "K": "6.29", "S": "3.89"}}
      ]
    },
    {
      "id": "DD-WRL-001",
      "name": "Cybersecurity Architecture",
      "omp": ["652"],
      "category": "DD",
      "tks_related": [
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 90.38, "tks_breakdown": {"T": 87.98, "K": 92.78, "S": 90.38}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 58, "tks_breakdown": {"T": 55.6, "K": 60.4, "S": 58}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 52.59, "tks_breakdown": {"T": 50.19, "K": 54.99, "S": 52.59}},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": 51.45, "tks_breakdown": {"T": 49.05, "K": 53.85, "S": 51.45}},
        {"id": "IO-WRL-004", "name": "Network Operations", "percentage": 49.18, "tks_breakdown": {"T": 46.78, "K": 51.58, "S": 49.18}}
      ],
      "on_ramps": [
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 89.5, "tks_breakdown": {"T": 86.3, "K": 92.7, "S": 89.5}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 85.2, "tks_breakdown": {"T": 82.0, "K": 88.4, "S": 85.2}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": 80.9, "tks_breakdown": {"T": 77.7, "K": 84.1, "S": 80.9}}
      ],
      "off_ramps": [
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 92.3, "tks_breakdown": {"T": 89.1, "K": 95.5, "S": 92.3}},
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 88.7, "tks_breakdown": {"T": 85.5, "K": 91.9, "S": 88.7}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 85.1, "tks_breakdown": {"T": 81.9, "K": 88.3, "S": 85.1}},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 81.5, "tks_breakdown": {"T": 78.3, "K": 84.7, "S": 81.5}},
        {"id": "OG-WRL-010", "name": "Program Management", "percentage": 77.9, "tks_breakdown": {"T": 74.7, "K": 81.1, "S": 77.9}},
        {"id": "OG-WRL-007", "name": "Executive Cybersecurity Leadership", "percentage": 74.3, "tks_breakdown": {"T": 71.1, "K": 77.5, "S": 74.3}}
      ],
      "secondary_roles": [
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": "13.74", "tks_breakdown": {"T": "11.34", "K": "16.14", "S": "13.74"}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": "12.8", "tks_breakdown": {"T": "10.4", "K": "15.2", "S": "12.8"}},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": "8.53", "tks_breakdown": {"T": "6.13", "K": "10.93", "S": "8.53"}},
        {"id": "DD-WRL-006", "name": "Systems Requirements Planning", "percentage": "8.06", "tks_breakdown": {"T": "5.66", "K": "10.46", "S": "8.06"}},
        {"id": "OG-WRL-011", "name": "Secure Project Management", "percentage": "5.69", "tks_breakdown": {"T": "3.29", "K": "8.09", "S": "5.69"}}
      ]
    },
    {
      "id": "OG-WRL-004",
      "name": "Cybersecurity Curriculum Development",
      "omp": ["711"],
      "category": "OG",
      "dcwf_info": {
        "opm_id": "711",
        "dcwf_title": "Cybersecurity Curriculum Development",
        "dcwf_description": "Responsible for developing cybersecurity curriculum and training programs to enhance workforce capabilities."
      },
      "tks_related": [
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 85.2, "tks_breakdown": {"T": 82.8, "K": 87.6, "S": 85.2}},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 78.5, "tks_breakdown": {"T": 76.1, "K": 80.9, "S": 78.5}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 72.3, "tks_breakdown": {"T": 69.9, "K": 74.7, "S": 72.3}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": 68.9, "tks_breakdown": {"T": 66.5, "K": 71.3, "S": 68.9}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 65.4, "tks_breakdown": {"T": 63.0, "K": 67.8, "S": 65.4}}
      ],
      "on_ramps": [
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": 88.5, "tks_breakdown": {"T": 86.1, "K": 90.9, "S": 88.5}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 84.2, "tks_breakdown": {"T": 81.8, "K": 86.6, "S": 84.2}},
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 79.9, "tks_breakdown": {"T": 77.5, "K": 82.3, "S": 79.9}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": 75.6, "tks_breakdown": {"T": 73.2, "K": 78.0, "S": 75.6}}
      ],
      "off_ramps": [
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": 92.3, "tks_breakdown": {"T": 89.9, "K": 94.7, "S": 92.3}},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 88.7, "tks_breakdown": {"T": 86.3, "K": 91.1, "S": 88.7}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 85.1, "tks_breakdown": {"T": 82.7, "K": 87.5, "S": 85.1}},
        {"id": "OG-WRL-011", "name": "IT Project Manager", "percentage": 81.5, "tks_breakdown": {"T": 79.1, "K": 83.9, "S": 81.5}}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-005", "name": "Cybersecurity Instruction", "percentage": "18.45", "tks_breakdown": {"T": "16.05", "K": "20.85", "S": "18.45"}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": "12.2", "tks_breakdown": {"T": "9.8", "K": "14.6", "S": "12.2"}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": "10.8", "tks_breakdown": {"T": "8.4", "K": "13.2", "S": "10.8"}},
        {"id": "OG-WRL-011", "name": "IT Project Manager", "percentage": "8.7", "tks_breakdown": {"T": "6.3", "K": "11.1", "S": "8.7"}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": "6.5", "tks_breakdown": {"T": "4.1", "K": "8.9", "S": "6.5"}}
      ]
    },
    {
      "id": "OG-WRL-005",
      "name": "Cybersecurity Instruction",
      "omp": ["712"],
      "category": "OG",
      "dcwf_info": {
        "opm_id": "712",
        "dcwf_title": "Cybersecurity Instruction",
        "dcwf_description": "Responsible for providing cybersecurity instruction and training to develop workforce capabilities."
      },
      "tks_related": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 88.5, "tks_breakdown": {"T": 86.1, "K": 90.9, "S": 88.5}},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 82.1, "tks_breakdown": {"T": 79.7, "K": 84.5, "S": 82.1}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 78.6, "tks_breakdown": {"T": 76.2, "K": 81.0, "S": 78.6}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": 72.4, "tks_breakdown": {"T": 70.0, "K": 74.8, "S": 72.4}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 68.9, "tks_breakdown": {"T": 66.5, "K": 71.3, "S": 68.9}}
      ],
      "on_ramps": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 91.8, "tks_breakdown": {"T": 89.4, "K": 94.2, "S": 91.8}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": 87.4, "tks_breakdown": {"T": 85.0, "K": 89.8, "S": 87.4}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": 83.2, "tks_breakdown": {"T": 80.8, "K": 85.6, "S": 83.2}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": 79.0, "tks_breakdown": {"T": 76.6, "K": 81.4, "S": 79.0}}
      ],
      "off_ramps": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": 94.2, "tks_breakdown": {"T": 91.8, "K": 96.6, "S": 94.2}},
        {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning", "percentage": 90.1, "tks_breakdown": {"T": 87.7, "K": 92.5, "S": 90.1}},
        {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management", "percentage": 86.0, "tks_breakdown": {"T": 83.6, "K": 88.4, "S": 96.0}},
        {"id": "OG-WRL-011", "name": "IT Project Manager", "percentage": 81.9, "tks_breakdown": {"T": 79.5, "K": 84.3, "S": 81.9}}
      ],
      "secondary_roles": [
        {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development", "percentage": "22.8", "tks_breakdown": {"T": "20.4", "K": "25.2", "S": "22.8"}},
        {"id": "OG-WRL-011", "name": "IT Project Manager", "percentage": "15.6", "tks_breakdown": {"T": "13.2", "K": "18.0", "S": "15.6"}},
        {"id": "DD-WRL-003", "name": "Secure Software Development", "percentage": "11.3", "tks_breakdown": {"T": "8.9", "K": "13.7", "S": "11.3"}},
        {"id": "DD-WRL-004", "name": "Secure Systems Development", "percentage": "9.2", "tks_breakdown": {"T": "6.8", "K": "11.6", "S": "9.2"}},
        {"id": "DD-WRL-008", "name": "Technology Research and Development", "percentage": "7.1", "tks_breakdown": {"T": "4.7", "K": "9.5", "S": "7.1"}}
      ]
    },
    {
      "id": "IO-WRL-001",
      "name": "Data Analysis",
      "omp": ["661"],
      "category": "IO",
      "dcwf_info": {
        "opm_id": "661",
        "dcwf_title": "Data Analysis",
        "dcwf_description": "Responsible for analyzing data to identify patterns, trends, and insights to support cybersecurity decision-making."
      },
      "tks_related": [
        {"id": "IO-WRL-002", "name": "Database Administration", "percentage": 84.5, "tks_breakdown": {"T": 82.1, "K": 86.9, "S": 84.5}},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": 78.2, "tks_breakdown": {"T": 75.8, "K": 80.6, "S": 78.2}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 72.1, "tks_breakdown": {"T": 69.7, "K": 74.5, "S": 72.1}},
        {"id": "DD-WRL-001", "name": "Cybersecurity Architecture", "percentage": 68.9, "tks_breakdown": {"T": 66.5, "K": 71.3, "S": 68.9}},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 65.4, "tks_breakdown": {"T": 63.0, "K": 67.8, "S": 65.4}}
      ],
      "on_ramps": [
        {"id": "IO-WRL-002", "name": " Database Administration", "percentage": 89.9, "tks_breakdown": {"T": 87.5, "K": 92.3, "S": 89.9}},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": 85.2, "tks_breakdown": {"T": 82.8, "K": 87.6, "S": 85.2}},
        {"id": "DD-WRL-001", "name": "Cybersecurity Architecture", "percentage": 80.6, "tks_breakdown": {"T": 78.2, "K": 83.0, "S": 80.6}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 76.1, "tks_breakdown": {"T": 73.7, "K": 78.5, "S": 76.1}}
      ],
      "off_ramps": [
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": 91.8, "tks_breakdown": {"T": 89.4, "K": 94.2, "S": 91.8}},
        {"id": "DD-WRL-001", "name": "Cybersecurity Architecture", "percentage": 87.4, "tks_breakdown": {"T": 85.0, "K": 89.8, "S": 87.4}},
        {"id": "IO-WRL-002", "name": "Database Administration", "percentage": 83.2, "tks_breakdown": {"T": 80.8, "K": 85.6, "S": 83.2}},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": 79.0, "tks_breakdown": {"T": 76.6, "K": 81.4, "S": 79.0}}
      ],
      "secondary_roles": [
        {"id": "IO-WRL-002", "name": "Database Administration", "percentage": "16.8", "tks_breakdown": {"T": "14.4", "K": "19.2", "S": "16.8"}},
        {"id": "IO-WRL-006", "name": "Systems Security Analysis", "percentage": "13.4", "tks_breakdown": {"T": "11.0", "K": "15.8", "S": "13.4"}},
        {"id": "DD-WRL-001", "name": "Cybersecurity Architecture", "percentage": "9.7", "tks_breakdown": {"T": "7.3", "K": "12.1", "S": "9.7"}},
        {"id": "DD-WRL-002", "name": "Enterprise Architecture", "percentage": "7.2", "tks_breakdown": {"T": "4.8", "K": "9.6", "S": "7.2"}},
        {"id": "IO-WRL-003", "name": "Knowledge Management", "percentage": "5.9", "tks_breakdown": {"T": "3.5", "K": "8.3", "S": "5.9"}}
      ]
    },
    {
      "id": "IN-WRL-003",
      "name": "Threat Analyst",
      "omp": ["141"],
      "category": "IN",
      "dcwf_info": {
        "opm_id": "141",
        "dcwf_title": "Threat Analyst",
        "dcwf_description": "Collects, receives, processes, analyzes, and disseminates cybersecurity threat assessments."
      },
      "tks_related": [
        {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst", "percentage": 88.5, "tks_breakdown": {"T": 86.1, "K": 90.9, "S": 88.5}},
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": 84.2, "tks_breakdown": {"T": 81.8, "K": 86.6, "S": 84.2}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 79.9, "tks_breakdown": {"T": 77.5, "K": 82.3, "S": 79.9}},
        {"id": "IN-CI-001", "name": "Cyber Crime Investigator", "percentage": 75.6, "tks_breakdown": {"T": 73.2, "K": 78.0, "S": 75.6}},
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": 71.3, "tks_breakdown": {"T": 68.9, "K": 73.7, "S": 71.3}}
      ],
      "on_ramps": [
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": 92.5, "tks_breakdown": {"T": 90.1, "K": 94.9, "S": 92.5}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 88.8, "tks_breakdown": {"T": 86.4, "K": 91.2, "S": 88.8}},
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": 85.1, "tks_breakdown": {"T": 82.7, "K": 87.5, "S": 85.1}},
        {"id": "IN-CI-001", "name": "Cyber Crime Investigator", "percentage": 81.4, "tks_breakdown": {"T": 79.0, "K": 83.8, "S": 81.4}}
      ],
      "off_ramps": [
        {"id": "IN-CI-001", "name": "Cyber Crime Investigator", "percentage": 94.7, "tks_breakdown": {"T": 92.3, "K": 97.1, "S": 94.7}},
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": 91.4, "tks_breakdown": {"T": 89.0, "K": 93.8, "S": 91.4}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 88.1, "tks_breakdown": {"T": 85.7, "K": 90.5, "S": 88.1}},
        {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst", "percentage": 84.8, "tks_breakdown": {"T": 82.4, "K": 87.2, "S": 84.8}}
      ],
      "secondary_roles": [
        {"id": "IN-CI-001", "name": "Cyber Crime Investigator", "percentage": "15.8", "tks_breakdown": {"T": "13.4", "K": "18.2", "S": "15.8"}},
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": "12.6", "tks_breakdown": {"T": "10.2", "K": "15.0", "S": "12.6"}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": "9.4", "tks_breakdown": {"T": "7.0", "K": "11.8", "S": "9.4"}},
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": "6.2", "tks_breakdown": {"T": "3.8", "K": "8.6", "S": "6.2"}},
        {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst", "percentage": "3.0", "tks_breakdown": {"T": "0.6", "K": "5.4", "S": "3.0"}}
      ]
    },
    {
      "id": "PR-IR-001",
      "name": "Cyber Defense Incident Responder",
      "omp": ["531"],
      "category": "PR",
      "dcwf_info": {
        "opm_id": "531",
        "dcwf_title": "Cyber Defense Incident Responder",
        "dcwf_description": "Investigates, analyzes, and responds to cyber events within the network environment or enclave."
      },
      "tks_related": [
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": 87.5, "tks_breakdown": {"T": 84.5, "K": 90.5, "S": 87.5}},
        {"id": "PR-INF-001", "name": "Cyber Defense Infrastructure Support Specialist", "percentage": 82.3, "tks_breakdown": {"T": 79.3, "K": 85.3, "S": 82.4}},
        {"id": "IN-WRL-003", "name": "Threat Analyst", "percentage": 78.9, "tks_breakdown": {"T": 75.9, "K": 81.9, "S": 78.9}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 75.4, "tks_breakdown": {"T": 72.4, "K": 78.4, "S": 75.4}},
        {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist", "percentage": 71.8, "tks_breakdown": {"T": 68.8, "K": 74.8, "S": 71.8}}
      ],
      "on_ramps": [
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": 91.2, "tks_breakdown": {"T": 88.2, "K": 94.2, "S": 91.2}},
        {"id": "PR-INF-001", "name": "Cyber Defense Infrastructure Support Specialist", "percentage": 86.8, "tks_breakdown": {"T": 83.8, "K": 89.8, "S": 86.8}},
        {"id": "IN-WRL-003", "name": "Threat Analyst", "percentage": 83.4, "tks_breakdown": {"T": 80.4, "K": 86.4, "S": 83.4}}
      ],
      "off_ramps": [
        {"id": "OV-MG-001", "name": "Information Systems Security Manager", "percentage": 89.7, "tks_breakdown": {"T": 86.7, "K": 92.7, "S": 89.7}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 85.3, "tks_breakdown": {"T": 82.3, "K": 88.3, "S": 85.3}},
        {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist", "percentage": 81.9, "tks_breakdown": {"T": 78.9, "K": 84.9, "S": 81.9}}
      ],
      "secondary_roles": [
        {"id": "PR-DA-001", "name": "Cyber Defense Analyst", "percentage": "16.8", "tks_breakdown": {"T": "13.8", "K": "19.8", "S": "16.8"}},
        {"id": "PR-INF-001", "name": "Cyber Defense Infrastructure Support Specialist", "percentage": "12.4", "tks_breakdown": {"T": "9.4", "K": "15.4", "S": "12.4"}},
        {"id": "IN-WRL-003", "name": "Threat Analyst", "percentage": "8.9", "tks_breakdown": {"T": "5.9", "K": "11.9", "S": "8.9"}}
      ]
    },
    {
      "id": "SP-DEV-001",
      "name": "Software Developer",
      "omp": ["621"],
      "category": "SP",
      "dcwf_info": {
        "opm_id": "621",
        "dcwf_title": "Software Developer",
        "dcwf_description": "Develops and writes/codes new computer applications, software, or specialized utility programs following software assurance best practices."
      },
      "tks_related": [
        {"id": "SP-DEV-002", "name": "Secure Software Assessor", "percentage": 92.7, "tks_breakdown": {"T": 89.7, "K": 95.7, "S": 92.7}},
        {"id": "SP-SYS-001", "name": "Information Systems Security Developer", "percentage": 88.4, "tks_breakdown": {"T": 85.4, "K": 91.4, "S": 88.4}},
        {"id": "SP-SYS-002", "name": "Systems Developer", "percentage": 84.1, "tks_breakdown": {"T": 81.1, "K": 87.1, "S": 84.1}},
        {"id": "DD-WRL-001", "name": "Security Architect", "percentage": 79.8, "tks_breakdown": {"T": 76.8, "K": 82.8, "S": 79.8}},
        {"id": "SP-TE-001", "name": "System Testing and Evaluation Specialist", "percentage": 76.5, "tks_breakdown": {"T": 73.5, "K": 79.5, "S": 76.5}}
      ],
      "on_ramps": [
        {"id": "SP-SYS-002", "name": "Systems Developer", "percentage": 94.3, "tks_breakdown": {"T": 91.3, "K": 97.3, "S": 94.3}},
        {"id": "SP-SYS-001", "name": "Information Systems Security Developer", "percentage": 89.7, "tks_breakdown": {"T": 86.7, "K": 92.7, "S": 89.7}},
        {"id": "DD-WRL-001", "name": "Security Architect", "percentage": 85.1, "tks_breakdown": {"T": 82.1, "K": 88.1, "S": 85.1}}
      ],
      "off_ramps": [
        {"id": "DD-WRL-001", "name": "Security Architect", "percentage": 91.6, "tks_breakdown": {"T": 88.6, "K": 94.6, "S": 91.6}},
        {"id": "OV-MG-001", "name": "Information Systems Security Manager", "percentage": 87.9, "tks_breakdown": {"T": 84.9, "K": 90.9, "S": 87.9}},
        {"id": "SP-DEV-002", "name": "Secure Software Assessor", "percentage": 84.2, "tks_breakdown": {"T": 87.2, "K": 81.2, "S": 84.2}}
      ],
      "secondary_roles": [
        {"id": "SP-DEV-002", "name": "Secure Software Assessor", "percentage": "18.3", "tks_breakdown": {"T": "15.3", "K": "21.3", "S": "18.3"}},
        {"id": "SP-SYS-001", "name": "Information Systems Security Developer", "percentage": "14.7", "tks_breakdown": {"T": "11.7", "K": "17.7", "S": "14.7"}},
        {"id": "SP-SYS-002", "name": "Systems Developer", "percentage": "11.1", "tks_breakdown": {"T": "8.1", "K": "14.1", "S": "11.1"}}
      ]
    },
    {
      "id": "AN-ASA-001",
      "name": "All-Source Analyst",
      "omp": ["111"],
      "category": "AN",
      "dcwf_info": {
        "opm_id": "111",
        "dcwf_title": "All-Source Analyst",
        "dcwf_description": "Analyzes data/information from one or multiple sources to conduct preparation of the environment, respond to requests for information."
      },
      "tks_related": [
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": 85.0, "tks_breakdown": {"T": 82.6, "K": 87.4, "S": 85.0}},
        {"id": "AN-WRL-031", "name": "Joint Targeting Analyst", "percentage": 81.0, "tks_breakdown": {"T": 78.6, "K": 83.4, "S": 81.0}},
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 77.0, "tks_breakdown": {"T": 74.6, "K": 79.4, "S": 77.0}},
        {"id": "CO-CL-001", "name": "All-Source Collection Manager", "percentage": 73.0, "tks_breakdown": {"T": 70.6, "K": 75.4, "S": 73.0}}
      ],
      "on_ramps": [
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": 90.0, "tks_breakdown": {"T": 87.6, "K": 92.4, "S": 90.0}},
        {"id": "AN-WRL-031", "name": "Joint Targeting Analyst", "percentage": 86.0, "tks_breakdown": {"T": 83.6, "K": 88.4, "S": 86.0}}
      ],
      "off_ramps": [
        {"id": "IN-FO-001", "name": "Forensics Analyst", "percentage": 88.0, "tks_breakdown": {"T": 85.6, "K": 90.4, "S": 88.0}},
        {"id": "CO-CL-001", "name": "All-Source Collection Manager", "percentage": 84.0, "tks_breakdown": {"T": 81.6, "K": 86.4, "S": 84.0}}
      ],
      "secondary_roles": [
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": "12.0", "tks_breakdown": {"T": "9.6", "K": "14.4", "S": "12.0"}},
        {"id": "AN-WRL-031", "name": "Joint Targeting Analyst", "percentage": "8.0", "tks_breakdown": {"T": "5.6", "K": "10.4", "S": "8.0"}}
      ]
    },
    {
      "id": "PR-DA-001",
      "omp": ["511"],
      "category": "PR", 
      "dcwf_info": {
        "opm_id": "511",
        "dcwf_title": "Cyber Defense Analyst",
        "dcwf_description": "Uses protective monitoring technologies to scan, identify, contain, eradicate and recover from actions of active adversaries who have gained access to an organization's network."
      },
      "tks_related": [
        {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder", "percentage": 89.0, "tks_breakdown": {"T": 86.6, "K": 91.4, "S": 89.0}},
        {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist", "percentage": 85.0, "tks_breakdown": {"T": 82.6, "K": 87.4, "S": 85.0}},
        {"id": "PR-INF-001", "name": "Cyber Defense Infrastructure Support Specialist", "percentage": 81.0, "tks_breakdown": {"T": 78.6, "K": 83.4, "S": 81.0}},
        {"id": "PR-WRL-051", "name": "Red Team Specialist", "percentage": 77.0, "tks_breakdown": {"T": 74.6, "K": 79.4, "S": 77.0}}
      ],
      "on_ramps": [
        {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder", "percentage": 92.0, "tks_breakdown": {"T": 89.6, "K": 94.4, "S": 92.0}},
        {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist", "percentage": 88.0, "tks_breakdown": {"T": 85.6, "K": 90.4, "S": 88.0}}
      ],
      "off_ramps": [
        {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder", "percentage": 94.0, "tks_breakdown": {"T": 91.6, "K": 96.4, "S": 94.0}},
        {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist", "percentage": 90.0, "tks_breakdown": {"T": 87.6, "K": 92.4, "S": 90.0}}
      ],
      "secondary_roles": [
        {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder", "percentage": "15.0", "tks_breakdown": {"T": "12.6", "K": "17.4", "S": "15.0"}},
        {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist", "percentage": "11.0", "tks_breakdown": {"T": "8.6", "K": "13.4", "S": "11.0"}}
      ]
    },
    {
      "id": "WRL-OPM-112",
      "name": "All-Source Analyst",
      "omp": ["112"],
      "category": "AN", 
      "dcwf_info": {
        "opm_id": "112",
        "dcwf_title": "All-Source Analyst",
        "dcwf_description": "Analyst responsible for collecting, processing, and analyzing information from multiple sources to support cybersecurity operations."
      },
      "tks_related": [
        {"id": "AN-ASA-001", "name": "All-Source Analyst", "percentage": 95.0, "tks_breakdown": {"T": 92.5, "K": 97.5, "S": 95.0}},
        {"id": "AN-WRL-022", "name": "Digital Network Exploitation Analyst", "percentage": 87.3, "tks_breakdown": {"T": 84.8, "K": 89.8, "S": 87.3}},
        {"id": "AN-WRL-031", "name": "Joint Targeting Analyst", "percentage": 82.7, "tks_breakdown": {"T": 80.2, "K": 85.2, "S": 82.7}},
        {"id": "IN-WRL-003", "name": "Threat Analyst", "percentage": 78.4, "tks_breakdown": {"T": 75.9, "K": 80.9, "S": 78.4}},
        {"id": "CO-CL-001", "name": "All-Source Collection Manager", "percentage": 74.1, "tks_breakdown": {"T": 71.6, "K": 76.6, "S": 74.1}}
      ],
      "on_ramps": [
        {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst", "percentage": 89.5, "tks_breakdown": {"T": 87.0, "K": 92.0, "S": 89.5}},
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": 85.2, "tks_breakdown": {"T": 82.7, "K": 87.7, "S": 85.2}}
      ],
      "off_ramps": [
        {"id": "CO-CL-001", "name": "All-Source Collection Manager", "percentage": 91.8, "tks_breakdown": {"T": 89.3, "K": 94.3, "S": 91.8}},
        {"id": "CO-PL-001", "name": "Cyber Intelligence Planner", "percentage": 87.6, "tks_breakdown": {"T": 85.1, "K": 90.1, "S": 87.6}}
      ],
      "secondary_roles": [
        {"id": "AN-XA-001", "name": "Exploitation Analyst", "percentage": "12.8", "tks_breakdown": {"T": "10.3", "K": "15.3", "S": "12.8"}},
        {"id": "IN-WRL-003", "name": "Threat Analyst", "percentage": "8.4", "tks_breakdown": {"T": "5.9", "K": "10.9", "S": "8.4"}}
      ]
    },
    {
      "id": "WRL-OPM-641", 
      "name": "Systems Requirements Planner",
      "omp": ["641"],
      "category": "SP",
      "dcwf_info": {
        "opm_id": "641",
        "dcwf_title": "Systems Requirements Planner",
        "dcwf_description": "Plans and develops system requirements for complex cybersecurity systems and ensures comprehensive requirement specifications."
      },
      "tks_related": [
        {"id": "SP-ARC-001", "name": "Enterprise Architect", "percentage": 93.4, "tks_breakdown": {"T": 90.9, "K": 95.9, "S": 93.4}},
        {"id": "SP-DEV-001", "name": "Software Developer", "percentage": 87.1, "tks_breakdown": {"T": 84.6, "K": 89.6, "S": 87.1}},
        {"id": "SP-SYS-001", "name": "Information Systems Security Developer", "percentage": 82.8, "tks_breakdown": {"T": 80.3, "K": 85.3, "S": 82.8}},
        {"id": "OV-MG-001", "name": "Information Systems Security Manager", "percentage": 78.5, "tks_breakdown": {"T": 76.0, "K": 81.0, "S": 78.5}},
        {"id": "SP-TE-001", "name": "System Testing and Evaluation Specialist", "percentage": 74.2, "tks_breakdown": {"T": 71.7, "K": 76.7, "S": 74.2}}
      ],
      "on_ramps": [
        {"id": "SP-SYS-002", "name": "Systems Developer", "percentage": 91.3, "tks_breakdown": {"T": 88.8, "K": 93.8, "S": 91.3}},
        {"id": "SP-DEV-001", "name": "Software Developer", "percentage": 86.9, "tks_breakdown": {"T": 84.4, "K": 89.4, "S": 86.9}}
      ],
      "off_ramps": [
        {"id": "SP-ARC-001", "name": "Enterprise Architect", "percentage": 94.7, "tks_breakdown": {"T": 92.2, "K": 97.2, "S": 94.7}},
        {"id": "OV-MG-001", "name": "Information Systems Security Manager", "percentage": 88.4, "tks_breakdown": {"T": 85.9, "K": 90.9, "S": 88.4}}
      ],
      "secondary_roles": [
        {"id": "SP-SYS-001", "name": "Information Systems Security Developer", "percentage": "14.6", "tks_breakdown": {"T": "12.1", "K": "17.1", "S": "14.6"}},
        {"id": "SP-TE-001", "name": "System Testing and Evaluation Specialist", "percentage": "10.2", "tks_breakdown": {"T": "7.7", "K": "12.7", "S": "10.2"}}
      ]
    }
  ],
  "categories": {
    "AN": {"class": "analysis", "name": "Analysis", "roles": 5},
    "DD": {"class": "design-development", "name": "Design and Development", "roles": 9},
    "IN": {"class": "investigation", "name": "Investigation", "roles": 3},
    "IO": {"class": "implementation-operation", "name": "Implementation and Operation", "roles": 7},
    "OG": {"class": "oversight-governance", "name": "Oversight and Governance", "roles": 16},
    "PD": {"class": "protection-defense", "name": "Protection and Defense", "roles": 2},
    "PR": {"class": "protection-defense", "name": "Protection and Defense", "roles": 5},
    "CO": {"class": "collections-operations", "name": "Collections and Operations", "roles": 7},
    "SP": {"class": "specialized", "name": "Specialized", "roles": 10},
    "OV": {"class": "oversight", "name": "Oversight", "roles": 8},
    "MG": {"class": "management", "name": "Management", "roles": 2},
    "EX": {"class": "executive", "name": "Executive", "roles": 3}
  }
};

const searchIndices = {
  "by_omp": {
    "723": {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management"},
    "752": {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
    "751": {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
    "711": {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
    "712": {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
    "652": {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"},
    "661": {"id": "IO-WRL-001", "name": "Data Analysis"},
    "141": {"id": "IN-WRL-003", "name": "Threat Analyst"},
    "151": {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst"},
    "121": {"id": "AN-XA-001", "name": "Exploitation Analyst"},
    "211": {"id": "IN-FO-001", "name": "Forensics Analyst"},
    "221": {"id": "IN-CI-001", "name": "Cyber Crime Investigator"},
    "511": {"id": "PR-DA-001", "name": "Cyber Defense Analyst"},
    "111": {"id": "AN-ASA-001", "name": "All-Source Analyst"},
    "531": {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder"},
    "621": {"id": "SP-DEV-001", "name": "Software Developer"},
    "622": {"id": "WRL-OPM-622", "name": "Secure Software Assessor"},
    "623": {"id": "WRL-OPM-623", "name": "AI/ML Specialist"},
    "624": {"id": "WRL-OPM-624", "name": "Data Operations Specialist"},
    "625": {"id": "WRL-OPM-625", "name": "Product Designer User Interface (UI)"},
    "626": {"id": "WRL-OPM-626", "name": "Service Designer User Experience (UX)"},
    "627": {"id": "WRL-OPM-627", "name": "DevSecOps Specialist"},
    "628": {"id": "WRL-OPM-628", "name": "Software/Cloud Architect"},
    "629": {"id": "WRL-OPM-629", "name": "Test Evaluation Specialist"},
    "632": {"id": "WRL-OPM-632", "name": "Systems Developer"},
    "641": {"id": "WRL-OPM-641", "name": "Systems Requirements Planner"},
    "651": {"id": "WRL-OPM-651", "name": "Enterprise Architect"},
    "653": {"id": "WRL-OPM-653", "name": "Data Architect"},
    "661": {"id": "WRL-OPM-661", "name": "Research & Development Specialist"},
    "671": {"id": "WRL-OPM-671", "name": "System Testing and Evaluation Specialist"},
    "672": {"id": "WRL-OPM-672", "name": "AI Test & Evaluation Specialist"},
    "673": {"id": "WRL-OPM-673", "name": "Software Test & Evaluation Specialist"},
    "112": {"id": "AN-WRL-012", "name": "All-Source Analyst"},
    "122": {"id": "AN-WRL-022", "name": "Digital Network Exploitation Analyst"},
    "131": {"id": "AN-WRL-031", "name": "Joint Targeting Analyst"},
    "132": {"id": "AN-WRL-032", "name": "Target Digital Network Analyst"},
    "133": {"id": "AN-WRL-033", "name": "Target Analyst Reporter"},
    "212": {"id": "IN-FO-002", "name": "Cyber Defense Forensic Analyst"},
    "311": {"id": "CO-CL-001", "name": "All-Source Collection Manager"},
    "312": {"id": "CO-CL-002", "name": "All-Source Collection Requirements Manager"},
    "322": {"id": "CO-WRL-022", "name": "Cyberspace Operator"},
    "331": {"id": "CO-PL-001", "name": "Cyber Intelligence Planner"},
    "332": {"id": "CO-PL-002", "name": "Cyber Operations Planner"},
    "333": {"id": "CO-WRL-033", "name": "Cyber Operations Planner"},
    "341": {"id": "CO-WRL-041", "name": "Cyberspace Capability Developer"},
    "411": {"id": "OM-TS-001", "name": "Technical Support Specialist"},
    "423": {"id": "IO-WRL-023", "name": "Data Scientist"},
    "424": {"id": "IO-WRL-024", "name": "Data Steward"},
    "442": {"id": "IO-WRL-042", "name": "Network Technician"},
    "443": {"id": "IO-WRL-043", "name": "Network Analyst"},
    "462": {"id": "IO-WRL-062", "name": "Control Systems Security Specialist"},
    "463": {"id": "IO-WRL-063", "name": "Host Analyst"},
    "521": {"id": "PR-INF-001", "name": "Cyber Defense Infrastructure Support Specialist"},
    "531": {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder"},
    "541": {"id": "PR-VA-001", "name": "Vulnerability Assessment Specialist"},
    "551": {"id": "PR-WRL-051", "name": "Red Team Specialist"},
    "611": {"id": "SP-RM-001", "name": "Authorizing Official/Designated Representative"},
    "612": {"id": "SP-RM-002", "name": "Security Control Assessor"},
    "623": {"id": "SP-WRL-023", "name": "AI/ML Specialist"},
    "624": {"id": "SP-WRL-024", "name": "Data Operations Specialist"},
    "625": {"id": "SP-WRL-025", "name": "Product Designer User Interface (UI)"},
    "711": {"id": "OG-WRL-004", "name": "Cyber Instructional Curriculum Developer"},
    "722": {"id": "OV-MG-001", "name": "Information Systems Security Manager"},
    "731": {"id": "OV-LG-001", "name": "Cyber Legal Advisor"},
    "732": {"id": "OV-LG-002", "name": "Privacy Compliance Manager"},
    "733": {"id": "OV-WRL-033", "name": "AI Risk & Ethics Specialist"},
    "753": {"id": "OV-WRL-053", "name": "AI Adoption Specialist"},
    "801": {"id": "OV-PM-001", "name": "Program Manager"},
    "802": {"id": "OV-PM-002", "name": "IT Project Manager"},
    "803": {"id": "OV-PM-003", "name": "Product Support Manager"},
    "804": {"id": "OV-PM-004", "name": "IT Investment/Portfolio Manager"},
    "805": {"id": "OV-PM-005", "name": "IT Program Auditor"},
    "806": {"id": "MG-WRL-006", "name": "Product Manager"},
    "901": {"id": "OV-EX-001", "name": "Executive Cyber Leader"},
    "902": {"id": "EX-WRL-002", "name": "AI Innovation Leader"},
    "903": {"id": "EX-WRL-003", "name": "Data Officer"}
  },
  "by_wrl": {
    "PR-IR-001": {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder"},
    "SP-DEV-001": {"id": "SP-DEV-001", "name": "Software Developer"},
    "OG-WRL-001": {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management"},
    "OG-WRL-002": {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
    "OG-WRL-003": {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
    "OG-WRL-004": {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
    "OG-WRL-005": {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
    "DD-WRL-001": {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"},
    "IO-WRL-001": {"id": "IO-WRL-001", "name": "Data Analysis"},
    "IN-WRL-003": {"id": "IN-WRL-003", "name": "Threat Analyst"},
    "AN-LA-001": {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst"},
    "AN-XA-001": {"id": "AN-XA-001", "name": "Exploitation Analyst"},
    "IN-FO-001": {"id": "IN-FO-001", "name": "Forensics Analyst"},
    "IN-CI-001": {"id": "IN-CI-001", "name": "Cyber Crime Investigator"},
    "PR-DA-001": {"id": "PR-DA-001", "name": "Cyber Defense Analyst"},
    "AN-ASA-001": {"id": "AN-ASA-001", "name": "All-Source Analyst"}
  },
  "by_name": {
    "communications security (comsec) management": {"id": "OG-WRL-001", "name": "Communications Security (COMSEC) Management"},
    "cybersecurity policy and planning": {"id": "OG-WRL-002", "name": "Cybersecurity Policy and Planning"},
    "cybersecurity workforce management": {"id": "OG-WRL-003", "name": "Cybersecurity Workforce Management"},
    "cybersecurity curriculum development": {"id": "OG-WRL-004", "name": "Cybersecurity Curriculum Development"},
    "cybersecurity instruction": {"id": "OG-WRL-005", "name": "Cybersecurity Instruction"},
    "cybersecurity architecture": {"id": "DD-WRL-001", "name": "Cybersecurity Architecture"},
    "data analysis": {"id": "IO-WRL-001", "name": "Data Analysis"},
    "threat analyst": {"id": "IN-WRL-003", "name": "Threat Analyst"},
    "multi-disciplined language analyst": {"id": "AN-LA-001", "name": "Multi-Disciplined Language Analyst"},
    "exploitation analyst": {"id": "AN-XA-001", "name": "Exploitation Analyst"},
    "forensics analyst": {"id": "IN-FO-001", "name": "Forensics Analyst"},
    "cyber crime investigator": {"id": "IN-CI-001", "name": "Cyber Crime Investigator"},
    "cyber defense analyst": {"id": "PR-DA-001", "name": "Cyber Defense Analyst"},
    "all-source analyst": {"id": "AN-ASA-001", "name": "All-Source Analyst"},
    "cyber defense incident responder": {"id": "PR-IR-001", "name": "Cyber Defense Incident Responder"},
    "software developer": {"id": "SP-DEV-001", "name": "Software Developer"}
  }
};

// Application state
let currentRole = null;
let currentSuggestionIndex = -1;

// DOM elements
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearch');
const searchSuggestions = document.getElementById('searchSuggestions');
const loadingState = document.getElementById('loadingState');
const errorState = document.getElementById('errorState');
const roleDisplay = document.getElementById('roleDisplay');
const emptyState = document.getElementById('emptyState');

// Role display elements
const roleCategoryBadge = document.getElementById('roleCategoryBadge');
const roleOmpId = document.getElementById('roleOmpId');
const roleWrlId = document.getElementById('roleWrlId');
const roleName = document.getElementById('roleName');
const roleCategoryDescription = document.getElementById('roleCategoryDescription');
const tksRelatedList = document.getElementById('tksRelatedList');
const onRampsList = document.getElementById('onRampsList');
const offRampsList = document.getElementById('offRampsList');
const secondaryRolesList = document.getElementById('secondaryRolesList');

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
  initializeEventListeners();
  handleInitialLoad();
});

function initializeEventListeners() {
  // Search input events
  searchInput.addEventListener('input', handleSearchInput);
  searchInput.addEventListener('keydown', handleSearchKeydown);
  searchInput.addEventListener('blur', hideSuggestions);
  
  // Clear search button
  clearSearchBtn.addEventListener('click', clearSearch);
  
  // Example search buttons
  const exampleBtns = document.querySelectorAll('.example-btn');
  exampleBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const searchTerm = this.getAttribute('data-search');
      searchInput.value = searchTerm;
      performSearch(searchTerm);
    });
  });

  // Browser history
  window.addEventListener('popstate', handleHistoryChange);
}

function handleInitialLoad() {
  const urlParams = new URLSearchParams(window.location.search);
  const roleId = urlParams.get('role');
  
  if (roleId) {
    const role = findRoleById(roleId);
    if (role) {
      displayRole(role);
      searchInput.value = role.name;
    } else {
      showEmptyState();
    }
  } else {
    showEmptyState();
  }
}

function handleSearchInput(event) {
  const query = event.target.value.trim();
  
  if (query.length === 0) {
    hideSuggestions();
    return;
  }
  
  if (query.length >= 2) {
    showSuggestions(query);
  }
}

function handleSearchKeydown(event) {
  const suggestions = document.querySelectorAll('.suggestion-item');
  
  switch (event.key) {
    case 'Enter':
      event.preventDefault();
      if (currentSuggestionIndex >= 0 && suggestions[currentSuggestionIndex]) {
        const roleId = suggestions[currentSuggestionIndex].getAttribute('data-role-id');
        selectRole(roleId);
      } else {
        performSearch(searchInput.value.trim());
      }
      break;
      
    case 'ArrowDown':
      event.preventDefault();
      currentSuggestionIndex = Math.min(currentSuggestionIndex + 1, suggestions.length - 1);
      updateSuggestionSelection(suggestions);
      break;
      
    case 'ArrowUp':
      event.preventDefault();
      currentSuggestionIndex = Math.max(currentSuggestionIndex - 1, -1);
      updateSuggestionSelection(suggestions);
      break;
      
    case 'Escape':
      hideSuggestions();
      break;
  }
}

function showSuggestions(query) {
  const suggestions = searchForRoles(query);
  
  if (suggestions.length === 0) {
    hideSuggestions();
    return;
  }
  
  const html = suggestions.map(suggestion => 
    `<div class="suggestion-item" data-role-id="${suggestion.id}">
      <div class="suggestion-name">${suggestion.name}</div>
      <div class="suggestion-details">
        OMP: ${suggestion.omp.join(', ')} | WRL: ${suggestion.id}
      </div>
    </div>`
  ).join('');
  
  searchSuggestions.innerHTML = html;
  searchSuggestions.classList.remove('hidden');
  
  // Add click listeners to suggestions
  const suggestionItems = searchSuggestions.querySelectorAll('.suggestion-item');
  suggestionItems.forEach(item => {
    item.addEventListener('mousedown', function(event) {
      event.preventDefault(); // Prevent blur event
      const roleId = this.getAttribute('data-role-id');
      selectRole(roleId);
    });
  });
  
  currentSuggestionIndex = -1;
}

function updateSuggestionSelection(suggestions) {
  suggestions.forEach((item, index) => {
    if (index === currentSuggestionIndex) {
      item.classList.add('selected');
    } else {
      item.classList.remove('selected');
    }
  });
}

function hideSuggestions() {
  setTimeout(() => {
    searchSuggestions.classList.add('hidden');
    currentSuggestionIndex = -1;
  }, 150);
}

function clearSearch() {
  searchInput.value = '';
  hideSuggestions();
  showEmptyState();
  updateURL(null);
}

function searchForRoles(query) {
  const normalizedQuery = query.toLowerCase();
  const results = [];
  
  // Search by exact OMP ID
  if (searchIndices.by_omp[normalizedQuery]) {
    const result = searchIndices.by_omp[normalizedQuery];
    const role = findRoleById(result.id);
    if (role) results.push(role);
  }
  
  // Search by exact WRL ID
  const upperQuery = query.toUpperCase();
  if (searchIndices.by_wrl[upperQuery]) {
    const result = searchIndices.by_wrl[upperQuery];
    const role = findRoleById(result.id);
    if (role && !results.find(r => r.id === role.id)) results.push(role);
  }
  
  // Search by name (exact match first)
  if (searchIndices.by_name[normalizedQuery]) {
    const result = searchIndices.by_name[normalizedQuery];
    const role = findRoleById(result.id);
    if (role && !results.find(r => r.id === role.id)) results.push(role);
  }
  
  // Search by partial name match
  appData.work_roles.forEach(role => {
    if (role.name && role.name.toLowerCase().includes(normalizedQuery) && 
        !results.find(r => r.id === role.id)) {
      results.push(role);
    }
  });
  
  return results.slice(0, 5); // Limit to 5 suggestions
}

function performSearch(query) {
  if (!query) {
    showErrorState();
    return;
  }
  
  showLoadingState();
  
  setTimeout(() => {
    const results = searchForRoles(query);
    
    if (results.length > 0) {
      selectRole(results[0].id);
    } else {
      showErrorState();
    }
  }, 300);
}

function selectRole(roleId) {
  const role = findRoleById(roleId);
  
  if (role) {
    displayRole(role);
    searchInput.value = role.name;
    hideSuggestions();
    updateURL(roleId);
  } else {
    showErrorState();
  }
}

function findRoleById(id) {
  return appData.work_roles.find(role => role.id === id);
}

function displayRole(role) {
  currentRole = role;
  
  // Hide other states
  hideAllStates();
  roleDisplay.classList.remove('hidden');
  
  // Update role card
  const category = appData.categories[role.category];
  if (category) {
  roleCategoryBadge.textContent = category.name;
  roleCategoryBadge.className = `role-category-badge ${category.class}`;
  } else {
    roleCategoryBadge.textContent = role.category || "Unknown";
    roleCategoryBadge.className = "role-category-badge unknown";
  }
  
  roleOmpId.textContent = `OMP: ${role.omp.join(', ')}`;
  roleWrlId.textContent = `WRL: ${role.id}`;
  roleName.textContent = role.name;
  roleCategoryDescription.textContent = category ? category.name : (role.category || "Unknown");
  
  // Display DCWF information if available
  const dcwfInfo = document.getElementById('dcwfInfo');
  const dcwfOpmId = document.getElementById('dcwfOmpId');
  const dcwfTitle = document.getElementById('dcwfTitle');
  const dcwfDescription = document.getElementById('dcwfDescription');
  
  
  if (role.dcwf_info && dcwfInfo && dcwfOpmId && dcwfTitle && dcwfDescription) {
    dcwfOpmId.textContent = role.dcwf_info.opm_id;
    dcwfTitle.textContent = role.dcwf_info.dcwf_title;
    dcwfDescription.textContent = role.dcwf_info.dcwf_description;
    dcwfInfo.classList.remove('hidden');
  } else if (dcwfInfo) {
    dcwfInfo.classList.add('hidden');
  }
  
  // Update relationship panels
  if (tksRelatedList) displayRelationshipList(tksRelatedList, role.tks_related, true);
  if (onRampsList) displayRelationshipList(onRampsList, role.on_ramps, true); // Show percentages for on_ramps
  if (offRampsList) displayRelationshipList(offRampsList, role.off_ramps, true); // Show percentages for off_ramps
  if (secondaryRolesList) displayRelationshipList(secondaryRolesList, role.secondary_roles, true);
}

function displayRelationshipList(container, relationships, showPercentage) {
  if (!relationships || relationships.length === 0) {
    container.innerHTML = '<div class="empty-relationships">Aucune relation trouvée</div>';
    return;
  }
  
  const html = relationships.map(rel => {
    const percentage = showPercentage && rel.percentage ? 
      `<span class="relationship-item-percentage">${rel.percentage}%</span>` : '';
    
    // Get DCWF information for this role
    const dcwfInfo = dcwfMapping[rel.id];
    const dcwfInfoHtml = dcwfInfo ? 
      `<div class="relationship-item-dcwf">
        <div class="dcwf-opm-id">OPM: ${dcwfInfo.opm_id}</div>
        <div class="dcwf-title">${dcwfInfo.dcwf_title}</div>
      </div>` : '';
    
    // Add T-K-S breakdown if available
    const tksBreakdownHtml = rel.tks_breakdown ? 
      `<div class="relationship-item-tks">
        <div class="tks-breakdown">
          <span class="tks-item tks-tasks">T: ${rel.tks_breakdown.T}%</span>
          <span class="tks-item tks-knowledge">K: ${rel.tks_breakdown.K}%</span>
          <span class="tks-item tks-skills">S: ${rel.tks_breakdown.S}%</span>
        </div>
      </div>` : '';
    
    return `
      <div class="relationship-item" data-role-id="${rel.id}">
        <div class="relationship-item-info">
          <div class="relationship-item-id">${rel.id}</div>
          <div class="relationship-item-name">${rel.name}</div>
          ${dcwfInfoHtml}
          ${tksBreakdownHtml}
        </div>
        ${percentage}
      </div>
    `;
  }).join('');
  
  container.innerHTML = html;
  
  // Add click listeners
  const relationshipItems = container.querySelectorAll('.relationship-item');
  relationshipItems.forEach(item => {
    item.addEventListener('click', function() {
      const roleId = this.getAttribute('data-role-id');
      selectRole(roleId);
    });
  });
}

function showLoadingState() {
  hideAllStates();
  loadingState.classList.remove('hidden');
}

function showErrorState() {
  hideAllStates();
  errorState.classList.remove('hidden');
}

function showEmptyState() {
  hideAllStates();
  emptyState.classList.remove('hidden');
}

function hideAllStates() {
  loadingState.classList.add('hidden');
  errorState.classList.add('hidden');
  roleDisplay.classList.add('hidden');
  emptyState.classList.add('hidden');
}

function updateURL(roleId) {
  const url = new URL(window.location);
  
  if (roleId) {
    url.searchParams.set('role', roleId);
  } else {
    url.searchParams.delete('role');
  }
  
  window.history.pushState({roleId}, '', url);
}

function handleHistoryChange(event) {
  const roleId = event.state?.roleId;
  
  if (roleId) {
    const role = findRoleById(roleId);
    if (role) {
      displayRole(role);
      searchInput.value = role.name;
    }
  } else {
    showEmptyState();
    searchInput.value = '';
  }
}