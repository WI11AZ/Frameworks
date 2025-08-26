from django.template import loader
from collections import defaultdict
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse
from .models import (
    DcwfCategory,
    DcwfWorkRole,
    Ncwf2017WorkRole,
    Ncwf2024WorkRole,
    DcwfKsat,
    DcwfWorkRoleKsatRelation, Ncwf2017Ksat, Ncwf2024Tks
)
from .models.user_saved_data import UserSavedData
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def attributs_part_deux(request):
    """Vue pour la page AttributsPartDeux"""
    return render(request, 'web_app/main/AttributsPartDeux.html')



def get_nist_id(role):
    role_2024 = role.ncwf_2024_work_role
    if callable(role_2024):
        role_2024 = role_2024()
    return role_2024.nist_id if role_2024 else ""


def get_sorted_cyber_roles(roles):
    groups = defaultdict(list)

    for role in roles:
        nist_id = get_nist_id(role)
        prefix = nist_id[:2] if nist_id else "ZZ"
        groups[prefix].append(role)

    for prefix in groups:
        groups[prefix].sort(key=get_nist_id)

    return [
        groups["OG"],
        groups["PD"],
        groups["DD"] + [None] + groups["ZZ"],
    ]


def get_sorted_it_roles(roles):
    groups = defaultdict(list)

    for role in roles:
        nist_id = get_nist_id(role)
        prefix = nist_id[:2] if nist_id else "ZZ"
        groups[prefix].append(role)

    for prefix in groups:
        groups[prefix].sort(key=get_nist_id)

    return [
        groups["IO"],
        groups["DD"],
    ]


def get_sorted_cybereffects_roles(roles):
    groups = defaultdict(list)

    for role in roles:
        nist_id = get_nist_id(role)
        prefix = nist_id[:2] if nist_id else "ZZ"
        groups[prefix].append(role)

    for prefix in groups:
        groups[prefix].sort(key=get_nist_id)

    return [
        groups["CE"],
        groups["ZZ"],
    ]


def get_sorted_enabler_roles(roles):
    groups = defaultdict(list)

    for role in roles:
        nist_id = get_nist_id(role)
        prefix = nist_id[:2] if nist_id else "ZZ"
        groups[prefix].append(role)

    for prefix in groups:
        groups[prefix].sort(key=get_nist_id)

    return [
        groups["OG"] + [None] + groups["IN"],
    ]


def get_sorted_software_engineering_roles(roles):
    groups = defaultdict(list)

    for role in roles:
        nist_id = get_nist_id(role)
        prefix = nist_id[:2] if nist_id else "ZZ"
        groups[prefix].append(role)

    for prefix in groups:
        groups[prefix].sort(key=get_nist_id)

    return [
        groups["DD"] + [None] + groups["IO"],
        groups["ZZ"],
    ]


def get_sorted_data_ai_roles(roles):
    groups = defaultdict(list)

    for role in roles:
        nist_id = get_nist_id(role)
        prefix = nist_id[:2] if nist_id else "ZZ"
        groups[prefix].append(role)

    for prefix in groups:
        groups[prefix].sort(key=get_nist_id)

    return [
        groups["IO"],
        groups["ZZ"],
    ]


