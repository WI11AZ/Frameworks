from django.db import models


class DcwfCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
