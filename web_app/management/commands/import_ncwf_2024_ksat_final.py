import json
import os
from django.core.management.base import BaseCommand
from web_app.models import Ncwf2024Tks, Ncwf2024WorkRole


class Command(BaseCommand):
    help = 'Importe les données KSAT NCWF 2024 depuis le fichier JSON final pour les OPM IDs spécifiés'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='KSAT 2024 FINAL/filtered_by_opm_id.json',
            help='Chemin vers le fichier JSON à importer'
        )
        parser.add_argument(
            '--opm-ids',
            type=str,
            nargs='+',
            default=['112', '121', '131', '132', '321', '332', '333', '111', '151', '311', '312', '331'],
            help='Liste des OPM IDs à importer'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        target_opm_ids = set(options['opm_ids'])
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'Le fichier {file_path} n\'existe pas')
            )
            return

        self.stdout.write('Début de l\'importation des données KSAT NCWF 2024...')
        self.stdout.write(f'OPM IDs cibles: {sorted(target_opm_ids)}')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Filtrer uniquement les OPM IDs cibles
            filtered_data = [item for item in data if item.get('OPM-ID', '').strip() in target_opm_ids]
            self.stdout.write(f'Nombre de KSAT après filtrage: {len(filtered_data)}')

            # Statistiques
            total_ksats = 0
            ksats_created = 0
            ksats_updated = 0
            relations_created = 0
            work_roles_not_found = set()

            # Dictionnaire pour regrouper les KSAT par WRL-ID
            ksats_by_wrl = {}
            
            for item in filtered_data:
                wrl_id = item.get('WRL-ID', '').strip()
                if not wrl_id:
                    continue
                
                if wrl_id not in ksats_by_wrl:
                    ksats_by_wrl[wrl_id] = []
                
                ksats_by_wrl[wrl_id].append(item)

            self.stdout.write(f'Nombre de work roles trouvés dans le JSON: {len(ksats_by_wrl)}')

            # Supprimer uniquement les KSAT liés aux work roles des OPM IDs cibles
            # Pour cela, on doit d'abord trouver les work roles concernés
            from web_app.models import Opm
            target_opms = Opm.objects.filter(id__in=[int(opm_id) for opm_id in target_opm_ids])
            target_work_roles = Ncwf2024WorkRole.objects.filter(opms__in=target_opms).distinct()
            
            self.stdout.write(f'Nombre de work roles NCWF 2024 trouvés pour les OPM IDs: {target_work_roles.count()}')
            
            # Supprimer les relations existantes pour ces work roles
            for work_role in target_work_roles:
                work_role.ncwf_2024_tks.clear()
            
            self.stdout.write('Relations existantes supprimées pour les work roles cibles')

            # Traiter chaque work role
            for wrl_id, ksats_list in ksats_by_wrl.items():
                # Chercher le work role par nist_id (qui correspond au WRL-ID)
                work_role = Ncwf2024WorkRole.objects.filter(nist_id=wrl_id).first()
                
                if not work_role:
                    work_roles_not_found.add(wrl_id)
                    self.stdout.write(
                        self.style.WARNING(f'  WARNING: Work role non trouve pour WRL-ID: {wrl_id}')
                    )
                    continue

                self.stdout.write(f'\nTraitement du work role: {work_role.nist_id} - {work_role.title}')
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

                    # Créer ou mettre à jour le KSAT
                    ksat, created = Ncwf2024Tks.objects.get_or_create(
                        ncwf_id=ksat_id,
                        defaults={
                            'description': description,
                            'category': ksat_category
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
                        
                        if updated:
                            ksat.save()
                            ksats_updated += 1
                        total_ksats += 1

                    # Créer la relation work role - KSAT (ManyToMany)
                    if not work_role.ncwf_2024_tks.filter(id=ksat.id).exists():
                        work_role.ncwf_2024_tks.add(ksat)
                        relations_created += 1

            # Résumé
            self.stdout.write('\n' + '='*60)
            self.stdout.write(self.style.SUCCESS('Importation terminée avec succès!'))
            self.stdout.write('='*60)
            self.stdout.write(f'Statistiques:')
            self.stdout.write(f'  - KSAT créés: {ksats_created}')
            self.stdout.write(f'  - KSAT mis à jour: {ksats_updated}')
            self.stdout.write(f'  - Total KSAT: {total_ksats}')
            self.stdout.write(f'  - Relations créées: {relations_created}')
            
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