def home(request):
    template = loader.get_template("web_app/home/index.html")

    # 1. Tes requêtes existantes
    it_work_roles = DcwfCategory.objects.get(title="IT (Cyberspace)").dcwf_work_roles.all()
    cyber_security_work_roles = DcwfCategory.objects.get(title="Cybersecurity").dcwf_work_roles.all()
    cyber_effects_work_roles = DcwfCategory.objects.get(title="Cyberspace Effects").dcwf_work_roles.all()
    intel_work_roles = DcwfCategory.objects.get(title="Intelligence (Cyberspace)").dcwf_work_roles.all()
    enabler_work_roles = DcwfCategory.objects.get(title="Cyberspace Enablers").dcwf_work_roles.all()
    software_engineering_work_roles = DcwfCategory.objects.get(title="Software Engineering").dcwf_work_roles.all()
    data_work_roles = DcwfCategory.objects.get(title="Data/AI").dcwf_work_roles.all()

    # 2. Tes tris existants
    sorted_cyber_security_lines = get_sorted_cyber_roles(cyber_security_work_roles)
    it_work_lines = get_sorted_it_roles(it_work_roles)
    cyber_effects_work_lines = get_sorted_cybereffects_roles(cyber_effects_work_roles)
    enabler_work_lines = get_sorted_enabler_roles(enabler_work_roles)
    software_engineering_work_lines = get_sorted_software_engineering_roles(software_engineering_work_roles)
    data_work_lines = get_sorted_data_ai_roles(data_work_roles)

    # 3. Liste des OPM IDs à surligner
    #    Ajuste le type (int ou str) selon celui de work_role.opm_id
    highlight_ids = [901, 722, 723, 752, 661, 622, 631, 461, 511, 521,
        531, 541, 141, 121, 111, 112, 443, 151, 331, 332,
        333, 322, 221, 211, 212, 651, 652, 621, 641, 671,
        632, 411, 451, 803, 801, 802, 804, 312, 421, 422,
        612, 805, 731, 732, 751, 711, 712, 311, 431, 611,]

    # 4. Contexte final
    context = {
        "it_work_lines": it_work_lines,
        "cyber_security_lines": sorted_cyber_security_lines,
        "cyber_effects_work_lines": cyber_effects_work_lines,
        "intel_work_roles": intel_work_roles,
        "enabler_work_lines": enabler_work_lines,
        "software_engineering_work_lines": software_engineering_work_lines,
        "data_work_lines": data_work_lines,
        "categories": DcwfCategory.objects.all(),
        "highlight_ids": highlight_ids,
    }

    return HttpResponse(template.render(context, request))

def work_role(request, work_role_id):
    template = loader.get_template("web_app/work_role/index.html")
    work_role = DcwfWorkRole.objects.get(id=work_role_id)
    ksat_relations = DcwfWorkRoleKsatRelation.objects.filter(dcwf_work_role=work_role).all()
    ksats = [ksat_relation.dcwf_ksat for ksat_relation in ksat_relations]
    knowledge_list = [ksat for ksat in ksats if ksat.category == "knowledge"]
    skills_list = [ksat for ksat in ksats if ksat.category == "skill"]
    abilities_list = [ksat for ksat in ksats if ksat.category == "ability"]
    tasks_list = [ksat for ksat in ksats if ksat.category == "task"]
    cat_dict = {
        "knowledge": knowledge_list,
        "skill": skills_list,
        "abilitie": abilities_list,
        "task": tasks_list,
    }
    context = {
        "work_role": work_role,
        "cat_dict": cat_dict,
    }
    return HttpResponse(template.render(context, request))





