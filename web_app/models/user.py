from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from ..helpers.user_roles import get_role_from_matricule


class User(AbstractUser):
    # Choix pour les rôles
    ROLE_CHOICES = [
        ('super_user', 'Super User'),
        ('beta_tester', 'Bêta testeur'),
        ('normal_user', 'User Normal'),
    ]
    
    matricule = models.CharField(
        max_length=7,
        unique=True,
        null=True,  # Permettre null pour les utilisateurs existants
        blank=True,  # Permettre vide dans les formulaires administratifs
        validators=[
            MinLengthValidator(7, message="Le matricule doit contenir exactement 7 chiffres"),
            RegexValidator(
                regex=r'^\d{7}$',
                message="Le matricule doit contenir uniquement des chiffres"
            )
        ],
        help_text="Matricule à 7 chiffres"
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='normal_user',
        help_text="Rôle de l'utilisateur déterminé automatiquement par le matricule"
    )

    def __str__(self):
        return f"{self.last_name} ({self.matricule}) - {self.get_role_display()}"

    def detect_role_from_matricule(self):
        """Détecte automatiquement le rôle basé sur le matricule en utilisant le helper"""
        return get_role_from_matricule(self.matricule)
    
    def is_super_user(self):
        """Vérifie si l'utilisateur est un Super User"""
        return self.role == 'super_user'
    
    def is_beta_tester(self):
        """Vérifie si l'utilisateur est un Bêta testeur"""
        return self.role == 'beta_tester'
    
    def is_normal_user(self):
        """Vérifie si l'utilisateur est un User Normal"""
        return self.role == 'normal_user'
