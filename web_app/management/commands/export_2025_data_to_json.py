import json
from django.core.management.base import BaseCommand
from web_app.models import Dcwf2025WorkRole, Ncwf2025WorkRole, Dcwf2025Category


class Command(BaseCommand):
    help = 'Export DCWF 2025 and NCWF 2025 data to JSON (2025 only, no NIST IDs)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Exporting 2025 data to JSON...'))
        
        # Structure du JSON de sortie
        output_data = {
            "framework_info": {
                "version": "2025",
                "export_date": "2025-10-06",
                "description": "DCWF and NCWF 2025 work roles with their relations"
            },
            "dcwf_2025": [],
            "ncwf_2025": [],
            "relations": []
        }
        
        # 1. Exporter tous les work roles DCWF 2025 avec OPM ID
        self.stdout.write('Exporting DCWF 2025 work roles...')
        dcwf_roles = Dcwf2025WorkRole.objects.select_related('category').all()
        
        # Dictionnaire pour éviter les doublons et grouper par OPM ID
        dcwf_dict = {}
        
        for role in dcwf_roles:
            # Filtrer uniquement les rôles avec un OPM ID (dcwf_code)
            if not role.dcwf_code:
                continue
                
            # Si cet OPM ID n'existe pas encore, le créer
            if role.dcwf_code not in dcwf_dict:
                dcwf_dict[role.dcwf_code] = {
                    "opm_id": role.dcwf_code,
                    "title": role.title,
                    "definition": role.definition,
                    "category": role.category.title if role.category else None,
                    "category_description": role.category.description if role.category else None,
                    "related_ncwf_ids": []
                }
            
            # Ajouter le NCWF ID associé s'il existe
            if role.ncwf_id and role.ncwf_id not in dcwf_dict[role.dcwf_code]["related_ncwf_ids"]:
                dcwf_dict[role.dcwf_code]["related_ncwf_ids"].append(role.ncwf_id)
        
        # Convertir le dictionnaire en liste
        output_data["dcwf_2025"] = list(dcwf_dict.values())
        self.stdout.write(self.style.SUCCESS(f'Exported {len(output_data["dcwf_2025"])} unique DCWF 2025 work roles'))
        
        # 2. Exporter tous les work roles NCWF 2025 avec WRL ID
        self.stdout.write('Exporting NCWF 2025 work roles...')
        
        # Utiliser les données complètes depuis le fichier d'import
        ncwf_complete_data = self._get_complete_ncwf_data()
        
        # Créer un dictionnaire pour éviter les doublons
        ncwf_dict = {}
        
        for ncwf_data in ncwf_complete_data:
            ncwf_id = ncwf_data['ncwf_id']
            
            if ncwf_id not in ncwf_dict:
                # Chercher l'OPM ID correspondant dans DCWF 2025
                corresponding_opm = None
                dcwf_match = Dcwf2025WorkRole.objects.filter(ncwf_id=ncwf_id).first()
                if dcwf_match and dcwf_match.dcwf_code:
                    corresponding_opm = dcwf_match.dcwf_code
                
                ncwf_dict[ncwf_id] = {
                    "wrl_id": ncwf_id,  # Format XX-WRL-XXX
                    "name": ncwf_data['title'],
                    "definition": ncwf_data['definition'],
                    "category": ncwf_data['category'],
                    "corresponding_opm_id": corresponding_opm
                }
        
        output_data["ncwf_2025"] = list(ncwf_dict.values())
        self.stdout.write(self.style.SUCCESS(f'Exported {len(output_data["ncwf_2025"])} NCWF 2025 work roles'))
        
        # 3. Créer les relations entre DCWF et NCWF
        self.stdout.write('Creating relations between DCWF and NCWF...')
        
        # Relations basées sur les work roles DCWF qui ont un ncwf_id
        relations_set = set()  # Utiliser un set pour éviter les doublons
        
        for dcwf_role in dcwf_roles:
            if dcwf_role.dcwf_code and dcwf_role.ncwf_id:
                relation_tuple = (dcwf_role.dcwf_code, dcwf_role.ncwf_id)
                if relation_tuple not in relations_set:
                    relations_set.add(relation_tuple)
                    output_data["relations"].append({
                        "dcwf_opm_id": dcwf_role.dcwf_code,
                        "ncwf_wrl_id": dcwf_role.ncwf_id,
                        "dcwf_title": dcwf_role.title,
                        "ncwf_title": dcwf_role.ncwf_title or dcwf_role.title,
                        "category": dcwf_role.category.title if dcwf_role.category else None
                    })
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(output_data["relations"])} unique relations'))
        
        # 4. Écrire le fichier JSON
        output_file = 'dcwf_ncwf_2025_data.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        self.stdout.write(self.style.SUCCESS(f'\nData successfully exported to {output_file}'))
        
        # Statistiques finales
        self.stdout.write(self.style.SUCCESS('\n=== STATISTIQUES ==='))
        self.stdout.write(f'DCWF 2025 work roles (with OPM ID): {len(output_data["dcwf_2025"])}')
        self.stdout.write(f'NCWF 2025 work roles (with WRL ID): {len(output_data["ncwf_2025"])}')
        self.stdout.write(f'Relations (DCWF ↔ NCWF): {len(output_data["relations"])}')
        
        # Compter les work roles sans relation
        dcwf_with_relation = set(r['dcwf_opm_id'] for r in output_data["relations"])
        ncwf_with_relation = set(r['ncwf_wrl_id'] for r in output_data["relations"])
        
        self.stdout.write(f'\nDCWF 2025 without NCWF relation: {len(output_data["dcwf_2025"]) - len(dcwf_with_relation)}')
        self.stdout.write(f'NCWF 2025 without DCWF relation: {len(output_data["ncwf_2025"]) - len(ncwf_with_relation)}')
    
    def _get_complete_ncwf_data(self):
        """Retourne les données complètes des work roles NCWF 2025"""
        return [
            # OVERSIGHT and GOVERNANCE (OG)
            {'ncwf_id': 'OG-WRL-001', 'title': 'Communications Security (COMSEC) Management', 'definition': 'Responsible for managing the Communications Security (COMSEC) resources of an organization.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-002', 'title': 'Cybersecurity Policy and Planning', 'definition': 'Responsible for developing and maintaining cybersecurity plans, strategy, and policy to support and align with organizational cybersecurity initiatives and regulatory compliance.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-003', 'title': 'Cybersecurity Workforce Management', 'definition': 'Responsible for developing cybersecurity workforce plans, assessments, strategies, and guidance, including cybersecurity-related staff training, education, and hiring processes. Makes adjustments in response to or in anticipation of changes to cybersecurity-related policy, technology, and staffing needs and requirements. Authors mandated workforce planning strategies to maintain compliance with legislation, regulation, and policy.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-004', 'title': 'Cybersecurity Curriculum Development', 'definition': 'Responsible for developing, planning, coordinating, and evaluating cybersecurity awareness, training, or education content, methods, and techniques based on instructional needs and requirements.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-005', 'title': 'Cybersecurity Instruction', 'definition': 'Responsible for developing and conducting cybersecurity awareness, training, or education.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-006', 'title': 'Cybersecurity Legal Advice', 'definition': 'Responsible for providing cybersecurity legal advice and recommendations, including monitoring related legislation and regulations.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-007', 'title': 'Executive Cybersecurity Leadership', 'definition': 'Responsible for establishing vision and direction for an organization\'s cybersecurity operations and resources and their impact on digital and physical spaces. Possesses authority to make and execute decisions that impact an organization broadly, including policy approval and stakeholder engagement.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-008', 'title': 'Privacy Compliance', 'definition': 'Responsible for developing and overseeing an organization\'s privacy compliance program and staff, including establishing and managing privacy-related governance, policy, and incident response needs.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-009', 'title': 'Product Support Management', 'definition': 'Responsible for planning, estimating costs, budgeting, developing, implementing, and managing product support strategies in order to field and maintain the readiness and operational capability of systems and components.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-010', 'title': 'Program Management', 'definition': 'Responsible for leading, coordinating, and the overall success of a defined program. Includes communicating about the program and ensuring alignment with agency or organizational priorities.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-011', 'title': 'Secure Project Management', 'definition': 'Responsible for overseeing and directly managing technology projects. Ensures cybersecurity is built into projects to protect the organization\'s critical infrastructure and assets, reduce risk, and meet organizational goals. Tracks and communicates project status and demonstrates project value to the organization.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-012', 'title': 'Security Control Assessment', 'definition': 'Responsible for conducting independent comprehensive assessments of management, operational, and technical security controls and control enhancements employed within or inherited by a system to determine their overall effectiveness.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'OG-WRL-013', 'title': 'Systems Authorization', 'definition': 'Responsible for operating an information system at an acceptable level of risk to organizational operations, organizational assets, individuals, other organizations, and the nation.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'OG-WRL-014', 'title': 'Systems Security Management', 'definition': 'Responsible for managing the cybersecurity of a program, organization, system, or enclave.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'OG-WRL-015', 'title': 'Technology Portfolio Management', 'definition': 'Responsible for managing a portfolio of technology investments that align with the overall needs of mission and enterprise priorities.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-016', 'title': 'Technology Program Auditing', 'definition': 'Responsible for conducting evaluations of technology programs or their individual components to determine compliance with published standards.', 'category': 'Cyber Enablers'},
            
            # DESIGN and DEVELOPMENT (DD)
            {'ncwf_id': 'DD-WRL-001', 'title': 'Cybersecurity Architecture', 'definition': 'Responsible for ensuring that security requirements are adequately addressed in all aspects of enterprise architecture, including reference models, segment and solution architectures, and the resulting systems that protect and support organizational mission and business processes.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'DD-WRL-002', 'title': 'Enterprise Architecture', 'definition': 'Responsible for developing and maintaining business, systems, and information processes to support enterprise mission needs. Develops technology rules and requirements that describe baseline and target architectures.', 'category': 'Information Technology'},
            {'ncwf_id': 'DD-WRL-003', 'title': 'Secure Software Development', 'definition': 'Responsible for developing, creating, modifying, and maintaining computer applications, software, or specialized utility programs.', 'category': 'Software Engineering'},
            {'ncwf_id': 'DD-WRL-004', 'title': 'Secure Systems Development', 'definition': 'Responsible for the secure design, development, and testing of systems and the evaluation of system security throughout the systems development life cycle.', 'category': 'Software Engineering'},
            {'ncwf_id': 'DD-WRL-005', 'title': 'Software Security Assessment', 'definition': 'Responsible for analyzing the security of new or existing computer applications, software, or specialized utility programs and delivering actionable results.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'DD-WRL-006', 'title': 'Systems Requirements Planning', 'definition': 'Responsible for consulting with internal and external customers to evaluate and translate functional requirements and integrating security policies into technical solutions.', 'category': 'Information Technology'},
            {'ncwf_id': 'DD-WRL-007', 'title': 'Systems Testing and Evaluation', 'definition': 'Responsible for planning, preparing, and executing system tests; evaluating test results against specifications and requirements; and reporting test results and findings.', 'category': 'Software Engineering'},
            {'ncwf_id': 'DD-WRL-008', 'title': 'Technology Research and Development', 'definition': 'Responsible for conducting software and systems engineering and software systems research to develop new capabilities with fully integrated cybersecurity. Conducts comprehensive technology research to evaluate potential vulnerabilities in cyberspace systems.', 'category': 'Information Technology'},
            {'ncwf_id': 'DD-WRL-009', 'title': 'Operational Technology (OT) Cybersecurity Engineering', 'definition': 'Responsible for working within the engineering department to design and create systems, processes, and procedures that maintain the safety, reliability, controllability, and security of industrial systems in the face of intentional and incidental cyber-related events. Interfaces with Chief Information Security Officer, plant managers, and industrial cybersecurity technicians.', 'category': 'Software Engineering'},
            
            # IMPLEMENTATION and OPERATION (IO)
            {'ncwf_id': 'IO-WRL-001', 'title': 'Data Analysis', 'definition': 'Responsible for analyzing data from multiple disparate sources to provide cybersecurity and privacy insight. Designs and implements custom algorithms, workflow processes, and layouts for complex, enterprise-scale data sets used for modeling, data mining, and research purposes.', 'category': 'Data/AI'},
            {'ncwf_id': 'IO-WRL-002', 'title': 'Database Administration', 'definition': 'Responsible for administering databases and data management systems that allow for the secure storage, query, protection, and utilization of data.', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-003', 'title': 'Knowledge Management', 'definition': 'Responsible for managing and administering processes and tools to identify, document, and access an organization\'s intellectual capital.', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-004', 'title': 'Network Operations', 'definition': 'Responsible for planning, implementing, and operating network services and systems, including hardware and virtual environments.', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-005', 'title': 'Systems Administration', 'definition': 'Responsible for setting up and maintaining a system or specific components of a system in adherence with organizational security policies and procedures. Includes hardware and software installation, configuration, and updates; user account management; backup and recovery management; and security control implementation.', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-006', 'title': 'Systems Security Analysis', 'definition': 'Responsible for developing and analyzing the integration, testing, operations, and maintenance of systems security. Prepares, performs, and manages the security aspects of implementing and operating a system.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'IO-WRL-007', 'title': 'Technical Support', 'definition': 'Responsible for providing technical support to customers who need assistance utilizing client-level hardware and software in accordance with established or approved organizational policies and processes.', 'category': 'Information Technology'},
            
            # PROTECTION and DEFENSE (PD)
            {'ncwf_id': 'PD-WRL-001', 'title': 'Defensive Cybersecurity', 'definition': 'Responsible for analyzing data collected from various cybersecurity defense tools to mitigate risks.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-002', 'title': 'Digital Forensics', 'definition': 'Responsible for analyzing digital evidence from computer security incidents to derive useful information in support of system and network vulnerability mitigation.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'PD-WRL-003', 'title': 'Incident Response', 'definition': 'Responsible for investigating, analyzing, and responding to network cybersecurity incidents.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-004', 'title': 'Infrastructure Support', 'definition': 'Responsible for testing, implementing, deploying, maintaining, and administering infrastructure hardware and software for cybersecurity.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-005', 'title': 'Insider Threat Analysis', 'definition': 'Responsible for identifying and assessing the capabilities and activities of cybersecurity insider threats; produces findings to help initialize and support law enforcement and counterintelligence activities and investigations.', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-006', 'title': 'Threat Analysis', 'definition': 'Responsible for collecting, processing, analyzing, and disseminating cybersecurity threat assessments. Develops cybersecurity indicators to maintain awareness of the status of the highly dynamic operating environment.', 'category': 'Cyber Effects'},
            {'ncwf_id': 'PD-WRL-007', 'title': 'Vulnerability Analysis', 'definition': 'Responsible for assessing systems and networks to identify deviations from acceptable configurations, enclave policy, or local policy. Measure effectiveness of defense-in-depth architecture against known vulnerabilities.', 'category': 'Cybersecurity'},
            
            # CYBER EFFECTS (CE)
            {'ncwf_id': 'CE-WRL-001', 'title': 'Mission Assessment Specialist', 'definition': 'Develops assessment plans and measures of performance/effectiveness. Conducts strategic and operational effectiveness assessments as required for cyber events. Determines whether systems performed as expected and provides input to the determination of operational effectiveness.', 'category': 'Cyber Effects'},
            {'ncwf_id': 'CE-WRL-002', 'title': 'Partner Integration Planner', 'definition': 'Works to advance cooperation across organizational or national borders between cyber operations partners. Aids the integration of partner cyber teams by providing guidance, ressources, and collaboration to develop best practices and facilitate organizational support for achieving objectives in integrated cyber actions.', 'category': 'Cyber Effects'},
            
            # INVESTIGATION (IN)
            {'ncwf_id': 'IN-WRL-001', 'title': 'Cybercrime Investigation', 'definition': 'Responsible for investigating cyberspace intrusion incidents and crimes. Applies tactics, techniques, and procedures for a full range of investigative tools and processes and appropriately balances the benefits of prosecution versus intelligence gathering.', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'IN-WRL-002', 'title': 'Digital Evidence Analysis', 'definition': 'Responsible for identifying, collecting, examining, and preserving digital evidence using controlled and documented analytical and investigative techniques.', 'category': 'Cyber Enablers'},
        ]

