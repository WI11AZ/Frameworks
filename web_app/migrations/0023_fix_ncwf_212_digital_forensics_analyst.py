# Migration pour corriger le titre DCWF 2025 du rôle 212: -> Digital Forensics Analyst

from django.db import migrations


def fix_dcwf_212_title(apps, schema_editor):
    Dcwf2025WorkRole = apps.get_model('web_app', 'Dcwf2025WorkRole')
    Dcwf2025WorkRole.objects.filter(dcwf_code='212').update(title='Digital Forensics Analyst')


def reverse_fix(apps, schema_editor):
    Dcwf2025WorkRole = apps.get_model('web_app', 'Dcwf2025WorkRole')
    Dcwf2025WorkRole.objects.filter(dcwf_code='212').update(title='Cyber Defense Forensic Analyst')


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0022_populate_user_roles'),
    ]

    operations = [
        migrations.RunPython(fix_dcwf_212_title, reverse_fix),
    ]
