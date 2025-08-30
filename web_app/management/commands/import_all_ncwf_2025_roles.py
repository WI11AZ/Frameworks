from django.core.management.base import BaseCommand
from web_app.models import Dcwf2025Category, Dcwf2025WorkRole

class Command(BaseCommand):
    help = 'Import ALL NCWF 2025 roles from NCWF25Tempo.html'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Importing ALL NCWF 2025 roles...'))
        
        # Données complètes extraites du fichier NCWF25Tempo.html
        ncwf_roles = [
            # OVERSIGHT and GOVERNANCE (OG)
            {'ncwf_id': 'OG-WRL-001', 'title': 'Communications Security (COMSEC) Management', 'definition': 'Responsible for managing the Communications Security (COMSEC) resources of an organization.', 'opm_code': '723', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-002', 'title': 'Cybersecurity Policy and Planning', 'definition': 'Responsible for developing and maintaining cybersecurity plans, strategy, and policy to support and align with organizational cybersecurity initiatives and regulatory compliance.', 'opm_code': '752', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-003', 'title': 'Cybersecurity Workforce Management', 'definition': 'Responsible for developing cybersecurity workforce plans, assessments, strategies, and guidance, including cybersecurity-related staff training, education, and hiring processes. Makes adjustments in response to or in anticipation of changes to cybersecurity-related policy, technology, and staffing needs and requirements. Authors mandated workforce planning strategies to maintain compliance with legislation, regulation, and policy.', 'opm_code': '751', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-004', 'title': 'Cybersecurity Curriculum Development', 'definition': 'Responsible for developing, planning, coordinating, and evaluating cybersecurity awareness, training, or education content, methods, and techniques based on instructional needs and requirements.', 'opm_code': '711', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-005', 'title': 'Cybersecurity Instruction', 'definition': 'Responsible for developing and conducting cybersecurity awareness, training, or education.', 'opm_code': '712', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-006', 'title': 'Cybersecurity Legal Advice', 'definition': 'Responsible for providing cybersecurity legal advice and recommendations, including monitoring related legislation and regulations.', 'opm_code': '731', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-007', 'title': 'Executive Cybersecurity Leadership', 'definition': 'Responsible for establishing vision and direction for an organization\'s cybersecurity operations and resources and their impact on digital and physical spaces. Possesses authority to make and execute decisions that impact an organization broadly, including policy approval and stakeholder engagement.', 'opm_code': '901', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-008', 'title': 'Privacy Compliance', 'definition': 'Responsible for developing and overseeing an organization\'s privacy compliance program and staff, including establishing and managing privacy-related governance, policy, and incident response needs.', 'opm_code': '732', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-009', 'title': 'Product Support Management', 'definition': 'Responsible for planning, estimating costs, budgeting, developing, implementing, and managing product support strategies in order to field and maintain the readiness and operational capability of systems and components.', 'opm_code': '803', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-010', 'title': 'Program Management', 'definition': 'Responsible for leading, coordinating, and the overall success of a defined program. Includes communicating about the program and ensuring alignment with agency or organizational priorities.', 'opm_code': '801', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-011', 'title': 'Secure Project Management', 'definition': 'Responsible for overseeing and directly managing technology projects. Ensures cybersecurity is built into projects to protect the organization\'s critical infrastructure and assets, reduce risk, and meet organizational goals. Tracks and communicates project status and demonstrates project value to the organization.', 'opm_code': '802', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-012', 'title': 'Security Control Assessment', 'definition': 'Responsible for conducting independent comprehensive assessments of management, operational, and technical security controls and control enhancements employed within or inherited by a system to determine their overall effectiveness.', 'opm_code': '612', 'category': 'Cybersecurity'},
            {'ncwf_id': 'OG-WRL-013', 'title': 'Systems Authorization', 'definition': 'Responsible for operating an information system at an acceptable level of risk to organizational operations, organizational assets, individuals, other organizations, and the nation.', 'opm_code': '611', 'category': 'Cybersecurity'},
            {'ncwf_id': 'OG-WRL-014', 'title': 'Systems Security Management', 'definition': 'Responsible for managing the cybersecurity of a program, organization, system, or enclave.', 'opm_code': '722', 'category': 'Cybersecurity'},
            {'ncwf_id': 'OG-WRL-015', 'title': 'Technology Portfolio Management', 'definition': 'Responsible for managing a portfolio of technology investments that align with the overall needs of mission and enterprise priorities.', 'opm_code': '804', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'OG-WRL-016', 'title': 'Technology Program Auditing', 'definition': 'Responsible for conducting evaluations of technology programs or their individual components to determine compliance with published standards.', 'opm_code': '805', 'category': 'Cyber Enablers'},
            
            # DESIGN and DEVELOPMENT (DD)
            {'ncwf_id': 'DD-WRL-001', 'title': 'Cybersecurity Architecture', 'definition': 'Responsible for ensuring that security requirements are adequately addressed in all aspects of enterprise architecture, including reference models, segment and solution architectures, and the resulting systems that protect and support organizational mission and business processes.', 'opm_code': '652', 'category': 'Cybersecurity'},
            {'ncwf_id': 'DD-WRL-002', 'title': 'Enterprise Architecture', 'definition': 'Responsible for developing and maintaining business, systems, and information processes to support enterprise mission needs. Develops technology rules and requirements that describe baseline and target architectures.', 'opm_code': '651', 'category': 'Information Technology'},
            {'ncwf_id': 'DD-WRL-003', 'title': 'Secure Software Development', 'definition': 'Responsible for developing, creating, modifying, and maintaining computer applications, software, or specialized utility programs.', 'opm_code': '621', 'category': 'Software Engineering'},
            {'ncwf_id': 'DD-WRL-004', 'title': 'Secure Systems Development', 'definition': 'Responsible for the secure design, development, and testing of systems and the evaluation of system security throughout the systems development life cycle.', 'opm_code': '631 and 632', 'category': 'Software Engineering'},
            {'ncwf_id': 'DD-WRL-005', 'title': 'Software Security Assessment', 'definition': 'Responsible for analyzing the security of new or existing computer applications, software, or specialized utility programs and delivering actionable results.', 'opm_code': '622', 'category': 'Cybersecurity'},
            {'ncwf_id': 'DD-WRL-006', 'title': 'Systems Requirements Planning', 'definition': 'Responsible for consulting with internal and external customers to evaluate and translate functional requirements and integrating security policies into technical solutions.', 'opm_code': '641', 'category': 'Information Technology'},
            {'ncwf_id': 'DD-WRL-007', 'title': 'Systems Testing and Evaluation', 'definition': 'Responsible for planning, preparing, and executing system tests; evaluating test results against specifications and requirements; and reporting test results and findings.', 'opm_code': '671', 'category': 'Software Engineering'},
            {'ncwf_id': 'DD-WRL-008', 'title': 'Technology Research and Development', 'definition': 'Responsible for conducting software and systems engineering and software systems research to develop new capabilities with fully integrated cybersecurity. Conducts comprehensive technology research to evaluate potential vulnerabilities in cyberspace systems.', 'opm_code': '661', 'category': 'Information Technology'},
            {'ncwf_id': 'DD-WRL-009', 'title': 'Operational Technology (OT) Cybersecurity Engineering', 'definition': 'Responsible for working within the engineering department to design and create systems, processes, and procedures that maintain the safety, reliability, controllability, and security of industrial systems in the face of intentional and incidental cyber-related events. Interfaces with Chief Information Security Officer, plant managers, and industrial cybersecurity technicians.', 'opm_code': 'TBD', 'category': 'Software Engineering'},
            
            # IMPLEMENTATION and OPERATION (IO)
            {'ncwf_id': 'IO-WRL-001', 'title': 'Data Analysis', 'definition': 'Responsible for analyzing data from multiple disparate sources to provide cybersecurity and privacy insight. Designs and implements custom algorithms, workflow processes, and layouts for complex, enterprise-scale data sets used for modeling, data mining, and research purposes.', 'opm_code': '422', 'category': 'Data/AI'},
            {'ncwf_id': 'IO-WRL-002', 'title': 'Database Administration', 'definition': 'Responsible for administering databases and data management systems that allow for the secure storage, query, protection, and utilization of data.', 'opm_code': '421', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-003', 'title': 'Knowledge Management', 'definition': 'Responsible for managing and administering processes and tools to identify, document, and access an organization\'s intellectual capital.', 'opm_code': '431', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-004', 'title': 'Network Operations', 'definition': 'Responsible for planning, implementing, and operating network services and systems, including hardware and virtual environments.', 'opm_code': '441', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-005', 'title': 'Systems Administration', 'definition': 'Responsible for setting up and maintaining a system or specific components of a system in adherence with organizational security policies and procedures. Includes hardware and software installation, configuration, and updates; user account management; backup and recovery management; and security control implementation.', 'opm_code': '451', 'category': 'Information Technology'},
            {'ncwf_id': 'IO-WRL-006', 'title': 'Systems Security Analysis', 'definition': 'Responsible for developing and analyzing the integration, testing, operations, and maintenance of systems security. Prepares, performs, and manages the security aspects of implementing and operating a system.', 'opm_code': '461', 'category': 'Cybersecurity'},
            {'ncwf_id': 'IO-WRL-007', 'title': 'Technical Support', 'definition': 'Responsible for providing technical support to customers who need assistance utilizing client-level hardware and software in accordance with established or approved organizational policies and processes.', 'opm_code': '411', 'category': 'Information Technology'},
            
            # PROTECTION and DEFENSE (PD)
            {'ncwf_id': 'PD-WRL-001', 'title': 'Defensive Cybersecurity', 'definition': 'Responsible for analyzing data collected from various cybersecurity defense tools to mitigate risks.', 'opm_code': '511', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-002', 'title': 'Digital Forensics', 'definition': 'Responsible for analyzing digital evidence from computer security incidents to derive useful information in support of system and network vulnerability mitigation.', 'opm_code': '212', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'PD-WRL-003', 'title': 'Incident Response', 'definition': 'Responsible for investigating, analyzing, and responding to network cybersecurity incidents.', 'opm_code': '531', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-004', 'title': 'Infrastructure Support', 'definition': 'Responsible for testing, implementing, deploying, maintaining, and administering infrastructure hardware and software for cybersecurity.', 'opm_code': '521', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-005', 'title': 'Insider Threat Analysis', 'definition': 'Responsible for identifying and assessing the capabilities and activities of cybersecurity insider threats; produces findings to help initialize and support law enforcement and counterintelligence activities and investigations.', 'opm_code': 'TBD', 'category': 'Cybersecurity'},
            {'ncwf_id': 'PD-WRL-006', 'title': 'Threat Analysis', 'definition': 'Responsible for collecting, processing, analyzing, and disseminating cybersecurity threat assessments. Develops cybersecurity indicators to maintain awareness of the status of the highly dynamic operating environment.', 'opm_code': '141', 'category': 'Cyber Effects'},
            {'ncwf_id': 'PD-WRL-007', 'title': 'Vulnerability Analysis', 'definition': 'Responsible for assessing systems and networks to identify deviations from acceptable configurations, enclave policy, or local policy. Measure effectiveness of defense-in-depth architecture against known vulnerabilities.', 'opm_code': '541', 'category': 'Cybersecurity'},
            
            # INVESTIGATION (IN)
            {'ncwf_id': 'IN-WRL-001', 'title': 'Cybercrime Investigation', 'definition': 'Responsible for investigating cyberspace intrusion incidents and crimes. Applies tactics, techniques, and procedures for a full range of investigative tools and processes and appropriately balances the benefits of prosecution versus intelligence gathering.', 'opm_code': '221', 'category': 'Cyber Enablers'},
            {'ncwf_id': 'IN-WRL-002', 'title': 'Digital Evidence Analysis', 'definition': 'Responsible for identifying, collecting, examining, and preserving digital evidence using controlled and documented analytical and investigative techniques.', 'opm_code': '211', 'category': 'Cyber Enablers'},
        ]
        
        created_count = 0
        updated_count = 0
        
        for role_data in ncwf_roles:
            # Vérifier si le rôle existe déjà
            existing_role = Dcwf2025WorkRole.objects.filter(ncwf_id=role_data['ncwf_id']).first()
            
            if existing_role:
                # Mettre à jour le rôle existant
                existing_role.title = role_data['title']
                existing_role.definition = role_data['definition']
                existing_role.ncwf_definition = role_data['definition']
                existing_role.save()
                updated_count += 1
                self.stdout.write(f'  Mis à jour: {role_data["ncwf_id"]} - {role_data["title"]}')
            else:
                # Créer un nouveau rôle
                # Trouver la catégorie correspondante
                category = Dcwf2025Category.objects.filter(title=role_data['category']).first()
                
                if category:
                    new_role = Dcwf2025WorkRole.objects.create(
                        dcwf_code=role_data['opm_code'] if role_data['opm_code'] != 'TBD' else None,
                        ncwf_id=role_data['ncwf_id'],
                        title=role_data['title'],
                        definition=role_data['definition'],
                        ncwf_definition=role_data['definition'],
                        category=category
                    )
                    created_count += 1
                    self.stdout.write(f'  Créé: {role_data["ncwf_id"]} - {role_data["title"]} dans {category.title}')
                else:
                    self.stdout.write(f'  ERREUR: Catégorie "{role_data["category"]}" non trouvée pour {role_data["ncwf_id"]}')
        
        self.stdout.write(self.style.SUCCESS(f'Import terminé! {created_count} nouveaux rôles créés, {updated_count} rôles mis à jour.'))
        self.stdout.write(f'Total des rôles NCWF 2025: {Dcwf2025WorkRole.objects.count()}')
