from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from web_app.helpers.user_roles import get_role_from_matricule

User = get_user_model()


class Command(BaseCommand):
    help = 'Fix user roles for existing users who may have authentication issues'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be changed without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING('DRY RUN MODE - No changes will be made')
            )
        
        # Trouver les utilisateurs qui ont des problèmes potentiels
        users_without_role = User.objects.filter(
            role__isnull=True
        ) | User.objects.filter(role='')
        
        users_without_matricule = User.objects.filter(
            matricule__isnull=True
        ) | User.objects.filter(matricule='')
        
        total_fixed = 0
        
        # Corriger les utilisateurs sans rôle
        for user in users_without_role:
            if user.matricule:
                new_role = get_role_from_matricule(user.matricule)
                if not dry_run:
                    user.role = new_role
                    user.save()
                self.stdout.write(
                    f"{'[DRY RUN] ' if dry_run else ''}User {user.username} "
                    f"(matricule: {user.matricule}) -> role: {new_role}"
                )
                total_fixed += 1
            else:
                if not dry_run:
                    user.role = 'normal_user'
                    user.save()
                self.stdout.write(
                    f"{'[DRY RUN] ' if dry_run else ''}User {user.username} "
                    f"(no matricule) -> role: normal_user"
                )
                total_fixed += 1
        
        # Corriger les utilisateurs sans matricule
        for user in users_without_matricule:
            if not dry_run:
                user.role = 'normal_user'
                user.save()
            self.stdout.write(
                f"{'[DRY RUN] ' if dry_run else ''}User {user.username} "
                f"(no matricule) -> role: normal_user"
            )
            total_fixed += 1
        
        if dry_run:
            self.stdout.write(
                self.style.SUCCESS(
                    f'DRY RUN: Would fix {total_fixed} users'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully fixed {total_fixed} users'
                )
            )
