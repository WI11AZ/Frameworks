from django.db import models
from .user import User


class UserSavedData(models.Model):
    """
    Modèle pour stocker les données sauvegardées des utilisateurs.
    Une alternative côté serveur au localStorage du navigateur.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_data')
    key = models.CharField(max_length=255, help_text="Clé de stockage (équivalent à la clé du localStorage)")
    value = models.JSONField(help_text="Valeur associée à la clé (stockée en JSON)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'key')
        verbose_name = "Données sauvegardées utilisateur"
        verbose_name_plural = "Données sauvegardées utilisateurs"
        
    def __str__(self):
        return f"{self.user.username} - {self.key} ({self.updated_at})" 