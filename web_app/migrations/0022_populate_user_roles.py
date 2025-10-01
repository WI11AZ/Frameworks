# Generated manually to fix user authentication issues

from django.db import migrations
from web_app.helpers.user_roles import get_role_from_matricule


def populate_user_roles(apps, schema_editor):
    """
    Migration de données pour assigner des rôles aux utilisateurs existants
    qui n'en ont pas encore.
    """
    User = apps.get_model('web_app', 'User')
    
    # Récupérer tous les utilisateurs qui n'ont pas de rôle assigné
    users_without_role = User.objects.filter(role__isnull=True) | User.objects.filter(role='')
    
    for user in users_without_role:
        if user.matricule:
            # Assigner le rôle basé sur le matricule
            user.role = get_role_from_matricule(user.matricule)
            user.save()
        else:
            # Si pas de matricule, assigner le rôle par défaut
            user.role = 'normal_user'
            user.save()


def reverse_populate_user_roles(apps, schema_editor):
    """
    Migration inverse - remet les rôles à null
    """
    User = apps.get_model('web_app', 'User')
    User.objects.all().update(role=None)


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0021_dcwf2025ksat_dcwf2025workroleksatrelation'),
    ]

    operations = [
        migrations.RunPython(
            populate_user_roles,
            reverse_populate_user_roles,
        ),
    ]
