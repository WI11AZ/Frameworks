from django.db import models


class DcwfKsat(models.Model):
    dcwf_id = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)
    url = models.CharField(max_length=500, blank=True, null=True)
    ncwf_2017_ksat = models.ForeignKey(
        "Ncwf2017Ksat",
        blank=True,
        null=True,
        related_name="dcwf_ksats",
        on_delete=models.CASCADE,
    )
