from django.db import models


class Ncwf2017Ksat(models.Model):
    ncwf_id = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)

    @property
    def withdrawn_in_ncwf_2024(self):
        # Returns true if there is a ncwf_2024_tks related to this ksat
        return self.ncwf_2024_tks.exists()

    @property
    def url(self):
        return f"https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/NICE_1_1_0/home?element={self.ncwf_id}&type=work_role"
