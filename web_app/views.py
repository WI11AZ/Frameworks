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

def attributs_part_deux_opm_id(request):
    """Vue pour la page AttributsPartDeuxOpmId"""
    return render(request, 'web_app/ksat/AttributsPartDeuxOpmId.html')

def sfia_generic_attributes_json(request):
    """Vue pour servir le fichier JSON sfia_generic_attributes.json"""
    import os
    from django.http import HttpResponse, Http404
    from django.conf import settings
    
    json_path = os.path.join(settings.BASE_DIR, 'SCRAPE2', 'sfia_generic_attributes.json')
    
    if not os.path.exists(json_path):
        raise Http404("Fichier sfia_generic_attributes.json non trouvé")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/json; charset=utf-8')

def output_json(request):
    """Vue pour servir le fichier JSON output_merged (++).json depuis FORSAPINNOEL"""
    json_path = os.path.join(settings.BASE_DIR, 'FORSAPINNOEL', 'output_merged (++).json')
    
    if not os.path.exists(json_path):
        raise Http404("Fichier output_merged (++).json non trouvé")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/json; charset=utf-8')

def sfia_skills_json(request):
    """Vue pour servir le fichier JSON sfia_skills.json depuis SKILLS_SFIA"""
    json_path = os.path.join(settings.BASE_DIR, 'SKILLS_SFIA', 'sfia_skills.json')
    
    if not os.path.exists(json_path):
        raise Http404("Fichier sfia_skills.json non trouvé")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/json; charset=utf-8')

def idf_json(request):
    """Vue pour servir le fichier JSON IDF.json depuis Postes"""
    json_path = os.path.join(settings.BASE_DIR, 'Postes', 'IDF.json')
    
    if not os.path.exists(json_path):
        raise Http404("Fichier IDF.json non trouvé")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/json; charset=utf-8')

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

