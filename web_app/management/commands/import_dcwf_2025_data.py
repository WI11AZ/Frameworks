from django.core.management.base import BaseCommand
from web_app.models import Dcwf2025Category, Dcwf2025WorkRole
import re


class Command(BaseCommand):
    help = 'Import DCWF 2025 data from index25.html'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Importing DCWF 2025 data...'))
        
        # Définir les couleurs pour chaque catégorie (basées sur les couleurs existantes)
        category_colors = {
            'Cyber Effects': '220, 38, 127',  # Rose
            'Cyber Enablers': '14, 165, 233',  # Bleu
            'Cybersecurity': '34, 197, 94',   # Vert
            'Data/AI': '245, 158, 11',        # Orange
            'Information Technology': '168, 85, 247',  # Violet
            'Intel (Cyber)': '239, 68, 68',   # Rouge
            'Software Engineering': '6, 182, 212',     # Cyan
        }

        # Données extraites du fichier index25.html
        categories_data = [
            {
                'title': 'Cyber Effects',
                'short': 'CE',
                'description': 'Personnel who plan, support, and execute cyberspace capabilities where the primary purpose is to externally defend or conduct force projection in or through cyberspace.',
                'roles': [
                    {'dcwf_code': '122', 'title': 'Digital Network Exploitation Analyst', 'definition': 'The DNEA analyzes intercepted intelligence information for metadata and content. They use this data to reconstruct and document target networks to judge the intelligence value and maintain target continuity. DNEAs understand and analyze target implementation of communication technologies and digital network systems. They discover methods and suggest strategies to exploit specific target networks, computer systems, or specific hardware and/or software.'},
                    {'dcwf_code': '131', 'title': 'Joint Targeting Analyst', 'definition': 'Joint Targeting Analyst conduct target development at the system, component and entity levels. Builds and maintains Electronic Target Folders (ETFs), to include inputs from JIPOE, Target System Analysis (TSA), GMI and other IC sources. Senior analysts run collaborative target working groups across Geographic Combatant Commands (GCCs) and IC members, and present candidate targets for IC vetting and commander\'s approval for inclusion on target lists. JTAs assess damage resulting from the application of lethal or non-lethal military force, and write Battle Damage Assessment (BDA) reports and coordinate federated support as required.'},
                    {'dcwf_code': '132', 'title': 'Target Digital Network Analyst', 'definition': 'The TDNA conducts advanced analysis of collection and open-source data to ensure target continuity, profile targets and their activities, and develop techniques to gain more target cyberspace operations related information. They possess knowledge of target cyberspace technologies and apply skills and knowledge of cyberspace networks and the applications on them to determine how targets communicate, move, operate, and live within the cyberspace domain. TDNAs apply analytical techniques to review relevant content carried in target cyberspace communications. The TDNA uses data from networks of all forms for target development. TDNAs are technology savvy and can be flexible enough to rapidly shift from one target to another.'},
                    {'dcwf_code': '133', 'title': 'Target Analyst Reporter', 'definition': 'The Target Analyst Reporter (TAR) provides synthesized products to customers by researching, analyzing, and reporting intelligence via appropriate reporting vehicles in response to customer requirements and IAW missions of SIGINT, cybersecurity, and cyberspace operations. They prioritize, assess, evaluate, and report information obtained from SIGINT collection, cyber surveillance, and reconnaissance operations sources. The TAR enhances reporting with collateral information as required, maintains awareness of internal and external customer requirements, and collaborates with other collectors and analysts to refine collection and reporting requirements. The TAR shares target-related information and provides feedback to customers as appropriate. The TAR develops working aids and provides database updates on target activity to enhance and build target knowledge and improve collection. The TAR performs quality control and product-release functions.'},
                    {'dcwf_code': '321', 'title': 'Access Network Operator', 'definition': 'Conducts access collection, processing, and/or geolocation of wired or wireless computer and digital networks in order to exploit, locate, and/or track targets of interest.'},
                    {'dcwf_code': '322', 'title': 'Cyberspace Operator', 'definition': 'Cyberspace Operators use a wide range of software applications for network navigation, tactical forensic analysis, surveillance and reconnaissance, and executing on-net operations in support of offensive cyberspace operations when directed.'},
                    {'dcwf_code': '332', 'title': 'Cyber Operations Planner', 'definition': 'The Cyberspace Operations Planner applies in-depth knowledge of the JOPP to develop detailed plans and orders supporting CCMD cyberspace operation requirements. Uses Joint, Service, and interagency planning and operational experience to conduct strategic and operational level planning across the full range of military operations for integrated information and cyberspace operations. Develops and maintains deliberate and crisis action planning products. Collaborates with cyberspace operators to identify and levy requirements for intelligence collection and analysis. Participates in targeting selection, validation, synchronization, and execution of complex cyberspace operations. Has sufficient technical knowledge to understand cyberspace operations capabilities, target vulnerabilities, and effects. Collaborates with cyberspace operators, analysts, enablers and planners to gain access and technical intelligence to meet planning objectives.'},
                    {'dcwf_code': '341', 'title': 'Cyberspace Capability Developer', 'definition': 'Provides software and hardware capabilities that produce cyberspace effects in and throughout cyberspace operations through vulnerability analysis, and software research and development.'},
                    {'dcwf_code': '442', 'title': 'Network Technician', 'definition': 'The Network Technician provides enterprise and tactical infrastructure knowledge, experience, and integration to the Cyber Protection Team (CPT). The Network Technician supports CPT elements by understanding of network technologies, defining mission scope, and identifying terrain.'},
                    {'dcwf_code': '443', 'title': 'Network Analyst', 'definition': 'The Network Analyst will understand network traffic signatures and discover anomalies through network traffic and packet capture (PCAP) analysis. The Network Analyst will identify, assess, and mitigate intrusions into networks that are vital to cyberspace operations security. Network Analysts also use GUI or command-line based tools and assist in developing network mapping and signatures. Network Analysts will develop advanced network detection rules and alerts, queries and dashboards to gain a holistic view of the network.'},
                    {'dcwf_code': '463', 'title': 'Host Analyst', 'definition': 'A Host Analyst (HA) will have knowledge of various system configurations encountered. This work role also performs analysis using built-in tools and capabilities. A Host Analyst will have knowledge of system services and the security and configuration of them, as well as knowledge of file systems, permissions, and operation system configurations. The Host Analyst conducts analysis using built-in tools and capabilities.'},
                    {'dcwf_code': '551', 'title': 'Red Team Specialist', 'definition': 'Leverages tools, systems, and utilities necessary to enhance the security posture of an organization, conducts threat and risk assessments, and performs testing and evaluation in accordance with legal and organizational requirements, policies, and regulations.'},
                ]
            },
            {
                'title': 'Cyber Enablers',
                'short': 'EN',
                'description': 'Personnel who perform work roles to support or facilitate the functions of cyber IT, cybersecurity, cyberspace effects, or intelligence workforce (cyberspace) work roles. This includes actions to support acquisition, training and leadership activities.',
                'roles': [
                    {'dcwf_code': '751', 'ncwf_id': 'OG-WRL-003', 'title': 'Cyber Workforce Developer and Manager', 'definition': 'Develop cyberspace workforce plans, strategies and guidance to support cyberspace workforce manpower, personnel, training and education requirements and to address changes to cyberspace policy, doctrine, materiel, force structure, and education and training requirements.'},
                    {'dcwf_code': '752', 'ncwf_id': 'OG-WRL-002', 'title': 'Cyber Policy and Strategy Planner', 'definition': 'Develops cyberspace plans, strategy and policy to support and align with organizational cyberspace missions and initiatives.'},
                    {'dcwf_code': '901', 'ncwf_id': 'OG-WRL-007', 'title': 'Executive Cyber Leader', 'definition': 'Executes decision-making authorities and establishes vision and direction for an organization\'s cyber and cyber-related policies, resources, and/or operations, while maintaining responsibility for risk-related decisions affecting mission success.'},
                    {'dcwf_code': '711', 'ncwf_id': 'OG-WRL-004', 'title': 'Cyber Instructional Curriculum Developer', 'definition': 'Develops, plans, coordinates, and evaluates cyber training/education courses, methods, and techniques based on instructional needs.'},
                    {'dcwf_code': '712', 'ncwf_id': 'OG-WRL-005', 'title': 'Cyber Instructor', 'definition': 'Develops and conducts training or education of personnel within cyber domain.'},
                    {'dcwf_code': '211', 'ncwf_id': 'IN-WRL-002', 'title': 'Forensics Analyst', 'definition': 'Conducts deep-dive investigations on computer-based crimes establishing documentary or physical evidence, to include digital media and logs associated with cyber intrusion incidents.'},
                    {'dcwf_code': '221', 'ncwf_id': 'IN-WRL-001', 'title': 'Cyber Crime Investigator', 'definition': 'Identifies, collects, examines, and preserves evidence using controlled and documented analytical and investigative techniques.'},
                    {'dcwf_code': '731', 'ncwf_id': 'OG-WRL-006', 'title': 'Cyber Legal Advisor', 'definition': 'Provides legal advice and recommendations on relevant topics related to cyber law.'},
                    {'dcwf_code': '801', 'ncwf_id': 'OG-WRL-010', 'title': 'Program Manager', 'definition': 'Leads, coordinates, communicates, integrates and is accountable for the overall success of the program, ensuring alignment with critical agency priorities.'},
                    {'dcwf_code': '802', 'ncwf_id': 'OG-WRL-011', 'title': 'IT Project Manager', 'definition': 'Work that involves directly managing information technology projects to provide a unique service or product.'},
                    {'dcwf_code': '803', 'ncwf_id': 'OG-WRL-009', 'title': 'Product Support Manager', 'definition': 'Manages the package of support functions required to field and maintain the readiness and operational capability of systems and components.'},
                    {'dcwf_code': '804', 'ncwf_id': 'OG-WRL-015', 'title': 'IT Investment/Portfolio Manager', 'definition': 'Manages a portfolio of IT capabilities that align with the overall needs of mission and business enterprise priorities.'},
                    {'dcwf_code': '805', 'ncwf_id': 'OG-WRL-016', 'title': 'IT Program Auditor', 'definition': 'Conducts evaluations of an IT program or its individual components, to determine compliance with published standards.'},
                ]
            },
            {
                'title': 'Cybersecurity',
                'short': 'CS',
                'description': 'Personnel who secure, defend, and preserve data, networks, net-centric capabilities, and other designated systems by ensuring appropriate security controls and measures are in place, and taking internal defense actions. This includes access to system controls, monitoring, administration, and integration of cybersecurity into all aspects of engineering and acquisition of cyberspace capabilities.',
                'roles': [
                    {'dcwf_code': '462', 'title': 'Control Systems Security Specialist', 'definition': 'Responsible for device, equipment, and system-level cybersecurity configuration and day-to-day security operations of control systems, including security monitoring and maintenance along with stakeholder coordination to ensure the system and its interconnections are secure in support of mission operations.'},
                    {'dcwf_code': '511', 'ncwf_id': 'PD-WRL-001', 'title': 'Cyber Defense Analyst', 'definition': 'Uses data collected from a variety of cyber defense tools (e.g., IDS alerts, firewalls, network traffic logs.) to analyze events that occur within their environments for the purposes of mitigating threats.'},
                    {'dcwf_code': '521', 'ncwf_id': 'PD-WRL-004', 'title': 'Cyber Defense Infrastructure Support Specialist', 'definition': 'Tests, implements, deploys, maintains, and administers the infrastructure hardware and software.'},
                    {'dcwf_code': '531', 'ncwf_id': 'PD-WRL-003', 'title': 'Cyber Defense Incident Responder', 'definition': 'Investigates, analyzes, and responds to cyber incidents within the network environment or enclave.'},
                    {'dcwf_code': '541', 'ncwf_id': 'PD-WRL-007', 'title': 'Vulnerability Assessment Analyst', 'definition': 'Performs assessments of systems and networks within the NE or enclave and identifies where those systems/networks deviate from acceptable configurations, enclave policy, or local policy. Measures effectiveness of defense-in-depth architecture against known vulnerabilities.'},
                    {'dcwf_code': '611', 'ncwf_id': 'OG-WRL-013', 'title': 'Authorizing Official/Designated Representative', 'definition': 'Senior official or executive with the authority to formally assume responsibility for operating an information system at an acceptable level of risk to organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, and the Nation (CNSSI 4009).'},
                    {'dcwf_code': '612', 'ncwf_id': 'OG-WRL-012', 'title': 'Security Control Assessor', 'definition': 'Conducts independent comprehensive assessments of the management, operational, and technical security controls and control enhancements employed within or inherited by an information technology (IT) system to determine the overall effectiveness of the controls (as defined in NIST 800-37).'},
                    {'dcwf_code': '622', 'ncwf_id': 'DD-WRL-005', 'title': 'Secure Software Assessor', 'definition': 'Analyzes the security of new or existing computer applications, software, or specialized utility programs and provides actionable results.'},
                    {'dcwf_code': '631', 'ncwf_id': 'DD-WRL-004', 'title': 'Information Systems Security Developer', 'definition': 'Designs, develops, tests, and evaluates information system security throughout the systems development lifecycle.'},
                    {'dcwf_code': '652', 'ncwf_id': 'DD-WRL-001', 'title': 'Security Architect', 'definition': 'Designs enterprise and systems security throughout the development lifecycle; translates technology and environmental conditions (e.g., law and regulation) into security designs and processes.'},
                    {'dcwf_code': '722', 'ncwf_id': 'OG-WRL-014', 'title': 'Information Systems Security Manager', 'definition': 'Responsible for the cybersecurity of a program, organization, system, or enclave.'},
                    {'dcwf_code': '723', 'ncwf_id': 'OG-WRL-001', 'title': 'COMSEC Manager', 'definition': 'Manages the Communications Security (COMSEC) resources of an organization (CNSSI No. 4009).'},
                ]
            },
            {
                'title': 'Data/AI',
                'short': 'DA',
                'description': 'Personnel who drive and support data, analytic, and AI-enabled capabilities that harness information for decision-advantage.',
                'roles': [
                    {'dcwf_code': '423', 'title': 'Data Scientist', 'definition': 'Uncovers and explains actionable insights from data by combining scientific method, math and statistics, specialized programming, advanced analytics, AI, and storytelling.'},
                    {'dcwf_code': '424', 'title': 'Data Steward', 'definition': 'Develops and maintains plans, policies, and processes for data management, data governance, security, quality, accessibility, use, and disposal.'},
                    {'dcwf_code': '623', 'title': 'AI/ML Specialist', 'definition': 'Designs, develops, and modifies AI applications, tools, and/or other solutions to enable successful accomplishment of mission objectives.'},
                    {'dcwf_code': '624', 'title': 'Data Operations Specialist', 'definition': 'Builds, manages, and operationalizes data pipelines.'},
                    {'dcwf_code': '653', 'title': 'Data Architect', 'definition': 'Designs a system\'s data models, data flow, interfaces, and infrastructure to meet the information requirements of a business or mission.'},
                    {'dcwf_code': '672', 'title': 'AI Test & Evaluation Specialist', 'definition': 'Performs testing, evaluation, verification, and validation on AI solutions to ensure they are developed to be and remain robust, resilient, responsible, secure, and trustworthy; and communicates results and concerns to leadership.'},
                    {'dcwf_code': '733', 'title': 'AI Risk and Ethics Specialist', 'definition': 'Educates those involved in the development of AI and conducts assessments on the technical and societal risks across the lifecycle of AI solutions from acquisition or design to deployment and use.'},
                    {'dcwf_code': '753', 'title': 'AI Adoption Specialist', 'definition': 'Facilitates AI adoption by supporting the users of AI-enabled solutions.'},
                    {'dcwf_code': '902', 'title': 'AI Innovation Leader', 'definition': 'Builds the organization\'s AI vision and plan and leads policy and doctrine formation, including how AI solutions can or will be used.'},
                    {'dcwf_code': '903', 'title': 'Data Officer', 'definition': 'Holds responsibility for developing, promoting, and overseeing implementation of data as an asset and the establishment and enforcement of data-related strategies, policies, standards, processes, and governance.'},
                ]
            },
            {
                'title': 'Information Technology',
                'short': 'IT',
                'description': 'Personnel who design, build, configure, operate, and maintain IT, networks, and capabilities. This includes actions to prioritize implement, evaluate, and dispose of IT as well as information resource management; and the management, storage, transmission, and display of data and information.',
                'roles': [
                    {'dcwf_code': '421', 'ncwf_id': 'IO-WRL-002', 'title': 'Database Administrator', 'definition': 'Administers databases and/or data management systems that allow for the storage, query, and utilization of data.'},
                    {'dcwf_code': '431', 'ncwf_id': 'IO-WRL-003', 'title': 'Knowledge Manager', 'definition': 'Responsible for the management and administration of processes and tools that enable the organization to identify, document, and access intellectual capital and information content.'},
                    {'dcwf_code': '441', 'ncwf_id': 'IO-WRL-004', 'title': 'Network Operations Specialist', 'definition': 'Plans, implements, and operates network services/systems, to include hardware and virtual environments.'},
                    {'dcwf_code': '451', 'ncwf_id': 'IO-WRL-005', 'title': 'System Administrator', 'definition': 'Installs, configures, troubleshoots, and maintains hardware, software, and administers system accounts.'},
                    {'dcwf_code': '632', 'ncwf_id': 'DD-WRL-004', 'title': 'Systems Developer', 'definition': 'Designs, develops, tests, and evaluates information systems throughout the systems development lifecycle.'},
                    {'dcwf_code': '641', 'ncwf_id': 'DD-WRL-006', 'title': 'Systems Requirements Planner', 'definition': 'Consults with customers to evaluate functional requirements and translate functional requirements into technical solutions.'},
                    {'dcwf_code': '651', 'ncwf_id': 'DD-WRL-002', 'title': 'Enterprise Architect', 'definition': 'Develops and maintains business, systems, and information processes to support enterprise mission needs; develops information technology (IT) rules and requirements that describe baseline and target architectures.'},
                    {'dcwf_code': '661', 'ncwf_id': 'DD-WRL-008', 'title': 'Research & Development Specialist', 'definition': 'Conducts software and systems engineering and software systems research in order to develop new capabilities, ensuring cybersecurity is fully integrated. Conducts comprehensive technology research to evaluate potential vulnerabilities in cyberspace systems.'},
                    {'dcwf_code': '671', 'ncwf_id': 'DD-WRL-007', 'title': 'System Testing and Evaluation Specialist', 'definition': 'Plans, prepares, and executes tests of systems to evaluate results against specifications and requirements as well as analyze/report test results.'},
                ]
            },
            {
                'title': 'Intel (Cyber)',
                'short': 'IN',
                'description': 'Personnel who collect, process, analyze, and disseminate information from all sources of intelligence on foreign actors\' cyberspace programs, intentions, capabilities, research and development, and operational activities.',
                'roles': [
                    {'dcwf_code': '151', 'title': 'Multi-Disciplined Language Analyst', 'definition': 'Applies language and culture expertise with target/threat and technical knowledge to process, analyze, and/or disseminate intelligence information derived from language, voice and/or graphic material. Creates, and maintains language specific databases and working aids to support cyber action execution and ensure critical knowledge sharing. Provides subject matter expertise in foreign language-intensive or interdisciplinary projects.'},
                    {'dcwf_code': '311', 'title': 'All-Source Collection Manager', 'definition': 'Identifies collection authorities and environment; incorporates priority information requirements into collection management; develops concepts to meet leadership\'s intent. Determines capabilities of available collection assets, identifies new collection capabilities; and constructs and disseminates collection plans. Monitors execution of tasked collection to ensure effective execution of the collection plan.'},
                    {'dcwf_code': '312', 'title': 'All-Source Collection Requirements Manager', 'definition': 'Evaluates collection operations and develops effects-based collection requirements strategies using available sources and methods to improve collection. Develops, processes, validates, and coordinates submission of collection requirements. Evaluates performance of collection assets and collection operations.'},
                    {'dcwf_code': '331', 'title': 'Cyber Intelligence Planner', 'definition': 'Develops detailed intelligence plans to satisfy cyber operations requirements. Collaborates with cyber operations planners to identify, validate, and levy requirements for collection and analysis. Participates in targeting selection, validation, synchronization, and execution of cyber actions. Synchronizes intelligence activities to support organization objectives in cyberspace.'},
                ]
            },
            {
                'title': 'Software Engineering',
                'short': 'SE',
                'description': 'Personnel who manages and identifies program high-level technical specifications, which may include, application design, development, testing, deployment, cloud computing strategy and adoption, and integration of software applications into a functioning system to meet requirements.',
                'roles': [
                    {'dcwf_code': '621', 'ncwf_id': 'DD-WRL-003', 'title': 'Software Developer', 'definition': 'Executes software planning, requirements, risk management, design, development, architecture, modeling, estimation, configuration management, quality, security, and tests using software development methodologies, architectural structures, viewpoints, styles, design decisions, and frameworks across all lifecycle phases.'},
                    {'dcwf_code': '625', 'title': 'Product Designer User Interface (UI)', 'definition': 'Manages the user interface design portion of the design process of a product.'},
                    {'dcwf_code': '626', 'title': 'Service Designer User Experience (UX)', 'definition': 'Manages the user experience of a product focused on human factors by making products intuitive and maximizing usability, accessibility, and simplicity.'},
                    {'dcwf_code': '627', 'title': 'DevSecOps Specialist', 'definition': 'Selects/Deploys/Maintains the set of Continuous Integration/Continuous Deployment (CI/CD) tools and processes used by the development team and/or maintains the deployed software product and ensures observability and security across the lifecycle.'},
                    {'dcwf_code': '628', 'title': 'Software/Cloud Architect', 'definition': 'Manages and identifies program high-level technical specifications, which may include application design, cloud computing strategy and adoption, and integration of software applications into a functioning system to meet requirements.'},
                    {'dcwf_code': '673', 'title': 'Software Test & Evaluation Specialist', 'definition': 'Plans, prepares, and performs testing, evaluation, verification, and validation of software to evaluate results against specifications, requirements, and operational need.'},
                    {'dcwf_code': '806', 'title': 'Product Manager', 'definition': 'Manages the development of products including the resource management, product strategy (physical or digital), functional requirements, and releases. Coordinate work done by functions (like software engineers, data scientists, and product designers).'},
                ]
            }
        ]

        # Supprimer les données existantes
        Dcwf2025WorkRole.objects.all().delete()
        Dcwf2025Category.objects.all().delete()
        
        # Créer les catégories et work roles
        for cat_data in categories_data:
            # Créer la catégorie
            category = Dcwf2025Category.objects.create(
                title=cat_data['title'],
                description=cat_data['description'],
                color=category_colors.get(cat_data['title'], '128, 128, 128')  # Gris par défaut
            )
            
            self.stdout.write(f'Créé catégorie: {category.title}')
            
            # Créer les work roles pour cette catégorie
            for role_data in cat_data['roles']:
                work_role = Dcwf2025WorkRole.objects.create(
                    dcwf_code=role_data['dcwf_code'],
                    ncwf_id=role_data.get('ncwf_id', ''),
                    title=role_data['title'],
                    definition=role_data['definition'],
                    category=category
                )
                self.stdout.write(f'  Créé work role: {work_role.dcwf_code} - {work_role.title}')
        
        self.stdout.write(self.style.SUCCESS('Import terminé avec succès!'))
