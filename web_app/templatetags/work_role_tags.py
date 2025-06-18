from django import template

register = template.Library()

@register.filter
def has_ksat(work_role, ksat):
    return work_role.has_ksat(ksat)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def class_name(obj):
    return obj.__class__.__name__
