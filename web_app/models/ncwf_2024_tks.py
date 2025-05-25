from django.db import models

from web_app.models import Ncwf2017Ksat


class Ncwf2024Tks(models.Model):
    ncwf_id = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)
    ncwf_2017_ksats = models.ManyToManyField(
        "Ncwf2017Ksat", blank=True, related_name="ncwf_2024_tks"
    )

    def new_in_ncwf_2024(self):
        # Returns true if no Ncwf2017Ksat with ncwf_id with the same ncwf_id exists
        return not Ncwf2017Ksat.objects.filter(ncwf_id=self.ncwf_id).exists()