def dcwf_explorer_view(request):
    """Vue pour servir le programme Explorateur DCWF Pro v3"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    # Servir le fichier index.html de l'Explorateur DCWF Pro v3
    explorer_path = os.path.join(settings.BASE_DIR, 'Explorateur DCWF Pro v3', 'index.html')
    
    if not os.path.exists(explorer_path):
        raise Http404("Programme Explorateur DCWF Pro v3 non trouvé")
    
    with open(explorer_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='text/html; charset=utf-8')

def atlas_explorer_view(request):
    """Vue pour servir le programme Explorateur ATLAS (PRO VISU)"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    # Servir le fichier index.html de PRO VISU
    explorer_path = os.path.join(settings.BASE_DIR, 'PRO VISU', 'index.html')
    
    if not os.path.exists(explorer_path):
        raise Http404("Programme Explorateur ATLAS non trouvé")
    
    with open(explorer_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer les chemins relatifs par des URLs Django
    # Remplacer toutes les occurrences de E1.png
    content = content.replace('src="E1.png"', 'src="/atlas-explorer/E1.png"')
    content = content.replace("src='E1.png'", "src='/atlas-explorer/E1.png'")
    
    # Remplacer les références à flare.json
    content = content.replace("fetch('flare.json')", "fetch('/atlas-explorer/flare.json')")
    content = content.replace('fetch("flare.json")', 'fetch("/atlas-explorer/flare.json")')
    content = content.replace("'flare.json'", "'/atlas-explorer/flare.json'")
    content = content.replace('"flare.json"', '"/atlas-explorer/flare.json"')
    
    # Remplacer les références à miserables.json
    content = content.replace("fetch('miserables.json')", "fetch('/atlas-explorer/miserables.json')")
    content = content.replace('fetch("miserables.json")', 'fetch("/atlas-explorer/miserables.json")')
    content = content.replace("'miserables.json'", "'/atlas-explorer/miserables.json'")
    content = content.replace('"miserables.json"', '"/atlas-explorer/miserables.json"')
    
    return HttpResponse(content, content_type='text/html; charset=utf-8')

def atlas_explorer_static(request, filename):
    """Vue pour servir les fichiers statiques de l'Explorateur ATLAS (images, JSON, etc.)"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    file_path = os.path.join(settings.BASE_DIR, 'PRO VISU', filename)
    
    if not os.path.exists(file_path):
        raise Http404(f"Fichier {filename} non trouvé")
    
    # Déterminer le type MIME selon l'extension
    if filename.lower().endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content, content_type='application/json; charset=utf-8')
    elif filename.lower().endswith('.png'):
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')
    elif filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')
    elif filename.lower().endswith('.svg'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content, content_type='image/svg+xml')
    elif filename.lower().endswith('.gif'):
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/gif')
    else:
        # Type par défaut pour les autres fichiers
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='application/octet-stream')

def technologia_song_view(request):
    """Vue pour servir le fichier audio Technologia"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    # Servir le fichier audio
    song_path = os.path.join(settings.BASE_DIR, 'Song', 'technologia-original-video-technologia-arab-meme_dd2yhEz3.mp3')
    
    if not os.path.exists(song_path):
        raise Http404("Fichier audio non trouvé")
    
    response = FileResponse(open(song_path, 'rb'), content_type='audio/mpeg')
    response['Content-Disposition'] = 'inline; filename="technologia.mp3"'
    return response

def step0_baseline_view(request):
    """Vue pour servir le programme Step0 Baseline"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    # Servir le fichier index.html du Step0
    step0_path = os.path.join(settings.BASE_DIR, 'Step0', 'index.html')
    
    if not os.path.exists(step0_path):
        raise Http404("Programme Step0 Baseline non trouvé")
    
    with open(step0_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer le chemin relatif du fichier JSON par une URL Django
    # On utilise reverse pour obtenir l'URL correcte
    from django.urls import reverse
    try:
        json_url = reverse('step0_baseline_json')
        # Construire l'URL absolue si nécessaire
        json_url = request.build_absolute_uri(json_url)
    except:
        # Fallback si reverse échoue
        json_url = request.build_absolute_uri('/step0-baseline/json/')
    
    content = content.replace("fetch('mega_baseline.json')", f"fetch('{json_url}')")
    
    # Injecter la navbar Django dans le HTML
    # Charger le template menu.html
    from django.template.loader import render_to_string
    navbar_html = render_to_string('web_app/template/menu.html', {'user': request.user, 'request': request})
    
    # Trouver la balise <body> et insérer la navbar juste après
    if '<body' in content:
        # Trouver la position de <body> et insérer la navbar après
        body_pos = content.find('<body')
        body_tag_end = content.find('>', body_pos) + 1
        # Insérer la navbar après la balise <body>
        content = content[:body_tag_end] + '\n' + navbar_html + '\n' + content[body_tag_end:]
    else:
        # Si pas de body, ajouter avant le premier élément
        if '<div class="main-container">' in content:
            content = content.replace('<div class="main-container">', navbar_html + '\n<div class="main-container">')
        else:
            # Ajouter au début du contenu
            content = navbar_html + '\n' + content
    
    # Ajouter le CSS et JS nécessaires pour la navbar (Tailwind est déjà chargé dans base.html)
    # Ajouter Tailwind CSS et les scripts nécessaires pour la navbar
    tailwind_css = '<script src="https://cdn.tailwindcss.com"></script>'
    navbar_scripts = '''
    <script>
        // Script pour le menu mobile
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            
            if (mobileMenuButton && mobileMenu) {
                mobileMenuButton.addEventListener('click', () => {
                    mobileMenu.classList.toggle('hidden');
                });
            }
            
            // Script pour la modale info
            const infoButton = document.getElementById('info-button');
            const infoModal = document.getElementById('info-modal');
            const closeButtons = document.querySelectorAll('.info-modal-close');
            
            if (infoButton && infoModal) {
                infoButton.addEventListener('click', function() {
                    infoModal.classList.remove('hidden');
                    infoModal.classList.add('flex');
                    setTimeout(() => {
                        const modalContent = infoModal.querySelector('div > div');
                        if (modalContent) {
                            modalContent.classList.add('scale-100', 'opacity-100');
                            modalContent.classList.remove('scale-95', 'opacity-0');
                        }
                    }, 10);
                });
                
                function closeInfoModal() {
                    const modalContent = infoModal.querySelector('div > div');
                    if (modalContent) {
                        modalContent.classList.remove('scale-100', 'opacity-100');
                        modalContent.classList.add('scale-95', 'opacity-0');
                    }
                    setTimeout(() => {
                        infoModal.classList.add('hidden');
                        infoModal.classList.remove('flex');
                    }, 300);
                }
                
                closeButtons.forEach(button => {
                    button.addEventListener('click', closeInfoModal);
                });
                
                infoModal.addEventListener('click', function(e) {
                    if (e.target === infoModal) {
                        closeInfoModal();
                    }
                });
                
                document.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape' && !infoModal.classList.contains('hidden')) {
                        closeInfoModal();
                    }
                });
            }
        });
    </script>
    '''
    
    # Ajouter un style pour ajuster la marge du main-container si nécessaire
    style_adjustment = '''
    <style>
        body {
            padding-top: 64px; /* Hauteur de la navbar */
        }
        .main-container {
            margin-top: 0;
        }
        /* Styles pour la navbar */
        nav.bg-gray-800 {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            width: 100%;
        }
    </style>
    '''
    
    # Insérer Tailwind CSS dans le <head> si pas déjà présent
    if 'tailwindcss.com' not in content.lower():
        if '</head>' in content:
            content = content.replace('</head>', tailwind_css + '</head>')
        elif '<head>' in content:
            head_end = content.find('</head>')
            if head_end == -1:
                if '</style>' in content:
                    content = content.replace('</style>', '</style>' + tailwind_css)
                else:
                    content = tailwind_css + content
            else:
                content = content[:head_end] + tailwind_css + content[head_end:]
    
    # Insérer le style dans le <head>
    if '</head>' in content:
        content = content.replace('</head>', style_adjustment + '</head>')
    elif '<head>' in content:
        head_end = content.find('</head>')
        if head_end == -1:
            # Pas de </head>, chercher </style> ou <body>
            if '</style>' in content:
                content = content.replace('</style>', '</style>' + style_adjustment)
            else:
                content = style_adjustment + content
        else:
            content = content[:head_end] + style_adjustment + content[head_end:]
    
    # Ajouter les scripts JavaScript pour la navbar avant </body>
    if '</body>' in content:
        content = content.replace('</body>', navbar_scripts + '</body>')
    else:
        # Si pas de </body>, ajouter à la fin
        content = content + navbar_scripts
    
    return HttpResponse(content, content_type='text/html; charset=utf-8')

def step0_baseline_json(request):
    """Vue pour servir le fichier JSON mega_baseline.json du Step0"""
    # Vérifier que l'utilisateur est connecté
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    json_path = os.path.join(settings.BASE_DIR, 'Step0', 'mega_baseline.json')
    
    if not os.path.exists(json_path):
        raise Http404("Fichier mega_baseline.json non trouvé")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return HttpResponse(content, content_type='application/json; charset=utf-8')

def download_file(request, filename):
    """Vue pour télécharger les fichiers .md, .mm et .pdf"""
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
    elif filename.endswith('.pdf'):
        content_type = 'application/pdf'
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





def get_category_from_opm_id(opm_id):
    """
    Détermine la catégorie à partir de l'OPM ID.
    Retourne le titre de la catégorie ou None si non trouvé.
    """
    if not opm_id:
        return None
    
    opm_id_str = str(opm_id)
    
    # Cyber Effects (CE) / Cyberspace Effects
    if opm_id_str in ["112", "121", "122", "131", "132", "133", "332", "341", "322", "442", "443", "463", "551"]:
        return "Cyber Effects (CE)"
    
    # Software Engineering (SE)
    if opm_id_str in ["461", "621", "625", "626", "627", "628", "673", "806"]:
        return "Software Engineering (SE)"
    
    # Cybersecurity (CS)
    if opm_id_str in ["212", "462", "511", "521", "531", "541", "611", "612", "622", "631", "632", "641", "651", "652", "661", "671", "722", "723"]:
        return "Cybersecurity (CS)"
    
    # Information Technology (IT)
    if opm_id_str in ["411", "421", "431", "441", "451"]:
        return "Information Technology (IT)"
    
    # Cyber Enablers (EN)
    if opm_id_str in ["211", "221", "711", "712", "731", "732", "751", "752", "801", "802", "803", "804", "805", "901"]:
        return "Cyber Enablers (EN)"
    
    # Intel (CI)
    if opm_id_str in ["111", "141", "151", "311", "312", "331"]:
        return "Intel (CI)"
    
    # Data/AI (DA)
    if opm_id_str in ["422", "423", "424", "623", "624", "653", "672", "733", "753", "902", "903"]:
        return "Data/AI (DA)"
    
    return None


def get_category_color_from_t1(category_title):
    """
    Retourne la couleur RGB (format "R, G, B") correspondant à la catégorie
    selon les couleurs définies dans t1.html pour les relation-card.
    Les couleurs correspondent aux bordures des cartes dans t1.html.
    """
    if not category_title:
        return '107, 114, 128'  # Gris par défaut (CX)
    
    # Normaliser le titre : enlever les espaces multiples et convertir en minuscules
    category_title_normalized = ' '.join(category_title.lower().split())
    
    # Cyber Effects (CE) / Cyberspace Effects - Champagne #d4a574
    # Vérifier CE en premier car "cyber" pourrait matcher d'autres catégories
    if ('cyber effects' in category_title_normalized or 
        'cyberspace effects' in category_title_normalized or 
        '(ce)' in category_title_normalized or
        category_title_normalized.startswith('ce ') or
        category_title_normalized == 'ce'):
        return '212, 165, 116'
    
    # Software Engineering (SE) - Rouge #dc2626
    if ('software engineering' in category_title_normalized or 
        '(se)' in category_title_normalized):
        return '220, 38, 38'
    
    # Cybersecurity (CS) - Vert #16a34a
    if ('cybersecurity' in category_title_normalized or 
        '(cs)' in category_title_normalized):
        return '22, 163, 74'
    
    # Information Technology (IT) - Bleu #1d4ed8
    if ('information technology' in category_title_normalized or 
        '(it)' in category_title_normalized):
        return '29, 78, 216'
    
    # Cyber Enablers (EN) - Violet #7c3aed
    if ('cyber enablers' in category_title_normalized or 
        '(en)' in category_title_normalized):
        return '124, 58, 237'
    
    # Intel (CI) - Orange #d97706
    if ('intel' in category_title_normalized or 
        '(ci)' in category_title_normalized):
        return '217, 119, 6'
    
    # Data/AI (DA) - Turquoise #0d9488
    # Vérifier après les autres pour éviter les faux positifs
    if (('data' in category_title_normalized or 'ai' in category_title_normalized or '(da)' in category_title_normalized) and
        'cyber' not in category_title_normalized):  # Exclure si contient "cyber"
        return '13, 148, 136'
    
    # CX - Gris #6b7280
    if '(cx)' in category_title_normalized:
        return '107, 114, 128'
    
    # Par défaut, gris
    return '107, 114, 128'


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
        # Utiliser l'OPM ID comme source de vérité principale pour déterminer la catégorie
        opm_id = role.opm.id if hasattr(role, 'opm') and role.opm else None
        category_title = get_category_from_opm_id(opm_id)
        
        # Si l'OPM ID ne donne pas de catégorie, utiliser la catégorie de la base de données
        if not category_title:
            category_title = role.category.title if hasattr(role, 'category') and role.category else None
        
        # Utiliser la couleur de t1.html (priorité sur la couleur stockée en base)
        category_color = get_category_color_from_t1(category_title)
        
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
        # Utiliser l'OPM ID (dcwf_code) comme source de vérité principale pour déterminer la catégorie
        opm_id = role.dcwf_code
        category_title = get_category_from_opm_id(opm_id)
        
        # Si l'OPM ID ne donne pas de catégorie, utiliser la catégorie de la base de données
        if not category_title:
            category_title = role.category.title if hasattr(role, 'category') and role.category else None
        
        category_color = get_category_color_from_t1(category_title)
        
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
        category_color = '22, 163, 74'  # Vert par défaut (CS)
        if parent_dcwf_id:
            for dcwf_role in dcwf_formatted_roles:
                if dcwf_role['id'] == parent_dcwf_id:
                    category_color = dcwf_role.get('category_color', category_color)
                    break
        else:
            # Si pas de parent, essayer de récupérer la catégorie du rôle NCWF 2017
            category_title = None
            if hasattr(role, 'category') and role.category:
                category_title = role.category.title
            
            # Si pas de catégorie, utiliser l'OPM ID pour déterminer la catégorie
            if not category_title:
                opm_id = role.opms.first().id if role.opms.exists() else None
                category_title = get_category_from_opm_id(opm_id)
            
            category_color = get_category_color_from_t1(category_title)
                    
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
        category_color = '220, 38, 38'  # Rouge par défaut (SE)
        if parent_dcwf_id:
            for dcwf_role in dcwf_formatted_roles:
                if dcwf_role['id'] == parent_dcwf_id:
                    category_color = dcwf_role.get('category_color', category_color)
                    break
        else:
            # Si pas de parent, essayer de récupérer la catégorie du rôle NCWF 2024
            category_title = None
            if hasattr(role, 'category') and role.category:
                category_title = role.category.title
            
            # Si pas de catégorie, utiliser l'OPM ID pour déterminer la catégorie
            if not category_title:
                opm_id = role.opms.first().id if role.opms.exists() else None
                category_title = get_category_from_opm_id(opm_id)
            
            category_color = get_category_color_from_t1(category_title)
                    
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
        
        # Chercher d'abord dans les work roles DCWF 2025 sélectionnés
        for dcwf_2025_role in dcwf_2025_work_roles:
            if dcwf_2025_role.ncwf_id == role.ncwf_id:
                parent_dcwf_2025_id = dcwf_2025_role.id
                parent_opm_id = dcwf_2025_role.dcwf_code  # Le dcwf_code est l'OPM ID
                break
        
        # Si pas trouvé dans les sélectionnés, chercher dans toute la base de données
        if not parent_opm_id:
            from web_app.models.dcwf_2025_work_role import Dcwf2025WorkRole
            dcwf_2025_parent = Dcwf2025WorkRole.objects.filter(ncwf_id=role.ncwf_id).first()
            if dcwf_2025_parent:
                parent_opm_id = dcwf_2025_parent.dcwf_code  # Le dcwf_code est l'OPM ID
        
        # Utiliser la couleur du parent DCWF 2025 si disponible
        category_color = '29, 78, 216'  # Bleu par défaut pour 2025 (IT)
        if parent_dcwf_2025_id:
            for dcwf_2025_role in dcwf_2025_formatted_roles:
                if dcwf_2025_role['id'] == parent_dcwf_2025_id:
                    category_color = dcwf_2025_role.get('category_color', category_color)
                    break
        else:
            # Si pas de parent sélectionné, essayer de récupérer la catégorie du rôle NCWF 2025
            category_title = None
            if hasattr(role, 'category') and role.category:
                category_title = role.category.title
            
            # Si pas de catégorie, utiliser l'OPM ID pour déterminer la catégorie
            if not category_title and parent_opm_id:
                category_title = get_category_from_opm_id(parent_opm_id)
            
            if category_title:
                category_color = get_category_color_from_t1(category_title)
        
        ncwf_2025_formatted_roles.append({
            'model_obj': role,
            'title': role.name,
            'framework': 'NCWF 2025',
            'id': role.id,
            'model_type': 'ncwf_2025',
            'parent_dcwf_2025_id': parent_dcwf_2025_id,
            'opm_id': parent_opm_id,  # Utiliser l'OPM ID du parent DCWF 2025 (même s'il n'est pas sélectionné)
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
    
    # Debug: Compter les abilities dans ksats_dcwf_2025
    abilities_dcwf_2025 = ksats_dcwf_2025.filter(category='ability')
    print(f"DEBUG: Abilities in ksats_dcwf_2025: {abilities_dcwf_2025.count()}")
    
    # Debug spécifique pour le work role 441
    if dcwf_2025_work_roles:
        wr_441 = dcwf_2025_work_roles.filter(dcwf_code='441').first()
        if wr_441:
            abilities_441 = Dcwf2025Ksat.objects.filter(
                category='ability',
                work_role_relations__work_role=wr_441
            ).distinct()
            print(f"DEBUG: Abilities for work role 441: {abilities_441.count()}")
            if abilities_441.exists():
                print(f"DEBUG: First ability 441: {abilities_441.first().dcwf_id} - {abilities_441.first().description[:60]}")
    
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
    print(f"DEBUG: ksats_ncwf_2025 count (avant filtrage JSON): {ksats_ncwf_2025.count()}")
    
    # Filtrer les KSAT NCWF 2025 pour ne garder que ceux présents dans nice_framework_2.1.0.json
    json_file_path = os.path.join(settings.BASE_DIR, 'KSAT 2025 FINAL', 'NCWF 2025', 'nice_framework_2.1.0.json')
    valid_ncwf_2025_ksat_ids = set()
    
    # Récupérer les WRL-ID des rôles NCWF 2025 sélectionnés pour un filtrage plus précis
    selected_wrl_ids = set()
    for role in ncwf_2025_work_roles:
        if hasattr(role, 'ncwf_id') and role.ncwf_id:
            selected_wrl_ids.add(role.ncwf_id)
    
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                # Extraire tous les IDs valides du JSON
                # Si on a des WRL-ID sélectionnés, filtrer aussi par WRL-ID pour être plus précis
                for item in json_data:
                    ksat_id = item.get('ID', '').strip()
                    wrl_id = item.get('WRL-ID', '').strip()
                    
                    # Ignorer les IDs invalides
                    if not ksat_id or ksat_id in ['NCWF #', '#'] or ksat_id.startswith('NCWF #'):
                        continue
                    
                    # Si on a des WRL-ID sélectionnés, ne garder que les KSAT correspondants
                    if selected_wrl_ids:
                        if wrl_id and wrl_id in selected_wrl_ids:
                            valid_ncwf_2025_ksat_ids.add(ksat_id)
                    else:
                        # Sinon, garder tous les IDs valides
                        valid_ncwf_2025_ksat_ids.add(ksat_id)
                        
            print(f"DEBUG: IDs valides dans nice_framework_2.1.0.json: {len(valid_ncwf_2025_ksat_ids)}")
            if selected_wrl_ids:
                print(f"DEBUG: WRL-ID sélectionnés: {selected_wrl_ids}")
        except Exception as e:
            print(f"DEBUG: Erreur lors du chargement du JSON: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"DEBUG: Fichier JSON non trouvé: {json_file_path}")
    
    # Filtrer les KSAT pour ne garder que ceux avec un ID valide dans le JSON
    if valid_ncwf_2025_ksat_ids:
        ksats_ncwf_2025 = ksats_ncwf_2025.filter(ncwf_id__in=valid_ncwf_2025_ksat_ids)
        print(f"DEBUG: ksats_ncwf_2025 count (après filtrage JSON): {ksats_ncwf_2025.count()}")
        
        # Debug: vérifier si T1551 est présent
        t1551_exists = ksats_ncwf_2025.filter(ncwf_id='T1551').exists()
        if t1551_exists:
            print(f"DEBUG: ATTENTION - T1551 est toujours présent après filtrage!")
        else:
            print(f"DEBUG: T1551 correctement filtré (n'existe pas dans le JSON)")
    else:
        print(f"DEBUG: Aucun ID valide trouvé dans le JSON, tous les KSAT sont conservés")

    # Combiner les KSATs pour la comparaison
    ksats = list(ksats_dcwf) + list(ksats_dcwf_2025) + list(ksats_ncwf_2017) + list(tks_ncwf_2024) + list(ksats_ncwf_2025)
    print(f"DEBUG: Total ksats count: {len(ksats)}")
    
    # Debug: Compter les abilities dans ksats_dcwf_2025
    abilities_441 = [k for k in ksats_dcwf_2025 if k.category == 'ability' and any(rel.work_role.dcwf_code == '441' for rel in k.work_role_relations.all())]
    print(f"DEBUG: Abilities for 441 in ksats_dcwf_2025: {len(abilities_441)}")
    if abilities_441:
        print(f"DEBUG: First ability 441: {abilities_441[0].dcwf_id} - {abilities_441[0].description[:60]}")
    
    # Les rôles originaux sont toujours nécessaires pour certaines fonctionnalités existantes
    work_roles = list(dcwf_work_roles) + list(dcwf_2025_work_roles) + list(ncwf_2017_work_roles) + list(ncwf_2024_work_roles) + list(ncwf_2025_work_roles)

    # --- Correction ici : on utilise les clés singulières et on force l'affichage des abilités ---
    ksat_dict = { 'task': [],'knowledge': [], 'skill': [], 'abilitie': []}
    
    # Vérifier les catégories disponibles
    categories_found = set()
    ability_ksats_found = False
    
    abilities_processed = 0
    abilities_skipped = 0
    
    for ksat in ksats:
        # Filtrer les KSAT invalides (sans description ou avec ID invalide)
        dcwf_id = getattr(ksat, 'dcwf_id', None)
        ncwf_id = getattr(ksat, 'ncwf_id', None)
        description = getattr(ksat, 'description', None)
        
        # Vérifier si le KSAT est valide
        ksat_id = dcwf_id or ncwf_id or str(getattr(ksat, 'id', ''))
        if not ksat_id or ksat_id.strip() == '' or ksat_id == 'DCWF #' or ksat_id == 'NCWF #' or ksat_id == '#':
            if getattr(ksat, 'category', '').lower() == 'ability':
                abilities_skipped += 1
            continue  # Ignorer les KSAT invalides
        
        if not description or description.strip() == '':
            if getattr(ksat, 'category', '').lower() == 'ability':
                abilities_skipped += 1
            continue  # Ignorer les KSAT sans description
        
        category = ksat.category.lower()
        categories_found.add(category)
        # Vérifier si des abilities sont présentes
        if category == 'ability':
            ability_ksats_found = True
            abilities_processed += 1
            # Debug pour les abilities du 441
            if dcwf_2025_work_roles:
                wr_441 = dcwf_2025_work_roles.filter(dcwf_code='441').first()
                if wr_441 and wr_441.has_ksat(ksat):
                    print(f"DEBUG: Processing ability for 441: {ksat.dcwf_id} - {ksat.description[:50]}")

            # S'assurer qu'il est ajouté à la bonne clé du dictionnaire
            ksat_dict['abilitie'].append(ksat)
        else:
            # Autres catégories
            ksat_dict.get(category, []).append(ksat)
    
    print(f"DEBUG: Abilities processed: {abilities_processed}, skipped: {abilities_skipped}")
    

    
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
    
    # Debug: Afficher le nombre d'abilities dans ksat_dict
    print(f"DEBUG: Abilities in ksat_dict['abilitie']: {len(ksat_dict['abilitie'])}")
    if ksat_dict['abilitie']:
        print(f"DEBUG: First ability in ksat_dict: {ksat_dict['abilitie'][0].dcwf_id} - {ksat_dict['abilitie'][0].description[:60]}")
        # Vérifier si le work role 441 a cette ability
        if dcwf_2025_work_roles:
            wr_441 = dcwf_2025_work_roles.filter(dcwf_code='441').first()
            if wr_441:
                first_ability = ksat_dict['abilitie'][0]
                has_it = wr_441.has_ksat(first_ability)
                print(f"DEBUG: Work role 441 has first ability? {has_it}")

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
    
    # D'abord, calculer quels OPM ID sont des familles (2+) et lesquels sont solo (1)
    opm_id_counts = {}
    for role in formatted_roles:
        opm_id = role.get('opm_id')
        if opm_id:
            opm_id_counts[opm_id] = opm_id_counts.get(opm_id, 0) + 1
    
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
    
    def is_family_group(role):
        """Retourne True si le rôle fait partie d'une famille (2+ rôles avec le même OPM ID)"""
        opm_id = role.get('opm_id')
        if not opm_id:
            return False
        return opm_id_counts.get(opm_id, 0) >= 2
    
    # Trier les rôles : d'abord les familles (2+), puis les solo, puis par OPM ID, année, framework
    formatted_roles.sort(key=lambda role: (
        0 if is_family_group(role) else 1,  # Familles (0) avant solo (1)
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

def summary_mil_view(request):
    return render(request, 'web_app/main/summary_mil.html')
    
def project_recap_view(request):
    """Vue pour la page de récapitulatif complet du projet"""
    return render(request, 'web_app/main/project_recap.html')

def military_skills_json(request):
    """Vue pour servir le fichier JSON des compétences militaires"""
    import json
    import os
    from django.conf import settings
    from django.http import HttpResponse, Http404
    
    json_path = os.path.join(settings.BASE_DIR, 'SUMAARYMIL', 'military_skills_data.json')
    
    if not os.path.exists(json_path):
        raise Http404("Fichier military_skills_data.json non trouvé")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return HttpResponse(
            json.dumps(data, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )
    except Exception as e:
        return HttpResponse(
            json.dumps({'error': str(e)}),
            content_type='application/json; charset=utf-8',
            status=500
        )
    
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

def get_ksat_data_view(request, framework):
    """Vue pour servir les fichiers JSON de données KSAT"""
    import os
    from django.conf import settings
    
    if framework == 'dcwf':
        file_path = os.path.join(settings.BASE_DIR, 'KSAT 2025 FINAL', 'DCWF 2025', 'dcwf_data.json')
    elif framework == 'ncwf':
        file_path = os.path.join(settings.BASE_DIR, 'KSAT 2025 FINAL', 'NCWF 2025', 'nice_framework_2.1.0.json')
    else:
        return JsonResponse({'error': 'Framework invalide'}, status=400)
    
    if not os.path.exists(file_path):
        return JsonResponse({'error': 'Fichier non trouvé'}, status=404)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return JsonResponse(data, safe=False)