def compare(request):
    # 1. Récupère les ids passés en GET
    dcwf_ids = request.GET.getlist('dcwf_ids')
    ncwf_2017_ids = request.GET.getlist('ncwf_2017_ids')
    ncwf_2024_ids = request.GET.getlist('ncwf_2024_ids')
    try:
        dcwf_ids = [int(i) for i in dcwf_ids]
    except ValueError:
        dcwf_ids = []

    # Peut-être que fais un try/except ici aussi, mais je pense pas que c'est nécessaire ?
    ncwf_2017_ids = [int(i) for i in ncwf_2017_ids]
    ncwf_2024_ids = [int(i) for i in ncwf_2024_ids]

    # 2. Récupère les Work Roles avec leurs titres spécifiques
    # Initialiser les listes de rôles formatés et la liste finale
    dcwf_formatted_roles = []
    ncwf_2017_formatted_roles = []
    ncwf_2024_formatted_roles = []
    
    # Créer des dictionnaires pour les mappings entre frameworks
    dcwf_to_ncwf_2017 = {}
    dcwf_to_ncwf_2024 = {}
    
    # Récupérer tous les rôles DCWF et leurs correspondances
    dcwf_work_roles = DcwfWorkRole.objects.filter(id__in=dcwf_ids)
    for role in dcwf_work_roles:
        # Récupérer la couleur de la catégorie
        category_color = role.category.color if hasattr(role, 'category') and role.category else '59, 130, 246'  # Bleu par défaut
        
        # Ajouter le rôle DCWF formaté
        dcwf_formatted_roles.append({
            'model_obj': role,
            'title': role.title,
            'framework': 'DCWF',
            'id': role.id,
            'model_type': 'dcwf',
            'parent_dcwf_id': role.id,  # Pour faciliter le regroupement
            'opm_id': role.opm.id if hasattr(role, 'opm') and role.opm else None,
            'category_color': category_color
        })
        
        # Stocker les mappings vers les autres frameworks
        # Vérifier si c'est un attribut ou une méthode (dans ce cas, l'appeler)
        if hasattr(role, 'ncwf_2017_work_role'):
            # Si c'est une méthode, l'appeler
            if callable(role.ncwf_2017_work_role):
                related_role = role.ncwf_2017_work_role()
                if related_role and hasattr(related_role, 'id'):
                    dcwf_to_ncwf_2017[role.id] = related_role.id
            # Si c'est un attribut et qu'il n'est pas None
            elif role.ncwf_2017_work_role and hasattr(role.ncwf_2017_work_role, 'id'):
                dcwf_to_ncwf_2017[role.id] = role.ncwf_2017_work_role.id
                
        if hasattr(role, 'ncwf_2024_work_role'):
            # Si c'est une méthode, l'appeler
            if callable(role.ncwf_2024_work_role):
                related_role = role.ncwf_2024_work_role()
                if related_role and hasattr(related_role, 'id'):
                    dcwf_to_ncwf_2024[role.id] = related_role.id
            # Si c'est un attribut et qu'il n'est pas None
            elif role.ncwf_2024_work_role and hasattr(role.ncwf_2024_work_role, 'id'):
                dcwf_to_ncwf_2024[role.id] = role.ncwf_2024_work_role.id
    
    # Récupérer tous les rôles NCWF 2017
    ncwf_2017_work_roles = Ncwf2017WorkRole.objects.filter(id__in=ncwf_2017_ids)
    for role in ncwf_2017_work_roles:
        # Trouver le DCWF parent (s'il existe)
        parent_dcwf_id = None
        for dcwf_id, ncwf_id in dcwf_to_ncwf_2017.items():
            if ncwf_id == role.id:
                parent_dcwf_id = dcwf_id
                break
                
        # Chercher la couleur de la catégorie du rôle parent DCWF s'il existe
        category_color = '16, 185, 129'  # Vert par défaut
        if parent_dcwf_id:
            for dcwf_role in dcwf_formatted_roles:
                if dcwf_role['id'] == parent_dcwf_id:
                    category_color = dcwf_role.get('category_color', category_color)
                    break
                    
        ncwf_2017_formatted_roles.append({
            'model_obj': role,
            'title': role.title,
            'framework': 'NCWF 2017',
            'id': role.id,
            'model_type': 'ncwf_2017',
            'parent_dcwf_id': parent_dcwf_id,  # Peut être None si pas de parent DCWF
            'opm_id': role.opms.first().id if role.opms.exists() else None,
            'category_color': category_color
        })
    
    # Récupérer tous les rôles NCWF 2024
    ncwf_2024_work_roles = Ncwf2024WorkRole.objects.filter(id__in=ncwf_2024_ids)
    for role in ncwf_2024_work_roles:
        # Trouver le DCWF parent (s'il existe)
        parent_dcwf_id = None
        for dcwf_id, ncwf_id in dcwf_to_ncwf_2024.items():
            if ncwf_id == role.id:
                parent_dcwf_id = dcwf_id
                break
                
        # Chercher la couleur de la catégorie du rôle parent DCWF s'il existe
        category_color = '239, 68, 68'  # Rouge par défaut
        if parent_dcwf_id:
            for dcwf_role in dcwf_formatted_roles:
                if dcwf_role['id'] == parent_dcwf_id:
                    category_color = dcwf_role.get('category_color', category_color)
                    break
                    
        ncwf_2024_formatted_roles.append({
            'model_obj': role,
            'title': role.title,
            'framework': 'NCWF 2024',
            'id': role.id,
            'model_type': 'ncwf_2024',
            'parent_dcwf_id': parent_dcwf_id,  # Peut être None si pas de parent DCWF
            'opm_id': role.opms.first().id if role.opms.exists() else None,
            'category_color': category_color
        })
        
    # Organiser tous les rôles par work_role d'origine
    # 1. D'abord, regrouper par DCWF parent
    formatted_roles = []
    processed_roles = set()  # Pour suivre les rôles déjà traités
    group_counter = 0  # Compteur pour générer des ID de groupe uniques
    
    # Traiter d'abord les rôles avec un parent DCWF
    for dcwf_role in dcwf_formatted_roles:
        dcwf_id = dcwf_role['id']
        if ('dcwf', dcwf_id) not in processed_roles and dcwf_id in dcwf_ids:
            # Créer un nouvel ID de groupe pour ce work_role compatible avec les classes CSS
            current_group_id = f"group-{group_counter % 10}"  # Modulo 10 pour limiter à 10 couleurs
            group_counter += 1
            
            # Ajouter le rôle DCWF
            dcwf_role['group_id'] = current_group_id
            formatted_roles.append(dcwf_role)
            processed_roles.add(('dcwf', dcwf_id))
            
            # Ajouter le rôle NCWF 2017 correspondant s'il est sélectionné
            if dcwf_id in dcwf_to_ncwf_2017 and dcwf_to_ncwf_2017[dcwf_id] in ncwf_2017_ids:
                for role in ncwf_2017_formatted_roles:
                    if role['id'] == dcwf_to_ncwf_2017[dcwf_id]:
                        role['group_id'] = current_group_id  # Ajouter le même ID de groupe
                        formatted_roles.append(role)
                        processed_roles.add(('ncwf_2017', role['id']))
            
            # Ajouter le rôle NCWF 2024 correspondant s'il est sélectionné
            if dcwf_id in dcwf_to_ncwf_2024 and dcwf_to_ncwf_2024[dcwf_id] in ncwf_2024_ids:
                for role in ncwf_2024_formatted_roles:
                    if role['id'] == dcwf_to_ncwf_2024[dcwf_id]:
                        role['group_id'] = current_group_id  # Ajouter le même ID de groupe
                        formatted_roles.append(role)
                        processed_roles.add(('ncwf_2024', role['id']))
                        break
    
    # Ajouter les rôles NCWF 2017 sans parent DCWF
    for role in ncwf_2017_formatted_roles:
        if ('ncwf_2017', role['id']) not in processed_roles and role['id'] in ncwf_2017_ids:
            # Créer un nouvel ID de groupe pour ce rôle
            current_group_id = f"group-{group_counter}"
            group_counter += 1
            role['group_id'] = current_group_id
            formatted_roles.append(role)
            processed_roles.add(('ncwf_2017', role['id']))
    
    # Ajouter les rôles NCWF 2024 sans parent DCWF
    for role in ncwf_2024_formatted_roles:
        if ('ncwf_2024', role['id']) not in processed_roles and role['id'] in ncwf_2024_ids:
            # Créer un nouvel ID de groupe pour ce rôle
            current_group_id = f"group-{group_counter}"
            group_counter += 1
            role['group_id'] = current_group_id
            formatted_roles.append(role)
            processed_roles.add(('ncwf_2024', role['id']))

    # 3. Récupère les KSATs
    ksats_dcwf = DcwfKsat.objects.filter(dcwf_work_role_relations__dcwf_work_role__in=dcwf_work_roles).distinct()
    # Prenez les ksats ncwf_2017 qui sont les mêmes que ceux dcwf
    ncwf_2017_ksats_in_dcwf = ksats_dcwf.values_list('ncwf_2017_ksat', flat=True)
    # Exclure les ksats ncwf_2017 qui sont déjà dans dcwf
    ksats_ncwf_2017 = Ncwf2017Ksat.objects.filter(ncwf_2017_work_roles__in=ncwf_2017_work_roles).exclude(id__in=ncwf_2017_ksats_in_dcwf).distinct()
    tks_ncwf_2024 = Ncwf2024Tks.objects.filter(ncwf_2024_work_roles__in=ncwf_2024_work_roles).distinct()


    # Combiner les KSATs pour la comparaison
    ksats = list(ksats_dcwf) + list(ksats_ncwf_2017) + list(tks_ncwf_2024)
    
    # Les rôles originaux sont toujours nécessaires pour certaines fonctionnalités existantes
    work_roles = list(dcwf_work_roles) + list(ncwf_2017_work_roles) + list(ncwf_2024_work_roles)

    # --- Correction ici : on utilise les clés singulières et on force l'affichage des abilités ---
    ksat_dict = { 'task': [],'knowledge': [], 'skill': [], 'abilitie': []}
    
    # Vérifier les catégories disponibles
    categories_found = set()
    ability_ksats_found = False
    
    for ksat in ksats:
        category = ksat.category.lower()
        categories_found.add(category)
        # Vérifier si des abilities sont présentes
        if category == 'ability':
            ability_ksats_found = True

            # S'assurer qu'il est ajouté à la bonne clé du dictionnaire
            ksat_dict['abilitie'].append(ksat)
        else:
            # Autres catégories
            ksat_dict.get(category, []).append(ksat)
    

    
    # Fonction pour extraire la partie numérique de dcwf_id
    def get_dcwf_numeric_id(ksat):
        # Vérifier si l'objet a l'attribut dcwf_id
        dcwf_id = getattr(ksat, 'dcwf_id', None)
        if not dcwf_id:
            return 0  # Valeur par défaut si pas de dcwf_id
            
        # Extraire seulement les chiffres du dcwf_id
        import re
        numeric_part = re.search(r'\d+', dcwf_id)
        return int(numeric_part.group()) if numeric_part else 0
    
    # Trier chaque catégorie de KSATs par ID DCWF de manière croissante
    for category in ksat_dict:
        ksat_dict[category] = sorted(ksat_dict[category], key=get_dcwf_numeric_id)

    # Initialiser tous les rôles avec show_opm_id = False
    for role in formatted_roles:
        role['show_opm_id'] = False
        
    # Regrouper les rôles par OPM ID pour les afficher centrés
    opm_groups = {}
    
    for idx, role in enumerate(formatted_roles):
        opm_id = role.get('opm_id')
        if not opm_id:
            continue
            
        if opm_id not in opm_groups:
            opm_groups[opm_id] = {
                'roles': [],
                'start_index': idx,
                'bgcolor': role.get('group_id', ''),  # Capturer la couleur du groupe
                'colspan': 0
            }
        
        # Si c'est le premier rôle de ce groupe OPM ID, marquer pour afficher l'OPM ID
        if len(opm_groups[opm_id]['roles']) == 0:
            role['show_opm_id'] = True
            
        opm_groups[opm_id]['roles'].append(role)
        opm_groups[opm_id]['colspan'] += 1
    
    # Créer une liste des groupes d'OPM ID dans l'ordre d'apparition
    opm_id_groups = []
    processed_opm_ids = set()
    
    for role in formatted_roles:
        opm_id = role.get('opm_id')
        if opm_id and opm_id not in processed_opm_ids:
            processed_opm_ids.add(opm_id)
            opm_id_groups.append({
                'opm_id': opm_id,
                'bgcolor': opm_groups[opm_id]['bgcolor'],
                'colspan': opm_groups[opm_id]['colspan'],
                'start_index': opm_groups[opm_id]['start_index']
            })
    

    return render(request, 'web_app/ksat/compare_ksat.html', {
        'work_roles': work_roles,
        'ksat_dict': ksat_dict,
        'formatted_roles': formatted_roles,
        'opm_id_groups': opm_id_groups,
    })


