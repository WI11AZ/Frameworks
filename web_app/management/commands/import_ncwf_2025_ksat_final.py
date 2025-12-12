import json
import os
import re
from django.core.management.base import BaseCommand
from web_app.models import Ncwf2025Ksat, Ncwf2025WorkRole, Ncwf2025WorkRoleKsatRelation


class Command(BaseCommand):
    help = 'Importe les données KSAT NCWF 2025 depuis le fichier JSON final'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='KSAT 2025 FINAL/NCWF 2025/nice_framework_2.1.0.json',
            help='Chemin vers le fichier JSON à importer'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'Le fichier {file_path} n\'existe pas')
            )
            return

        self.stdout.write('Début de l\'importation des données KSAT NCWF 2025...')

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

            # Dictionnaire pour regrouper les KSAT par WRL-ID
            ksats_by_wrl = {}
            
            for item in data:
                wrl_id = item.get('WRL-ID', '').strip()
                if not wrl_id:
                    continue
                
                if wrl_id not in ksats_by_wrl:
                    ksats_by_wrl[wrl_id] = []
                
                ksats_by_wrl[wrl_id].append(item)

            self.stdout.write(f'Nombre de work roles trouvés dans le JSON: {len(ksats_by_wrl)}')
            self.stdout.write(f'Nombre total de KSAT à importer: {len(data)}')

            # Supprimer tous les KSAT NCWF 2025 existants et leurs relations
            self.stdout.write('Suppression des KSAT NCWF 2025 existants...')
            Ncwf2025WorkRoleKsatRelation.objects.all().delete()
            deleted_count = Ncwf2025Ksat.objects.all().delete()[0]
            self.stdout.write(f'  {deleted_count} KSAT supprimés')

            # Traiter chaque work role
            for wrl_id, ksats_list in ksats_by_wrl.items():
                # Chercher le work role par ncwf_id
                work_role = Ncwf2025WorkRole.objects.filter(ncwf_id=wrl_id).first()
                
                if not work_role:
                    work_roles_not_found.add(wrl_id)
                    self.stdout.write(
                        self.style.WARNING(f'  WARNING: Work role non trouve pour WRL-ID: {wrl_id}')
                    )
                    continue

                self.stdout.write(f'\nTraitement du work role: {work_role.ncwf_id} - {work_role.name}')
                self.stdout.write(f'  Nombre de KSAT: {len(ksats_list)}')

                # Traiter chaque KSAT
                for ksat_data in ksats_list:
                    ksat_id = ksat_data.get('ID', '').strip()
                    # Ignorer les IDs invalides
                    if not ksat_id or ksat_id == 'NCWF #' or ksat_id == '#' or ksat_id.startswith('NCWF #'):
                        continue
                    
                    # Ignorer les KSAT sans description
                    description = ksat_data.get('Description') or ''
                    if description:
                        description = str(description).strip()
                    else:
                        description = ''
                    
                    if not description:
                        self.stdout.write(
                            self.style.WARNING(f'    WARNING: KSAT ignore (pas de description): ID {ksat_id}')
                        )
                        continue

                    # Déterminer la catégorie
                    ksat_type_raw = ksat_data.get('KSAT', '').strip()
                    if ksat_type_raw == 'T':
                        ksat_category = 'task'
                    elif ksat_type_raw == 'K':
                        ksat_category = 'knowledge'
                    elif ksat_type_raw == 'S':
                        ksat_category = 'skill'
                    elif ksat_type_raw == 'A':
                        ksat_category = 'ability'
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'    WARNING: Type KSAT inconnu: {ksat_type_raw} pour ID: {ksat_id}')
                        )
                        continue

                    # Pour NCWF 2025, pas de core_or_additional dans le JSON, utiliser 'A' par défaut
                    core_or_additional = 'A'

                    # Créer ou mettre à jour le KSAT
                    ksat, created = Ncwf2025Ksat.objects.get_or_create(
                        ncwf_id=ksat_id,
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
                    relation, created = Ncwf2025WorkRoleKsatRelation.objects.get_or_create(
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
                        f'\nWARNING: {len(work_roles_not_found)} work roles non trouves dans la base de donnees:'
                    )
                )
                for wrl_id in sorted(work_roles_not_found)[:20]:  # Limiter à 20 pour l'affichage
                    self.stdout.write(f'    - {wrl_id}')

        except Exception as e:
            import traceback
            self.stdout.write(
                self.style.ERROR(f'Erreur lors de l\'importation: {str(e)}')
            )
            self.stdout.write(traceback.format_exc())

