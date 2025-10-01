from django import template
from django.utils.html import format_html
from web_app.models import DcwfKsat, Ncwf2017Ksat, Ncwf2025Ksat

register = template.Library()

@register.simple_tag
def dcwf_url(ksat):
    if isinstance(ksat, Ncwf2017Ksat):
        ksat = ksat.dcwf_ksats.first()
    if isinstance(ksat, DcwfKsat) and ksat.url and ksat.dcwf_id:
        return format_html('<a href="{}" class="underline">DCWF {}</a>', ksat.url, ksat.dcwf_id)
    return ''

@register.simple_tag
def ncwf_2017_url(ksat):
    if isinstance(ksat, DcwfKsat):
        ksat = ksat.ncwf_2017_ksat
    if isinstance(ksat, Ncwf2017Ksat) and ksat.url and ksat.ncwf_id:
        return format_html('<a href="{}" class="underline">NCWF-2017 {}</a>', ksat.url, ksat.ncwf_id)
    return ''

@register.simple_tag
def ncwf_2025_url(ksat):
    if isinstance(ksat, Ncwf2025Ksat) and ksat.url and ksat.ncwf_id:
        return format_html('<a href="{}" class="underline">NCWF-2025 {}</a>', ksat.url, ksat.ncwf_id)
    return ''