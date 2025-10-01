#!/usr/bin/env python
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcwf.settings')
django.setup()

from web_app.models.ncwf_2025_ksat import Ncwf2025WorkRole

def fix_ncwf_2025_titles():
    """Supprime la partie WRL entre parenthèses des titres NCWF 2025"""
    
    # Récupérer tous les work roles NCWF 2025
    work_roles = Ncwf2025WorkRole.objects.all()
    
    print(f"Traitement de {work_roles.count()} work roles NCWF 2025...")
    
    updated_count = 0
    
    for work_role in work_roles:
        original_name = work_role.name
        
        # Supprimer la partie entre parenthèses qui contient WRL
        # Exemple: "Database Administration (IO-WRL-002)" -> "Database Administration"
        if '(' in original_name and 'WRL' in original_name:
            # Trouver la position de la parenthèse ouvrante
            paren_pos = original_name.find('(')
            if paren_pos != -1:
                # Garder seulement la partie avant la parenthèse
                new_name = original_name[:paren_pos].strip()
                
                # Mettre à jour le work role
                work_role.name = new_name
                work_role.save()
                
                print(f"✓ Mis à jour: '{original_name}' -> '{new_name}'")
                updated_count += 1
    
    print(f"\n✅ Modification terminée! {updated_count} work roles mis à jour.")

if __name__ == "__main__":
    fix_ncwf_2025_titles()
