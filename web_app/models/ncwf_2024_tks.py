from django.db import models


class Ncwf2024Tks(models.Model):
    ncwf_id = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)
    ncwf_2017_ksats = models.ManyToManyField(
        "Ncwf2017Ksat", blank=True, related_name="ncwf_2024_tks"
    )
