from django.db import models


class Ncwf2017Ksat(models.Model):
    ncwf_id = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)

    @property
    def url(self):
        return f"https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/NICE_1_1_0/home?element={self.ncwf_id}&type=work_role"