def get_modal_info_json_view(request):
    """
    Vue pour retourner les informations des modales au format JSON.
    Cette vue est utilisée par le code JavaScript pour charger dynamiquement
    les informations des modales.
    """
    from web_app.templatetags.modal_info_tags import get_modal_info_json
    import json
    
    # Récupérer les données depuis la fonction du template tag
    json_str = get_modal_info_json()
    
    # Parser le JSON pour le repasser à JsonResponse
    json_data = json.loads(json_str)
    
    # Retourner le JSON avec les bons headers CORS
    return JsonResponse(json_data)


def get_select_options_json_view(request):
    """
    Vue pour retourner les données des select options au format JSON.
    Utilisée par les modales d'information des niveaux KSAT.
    """
    from web_app.models import SelectOption, KsatType, SelectCategory
    
    try:
        # Structure de données à retourner
        data = {}
        
        # Récupérer tous les types KSAT
        ksat_types = KsatType.objects.all()
        
        for ksat_type in ksat_types:
            data[ksat_type.name] = {}
            
            # Récupérer toutes les catégories de select
            categories = SelectCategory.objects.all()
            
            for category in categories:
                # Récupérer les options pour ce type KSAT et cette catégorie
                options = SelectOption.objects.filter(
                    ksat_type=ksat_type,
                    category=category
                ).order_by('order')
                
                if options.exists():
                    data[ksat_type.name][category.name] = []
                    
                    for option in options:
                        data[ksat_type.name][category.name].append({
                            'value': option.value,
                            'title': option.title,
                            'description': option.description,
                            'order': option.order
                        })
        
        return JsonResponse(data)
        
    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": f"Erreur lors du chargement des données: {str(e)}"}, 
            status=500
        )


