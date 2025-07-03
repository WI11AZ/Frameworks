from django.db import models


class SelectCategory(models.Model):
    """Catégorie de select (Importance, Type de maîtrise, etc.)"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class KsatType(models.Model):
    """Type de KSAT (Knowledge, Skill, Ability, Task)"""
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name


class SelectOption(models.Model):
    """Option pour les selects avec texte détaillé"""
    category = models.ForeignKey(SelectCategory, on_delete=models.CASCADE, related_name='options')
    ksat_type = models.ForeignKey(KsatType, on_delete=models.CASCADE, related_name='options')
    value = models.CharField(max_length=10)  # La valeur affichée (0, 1, 2, 3, B, S, M)
    title = models.CharField(max_length=255)  # Le tooltip court
    description = models.TextField()  # Le texte détaillé pour le tooltip et le modal
    order = models.IntegerField(default=0)  # Pour l'ordre d'affichage
    
    class Meta:
        unique_together = ('category', 'ksat_type', 'value')
        ordering = ['category', 'ksat_type', 'order']
    
    def __str__(self):
        return f"{self.ksat_type} - {self.category} - {self.value}"
