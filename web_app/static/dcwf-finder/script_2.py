# Continuer avec DATA/AI (DA) et SOFTWARE ENGINEERING (SE)

# DATA/AI (DA) - 11 work roles
da_roles = [
    # IMPLEMENTATION and OPERATION (IO)
    ("DA", "422", "IO-WRL-001", "Data Analyst", "Analyzes and interprets data from multiple disparate sources and builds visualizations and dashboards to report insights"),
    # Hors catégories NCWF
    ("DA", "423", "N/A", "Data Scientist", "Uncovers and explains actionable insights from data by combining scientific method, math and statistics, specialized programming, advanced analytics, AI, and storytelling."),
    ("DA", "424", "N/A", "Data Steward", "Develops and maintains plans, policies, and processes for data management, data governance, security, quality, accessibility, use, and disposal."),
    ("DA", "623", "N/A", "AI/ML Specialist", "Designs, develops, and modifies AI applications, tools, and/or other solutions to enable successful accomplishment of mission objectives."),
    ("DA", "624", "N/A", "Data Operations Specialist", "Builds, manages, and operationalizes data pipelines."),
    ("DA", "653", "N/A", "Data Architect", "Designs a system's data models, data flow, interfaces, and infrastructure to meet the information requirements of a business or mission."),
    ("DA", "672", "N/A", "AI Test & Evaluation Specialist", "Performs testing, evaluation, verification, and validation on AI solutions to ensure they are developed to be and remain robust, resilient, responsible, secure, and trustworthy; and communicates results and concerns to leadership."),
    ("DA", "733", "N/A", "AI Risk and Ethics Specialist", "Educates those involved in the development of AI and conducts assessments on the technical and societal risks across the lifecycle of AI solutions from acquisition or design to deployment and use."),
    ("DA", "753", "N/A", "AI Adoption Specialist", "Facilitates AI adoption by supporting the users of AI-enabled solutions."),
    ("DA", "902", "N/A", "AI Innovation Leader", "Builds the organization's AI vision and plan and leads policy and doctrine formation, including how AI solutions can or will be used."),
    ("DA", "903", "N/A", "Data Officer", "Holds responsibility for developing, promoting, and overseeing implementation of data as an asset and the establishment and enforcement of data-related strategies, policies, standards, processes, and governance."),
]

# SOFTWARE ENGINEERING (SE) - 8 work roles
se_roles = [
    # DESIGN and DEVELOPMENT (DD)
    ("SE", "621", "DD-WRL-003", "Software Developer", "Executes software planning, requirements, risk management, design, development, architecture, modeling, estimation, configuration management, quality, security, and tests using software development methodologies, architectural structures, viewpoints, styles, design decisions, and frameworks across all lifecycle phases."),
    # IMPLEMENTATION and OPERATION (IO)
    ("SE", "461", "IO-WRL-006", "Systems Security Analyst", "Responsible for analysis and development of systems/software security through the product lifecycle to include integration, testing, operations and maintenance."),
    # Hors catégories NCWF
    ("SE", "625", "N/A", "Product Designer User Interface (UI)", "Manages the user interface design portion of the design process of a product."),
    ("SE", "626", "N/A", "Service Designer User Experience (UX)", "Manages the user interface design portion of the design process of a product."),
    ("SE", "627", "N/A", "DevSecOps Specialist", "Selects/Deploys/Maintains the set of Continuous Integration/Continuous Deployment (CI/CD) tools and processes used by the development team and/or maintains the deployed software product and ensures observability and security across the lifecycle."),
    ("SE", "628", "N/A", "Software/Cloud Architect", "Manages and identifies program high-level technical specifications, which may include application design, cloud computing strategy and adoption, and integration of software applications into a functioning system to meet requirements."),
    ("SE", "673", "N/A", "Software Test & Evaluation Specialist", "Plans, prepares, and performs testing, evaluation, verification, and validation of software to evaluate results against specifications, requirements, and operational need."),
    ("SE", "806", "N/A", "Product Manager", "Manages the development of products including the resource management, product strategy (physical or digital), functional requirements, and releases. Coordinate work done by functions (like software engineers, data scientists, and product designers)."),
]

# SANS COMMUNAUTÉ (Cx) - 2 work roles
cx_roles = [
    # Note: TBD-A est dans une section DD mais a un WRL-ID PD-WRL-005
    ("Cx", "TBD-A", "PD-WRL-005", "Insider Threat Analysis", "Responsible for identifying and assessing the capabilities and activities of cybersecurity insider threats; produces findings to help initialize and support law enforcement and counterintelligence activities and investigations."),
    # Note: TBD-B est dans une section PD mais a un WRL-ID DD-WRL-009  
    ("Cx", "TBD-B", "DD-WRL-009", "Operational Technology (OT) Cybersecurity Engineering", "Responsible for working within the engineering department to design and create systems, processes, and procedures that maintain the safety, reliability, controllability, and security of industrial systems in the face of intentional and incidental cyber events. Interfaces with Chief Information Security Officer, plant managers, and industrial cybersecurity technicians."),
]

print(f"✅ DA: {len(da_roles)} work roles")
print(f"✅ SE: {len(se_roles)} work roles") 
print(f"✅ Cx: {len(cx_roles)} work roles")

total_final = total_so_far + len(da_roles) + len(se_roles) + len(cx_roles)
print(f"\n🎉 TOTAL FINAL: {total_final} work roles")

# Vérification: doit être 79
print(f"✅ Objectif 79 work roles: {'ATTEINT' if total_final == 79 else 'MANQUÉ'}")

# Combiner tous les rôles
all_roles = en_roles + it_roles + cs_roles + ci_roles + ce_roles + da_roles + se_roles + cx_roles

print(f"\n📊 RÉPARTITION PAR COMMUNAUTÉ DCWF:")
dcwf_counts = {}
for dcwf, _, _, _, _ in all_roles:
    dcwf_counts[dcwf] = dcwf_counts.get(dcwf, 0) + 1

for dcwf, count in sorted(dcwf_counts.items()):
    print(f"   {dcwf}: {count} work roles")

print(f"\n📋 RÉPARTITION PAR CATÉGORIE NCWF:")
ncwf_counts = {}
for _, _, wrl_id, _, _ in all_roles:
    # Déterminer la catégorie depuis le WRL-ID
    if wrl_id == "N/A":
        category = "N/A"
    else:
        category = wrl_id.split("-")[0]
    ncwf_counts[category] = ncwf_counts.get(category, 0) + 1

for ncwf, count in sorted(ncwf_counts.items()):
    print(f"   {ncwf}: {count} work roles")

print(f"\n🔥 VÉRIFICATION CATÉGORIE PD:")
pd_roles = []
for dcwf, omp_id, wrl_id, title, desc in all_roles:
    if wrl_id.startswith("PD-WRL-") or wrl_id == "PD-WRL-005":
        pd_roles.append((dcwf, omp_id, wrl_id, title))

print(f"Catégorie PD contient {len(pd_roles)} work roles:")
for dcwf, omp_id, wrl_id, title in pd_roles:
    print(f"  • {omp_id} ({wrl_id}) - {title} - Communauté: {dcwf}")

print(f"\n✅ AUCUNE COMMUNAUTÉ OU CATÉGORIE VIDE: {len(dcwf_counts) == 8 and len(ncwf_counts) == 6}")