import json
import os
from django.core.management.base import BaseCommand
from web_app.models import Ncwf2025Ksat, Ncwf2025WorkRole, Ncwf2025WorkRoleKsatRelation


class Command(BaseCommand):
    help = 'Importe les données KSAT 2025 depuis le fichier JSON'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='KSAT25/work_roles.json',
            help='Chemin vers le fichier JSON à importer'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'Le fichier {file_path} n\'existe pas')
            )
            return

        self.stdout.write('Début de l\'importation des données KSAT 2025...')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            work_roles_data = data.get('work_roles', [])
            
            # Statistiques
            total_work_roles = len(work_roles_data)
            total_ksats = 0
            total_relations = 0

            self.stdout.write(f'Importation de {total_work_roles} work roles...')

            for work_role_data in work_roles_data:
                # Déterminer l'ID à utiliser (work_role_code ou opm_id)
                work_role_id = None
                if 'work_role_code' in work_role_data:
                    work_role_id = work_role_data['work_role_code']
                elif 'opm_id' in work_role_data:
                    work_role_id = f"OPM-{work_role_data['opm_id']}"
                else:
                    self.stdout.write(f'  ⚠ Work role ignoré (pas de work_role_code ni opm_id): {work_role_data.get("name", "Sans nom")}')
                    continue
                    
                # Créer ou récupérer le work role selon le framework
                framework = work_role_data.get('framework', 'NCWF')
                if framework == 'DCWF':
                    # Créer un work role DCWF 2025
                    from web_app.models import Dcwf2025WorkRole
                    work_role, created = Dcwf2025WorkRole.objects.get_or_create(
                        dcwf_code=work_role_data.get('opm_id', ''),
                        defaults={
                            'title': work_role_data['name'],
                            'ncwf_id': work_role_data.get('ncwf_id', ''),
                            'definition': work_role_data.get('description', ''),
                            'ncwf_title': work_role_data.get('ncwf_title', ''),
                            'ncwf_definition': work_role_data.get('ncwf_definition', '')
                        }
                    )
                else:
                    # Créer un work role NCWF 2025
                    work_role, created = Ncwf2025WorkRole.objects.get_or_create(
                        ncwf_id=work_role_id,
                        defaults={
                            'name': work_role_data['name'],
                            'framework': framework,
                            'description': work_role_data.get('description', '')
                        }
                    )

                if created:
                    self.stdout.write(f'  ✓ Work role créé: {work_role.ncwf_id}')
                else:
                    self.stdout.write(f'  - Work role existant: {work_role.ncwf_id}')

                # Traiter les KSATs par catégorie
                for category, ksats_list in work_role_data.items():
                    if category in ['tasks', 'knowledge', 'skills', 'abilities'] and isinstance(ksats_list, list):
                        # Déterminer le type de KSAT
                        ksat_type = 'task' if category == 'tasks' else category.rstrip('s')
                        
                        for ksat_data in ksats_list:
                            # Vérifier que l'ID existe
                            if 'id' not in ksat_data or not ksat_data['id']:
                                continue
                                
                            # Déterminer core_or_additional avec une valeur par défaut sûre
                            core_or_additional = 'C'  # Par défaut Core
                            if 'core_or_additional' in ksat_data and ksat_data['core_or_additional']:
                                core_or_additional = ksat_data['core_or_additional']
                                
                            # Créer ou récupérer le KSAT
                            ksat, created = Ncwf2025Ksat.objects.get_or_create(
                                ncwf_id=ksat_data['id'],
                                defaults={
                                    'description': ksat_data.get('description', ''),
                                    'category': ksat_type,
                                    'core_or_additional': core_or_additional
                                }
                            )

                            if created:
                                total_ksats += 1
                                self.stdout.write(f'    ✓ KSAT créé: {ksat.ncwf_id}')

                            # Créer la relation work role - KSAT
                            if framework == 'DCWF':
                                # Pour les work roles DCWF 2025, créer des KSATs DCWF 2025 et leurs relations
                                from web_app.models import Dcwf2025Ksat, Dcwf2025WorkRoleKsatRelation
                                
                                # Créer ou récupérer le KSAT DCWF 2025 avec un ID unique
                                # Utiliser une combinaison du work role et de la description pour créer un ID unique
                                unique_id = f"{work_role.dcwf_code}_{ksat_type}_{hash(ksat_data.get('description', '')) % 10000}"
                                dcwf_ksat, created = Dcwf2025Ksat.objects.get_or_create(
                                    dcwf_id=unique_id,
                                    defaults={
                                        'description': ksat_data.get('description', ''),
                                        'category': ksat_type,
                                        'core_or_additional': core_or_additional
                                    }
                                )
                                
                                # Créer la relation work role DCWF 2025 - KSAT DCWF 2025
                                relation, created = Dcwf2025WorkRoleKsatRelation.objects.get_or_create(
                                    work_role=work_role,
                                    ksat=dcwf_ksat,
                                    defaults={
                                        'core_or_additional': core_or_additional
                                    }
                                )
                                if created:
                                    total_relations += 1
                            else:
                                # Pour les work roles NCWF 2025, créer la relation directement
                                relation, created = Ncwf2025WorkRoleKsatRelation.objects.get_or_create(
                                    work_role=work_role,
                                    ksat=ksat,
                                    defaults={
                                        'core_or_additional': core_or_additional
                                    }
                                )
                                if created:
                                    total_relations += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f'Importation terminée avec succès!\n'
                    f'- Work roles: {total_work_roles}\n'
                    f'- KSATs créés: {total_ksats}\n'
                    f'- Relations créées: {total_relations}'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Erreur lors de l\'importation: {str(e)}')
            )
