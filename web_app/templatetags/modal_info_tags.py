from django import template
import json
from web_app.models import ModalInfo, ModalInfoCategory, KsatType

register = template.Library()

@register.simple_tag
def get_modal_info_json():
    """
    Récupère toutes les informations des modals et les retourne sous forme de JSON
    pour être utilisées par JavaScript.
    
    Returns:
        str: Un objet JSON contenant toutes les informations nécessaires pour 
             afficher les modals d'information.
    """
    # Structure de données qui sera convertie en JSON
    result = {
        'categories': {}
    }
    
    # Parcourir chaque catégorie de modal (info-button-1, info-button-2, info-button-3)
    for category in ModalInfoCategory.objects.all():
        result['categories'][category.button_id] = {
            'name': category.name,
            'description': category.description,
            'infos': {}
        }
        
        # Récupérer toutes les infos pour cette catégorie
        for ksat_type in KsatType.objects.all():
            try:
                modal_info = ModalInfo.objects.get(category=category, ksat_type=ksat_type)
                options = modal_info.options.all().order_by('order')
                
                result['categories'][category.button_id]['infos'][ksat_type.name.lower()] = {
                    'title': modal_info.title,
                    'options': [{'text': option.text, 'title': option.title} for option in options]
                }
            except ModalInfo.DoesNotExist:
                # Si pas d'info pour ce type de KSAT, on passe
                pass
    
    return json.dumps(result)
