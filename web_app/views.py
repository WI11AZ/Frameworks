from django.template import loader
from collections import defaultdict
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, JsonResponse, FileResponse, Http404
from .models import (
    DcwfCategory,
    DcwfWorkRole,
    Ncwf2017WorkRole,
    Ncwf2024WorkRole,
    Ncwf2025WorkRole,
    DcwfKsat,
    DcwfWorkRoleKsatRelation, Ncwf2017Ksat, Ncwf2024Tks, Ncwf2025Ksat,
    AIWorkRole
)
from .models.user_saved_data import UserSavedData
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import os


def attributs_part_deux(request):
    """Vue pour la page AttributsPartDeux"""
    return render(request, 'web_app/main/AttributsPartDeux.html')

def dcwf_finder_view(request):
    """Vue pour servir le programme DCWF Finder"""
    from django.contrib.auth.decorators import login_required
    
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    # Servir le fichier index.html du dcwf-finder
    dcwf_finder_path = os.path.join(settings.BASE_DIR, 'web_app', 'static', 'dcwf-finder', 'index.html')
    
    if not os.path.exists(dcwf_finder_path):
        raise Http404("Programme DCWF Finder non trouvé")
    
    with open(dcwf_finder_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer les chemins statiques par des URLs Django
    content = content.replace('/static/dcwf-finder/style.css', '/dcwf-finder/css/')
    content = content.replace('/static/dcwf-finder/app.js', '/dcwf-finder/js/')
    content = content.replace('/static/dcwf-finder/dcwf_complete_79_roles.json', '/dcwf-finder/data/')
    
    return HttpResponse(content, content_type='text/html; charset=utf-8')

def dcwf_finder_css(request):
    """Vue pour servir le CSS du DCWF Finder"""
    css_path = os.path.join(settings.BASE_DIR, 'web_app', 'static', 'dcwf-finder', 'style.css')
    
    if not os.path.exists(css_path):
        raise Http404("Fichier CSS non trouvé")
    
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='text/css; charset=utf-8')

def dcwf_finder_js(request):
    """Vue pour servir le JavaScript du DCWF Finder"""
    js_path = os.path.join(settings.BASE_DIR, 'web_app', 'static', 'dcwf-finder', 'app.js')
    
    if not os.path.exists(js_path):
        raise Http404("Fichier JavaScript non trouvé")
    
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/javascript; charset=utf-8')

