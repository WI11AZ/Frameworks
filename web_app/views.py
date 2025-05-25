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
    formatted_roles = []
    
    # Rôles DCWF
    dcwf_work_roles = DcwfWorkRole.objects.filter(id__in=dcwf_ids)
    for role in dcwf_work_roles:
        formatted_roles.append({
            'model_obj': role,
            'title': role.title,
            'framework': 'DCWF',
            'id': role.id,
            'model_type': 'dcwf'
        })
    
    # Rôles NCWF 2017
    ncwf_2017_work_roles = Ncwf2017WorkRole.objects.filter(id__in=ncwf_2017_ids)
    for role in ncwf_2017_work_roles:
        formatted_roles.append({
            'model_obj': role,
            'title': role.title,  # Utilise le titre spécifique du NCWF 2017
            'framework': 'NCWF 2017',
            'id': role.id,
            'model_type': 'ncwf_2017'
        })
        
    # Rôles NCWF 2024
    ncwf_2024_work_roles = Ncwf2024WorkRole.objects.filter(id__in=ncwf_2024_ids)
    for role in ncwf_2024_work_roles:
        formatted_roles.append({
            'model_obj': role,
            'title': role.title,  # Utilise le titre spécifique du NCWF 2024
            'framework': 'NCWF 2024',
            'id': role.id,
            'model_type': 'ncwf_2024'
        })

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
            print(f"ABILITY TROUVÉ: KSAT ID: {ksat.id}, Description: {ksat.description}")
            # S'assurer qu'il est ajouté à la bonne clé du dictionnaire
            ksat_dict['abilitie'].append(ksat)
        else:
            # Autres catégories
            ksat_dict.get(category, []).append(ksat)
    
    # Afficher les catégories trouvées pour le débogage
    print(f"Catégories trouvées: {categories_found}")
    print(f"Des KSATs de type 'ability' ont été trouvés: {ability_ksats_found}")
    print(f"Contenu du ksat_dict: {[key + ': ' + str(len(items)) for key, items in ksat_dict.items()]}")
    
    # Si aucun KSAT de type ability n'est trouvé, ajouter un KSAT fictif pour déboguer
    if not ability_ksats_found:
        print("Aucun KSAT de type 'ability' trouvé, ajout d'un KSAT fictif pour déboguer")
        # Créer un objet dict qui reproduit la structure minimale d'un KSAT
        dummy_ability = {'id': 0, 'description': 'TEST - Ceci est un KSAT fictif pour déboguer'}
        # Vous pouvez remplacer ce dictionnaire par un vrai objet DcwfKsat si nécessaire
        # ksat_dict['abilitie'].append(dummy_ability)

    return render(request, 'web_app/ksat/compare_ksat.html', {
        'work_roles': work_roles,
        'ksat_dict': ksat_dict,
        'formatted_roles': formatted_roles,
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
