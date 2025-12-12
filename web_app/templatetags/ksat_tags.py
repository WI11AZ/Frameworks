from django import template
from django.utils.html import format_html
from web_app.models import DcwfKsat, Ncwf2017Ksat, Ncwf2025Ksat, Dcwf2025Ksat

register = template.Library()

@register.simple_tag
def dcwf_url(ksat):
    if isinstance(ksat, Ncwf2017Ksat):
        ksat = ksat.dcwf_ksats.first()
    # Gérer Dcwf2025Ksat
    if isinstance(ksat, Dcwf2025Ksat):
        # Pour DCWF 2025, on affiche juste l'ID car il n'y a pas d'URL
        if ksat.dcwf_id:
            return format_html('<span class="text-gray-600">DCWF {}</span>', ksat.dcwf_id)
        return ''
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
    if isinstance(ksat, Ncwf2025Ksat):
        if ksat.ncwf_id:
            # Utiliser l'URL du modèle si disponible, sinon afficher juste l'ID
            if hasattr(ksat, 'url') and ksat.url:
                return format_html('<a href="{}" class="underline">NCWF-2025 {}</a>', ksat.url, ksat.ncwf_id)
            else:
                return format_html('<span class="text-gray-600">NCWF-2025 {}</span>', ksat.ncwf_id)
    return ''