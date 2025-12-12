import json
import os
import re
from django.core.management.base import BaseCommand
from web_app.models import Dcwf2025Ksat, Dcwf2025WorkRole, Dcwf2025WorkRoleKsatRelation


class Command(BaseCommand):
    help = 'Importe les données KSAT DCWF 2025 depuis le fichier JSON final'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='KSAT 2025 FINAL/DCWF 2025/dcwf_data.json',
            help='Chemin vers le fichier JSON à importer'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'Le fichier {file_path} n\'existe pas')
            )
            return

        self.stdout.write('Début de l\'importation des données KSAT DCWF 2025...')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Statistiques
            total_ksats = 0
            total_relations = 0
            ksats_created = 0
            ksats_updated = 0
            relations_created = 0
            relations_updated = 0
            work_roles_not_found = set()

            # Dictionnaire pour regrouper les KSAT par opm_id
            ksats_by_opm = {}
            
            for item in data:
                opm_id = item.get('opm_id', '').strip()
                if not opm_id:
                    continue
                
                # Extraire le code OPM (ex: "(CE-121)" -> "121", "(CS-511)" -> "511")
                # Format: (CATEGORY-NUMBER) -> NUMBER
                match = re.search(r'\([^-]+-(\d+)\)', opm_id)
                if match:
                    opm_code = match.group(1)  # Extraire juste le numéro
                else:
                    # Fallback: enlever les parenthèses et essayer de trouver le numéro
                    opm_code = opm_id.strip('()')
                    # Si format "CATEGORY-NUMBER", extraire le numéro
                    if '-' in opm_code:
                        opm_code = opm_code.split('-')[-1]
                
                if opm_code not in ksats_by_opm:
                    ksats_by_opm[opm_code] = []
                
                ksats_by_opm[opm_code].append(item)

            self.stdout.write(f'Nombre de work roles trouvés dans le JSON: {len(ksats_by_opm)}')
            self.stdout.write(f'Nombre total de KSAT à importer: {len(data)}')

            # Supprimer tous les KSAT DCWF 2025 existants et leurs relations
            self.stdout.write('Suppression des KSAT DCWF 2025 existants...')
            Dcwf2025WorkRoleKsatRelation.objects.all().delete()
            deleted_count = Dcwf2025Ksat.objects.all().delete()[0]
            self.stdout.write(f'  {deleted_count} KSAT supprimés')

            # Traiter chaque work role
            for opm_code, ksats_list in ksats_by_opm.items():
                # Chercher le work role par dcwf_code
                work_role = Dcwf2025WorkRole.objects.filter(dcwf_code=opm_code).first()
                
                if not work_role:
                    work_roles_not_found.add(opm_code)
                    self.stdout.write(
                        self.style.WARNING(f'  ⚠ Work role non trouvé pour OPM code: {opm_code}')
                    )
                    continue

                self.stdout.write(f'\nTraitement du work role: {work_role.dcwf_code} - {work_role.title}')
                self.stdout.write(f'  Nombre de KSAT: {len(ksats_list)}')

                # Traiter chaque KSAT
                for ksat_data in ksats_list:
                    ksat_id = ksat_data.get('id', '').strip()
                    # Ignorer les IDs invalides
                    if not ksat_id or ksat_id == 'DCWF #' or ksat_id == '#' or ksat_id.startswith('DCWF #'):
                        continue
                    
                    # Ignorer les KSAT sans description
                    description = ksat_data.get('description') or ''
                    if description:
                        description = str(description).strip()
                    else:
                        description = ''
                    
                    if not description:
                        self.stdout.write(
                            self.style.WARNING(f'    ⚠ KSAT ignoré (pas de description): ID {ksat_id}')
                        )
                        continue

                    # Déterminer la catégorie
                    ksat_type_raw = ksat_data.get('ksat', '').strip()
                    # Mapper K* à K (les knowledge communs)
                    if ksat_type_raw == 'K*':
                        ksat_category = 'knowledge'
                    elif ksat_type_raw == 'T':
                        ksat_category = 'task'
                    elif ksat_type_raw == 'K':
                        ksat_category = 'knowledge'
                    elif ksat_type_raw == 'S':
                        ksat_category = 'skill'
                    elif ksat_type_raw == 'A':
                        ksat_category = 'ability'
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'    ⚠ Type KSAT inconnu: {ksat_type_raw} pour ID: {ksat_id}')
                        )
                        continue

                    # Récupérer core_or_additional
                    core_or_additional_raw = ksat_data.get('core_or_additional') or 'A'
                    if core_or_additional_raw:
                        core_or_additional = str(core_or_additional_raw).strip().upper()
                    else:
                        core_or_additional = 'A'
                    if core_or_additional not in ['C', 'A']:
                        core_or_additional = 'A'

                    # Créer ou mettre à jour le KSAT
                    ksat, created = Dcwf2025Ksat.objects.get_or_create(
                        dcwf_id=ksat_id,
                        defaults={
                            'description': description,
                            'category': ksat_category,
                            'core_or_additional': core_or_additional
                        }
                    )

                    if created:
                        ksats_created += 1
                        total_ksats += 1
                    else:
                        # Mettre à jour si nécessaire
                        updated = False
                        if ksat.description != description:
                            ksat.description = description
                            updated = True
                        if ksat.category != ksat_category:
                            ksat.category = ksat_category
                            updated = True
                        if ksat.core_or_additional != core_or_additional:
                            ksat.core_or_additional = core_or_additional
                            updated = True
                        
                        if updated:
                            ksat.save()
                            ksats_updated += 1
                        total_ksats += 1

                    # Créer la relation work role - KSAT
                    relation, created = Dcwf2025WorkRoleKsatRelation.objects.get_or_create(
                        work_role=work_role,
                        ksat=ksat,
                        defaults={
                            'core_or_additional': core_or_additional
                        }
                    )

                    if created:
                        relations_created += 1
                        total_relations += 1
                    else:
                        # Mettre à jour si nécessaire
                        if relation.core_or_additional != core_or_additional:
                            relation.core_or_additional = core_or_additional
                            relation.save()
                            relations_updated += 1
                        total_relations += 1

            # Résumé
            self.stdout.write('\n' + '='*60)
            self.stdout.write(self.style.SUCCESS('Importation terminée avec succès!'))
            self.stdout.write('='*60)
            self.stdout.write(f'Statistiques:')
            self.stdout.write(f'  - KSAT créés: {ksats_created}')
            self.stdout.write(f'  - KSAT mis à jour: {ksats_updated}')
            self.stdout.write(f'  - Total KSAT: {total_ksats}')
            self.stdout.write(f'  - Relations créées: {relations_created}')
            self.stdout.write(f'  - Relations mises à jour: {relations_updated}')
            self.stdout.write(f'  - Total relations: {total_relations}')
            
            if work_roles_not_found:
                self.stdout.write(
                    self.style.WARNING(
                        f'\n⚠ {len(work_roles_not_found)} work roles non trouvés dans la base de données:'
                    )
                )
                for opm_code in sorted(work_roles_not_found):
                    self.stdout.write(f'    - {opm_code}')

        except Exception as e:
            import traceback
            self.stdout.write(
                self.style.ERROR(f'Erreur lors de l\'importation: {str(e)}')
            )
            self.stdout.write(traceback.format_exc())

