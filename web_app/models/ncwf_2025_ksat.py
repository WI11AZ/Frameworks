from django.db import models


class Ncwf2025Ksat(models.Model):
    ncwf_id = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20)
    core_or_additional = models.CharField(
        choices=[('C', 'Core'), ('A', 'Additional')], 
        default='A', 
        help_text='Core (C) ou Additional (A)', 
        max_length=1
    )

    class Meta:
        verbose_name = 'KSAT NCWF 2025'
        verbose_name_plural = 'KSAT NCWF 2025'
        ordering = ['ncwf_id']

    def __str__(self):
        return f"{self.ncwf_id}: {self.description[:50]}..."

    @property
    def url(self):
        return f"https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/NICE_1_1_0/home?element={self.ncwf_id}&type=work_role"


class Ncwf2025WorkRole(models.Model):
    ncwf_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    framework = models.CharField(max_length=10, default='NCWF')
    
    class Meta:
        verbose_name = 'Work Role NCWF 2025'
        verbose_name_plural = 'Work Roles NCWF 2025'
        ordering = ['ncwf_id']

    def __str__(self):
        return f"{self.ncwf_id}: {self.name}"
    
    def has_ksat(self, ksat):
        """Vérifie si ce work role a le KSAT donné"""
        if isinstance(ksat, Ncwf2025Ksat):
            return self.ksat_relations.filter(ksat=ksat).exists()
        return False


class Ncwf2025WorkRoleKsatRelation(models.Model):
    work_role = models.ForeignKey(
        Ncwf2025WorkRole, 
        on_delete=models.CASCADE, 
        related_name='ksat_relations'
    )
    ksat = models.ForeignKey(
        Ncwf2025Ksat, 
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
        verbose_name = 'Relation Work Role NCWF 2025 - KSAT'
        verbose_name_plural = 'Relations Work Role NCWF 2025 - KSAT'
        unique_together = ('work_role', 'ksat')

    def __str__(self):
        return f"{self.work_role.ncwf_id} - {self.ksat.ncwf_id}"
