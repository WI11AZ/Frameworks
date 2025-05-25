from django.db import models


class ModalInfoCategory(models.Model):
    """Catégorie d'information modal (info-button-1, info-button-2, info-button-3)"""
    button_id = models.CharField(max_length=20, unique=True)  # ex: info-button-1
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ModalInfo(models.Model):
    """Information pour les modals affichées par les boutons d'information"""
    category = models.ForeignKey(ModalInfoCategory, on_delete=models.CASCADE, related_name='modal_infos')
    ksat_type = models.ForeignKey('KsatType', on_delete=models.CASCADE, related_name='modal_infos')
    title = models.CharField(max_length=255)  # Titre du modal
    
    class Meta:
        unique_together = ('category', 'ksat_type')
    
    def __str__(self):
        return f"{self.ksat_type} - {self.category}"


class ModalInfoOption(models.Model):
    """Option dans un modal d'information"""
    modal_info = models.ForeignKey(ModalInfo, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=10)  # texte affiché (1, 2, 3, A, B, etc.)
    title = models.TextField()  # description complète
    order = models.IntegerField(default=0)  # ordre d'affichage
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.modal_info} - {self.text}"