def dcwf_finder_data(request):
    """Vue pour servir les données JSON du DCWF Finder"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    data_path = os.path.join(settings.BASE_DIR, 'web_app', 'static', 'dcwf-finder', 'dcwf_complete_79_roles.json')
    
    if not os.path.exists(data_path):
        raise Http404("Fichier de données non trouvé")
    
    with open(data_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/json; charset=utf-8')

def download_file(request, filename):
    """Vue pour télécharger les fichiers .md et .mm"""
    import os
    from django.http import FileResponse, Http404
    from django.conf import settings
    from django.contrib.auth.decorators import login_required
    
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    # Définir le répertoire où se trouvent les fichiers
    files_dir = os.path.join(settings.BASE_DIR, 'static', 'downloads')
    
    # Vérifier que le fichier existe
    file_path = os.path.join(files_dir, filename)
    if not os.path.exists(file_path):
        # Essayer avec un chemin absolu alternatif
        alt_file_path = os.path.join(os.getcwd(), 'static', 'downloads', filename)
        if os.path.exists(alt_file_path):
            file_path = alt_file_path
        else:
            raise Http404(f"Fichier non trouvé: {file_path}")
    
    # Définir le type MIME selon l'extension
    if filename.endswith('.md'):
        content_type = 'text/markdown'
    elif filename.endswith('.mm'):
        content_type = 'application/x-freemind'
    else:
        content_type = 'application/octet-stream'
    
    # Retourner le fichier en tant que réponse de téléchargement
    response = FileResponse(open(file_path, 'rb'), content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response



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
    # Utiliser t1.html avec le template Django
    template = loader.get_template("web_app/main/t1.html")
    return HttpResponse(template.render({}, request))

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
    dcwf_2025_ids = request.GET.getlist('dcwf_2025_ids')
    ncwf_2017_ids = request.GET.getlist('ncwf_2017_ids')
    ncwf_2024_ids = request.GET.getlist('ncwf_2024_ids')
    ncwf_2025_ids = request.GET.getlist('ncwf_2025_ids')
    try:
        dcwf_ids = [int(i) for i in dcwf_ids]
    except ValueError:
        dcwf_ids = []
    
    try:
        dcwf_2025_ids = [int(i) for i in dcwf_2025_ids]
    except ValueError:
        dcwf_2025_ids = []

    # Peut-être que fais un try/except ici aussi, mais je pense pas que c'est nécessaire ?
    ncwf_2017_ids = [int(i) for i in ncwf_2017_ids]
    ncwf_2024_ids = [int(i) for i in ncwf_2024_ids]
    ncwf_2025_ids = [int(i) for i in ncwf_2025_ids]

    # 2. Récupère les Work Roles avec leurs titres spécifiques
    # Initialiser les listes de rôles formatés et la liste finale
    dcwf_formatted_roles = []
    dcwf_2025_formatted_roles = []
    ncwf_2017_formatted_roles = []
    ncwf_2024_formatted_roles = []
    ncwf_2025_formatted_roles = []
    
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
            'framework': 'DCWF 2017',
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
    
    # Récupérer tous les rôles DCWF 2025
    from web_app.models import Dcwf2025WorkRole
    dcwf_2025_work_roles = Dcwf2025WorkRole.objects.filter(id__in=dcwf_2025_ids)
    for role in dcwf_2025_work_roles:
        # Récupérer la couleur de la catégorie
        category_color = role.category.color if hasattr(role, 'category') and role.category else '59, 130, 246'  # Bleu par défaut
        
        # Ajouter le rôle DCWF 2025 formaté
        dcwf_2025_formatted_roles.append({
            'model_obj': role,
            'title': role.title,
            'framework': 'DCWF 2025',
            'id': role.id,
            'model_type': 'dcwf_2025',
            'parent_dcwf_id': role.id,  # Pour faciliter le regroupement
            'opm_id': role.dcwf_code,  # Code DCWF comme OPM ID
            'category_color': category_color
        })
    
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
            'nist_id': role.nist_id,  # Code civil pour NCWF
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
            'nist_id': role.nist_id,  # Code civil pour NCWF
            'category_color': category_color
        })
    
    # Récupérer tous les rôles NCWF 2025 directement par ID (comme les autres frameworks)
    ncwf_2025_work_roles = Ncwf2025WorkRole.objects.filter(id__in=ncwf_2025_ids)
    print(f"DEBUG: ncwf_2025_ids from GET: {ncwf_2025_ids}")
    print(f"DEBUG: ncwf_2025_work_roles found: {ncwf_2025_work_roles.count()}")
    
    for role in ncwf_2025_work_roles:
        # Trouver le DCWF 2025 parent via le champ ncwf_id
        parent_dcwf_2025_id = None
        parent_opm_id = None
        
        # Chercher dans les work roles DCWF 2025
        for dcwf_2025_role in dcwf_2025_work_roles:
            if dcwf_2025_role.ncwf_id == role.ncwf_id:
                parent_dcwf_2025_id = dcwf_2025_role.id
                parent_opm_id = dcwf_2025_role.dcwf_code  # Le dcwf_code est l'OPM ID
                break
        
        # Utiliser la couleur du parent DCWF 2025 si disponible
        category_color = '59, 130, 246'  # Bleu par défaut pour 2025
        if parent_dcwf_2025_id:
            for dcwf_2025_role in dcwf_2025_formatted_roles:
                if dcwf_2025_role['id'] == parent_dcwf_2025_id:
                    category_color = dcwf_2025_role.get('category_color', category_color)
                    break
        
        ncwf_2025_formatted_roles.append({
            'model_obj': role,
            'title': role.name,
            'framework': 'NCWF 2025',
            'id': role.id,
            'model_type': 'ncwf_2025',
            'parent_dcwf_2025_id': parent_dcwf_2025_id,
            'opm_id': parent_opm_id,  # Utiliser l'OPM ID du parent DCWF 2025
            'nist_id': role.ncwf_id,  # Code NCWF pour 2025
            'category_color': category_color
        })
        
    # Organiser tous les rôles par work_role d'origine
    # 1. D'abord, regrouper par DCWF parent
    formatted_roles = []
    processed_roles = set()  # Pour suivre les rôles déjà traités
    group_counter = 0  # Compteur pour générer des ID de groupe uniques
    
    # Traiter d'abord les rôles DCWF 2017
    print(f"DEBUG: dcwf_formatted_roles count: {len(dcwf_formatted_roles)}")
    print(f"DEBUG: dcwf_ids: {dcwf_ids}")
    for dcwf_role in dcwf_formatted_roles:
        dcwf_id = dcwf_role['id']
        print(f"DEBUG: Processing DCWF role {dcwf_id}: {dcwf_role['title']}")
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
            
            # Ajouter le rôle NCWF 2025 correspondant s'il existe
            # MAIS seulement s'il n'est pas sélectionné directement (pour éviter la duplication)
            for role in ncwf_2025_formatted_roles:
                # Vérifier si le rôle a un parent DCWF (peut être DCWF 2017 ou DCWF 2025)
                parent_id = role.get('parent_dcwf_id') or role.get('parent_dcwf_2025_id')
                if parent_id and parent_id == dcwf_id:
                    # Vérifier si ce rôle NCWF 2025 est sélectionné directement
                    if role['id'] not in ncwf_2025_ids:
                        role['group_id'] = current_group_id  # Ajouter le même ID de groupe
                        formatted_roles.append(role)
                        processed_roles.add(('ncwf_2025', role['id']))
                        print(f"DEBUG: Added NCWF 2025 role: {role['title']}")
                        break
    
    # Traiter les rôles DCWF 2025
    print(f"DEBUG: dcwf_2025_formatted_roles count: {len(dcwf_2025_formatted_roles)}")
    print(f"DEBUG: dcwf_2025_ids: {dcwf_2025_ids}")
    for dcwf_2025_role in dcwf_2025_formatted_roles:
        dcwf_2025_id = dcwf_2025_role['id']
        print(f"DEBUG: Processing DCWF 2025 role {dcwf_2025_id}: {dcwf_2025_role['title']}")
        if ('dcwf_2025', dcwf_2025_id) not in processed_roles and dcwf_2025_id in dcwf_2025_ids:
            # Créer un nouvel ID de groupe pour ce work_role
            current_group_id = f"group-{group_counter % 10}"
            group_counter += 1
            
            # Ajouter le rôle DCWF 2025
            dcwf_2025_role['group_id'] = current_group_id
            formatted_roles.append(dcwf_2025_role)
            processed_roles.add(('dcwf_2025', dcwf_2025_id))
            print(f"DEBUG: Added DCWF 2025 role: {dcwf_2025_role['title']}")
            
            # Ajouter le rôle NCWF 2025 correspondant s'il existe
            # MAIS seulement s'il n'est pas sélectionné directement (pour éviter la duplication)
            for role in ncwf_2025_formatted_roles:
                # Vérifier si le rôle a un parent DCWF 2025
                parent_id = role.get('parent_dcwf_2025_id')
                if parent_id and parent_id == dcwf_2025_id:
                    # Vérifier si ce rôle NCWF 2025 est sélectionné directement
                    if role['id'] not in ncwf_2025_ids:
                        role['group_id'] = current_group_id  # Ajouter le même ID de groupe
                        formatted_roles.append(role)
                        processed_roles.add(('ncwf_2025', role['id']))
                        print(f"DEBUG: Added NCWF 2025 role for DCWF 2025: {role['title']}")
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
    
    # Ajouter les rôles NCWF 2025 sans parent DCWF (comme les autres frameworks)
    for role in ncwf_2025_formatted_roles:
        if ('ncwf_2025', role['id']) not in processed_roles and role['id'] in ncwf_2025_ids:
            # Créer un nouvel ID de groupe pour ce rôle
            current_group_id = f"group-{group_counter}"
            group_counter += 1
            role['group_id'] = current_group_id
            formatted_roles.append(role)
            processed_roles.add(('ncwf_2025', role['id']))
            print(f"DEBUG: Added standalone NCWF 2025 role: {role['title']}")
    

    # 3. Récupère les KSATs
    # Si seulement NCWF 2017 est sélectionné, simuler la sélection de DCWF correspondant
    if not dcwf_work_roles.exists() and ncwf_2017_work_roles.exists():
        # Récupérer les work roles DCWF correspondants aux work roles NCWF 2017 sélectionnés
        dcwf_corresponding_roles = []
        print(f"DEBUG: ncwf_2017_work_roles count: {ncwf_2017_work_roles.count()}")
        
        # Approche alternative : chercher les work roles DCWF qui ont les mêmes OPM IDs
        for ncwf_role in ncwf_2017_work_roles:
            print(f"DEBUG: Processing NCWF role {ncwf_role.id} - {ncwf_role.title}")
            
            # Chercher les OPMs de ce work role NCWF 2017
            opms = ncwf_role.opms.all()
            print(f"DEBUG: Found {opms.count()} OPMs for NCWF role {ncwf_role.id}")
            
            for opm in opms:
                print(f"DEBUG: Checking OPM {opm.id}")
                # Chercher le work role DCWF qui a cet OPM
                try:
                    dcwf_role = DcwfWorkRole.objects.get(opm=opm)
                    print(f"DEBUG: Found DCWF work role {dcwf_role.id} for OPM {opm.id}")
                    dcwf_corresponding_roles.append(dcwf_role)
                    # Créer le mapping dans l'autre sens
                    dcwf_to_ncwf_2017[dcwf_role.id] = ncwf_role.id
                    break  # Un seul work role DCWF par OPM
                except DcwfWorkRole.DoesNotExist:
                    print(f"DEBUG: No DCWF work role found for OPM {opm.id}")
        
        print(f"DEBUG: Found {len(dcwf_corresponding_roles)} DCWF corresponding roles")
        print(f"DEBUG: dcwf_to_ncwf_2017 mapping: {dcwf_to_ncwf_2017}")
        
        if dcwf_corresponding_roles:
            # Simuler la sélection de DCWF en ajoutant ces work roles à dcwf_work_roles
            dcwf_work_roles = list(dcwf_work_roles) + dcwf_corresponding_roles
            print(f"DEBUG: Added {len(dcwf_corresponding_roles)} DCWF roles to simulation")
    
    # Maintenant récupérer les KSATs avec la logique normale
    ksats_dcwf = DcwfKsat.objects.filter(dcwf_work_role_relations__dcwf_work_role__in=dcwf_work_roles).distinct()
    
    # Récupérer les KSATs pour les work roles DCWF 2025
    from web_app.models import Dcwf2025Ksat
    ksats_dcwf_2025 = Dcwf2025Ksat.objects.filter(work_role_relations__work_role__in=dcwf_2025_work_roles).distinct()
    print(f"DEBUG: ksats_dcwf_2025 count: {ksats_dcwf_2025.count()}")
    
    # Logique pour les KSATs NCWF 2017
    if dcwf_work_roles:
        # Si DCWF est sélectionné (ou simulé), exclure les KSATs NCWF 2017 qui sont déjà dans DCWF
        ncwf_2017_ksats_in_dcwf = ksats_dcwf.values_list('ncwf_2017_ksat', flat=True)
        ksats_ncwf_2017 = Ncwf2017Ksat.objects.filter(ncwf_2017_work_roles__in=ncwf_2017_work_roles).exclude(id__in=ncwf_2017_ksats_in_dcwf).distinct()
        print(f"DEBUG: Final NCWF 2017 KSATs count: {ksats_ncwf_2017.count()}")
    else:
        # Si aucun DCWF n'est sélectionné, retourner une liste vide
        ksats_ncwf_2017 = Ncwf2017Ksat.objects.none()
        print("DEBUG: No DCWF roles found")
    
    tks_ncwf_2024 = Ncwf2024Tks.objects.filter(ncwf_2024_work_roles__in=ncwf_2024_work_roles).distinct()
    
    # Récupérer les KSATs NCWF 2025
    print(f"DEBUG: ncwf_2025_work_roles count: {len(ncwf_2025_work_roles)}")
    ksats_ncwf_2025 = Ncwf2025Ksat.objects.filter(work_role_relations__work_role__in=ncwf_2025_work_roles).distinct()
    print(f"DEBUG: ksats_ncwf_2025 count: {ksats_ncwf_2025.count()}")

    # Combiner les KSATs pour la comparaison
    ksats = list(ksats_dcwf) + list(ksats_dcwf_2025) + list(ksats_ncwf_2017) + list(tks_ncwf_2024) + list(ksats_ncwf_2025)
    print(f"DEBUG: Total ksats count: {len(ksats)}")
    
    # Les rôles originaux sont toujours nécessaires pour certaines fonctionnalités existantes
    work_roles = list(dcwf_work_roles) + list(dcwf_2025_work_roles) + list(ncwf_2017_work_roles) + list(ncwf_2024_work_roles) + list(ncwf_2025_work_roles)

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
    
    # Trier les rôles par OPM ID pour regrouper DCWF et NCWF ensemble
    def get_opm_id_for_sorting(role):
        opm_id = role.get('opm_id')
        if opm_id:
            # Extraire la partie numérique de l'OPM ID pour le tri
            import re
            numeric_part = re.search(r'\d+', str(opm_id))
            return int(numeric_part.group()) if numeric_part else 999999
        return 999999  # Mettre les rôles sans OPM ID à la fin
    
    def get_year_for_sorting(role):
        """Extraire l'année du framework pour le tri"""
        framework = role.get('framework', '')
        # Chercher un pattern d'année (4 chiffres)
        import re
        year_match = re.search(r'(\d{4})', framework)
        if year_match:
            return int(year_match.group())
        # Ordre par défaut si pas d'année trouvée
        if '2017' in framework:
            return 2017
        elif '2024' in framework:
            return 2024
        elif '2025' in framework:
            return 2025
        return 9999
    
    # Trier les rôles par OPM ID, puis par année (2025 avant 2017), puis par framework (DCWF avant NCWF)
    formatted_roles.sort(key=lambda role: (
        get_opm_id_for_sorting(role),
        -get_year_for_sorting(role),  # Année inverse (2025 avant 2017)
        0 if role.get('framework', '').startswith('DCWF') else 1  # DCWF avant NCWF
    ))
    
    # Recalculer les groupes OPM après le tri
    opm_groups = {}
    for idx, role in enumerate(formatted_roles):
        opm_id = role.get('opm_id')
        if not opm_id:
            continue
            
        if opm_id not in opm_groups:
            opm_groups[opm_id] = {
                'roles': [],
                'start_index': idx,
                'bgcolor': role.get('group_id', ''),
                'colspan': 0
            }
        
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
    """Vue pour la page des modèles 2025 avec DCWF ET NICE Framework séparés"""
    from .models import Dcwf2025Category, Dcwf2025WorkRole, NiceFrameworkWorkRole
    
    template = loader.get_template("web_app/home/index25.html")
    
    categories = []
    
    # 1. Récupérer les catégories DCWF 2025 existantes
    for category in Dcwf2025Category.objects.all().order_by('title'):
        work_roles = list(category.work_roles.all())
        
        # Organiser les work roles DCWF par famille de codes NCWF
        work_lines = get_sorted_2025_roles(work_roles)
        
        if work_lines:
            # Ajouter l'OPM ID correspondant à la catégorie
            opm_id = get_category_opm_id(category.title)
            
            categories.append({
                'category': category,
                'work_lines': work_lines,
                'type': 'dcwf_2025',
                'opm_id': opm_id
            })
    
    # 2. Les work roles NICE Framework sont déjà intégrés dans les catégories DCWF existantes
    # Pas besoin de créer des catégories séparées
    
    # Liste vide pour les IDs à surligner
    highlight_ids = []
    
    context = {
        "categories": categories,
        "highlight_ids": highlight_ids,
    }
    
    return HttpResponse(template.render(context, request))


