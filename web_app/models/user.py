from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class User(AbstractUser):
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

    def __str__(self):
        return f"{self.last_name} ({self.matricule})"
