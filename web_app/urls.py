from django.urls import path
from .views import home, work_role, compare

urlpatterns = [
    path('', home, name='home'),
    path('work_role/<int:id>/', work_role, name='work_role'),
    path('compare/', compare, name='compare'),
]