from django.db import models


class AIWorkRole(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, default="Emerging AI work roles with Real Impact (SANS)")
    
    def __str__(self):
        return self.title
