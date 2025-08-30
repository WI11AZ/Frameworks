from django.db import models

class NiceFrameworkWorkRole(models.Model):
    CATEGORY_CHOICES = [
        ('OVERSIGHT and GOVERNANCE (OG)', 'OVERSIGHT and GOVERNANCE (OG)'),
        ('DESIGN and DEVELOPMENT (DD)', 'DESIGN and DEVELOPMENT (DD)'),
        ('IMPLEMENTATION and OPERATION (IO)', 'IMPLEMENTATION and OPERATION (IO)'),
        ('PROTECTION and DEFENSE (PD)', 'PROTECTION and DEFENSE (PD)'),
        ('INVESTIGATION (IN)', 'INVESTIGATION (IN)'),
    ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    definition = models.TextField()
    nice_id = models.CharField(max_length=20, unique=True)  # ex: OG-WRL-001
    opm_code = models.CharField(max_length=20)  # ex: 723, TBD
    
    class Meta:
        ordering = ['category', 'nice_id']
    
    def __str__(self):
        return f"{self.nice_id} - {self.title}"
    
    @property
    def id(self):
        return self.pk
