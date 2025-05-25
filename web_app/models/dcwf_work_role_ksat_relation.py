from django.db import models


class KsatRelation(models.TextChoices):
    CORE = "CORE", "Core"
    ADDITIONAL = "ADDITIONAL", "Additional"


class DcwfWorkRoleKsatRelation(models.Model):
    dcwf_work_role = models.ForeignKey("DcwfWorkRole", on_delete=models.CASCADE, related_name="dcwf_ksat_relations")
    dcwf_ksat = models.ForeignKey("DcwfKsat", on_delete=models.CASCADE, related_name="dcwf_work_role_relations")
    type = models.CharField(max_length=10, choices=KsatRelation.choices)

    class Meta:
        unique_together = (
            "dcwf_work_role",
            "dcwf_ksat",
            "type",
        )  # A work role can have a ksat only once
