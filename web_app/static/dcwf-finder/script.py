# EXTRACTION EXHAUSTIVE DE TOUS LES 79 WORK ROLES SELON VOS INSTRUCTIONS
# Structure: (DCWF) (OMP-ID) (WRL-ID) Titre Description

print("🔧 EXTRACTION COMPLÈTE DES 79 WORK ROLES")
print("=" * 60)

all_work_roles = []

# CYBER ENABLERS (EN) - 14 work roles
en_roles = [
    # OVERSIGHT and GOVERNANCE (OG)
    ("EN", "711", "OG-WRL-004", "Cyber Instructional Curriculum Developer", "Develops, plans, coordinates, and evaluates cyber training/education courses, methods, and techniques based on instructional needs."),
    ("EN", "712", "OG-WRL-005", "Cyber Instructor", "Develops and conducts training or education of personnel within cyber domain."),
    ("EN", "801", "OG-WRL-010", "Program Manager", "Leads, coordinates, communicates, integrates and is accountable for the overall success of the program, ensuring alignment with critical agency priorities."),
    ("EN", "802", "OG-WRL-011", "IT Project Manager", "Work that involves directly managing information technology projects to provide a unique service or product."),
    ("EN", "803", "OG-WRL-009", "Product Support Manager", "Manages the package of support functions required to field and maintain the readiness and operational capability of systems and components."),
    ("EN", "804", "OG-WRL-015", "IT Investment/Portfolio Manager", "Manages a portfolio of IT capabilities that align with the overall needs of mission and business enterprise priorities."),
    ("EN", "805", "OG-WRL-016", "IT Program Auditor", "Conducts evaluations of an IT program or its individual components, to determine compliance with published standards."),
    ("EN", "732", "OG-WRL-008", "Privacy Compliance Manager", "Develops and oversees privacy compliance program and privacy program staff, supporting privacy compliance needs of privacy and security executives and their teams."),
    ("EN", "751", "OG-WRL-003", "Cyber Workforce Developer and Manager", "Develop cyberspace workforce plans, strategies and guidance to support cyberspace workforce manpower, personnel, training and education requirements and to address changes to cyberspace policy, doctrine, materiel, force structure, and education and training requirements."),
    ("EN", "752", "OG-WRL-002", "Cyber Policy and Strategy Planner", "Develops cyberspace plans, strategy and policy to support and align with organizational cyberspace missions and initiatives."),
    ("EN", "901", "OG-WRL-007", "Executive Cyber Leader", "Executes decision-making authorities and establishes vision and direction for an organization's cyber and cyber-related policies, resources, and/or operations, while maintaining responsibility for risk-related decisions affecting mission success."),
    ("EN", "731", "OG-WRL-006", "Cyber Legal Advisor", "Provides legal advice and recommendations on relevant topics related to cyber law."),
    # INVESTIGATION (IN)
    ("EN", "211", "IN-WRL-002", "Forensics Analyst", "Conducts deep-dive investigations on computer-based crimes establishing documentary or physical evidence, to include digital media and logs associated with cyber intrusion incidents."),
    ("EN", "221", "IN-WRL-001", "Cyber Crime Investigator", "Identifies, collects, examines, and preserves evidence using controlled and documented analytical and investigative techniques."),
]

# INFORMATION TECHNOLOGY (IT) - 10 work roles  
it_roles = [
    # IMPLEMENTATION and OPERATION (IO)
    ("IT", "411", "IO-WRL-007", "Technical Support Specialist", "Provides technical support to customers who need assistance utilizing client level hardware and software in accordance with established or approved organizational process components."),
    ("IT", "421", "IO-WRL-002", "Database Administrator", "Administers databases and/or data management systems that allow for the storage, query, and utilization of data."),
    ("IT", "431", "IO-WRL-003", "Knowledge Manager", "Responsible for the management and administration of processes and tools that enable the organization to identify, document, and access intellectual capital and information content."),
    ("IT", "441", "IO-WRL-004", "Network Operations Specialist", "Plans, implements, and operates network services/systems, to include hardware and virtual environments."),
    ("IT", "451", "IO-WRL-005", "System Administrator", "Installs, configures, troubleshoots, and maintains hardware, software, and administers system accounts."),
    # DESIGN and DEVELOPMENT (DD)
    ("IT", "632", "DD-WRL-004", "Systems Developer", "Designs, develops, tests, and evaluates information systems throughout the systems development lifecycle."),
    ("IT", "641", "DD-WRL-006", "Systems Requirements Planner", "Consults with customers to evaluate functional requirements and translate functional requirements into technical solutions."),
    ("IT", "651", "DD-WRL-002", "Enterprise Architect", "Develops and maintains business, systems, and information processes to support enterprise mission needs; develops information technology (IT) rules and requirements that describe baseline and target architectures."),
    ("IT", "661", "DD-WRL-008", "Research & Development Specialist", "Conducts software and systems engineering and software systems research in order to develop new capabilities, ensuring cybersecurity is fully integrated. Conducts comprehensive technology research to evaluate potential vulnerabilities in cyberspace systems."),
    ("IT", "671", "DD-WRL-007", "System Testing and Evaluation Specialist", "Plans, prepares, and executes tests of systems to evaluate results against specifications and requirements as well as analyze/report test results."),
]

