from django.urls import path

from web_app.views import home, work_role

urlpatterns = [
    path("", home, name="home"),
    path("work_role/<int:work_role_id>", work_role, name="work_role"),
]
