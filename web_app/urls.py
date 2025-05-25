from django.urls import path
from .views import home, work_role, compare, get_modal_info_json_view

urlpatterns = [
    path('', home, name='home'),
    path('work_role/<int:id>/', work_role, name='work_role'),
    path('compare/', compare, name='compare'),
    path('api/modal-info/', get_modal_info_json_view, name='modal_info_json'),
]