# CYBERSECURITY (CS) - 13 work roles
cs_roles = [
    # OVERSIGHT and GOVERNANCE (OG) 
    ("CS", "611", "OG-WRL-013", "Authorizing Official/Designated Representative", "Senior official or executive with the authority to formally assume responsibility for operating an information system at an acceptable level of risk to organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, and the Nation (CNSSI 4009)."),
    ("CS", "612", "OG-WRL-012", "Security Control Assessor", "Conducts independent comprehensive assessments of the management, operational, and technical security controls and control enhancements employed within or inherited by an information technology (IT) system to determine the overall effectiveness of the controls (as defined in NIST 800-37)."),
    ("CS", "722", "OG-WRL-014", "Information Systems Security Manager", "Responsible for the cybersecurity of a program, organization, system, or enclave."),
    ("CS", "723", "OG-WRL-001", "COMSEC Manager", "Manages the Communications Security (COMSEC) resources of an organization (CNSSI No. 4009)."),
    # DESIGN and DEVELOPMENT (DD)
    ("CS", "622", "DD-WRL-005", "Secure Software Assessor", "Analyzes the security of new or existing computer applications, software, or specialized utility programs and provides actionable results."),
    ("CS", "631", "DD-WRL-004", "Information Systems Security Developer", "Designs, develops, tests, and evaluates information system security throughout the systems development lifecycle."),
    ("CS", "652", "DD-WRL-001", "Security Architect", "Designs enterprise and systems security throughout the development lifecycle; translates technology and environmental conditions (e.g., law and regulation) into security designs and processes."),
    # PROTECTION and DEFENSE (PD) - VOICI LES PD !
    ("CS", "212", "PD-WRL-002", "Cyber Defense Forensic Analyst", "Analyzes digital evidence and investigates computer security incidents to derive useful information in support of system/network vulnerability mitigation."),
    ("CS", "511", "PD-WRL-001", "Cyber Defense Analyst", "Uses data collected from a variety of cyber defense tools (e.g., IDS alerts, firewalls, network traffic logs.) to analyze events that occur within their environments for the purposes of mitigating threats."),
    ("CS", "521", "PD-WRL-004", "Cyber Defense Infrastructure Support Specialist", "Tests, implements, deploys, maintains, and administers the infrastructure hardware and software."),
    ("CS", "531", "PD-WRL-003", "Cyber Defense Incident Responder", "Investigates, analyzes, and responds to cyber incidents within the network environment or enclave."),
    ("CS", "541", "PD-WRL-007", "Vulnerability Assessment Specialist", "Performs assessments of systems and networks within the NE or enclave and identifies where those systems/networks deviate from acceptable configurations, enclave policy, or local policy. Measures effectiveness of defense-in-depth architecture against known vulnerabilities."),
    # Hors catégories NCWF
    ("CS", "462", "N/A", "Control Systems Security Specialist", "Responsible for device, equipment, and system-level cybersecurity configuration and day-to-day security operations of control systems, including security monitoring and maintenance along with stakeholder coordination to ensure the system and its interconnections are secure in support of mission operations."),
]

print(f"✅ EN: {len(en_roles)} work roles")
print(f"✅ IT: {len(it_roles)} work roles")  
print(f"✅ CS: {len(cs_roles)} work roles")

# Continuer avec les autres communautés...
total_so_far = len(en_roles) + len(it_roles) + len(cs_roles)
print(f"Total jusqu'ici: {total_so_far}")