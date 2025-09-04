from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from web_app.helpers.user_roles import (
    get_role_from_matricule, 
    add_super_user_matricule, 
    remove_super_user_matricule,
    add_beta_tester_matricule, 
    remove_beta_tester_matricule,
    get_all_super_user_matricules,
    get_all_beta_tester_matricules
)

User = get_user_model()

class Command(BaseCommand):
    help = 'Gérer les rôles utilisateur basés sur les matricules'

    def add_arguments(self, parser):
        parser.add_argument(
            'action',
            choices=['list', 'add-super', 'remove-super', 'add-beta', 'remove-beta', 'update-all'],
            help='Action à effectuer'
        )
        parser.add_argument(
            '--matricule',
            type=str,
            help='Matricule de l\'utilisateur (requis pour add/remove)'
        )

    def handle(self, *args, **options):
        action = options['action']
        matricule = options.get('matricule')

        if action == 'list':
            self.list_roles()
        elif action == 'add-super':
            if not matricule:
                raise CommandError('Le matricule est requis pour ajouter un Super User')
            self.add_super_user(matricule)
        elif action == 'remove-super':
            if not matricule:
                raise CommandError('Le matricule est requis pour supprimer un Super User')
            self.remove_super_user(matricule)
        elif action == 'add-beta':
            if not matricule:
                raise CommandError('Le matricule est requis pour ajouter un Bêta testeur')
            self.add_beta_tester(matricule)
        elif action == 'remove-beta':
            if not matricule:
                raise CommandError('Le matricule est requis pour supprimer un Bêta testeur')
            self.remove_beta_tester(matricule)
        elif action == 'update-all':
            self.update_all_users()

    def list_roles(self):
        """Affiche tous les matricules par rôle"""
        self.stdout.write(self.style.SUCCESS('=== Super Users ==='))
        super_users = get_all_super_user_matricules()
        for matricule in super_users:
            self.stdout.write(f'  - {matricule}')
        
        self.stdout.write(self.style.SUCCESS('\n=== Bêta testeurs ==='))
        beta_testers = get_all_beta_tester_matricules()
        for matricule in beta_testers:
            self.stdout.write(f'  - {matricule}')
        
        self.stdout.write('')  # Ligne vide pour séparer
        self.stdout.write(self.style.SUCCESS('=== Utilisateurs en base ==='))
        users = User.objects.exclude(matricule__isnull=True).order_by('matricule')
        for user in users:
            role_display = user.get_role_display()
            self.stdout.write(f'  - {user.matricule} ({user.last_name}): {role_display}')

    def add_super_user(self, matricule):
        """Ajoute un matricule à la liste des Super Users"""
        if add_super_user_matricule(matricule):
            self.stdout.write(
                self.style.SUCCESS(f'Matricule {matricule} ajouté aux Super Users')
            )
            # Mettre à jour l'utilisateur en base si il existe
            try:
                user = User.objects.get(matricule=matricule)
                user.role = 'super_user'
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Utilisateur {user.last_name} mis à jour en Super User')
                )
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Aucun utilisateur trouvé avec le matricule {matricule}')
                )
        else:
            self.stdout.write(
                self.style.WARNING(f'Le matricule {matricule} est déjà dans la liste des Super Users')
            )

    def remove_super_user(self, matricule):
        """Supprime un matricule de la liste des Super Users"""
        if remove_super_user_matricule(matricule):
            self.stdout.write(
                self.style.SUCCESS(f'Matricule {matricule} supprimé des Super Users')
            )
            # Mettre à jour l'utilisateur en base si il existe
            try:
                user = User.objects.get(matricule=matricule)
                user.role = 'normal_user'
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Utilisateur {user.last_name} mis à jour en User Normal')
                )
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Aucun utilisateur trouvé avec le matricule {matricule}')
                )
        else:
            self.stdout.write(
                self.style.WARNING(f'Le matricule {matricule} n\'était pas dans la liste des Super Users')
            )

    def add_beta_tester(self, matricule):
        """Ajoute un matricule à la liste des Bêta testeurs"""
        if add_beta_tester_matricule(matricule):
            self.stdout.write(
                self.style.SUCCESS(f'Matricule {matricule} ajouté aux Bêta testeurs')
            )
            # Mettre à jour l'utilisateur en base si il existe
            try:
                user = User.objects.get(matricule=matricule)
                user.role = 'beta_tester'
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Utilisateur {user.last_name} mis à jour en Bêta testeur')
                )
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Aucun utilisateur trouvé avec le matricule {matricule}')
                )
        else:
            self.stdout.write(
                self.style.WARNING(f'Le matricule {matricule} est déjà dans la liste des Bêta testeurs')
            )

    def remove_beta_tester(self, matricule):
        """Supprime un matricule de la liste des Bêta testeurs"""
        if remove_beta_tester_matricule(matricule):
            self.stdout.write(
                self.style.SUCCESS(f'Matricule {matricule} supprimé des Bêta testeurs')
            )
            # Mettre à jour l'utilisateur en base si il existe
            try:
                user = User.objects.get(matricule=matricule)
                user.role = 'normal_user'
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Utilisateur {user.last_name} mis à jour en User Normal')
                )
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Aucun utilisateur trouvé avec le matricule {matricule}')
                )
        else:
            self.stdout.write(
                self.style.WARNING(f'Le matricule {matricule} n\'était pas dans la liste des Bêta testeurs')
            )

    def update_all_users(self):
        """Met à jour tous les utilisateurs selon leur matricule"""
        users = User.objects.all()
        updated_count = 0
        
        for user in users:
            if user.matricule:
                detected_role = get_role_from_matricule(user.matricule)
                if user.role != detected_role:
                    old_role = user.get_role_display()
                    user.role = detected_role
                    user.save()
                    new_role = user.get_role_display()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Utilisateur {user.last_name} ({user.matricule}): {old_role} → {new_role}'
                        )
                    )
                    updated_count += 1
        
        if updated_count == 0:
            self.stdout.write(self.style.SUCCESS('Aucun utilisateur mis à jour'))
        else:
            self.stdout.write(
                self.style.SUCCESS(f'{updated_count} utilisateur(s) mis à jour')
            )
