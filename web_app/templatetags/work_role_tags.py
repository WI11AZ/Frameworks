from django import template

register = template.Library()

@register.filter
def has_ksat(work_role, ksat):
    return work_role.has_ksat(ksat)
