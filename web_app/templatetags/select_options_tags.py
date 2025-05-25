from django import template
from web_app.models import SelectOption, KsatType, SelectCategory

register = template.Library()

@register.simple_tag
def get_select_options(ksat_type, category):
    """
    Récupère les options pour un type de KSAT et une catégorie de select donnés
    
    Args:
        ksat_type (str): 'Task', 'Knowledge', 'Skill', ou 'Ability'
        category (str): 'Importance', 'Type de maîtrise 1', 'Type de maîtrise 2', ou 'Type de maîtrise 3'
    
    Returns:
        QuerySet: Les options correspondantes
    """
    try:
        # Essayer de récupérer le type KSAT, d'abord par correspondance exacte puis par contenance
        try:
            ksat_type_obj = KsatType.objects.get(name=ksat_type)
        except KsatType.DoesNotExist:
            ksat_type_obj = KsatType.objects.filter(name__icontains=ksat_type).first()
            if not ksat_type_obj:
                print(f"ERREUR: Type KSAT '{ksat_type}' non trouvé. Types disponibles: {list(KsatType.objects.all().values_list('name', flat=True))}")
                return []
        
        # Essayer de récupérer la catégorie, d'abord par correspondance exacte puis par contenance
        try:
            category_obj = SelectCategory.objects.get(name=category)
        except SelectCategory.DoesNotExist:
            category_obj = SelectCategory.objects.filter(name__icontains=category).first()
            if not category_obj:
                print(f"ERREUR: Catégorie '{category}' non trouvée. Catégories disponibles: {list(SelectCategory.objects.all().values_list('name', flat=True))}")
                return []
        
        # Récupérer les options
        options = SelectOption.objects.filter(ksat_type=ksat_type_obj, category=category_obj).order_by('order')
        print(f"INFO: Trouvé {options.count()} options pour {ksat_type_obj.name}/{category_obj.name}")
        return options
    except Exception as e:
        print(f"ERREUR INATTENDUE: {str(e)}")
        return []

@register.inclusion_tag('web_app/tags/select_options.html')
def render_select_options(ksat_type, category, select_class, onchange_handler="", select_id=None):
    """
    Render un select avec les options d'une catégorie pour un type de KSAT
    
    Args:
        ksat_type (str): 'Task', 'Knowledge', 'Skill', ou 'Ability'
        category (str): 'Importance', 'Type de maîtrise 1', 'Type de maîtrise 2', ou 'Type de maîtrise 3'
        select_class (str): Classes CSS pour le select
        onchange_handler (str): Handler JavaScript pour l'événement onchange
        select_id (str, optional): Identifiant HTML pour le select
    """
    options = get_select_options(ksat_type, category)
    return {
        'options': options,
        'select_class': select_class,
        'onchange_handler': onchange_handler,
        'ksat_type': ksat_type,
        'category': category,
        'select_id': select_id
    }
