from django.db import models


class Dcwf2025Category(models.Model):
    """Catégories DCWF pour les modèles 2025"""
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.title or "Catégorie sans titre"

    class Meta:
        verbose_name = "Catégorie DCWF 2025"
        verbose_name_plural = "Catégories DCWF 2025"