def ksat_compare_details(request):
    """
    Vue pour afficher la page de comparaison détaillée des KSATs.
    Cette page affiche les résultats des sélections de l'utilisateur
    dans un format restructuré.
    """
    return render(request, 'web_app/ksat/compare_details.html')


def etape_deux(request):
    """
    Vue pour afficher la page de l'étape deux.
    Cette page permet à l'utilisateur de saisir un numéro de poste et
    affiche les cadres de niveaux de maîtrise et domaines de compétence.
    """
    return render(request, 'web_app/ksat/etape_deux.html')


def saved_ksat_selections(request):
    """
    Vue pour afficher la page des sélections KSAT sauvegardées.
    Cette page affiche toutes les sélections KSAT sauvegardées dans localStorage
    et permet à l'utilisateur de les ouvrir ou de les supprimer.
    """
    return render(request, 'web_app/ksat/saved_ksat_selections.html')


def resume_step2(request, index):
    """
    Affiche la page de reprise d'une sélection étape 2 (poste de compétences) sauvegardée.
    """
    return render(request, 'web_app/ksat/resume_step2.html', {'index': index})

def etape2_first_step(request):
    """
    Vue pour afficher la première étape de l'étape deux.
    Cette page permet à l'utilisateur de commencer le processus de l'étape 2.
    """
    return render(request, 'web_app/ksat/etape2_first_step.html')

