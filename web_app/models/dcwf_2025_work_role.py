from django.db import models


class Dcwf2025Ksat(models.Model):
    """KSATs pour les work roles DCWF 2025"""
    dcwf_id = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20)
    core_or_additional = models.CharField(
        choices=[('C', 'Core'), ('A', 'Additional')],
        default='A',
        help_text='Core (C) ou Additional (A)',
        max_length=1
    )

    class Meta:
        verbose_name = 'KSAT DCWF 2025'
        verbose_name_plural = 'KSAT DCWF 2025'
        ordering = ['dcwf_id']

    def __str__(self):
        return f"{self.dcwf_id}: {self.description[:50]}..."


class Dcwf2025WorkRoleKsatRelation(models.Model):
    """Relation entre work roles DCWF 2025 et leurs KSATs"""
    work_role = models.ForeignKey(
        'Dcwf2025WorkRole',
        on_delete=models.CASCADE,
        related_name='ksat_relations'
    )
    ksat = models.ForeignKey(
        Dcwf2025Ksat,
        on_delete=models.CASCADE,
        related_name='work_role_relations'
    )
    core_or_additional = models.CharField(
        choices=[('C', 'Core'), ('A', 'Additional')],
        default='A',
        help_text='Core (C) ou Additional (A)',
        max_length=1
    )

    class Meta:
        verbose_name = 'Relation Work Role DCWF 2025 - KSAT'
        verbose_name_plural = 'Relations Work Role DCWF 2025 - KSAT'
        unique_together = (('work_role', 'ksat'),)

    def __str__(self):
        return f"{self.work_role.dcwf_code} - {self.ksat.dcwf_id}"


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
    
    def has_ksat(self, ksat):
        """Vérifie si ce work role a le KSAT donné"""
        if isinstance(ksat, Dcwf2025Ksat):
            return self.ksat_relations.filter(ksat=ksat).exists()
        return False

    class Meta:
        verbose_name = "Work Role DCWF 2025"
        verbose_name_plural = "Work Roles DCWF 2025"
        ordering = ['dcwf_code']
