from django.db import models


class Ncwf2024WorkRole(models.Model):
    opms = models.ManyToManyField(
        "Opm", blank=True, related_name="ncwf_2024_work_roles"
    )
    nist_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    ncwf_2024_tks = models.ManyToManyField("Ncwf2024Tks", blank=True)
