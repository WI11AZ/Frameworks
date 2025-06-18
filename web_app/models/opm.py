from django.db import models


class Opm(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
