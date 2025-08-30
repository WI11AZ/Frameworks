from django.db import models


class Dcwf2025WorkRole(models.Model):
    """Work Roles DCWF pour les modèles 2025"""
    dcwf_code = models.CharField(max_length=10, blank=True, null=True)
    ncwf_id = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    ncwf_definition = models.TextField(blank=True, null=True, help_text="Définition NCWF 2025")
    ncwf_title = models.CharField(max_length=200, blank=True, null=True, help_text="Titre NCWF 2025")
    category = models.ForeignKey(
        "Dcwf2025Category",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="work_roles",
    )

    def __str__(self):
        return f"{self.dcwf_code} - {self.title}" if self.dcwf_code and self.title else "Work Role sans titre"

    @property
    def omp_id(self):
        """Retourne le DCWF Code comme OMP ID pour compatibilité avec le template"""
        return self.dcwf_code
    
    @property
    def description(self):
        """Alias pour definition pour compatibilité avec le template"""
        return self.definition

    class Meta:
        verbose_name = "Work Role DCWF 2025"
        verbose_name_plural = "Work Roles DCWF 2025"
        ordering = ['dcwf_code']
