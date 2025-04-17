from django.http import HttpResponse
from django.template import loader
from collections import defaultdict
from web_app.models import DcwfCategory, DcwfWorkRole, DcwfWorkRoleKsatRelation


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

    it_work_roles = DcwfCategory.objects.get(title="IT (Cyberspace)").dcwf_work_roles.all()
    cyber_security_work_roles = DcwfCategory.objects.get(title="Cybersecurity").dcwf_work_roles.all()
    cyber_effects_work_roles = DcwfCategory.objects.get(title="Cyberspace Effects").dcwf_work_roles.all()
    intel_work_roles = DcwfCategory.objects.get(title="Intelligence (Cyberspace)").dcwf_work_roles.all()
    enabler_work_roles = DcwfCategory.objects.get(title="Cyberspace Enablers").dcwf_work_roles.all()
    software_engineering_work_roles = DcwfCategory.objects.get(title="Software Engineering").dcwf_work_roles.all()
    data_work_roles = DcwfCategory.objects.get(title="Data/AI").dcwf_work_roles.all()

    sorted_cyber_security_lines = get_sorted_cyber_roles(cyber_security_work_roles)
    it_work_lines = get_sorted_it_roles(it_work_roles)
    cyber_effects_work_lines = get_sorted_cybereffects_roles(cyber_effects_work_roles)
    enabler_work_lines = get_sorted_enabler_roles(enabler_work_roles)
    software_engineering_work_lines = get_sorted_software_engineering_roles(software_engineering_work_roles)
    data_work_lines = get_sorted_data_ai_roles(data_work_roles)

    context = {
        "it_work_lines": it_work_lines,
        "cyber_security_lines": sorted_cyber_security_lines,
        "cyber_effects_work_lines": cyber_effects_work_lines,
        "intel_work_roles": intel_work_roles,
        "enabler_work_lines": enabler_work_lines,
        "software_engineering_work_lines": software_engineering_work_lines,
        "data_work_lines": data_work_lines,
        "categories": DcwfCategory.objects.all(),
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
