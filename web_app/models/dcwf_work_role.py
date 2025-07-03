from django.db import models

from web_app.models import DcwfKsat, Ncwf2017Ksat


class DcwfWorkRole(models.Model):
    opm = models.OneToOneField(
        "Opm", on_delete=models.CASCADE, blank=True, null=True, unique=True
    )
    nist_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(
        "DcwfCategory",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="dcwf_work_roles",
    )

    def has_ksat(self, ksat):
        if isinstance(ksat, DcwfKsat):
            return self.dcwf_ksat_relations.filter(dcwf_ksat=ksat).exists()
        if isinstance(ksat, Ncwf2017Ksat):
            return self.dcwf_ksat_relations.filter(dcwf_ksat__ncwf_2017_ksat=ksat).exists()
        return False

    def dcwf_ksats(self):
        return DcwfKsat.objects.filter(dcwf_work_role_relations__dcwf_work_role=self)

    def ncwf_2024_work_role(self):
        return self.opm.ncwf_2024_work_roles.first()

    def ncwf_2017_work_role(self):
        return self.opm.ncwf_2017_work_roles.first()
