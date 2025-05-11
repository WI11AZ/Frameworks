from django.template import loader
from collections import defaultdict
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import (
    DcwfCategory,
    DcwfWorkRole,
    Ncwf2017WorkRole,
    Ncwf2024WorkRole,
    DcwfKsat,
DcwfWorkRoleKsatRelation
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
        "skills": skills_list,
        "abilities": abilities_list,
        "tasks": tasks_list,
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

    # 2. Récupère les Work Roles
    dcwf_work_roles = DcwfWorkRole.objects.filter(id__in=dcwf_ids)
    ncwf_2017_work_roles = Ncwf2017WorkRole.objects.filter(id__in=ncwf_2017_ids)
    ncwf_2024_work_roles = Ncwf2024WorkRole.objects.filter(id__in=ncwf_2024_ids)

    # 3. Récupère les KSATs
    # On peut faire ca plus efficient, mais si c'est pas un problème de perf, on va pas compliquér le code
    ksats_dcwf = list(set([ksats for work_role in dcwf_work_roles for ksats in work_role.dcwf_ksats()]))
    ksats_ncwf_2017 = list(set([ksats for work_role in ncwf_2017_work_roles for ksats in work_role.ncwf_2017_ksats.all()]))
    tks_ncwf_2024 = list(set([tks for work_role in ncwf_2024_work_roles for tks in work_role.ncwf_2024_tks.all()]))


    ksats = ksats_dcwf + ksats_ncwf_2017 + tks_ncwf_2024
    work_roles = list(dcwf_work_roles) + list(ncwf_2017_work_roles) + list(ncwf_2024_work_roles)

    # --- Correction ici : on utilise les clés singulières ---
    ksat_dict = {'knowledge': [], 'skill': [], 'ability': [], 'task': []}
    for ksat in ksats:
        ksat_dict.get(ksat.category.lower(), []).append(ksat)

    return render(request, 'web_app/ksat/compare_ksat.html', {
        'work_roles': work_roles,
        'ksat_dict':   ksat_dict,
    })