def summary_chart_view(request):
    return render(request, 'web_app/main/summary_chart_full.html')
    
def nf_com_007_details(request):
    """
    Vue pour afficher les détails sur NF-COM-007 (Cyber Resiliency).
    """
    return render(request, 'web_app/ksat/nf_com_007_details.html')
    
def nf_com_002_details(request):
    """
    Vue pour afficher les détails sur NF-COM-002 (Artificial Intelligence Security).
    """
    return render(request, 'web_app/ksat/nf_com_002_details.html')

@csrf_exempt
@require_http_methods(["POST"])
def save_ksat_selection(request):
    """
    Sauvegarde une sélection KSAT dans la base de données.
    Cette vue accepte les requêtes non authentifiées pour plus de flexibilité.
    """
    try:
        data = json.loads(request.body)
        key = data.get("key")
        value = data.get("value")
        
        if not key or value is None:
            return JsonResponse({"status": "error", "message": "La clé et la valeur sont requises"}, status=400)
        
        # Si l'utilisateur est authentifié, associer la sauvegarde à son compte
        if request.user.is_authenticated:
            UserSavedData.objects.update_or_create(
                user=request.user,
                key=key,
                defaults={"value": value}
            )
            return JsonResponse({"status": "success", "message": "Données sauvegardées"})
        else:
            # Pour les utilisateurs non authentifiés, stocker dans la session
            if 'saved_ksat_selections' not in request.session:
                request.session['saved_ksat_selections'] = {}
            
            request.session['saved_ksat_selections'][key] = value
            request.session.modified = True
            return JsonResponse({"status": "success", "message": "Données sauvegardées en session"})
    
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Format JSON invalide"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def list_ksat_selections(request):
    """
    Liste toutes les sélections KSAT pour l'utilisateur.
    """
    try:
        results = []
        
        # Récupérer les données de l'utilisateur authentifié
        if request.user.is_authenticated:
            saved_data = UserSavedData.objects.filter(user=request.user, key__startswith='ksat_selection_')
            for item in saved_data:
                results.append({
                    "key": item.key,
                    "value": item.value,
                    "updated_at": item.updated_at.isoformat() if hasattr(item.updated_at, 'isoformat') else str(item.updated_at)
                })
        
        # Ajouter les données de session pour tous les utilisateurs
        session_data = request.session.get('saved_ksat_selections', {})
        for key, value in session_data.items():
            if key.startswith('ksat_selection_'):
                results.append({
                    "key": key,
                    "value": value,
                    "updated_at": None  # Pas de date pour les données de session
                })
        
        return JsonResponse({"status": "success", "data": results})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["DELETE", "POST"])  # Accepter aussi POST pour la compatibilité
