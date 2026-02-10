# Migration pour corriger la définition DCWF 2025 du rôle 212

from django.db import migrations

DCWF_212_NEW_DEFINITION = (
    "Analyzes digital evidence and investigates computer security incidents "
    "to derive useful information in support of system/network vulnerability mitigation."
)

DCWF_212_OLD_DEFINITION = (
    "Responsible for analyzing digital evidence from computer security incidents "
    "to derive useful information in support of system and network vulnerability mitigation."
)


def fix_dcwf_212_definition(apps, schema_editor):
    Dcwf2025WorkRole = apps.get_model('web_app', 'Dcwf2025WorkRole')
    Dcwf2025WorkRole.objects.filter(dcwf_code='212').update(definition=DCWF_212_NEW_DEFINITION)


def reverse_fix(apps, schema_editor):
    Dcwf2025WorkRole = apps.get_model('web_app', 'Dcwf2025WorkRole')
    Dcwf2025WorkRole.objects.filter(dcwf_code='212').update(definition=DCWF_212_OLD_DEFINITION)


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0023_fix_ncwf_212_digital_forensics_analyst'),
    ]

    operations = [
        migrations.RunPython(fix_dcwf_212_definition, reverse_fix),
    ]