def get_category_opm_id(category_title):
    """Retourner l'OPM ID correspondant à chaque catégorie"""
    opm_map = {
        'Cybersecurity': '900',  # OPM ID pour Cybersecurity
        'Design & Development': '600',  # OPM ID pour Design & Development
        'Implementation & Operation': '400',  # OPM ID pour Implementation & Operation
        'Protection & Defense': '500',  # OPM ID pour Protection & Defense
        'Investigation': '200',  # OPM ID pour Investigation
        'Oversight & Governance': '700',  # OPM ID pour Oversight & Governance
    }
    return opm_map.get(category_title, '000')  # 000 par défaut si pas trouvé


def check_saved_selections(request):
    """Vérifier si l'utilisateur a des sélections sauvegardées"""
    if not request.user.is_authenticated:
        return JsonResponse({'has_saved_selections': False})
    
    # Vérifier s'il y a des sauvegardes pour cet utilisateur
    saved_data = UserSavedData.objects.filter(user=request.user).exists()
    
    return JsonResponse({'has_saved_selections': saved_data})

def convert_t1_codes_to_ids(request):
    """Convertir les codes (omp_id, work_role_id, etc.) de t1.html en IDs de base de données"""
    from .models import DcwfWorkRole, Dcwf2025WorkRole, Ncwf2017WorkRole, Ncwf2024WorkRole, Ncwf2025WorkRole
    
    dcwf_2017_codes = request.GET.getlist('dcwf_2017_codes')
    dcwf_2025_codes = request.GET.getlist('dcwf_2025_codes')
    ncwf_2017_codes = request.GET.getlist('ncwf_2017_codes')
    ncwf_2024_codes = request.GET.getlist('ncwf_2024_codes')
    ncwf_2025_codes = request.GET.getlist('ncwf_2025_codes')
    
    print(f"DEBUG convert_t1_codes_to_ids: codes reçus:")
    print(f"  dcwf_2017_codes: {dcwf_2017_codes}")
    print(f"  dcwf_2025_codes: {dcwf_2025_codes}")
    print(f"  ncwf_2017_codes: {ncwf_2017_codes}")
    print(f"  ncwf_2024_codes: {ncwf_2024_codes}")
    print(f"  ncwf_2025_codes: {ncwf_2025_codes}")
    
    result = {
        'dcwf_ids': [],
        'dcwf_2025_ids': [],
        'ncwf_2017_ids': [],
        'ncwf_2024_ids': [],
        'ncwf_2025_ids': []
    }
    
    # Convertir DCWF 2017: omp_id -> id (via opm__id)
    try:
        dcwf_2017_codes = [int(c) for c in dcwf_2017_codes]
        result['dcwf_ids'] = list(DcwfWorkRole.objects.filter(opm__id__in=dcwf_2017_codes).values_list('id', flat=True))
        print(f"  DCWF 2017: {dcwf_2017_codes} -> IDs: {result['dcwf_ids']}")
    except Exception as e:
        print(f"  Erreur DCWF 2017: {e}")
    
    # Convertir DCWF 2025: dcwf_code -> id
    try:
        dcwf_2025_ids_list = list(Dcwf2025WorkRole.objects.filter(dcwf_code__in=dcwf_2025_codes).values_list('id', flat=True))
        result['dcwf_2025_ids'] = dcwf_2025_ids_list
        print(f"  DCWF 2025: {dcwf_2025_codes} -> IDs: {result['dcwf_2025_ids']}")
    except Exception as e:
        print(f"  Erreur DCWF 2025: {e}")
    
    # Convertir NCWF 2017: opm_code -> id via opms__id
    try:
        # Les codes sont maintenant des opm_code numériques
        ncwf_2017_codes = [int(c) for c in ncwf_2017_codes]
        ncwf_2017_ids_list = list(Ncwf2017WorkRole.objects.filter(opms__id__in=ncwf_2017_codes).values_list('id', flat=True))
        result['ncwf_2017_ids'] = ncwf_2017_ids_list
        print(f"  NCWF 2017: {ncwf_2017_codes} -> IDs: {result['ncwf_2017_ids']}")
    except Exception as e:
        print(f"  Erreur NCWF 2017: {e}")
    
    # Convertir NCWF 2024: opm_code -> id via opms__id
    try:
        # Les codes sont maintenant des opm_code numériques
        ncwf_2024_codes = [int(c) for c in ncwf_2024_codes]
        ncwf_2024_ids_list = list(Ncwf2024WorkRole.objects.filter(opms__id__in=ncwf_2024_codes).values_list('id', flat=True))
        result['ncwf_2024_ids'] = ncwf_2024_ids_list
        print(f"  NCWF 2024: {ncwf_2024_codes} -> IDs: {result['ncwf_2024_ids']}")
    except Exception as e:
        print(f"  Erreur NCWF 2024: {e}")
    
    # Convertir NCWF 2025: work_role_id -> id via ncwf_id ou name
    try:
        # Chercher d'abord par ncwf_id, sinon par name
        ncwf_2025_ids_list = []
        for code in ncwf_2025_codes:
            role = Ncwf2025WorkRole.objects.filter(ncwf_id=code).first()
            if role:
                ncwf_2025_ids_list.append(role.id)
        result['ncwf_2025_ids'] = ncwf_2025_ids_list
        print(f"  NCWF 2025: {ncwf_2025_codes} -> IDs: {result['ncwf_2025_ids']}")
    except Exception as e:
        print(f"  Erreur NCWF 2025: {e}")
    
    print(f"DEBUG: Résultat final: {result}")
    
    return JsonResponse(result)