def delete_ksat_selection(request, key):
    """
    Supprime une sélection KSAT.
    Cette vue accepte les requêtes non authentifiées pour plus de flexibilité.
    """
    try:
        success = False
        
        # Si l'utilisateur est authentifié, supprimer de la base de données
        if request.user.is_authenticated:
            try:
                data = UserSavedData.objects.get(user=request.user, key=key)
                data.delete()
                success = True
            except UserSavedData.DoesNotExist:
                pass
        
        # Supprimer de la session dans tous les cas
        if 'saved_ksat_selections' in request.session and key in request.session['saved_ksat_selections']:
            del request.session['saved_ksat_selections'][key]
            request.session.modified = True
            success = True
        
        if success:
            return JsonResponse({"status": "success", "message": "Données supprimées"})
        else:
            return JsonResponse({"status": "error", "message": "Données introuvables"}, status=404)
            
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


def get_ncwf_prefix(work_role):
    """Extraire le préfixe du code NCWF (ex: OG-WRL, PR-CDA, etc.)"""
    if work_role.ncwf_id:
        # Extraire les 2 premières parties du code NCWF (ex: OG-WRL de OG-WRL-001)
        parts = work_role.ncwf_id.split('-')
        if len(parts) >= 2:
            return f"{parts[0]}-{parts[1]}"
    return "ZZ-ZZZ"  # Pour les work roles sans code NCWF, les mettre à la fin


def get_sorted_2025_roles(work_roles):
    """Organiser les work roles par famille de codes NCWF et les trier"""
    groups = defaultdict(list)
    
    for work_role in work_roles:
        prefix = get_ncwf_prefix(work_role)
        groups[prefix].append(work_role)
    
    # Trier chaque groupe par code NCWF complet
    for prefix in groups:
        groups[prefix].sort(key=lambda wr: wr.ncwf_id or "ZZ-ZZZ-999")
    
    # Organiser en lignes, en créant une nouvelle ligne pour chaque famille
    work_lines = []
    
    # Trier les préfixes pour un ordre cohérent
    sorted_prefixes = sorted(groups.keys())
    
    for prefix in sorted_prefixes:
        roles_in_group = groups[prefix]
        current_line = []
        
        for work_role in roles_in_group:
            current_line.append(work_role)
            
            # Si la ligne atteint 5 éléments, la finaliser et commencer une nouvelle
            if len(current_line) == 5:
                work_lines.append(current_line)
                current_line = []
        
        # Si on a des work roles restants dans cette famille, finaliser la ligne
        if current_line:
            # Compléter avec des None si nécessaire
            while len(current_line) < 5:
                current_line.append(None)
            work_lines.append(current_line)
    
    return work_lines


def models_2025(request):
    """Vue pour la page des modèles 2025"""
    from .models import Dcwf2025Category, Dcwf2025WorkRole
    
    template = loader.get_template("web_app/home/index25.html")
    
    # Récupérer toutes les catégories avec leurs work roles
    categories = []
    for category in Dcwf2025Category.objects.all().order_by('title'):
        work_roles = list(category.work_roles.all())
        
        # Organiser les work roles par famille de codes NCWF (comme dans l'original)
        work_lines = get_sorted_2025_roles(work_roles)
        
        if work_lines:  # Seulement ajouter les catégories qui ont des work roles
            categories.append({
                'category': category,
                'work_lines': work_lines
            })
    
    # Liste vide pour les IDs à surligner (pas nécessaire pour 2025)
    highlight_ids = []
    
    context = {
        "categories": categories,
        "highlight_ids": highlight_ids,
    }
    
    return HttpResponse(template.render(context, request))
