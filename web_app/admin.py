from django.contrib import admin
from .models import DcwfCategory, SelectCategory, KsatType, SelectOption
from .models import ModalInfoCategory, ModalInfo, ModalInfoOption

# Modèles existants
admin.site.register(DcwfCategory)

# Administration des options de select
@admin.register(SelectCategory)
class SelectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(KsatType)
class KsatTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SelectOption)
class SelectOptionAdmin(admin.ModelAdmin):
    list_display = ('ksat_type', 'category', 'value', 'title', 'order')
    list_filter = ('ksat_type', 'category')
    search_fields = ('value', 'title', 'description')
    list_editable = ('value', 'title', 'order')

# Administration des modals d'information
@admin.register(ModalInfoCategory)
class ModalInfoCategoryAdmin(admin.ModelAdmin):
    list_display = ('button_id', 'name', 'description')
    search_fields = ('name', 'button_id')

@admin.register(ModalInfo)
class ModalInfoAdmin(admin.ModelAdmin):
    list_display = ('ksat_type', 'category', 'title')
    list_filter = ('ksat_type', 'category')
    search_fields = ('title',)

@admin.register(ModalInfoOption)
class ModalInfoOptionAdmin(admin.ModelAdmin):
    list_display = ('modal_info', 'text', 'order')
    list_filter = ('modal_info__ksat_type', 'modal_info__category')
    search_fields = ('text', 'title')
    list_editable = ('text', 'order')
