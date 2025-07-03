from django.db import models

from web_app.models import Ncwf2017Ksat, DcwfKsat


class Ncwf2017WorkRole(models.Model):
    opms = models.ManyToManyField(
        "Opm", blank=True, related_name="ncwf_2017_work_roles"
    )
    nist_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    ncwf_2024_workroles = models.ManyToManyField("Ncwf2024WorkRole", blank=True)
    ncwf_2017_ksats = models.ManyToManyField("Ncwf2017Ksat", blank=True, related_name="ncwf_2017_work_roles")

    def has_ksat(self, ksat):
        if isinstance(ksat, Ncwf2017Ksat):
            return self.ncwf_2017_ksats.filter(id=ksat.id).exists()
        if isinstance(ksat, DcwfKsat):
            return self.ncwf_2017_ksats.filter(id=ksat.ncwf_2017_ksat_id).exists()
        return False
