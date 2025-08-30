from django.core.management.base import BaseCommand
from web_app.models import Dcwf2025Category, Dcwf2025WorkRole

class Command(BaseCommand):
    help = 'Fix DCWF and NCWF role separation and titles'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Fixing DCWF and NCWF role separation...'))
        
        # Dictionnaire des titres corrects selon le framework
        dcwf_titles = {
            '651': 'Enterprise Architect',  # Au lieu de "Enterprise Architecture"
            '421': 'Database Administrator',
            '431': 'Knowledge Manager', 
            '441': 'Network Operations Specialist',
            '451': 'System Administrator',
            '411': 'Technical Support Specialist',
            '661': 'Research & Development Specialist',
            '652': 'Security Architect',
            '621': 'Software Developer',
            '622': 'Secure Software Assessor',
            '631': 'Information Systems Security Developer',
            '632': 'Systems Developer',
            '641': 'Systems Requirements Planner',
            '671': 'System Testing and Evaluation Specialist',
            '511': 'Cyber Defense Analyst',
            '521': 'Cyber Defense Infrastructure Support Specialist',
            '531': 'Cyber Defense Incident Responder',
            '541': 'Vulnerability Assessment Analyst',
            '611': 'Authorizing Official/Designated Representative',
            '612': 'Security Control Assessor',
            '722': 'Information Systems Security Manager',
            '723': 'COMSEC Manager',
            '731': 'Cyber Legal Advisor',
            '732': 'Privacy Compliance Specialist',
            '751': 'Cyber Workforce Developer and Manager',
            '752': 'Cyber Policy and Strategy Planner',
            '801': 'Program Manager',
            '802': 'IT Project Manager',
            '803': 'Product Support Manager',
            '804': 'IT Investment/Portfolio Manager',
            '805': 'IT Program Auditor',
            '901': 'Executive Cyber Leader',
            '122': 'Digital Network Exploitation Analyst',
            '131': 'Joint Targeting Analyst',
            '132': 'Target Digital Network Analyst',
            '133': 'Target Analyst Reporter',
            '141': 'Threat Analyst',
            '151': 'Intelligence Analyst',
            '211': 'Forensics Analyst',
            '212': 'Digital Forensics Specialist',
            '221': 'Cyber Crime Investigator',
            '321': 'Access Network Operator',
            '322': 'Cyberspace Operator',
            '331': 'Cyber Operations Planner',
            '332': 'Cyber Operations Planner',
            '333': 'Cyber Operations Planner',
            '341': 'Cyberspace Capability Developer',
            '442': 'Network Technician',
            '443': 'Network Analyst',
            '461': 'Host Analyst',
            '462': 'Control Systems Security Specialist',
            '463': 'Host Analyst',
            '551': 'Red Team Specialist',
            '611': 'Authorizing Official/Designated Representative',
            '612': 'Security Control Assessor',
            '623': 'AI/ML Specialist',
            '624': 'Data Operations Specialist',
            '641': 'Systems Requirements Planner',
            '651': 'Enterprise Architect',
            '652': 'Security Architect',
            '653': 'Data Architect',
            '661': 'Research & Development Specialist',
            '671': 'System Testing and Evaluation Specialist',
            '672': 'AI Test & Evaluation Specialist',
            '673': 'Software Test & Evaluation Specialist',
            '711': 'Cyber Instructional Curriculum Developer',
            '712': 'Cyber Instructor',
            '731': 'Cyber Legal Advisor',
            '732': 'Privacy Compliance Specialist',
            '733': 'AI Risk and Ethics Specialist',
            '751': 'Cyber Workforce Developer and Manager',
            '752': 'Cyber Policy and Strategy Planner',
            '753': 'AI Adoption Specialist',
            '801': 'Program Manager',
            '802': 'IT Project Manager',
            '803': 'Product Support Manager',
            '804': 'IT Investment/Portfolio Manager',
            '805': 'IT Program Auditor',
            '806': 'Product Manager',
            '901': 'Executive Cyber Leader',
            '902': 'AI Innovation Leader',
            '903': 'Data Officer',
            '422': 'Data Scientist',
            '423': 'Data Scientist',
            '424': 'Data Steward',
        }
        
        ncwf_titles = {
            'DD-WRL-001': 'Cybersecurity Architecture',
            'DD-WRL-002': 'Enterprise Architecture',
            'DD-WRL-003': 'Secure Software Development',
            'DD-WRL-004': 'Secure Systems Development',
            'DD-WRL-005': 'Software Security Assessment',
            'DD-WRL-006': 'Systems Requirements Planning',
            'DD-WRL-007': 'Systems Testing and Evaluation',
            'DD-WRL-008': 'Technology Research and Development',
            'DD-WRL-009': 'Operational Technology (OT) Cybersecurity Engineering',
            'IO-WRL-001': 'Data Analysis',
            'IO-WRL-002': 'Database Administration',
            'IO-WRL-003': 'Knowledge Management',
            'IO-WRL-004': 'Network Operations',
            'IO-WRL-005': 'Systems Administration',
            'IO-WRL-006': 'Systems Security Analysis',
            'IO-WRL-007': 'Technical Support',
            'OG-WRL-001': 'Communications Security (COMSEC) Management',
            'OG-WRL-002': 'Cybersecurity Policy and Planning',
            'OG-WRL-003': 'Cybersecurity Workforce Management',
            'OG-WRL-004': 'Cybersecurity Curriculum Development',
            'OG-WRL-005': 'Cybersecurity Instruction',
            'OG-WRL-006': 'Cybersecurity Legal Advice',
            'OG-WRL-007': 'Executive Cybersecurity Leadership',
            'OG-WRL-008': 'Privacy Compliance',
            'OG-WRL-009': 'Product Support Management',
            'OG-WRL-010': 'Program Management',
            'OG-WRL-011': 'Secure Project Management',
            'OG-WRL-012': 'Security Control Assessment',
            'OG-WRL-013': 'Systems Authorization',
            'OG-WRL-014': 'Systems Security Management',
            'OG-WRL-015': 'Technology Portfolio Management',
            'OG-WRL-016': 'Technology Program Auditing',
            'PD-WRL-001': 'Defensive Cybersecurity',
            'PD-WRL-002': 'Digital Forensics',
            'PD-WRL-003': 'Incident Response',
            'PD-WRL-004': 'Infrastructure Support',
            'PD-WRL-005': 'Insider Threat Analysis',
            'PD-WRL-006': 'Threat Analysis',
            'PD-WRL-007': 'Vulnerability Analysis',
            'IN-WRL-001': 'Cybercrime Investigation',
            'IN-WRL-002': 'Digital Evidence Analysis',
        }
        
        updated_count = 0
        
        # Mettre à jour tous les rôles avec les titres corrects
        for work_role in Dcwf2025WorkRole.objects.all():
            updated = False
            
            # Mettre à jour le titre DCWF si il y a un code DCWF
            if work_role.dcwf_code and work_role.dcwf_code in dcwf_titles:
                new_title = dcwf_titles[work_role.dcwf_code]
                if work_role.title != new_title:
                    work_role.title = new_title
                    updated = True
            
            # Mettre à jour le titre NCWF si il y a un ID NCWF
            if work_role.ncwf_id and work_role.ncwf_id in ncwf_titles:
                new_ncwf_title = ncwf_titles[work_role.ncwf_id]
                # Créer un champ séparé pour le titre NCWF
                if not hasattr(work_role, 'ncwf_title'):
                    work_role.ncwf_title = new_ncwf_title
                    updated = True
                elif work_role.ncwf_title != new_ncwf_title:
                    work_role.ncwf_title = new_ncwf_title
                    updated = True
            
            if updated:
                work_role.save()
                updated_count += 1
                self.stdout.write(f'  Mis à jour: {work_role.dcwf_code or "N/A"} / {work_role.ncwf_id or "N/A"} - {work_role.title}')
        
        self.stdout.write(self.style.SUCCESS(f'Correction terminée! {updated_count} rôles mis à jour.'))
        
        # Afficher quelques exemples pour vérification
        self.stdout.write('\n=== EXEMPLES DE CORRECTION ===')
        examples = Dcwf2025WorkRole.objects.filter(dcwf_code='651')[:3]
        for ex in examples:
            self.stdout.write(f'  DCWF 651: {ex.title}')
            if hasattr(ex, 'ncwf_title'):
                self.stdout.write(f'  NCWF {ex.ncwf_id}: {ex.ncwf_title}')
            self.stdout.write('  ---')
