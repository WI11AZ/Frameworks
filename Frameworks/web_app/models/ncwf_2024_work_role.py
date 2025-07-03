from django.db import models

from web_app.models import Ncwf2024Tks


class Ncwf2024WorkRole(models.Model):
    opms = models.ManyToManyField(
        "Opm", blank=True, related_name="ncwf_2024_work_roles"
    )
    nist_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    ncwf_2024_tks = models.ManyToManyField("Ncwf2024Tks", blank=True, related_name="ncwf_2024_work_roles")

    def has_ksat(self, ksat):
        if isinstance(ksat, Ncwf2024Tks):
            return self.ncwf_2024_tks.filter(id=ksat.id).exists()
        return False