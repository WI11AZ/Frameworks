import json
import os
from django.core.management.base import BaseCommand
from web_app.models import Ncwf2025Ksat, Dcwf2025Ksat, Ncwf2025WorkRoleKsatRelation, Dcwf2025WorkRoleKsatRelation


class Command(BaseCommand):
    help = 'Importe les lettres core_or_additional depuis le fichier NIST vers les modèles KSAT 2025'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='NIST/(U)+2025-07-25+DCWF+Work+Role+Tool_v5.1.json',
            help='Chemin vers le fichier JSON NIST à importer'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'Le fichier {file_path} n\'existe pas')
            )
            return

        self.stdout.write('Début de l\'importation des lettres core_or_additional...')

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Créer un mapping des descriptions NIST vers les KSAT 2025
            nist_elements = {}
            if 'elements' in data:
                for element in data['elements']:
                    element_id = element.get('element_identifier', '')
                    text = element.get('text', '')
                    if element_id and text:
                        nist_elements[element_id] = text

            # Statistiques
            total_updated_ncwf = 0
            total_updated_dcwf = 0
            total_updated_relations_ncwf = 0
            total_updated_relations_dcwf = 0

            # Parcourir les relations dans le fichier NIST
            if 'relationships' in data:
                for relationship in data['relationships']:
                    # Vérifier si c'est une relation avec core_or_additional
                    if 'core_or_additional' in relationship:
                        source_id = relationship.get('source_element_identifier', '')
                        dest_id = relationship.get('dest_element_identifier', '')
                        core_or_additional = relationship.get('core_or_additional', 'A')
                        
                        # Trouver le KSAT correspondant par description
                        if dest_id in nist_elements:
                            description = nist_elements[dest_id]
                            
                            # Chercher dans les KSAT NCWF 2025
                            ncwf_ksats = Ncwf2025Ksat.objects.filter(description__icontains=description[:50])
                            for ncwf_ksat in ncwf_ksats:
                                if ncwf_ksat.core_or_additional != core_or_additional:
                                    ncwf_ksat.core_or_additional = core_or_additional
                                    ncwf_ksat.save()
                                    total_updated_ncwf += 1
                                    self.stdout.write(f'  + KSAT NCWF 2025 mis à jour: {ncwf_ksat.ncwf_id} -> {core_or_additional}')
                                
                                # Mettre à jour les relations NCWF 2025
                                for relation in Ncwf2025WorkRoleKsatRelation.objects.filter(ksat=ncwf_ksat):
                                    if relation.core_or_additional != core_or_additional:
                                        relation.core_or_additional = core_or_additional
                                        relation.save()
                                        total_updated_relations_ncwf += 1
                                        self.stdout.write(f'  + Relation NCWF 2025 mise à jour: {relation.work_role.ncwf_id} - {ncwf_ksat.ncwf_id} -> {core_or_additional}')
                            
                            # Chercher dans les KSAT DCWF 2025
                            dcwf_ksats = Dcwf2025Ksat.objects.filter(description__icontains=description[:50])
                            for dcwf_ksat in dcwf_ksats:
                                if dcwf_ksat.core_or_additional != core_or_additional:
                                    dcwf_ksat.core_or_additional = core_or_additional
                                    dcwf_ksat.save()
                                    total_updated_dcwf += 1
                                    self.stdout.write(f'  + KSAT DCWF 2025 mis à jour: {dcwf_ksat.dcwf_id} -> {core_or_additional}')
                                
                                # Mettre à jour les relations DCWF 2025
                                for relation in Dcwf2025WorkRoleKsatRelation.objects.filter(ksat=dcwf_ksat):
                                    if relation.core_or_additional != core_or_additional:
                                        relation.core_or_additional = core_or_additional
                                        relation.save()
                                        total_updated_relations_dcwf += 1
                                        self.stdout.write(f'  + Relation DCWF 2025 mise à jour: {relation.work_role.dcwf_code} - {dcwf_ksat.dcwf_id} -> {core_or_additional}')

            self.stdout.write(
                self.style.SUCCESS(
                    f'Importation terminée avec succès!\n'
                    f'- KSATs NCWF 2025 mis à jour: {total_updated_ncwf}\n'
                    f'- KSATs DCWF 2025 mis à jour: {total_updated_dcwf}\n'
                    f'- Relations NCWF 2025 mises à jour: {total_updated_relations_ncwf}\n'
                    f'- Relations DCWF 2025 mises à jour: {total_updated_relations_dcwf}'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Erreur lors de l\'importation: {str(e)}')
            )
