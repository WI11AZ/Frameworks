from django.urls import path
from .views import (
    home, work_role, compare, get_modal_info_json_view, get_select_options_json_view, ksat_compare_details, etape_deux, 
    saved_ksat_selections, resume_step2, summary_chart_view, etape2_first_step, 
    save_ksat_selection, list_ksat_selections, delete_ksat_selection
)
from .views_auth import main_view, login_view, signup_view, logout_view
from .views_saved_data import get_saved_data, list_saved_data, save_data, delete_saved_data

urlpatterns = [
    # Page principale et authentification
    path('', main_view, name='main'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    
    # Routes existantes
    path('home/', home, name='home'),
    path('work_role/<int:id>/', work_role, name='work_role'),
    path('compare/', compare, name='compare'),
    path('compare/details/', ksat_compare_details, name='ksat_compare_details'),
    path('api/modal-info/', get_modal_info_json_view, name='modal_info_json'),
    path('api/select-options/', get_select_options_json_view, name='select_options_json'),
    path('ksat/etape_deux', etape_deux, name='etape_deux'),
    path('ksat/etape2_first_step', etape2_first_step, name='etape2_first_step'),
    path('ksat/saved_ksat_selections', saved_ksat_selections, name='saved_ksat_selections'),
    path('ksat/resume_step2/<int:index>/', resume_step2, name='resume_step2'),
    path('summary_chart/', summary_chart_view, name='summary_chart'),
    
    # API pour les données sauvegardées utilisateur
    path('api/saved-data/', list_saved_data, name='list_saved_data'),
    path('api/saved-data/<str:key>/', get_saved_data, name='get_saved_data'),
    path('api/saved-data/save/', save_data, name='save_data'),
    path('api/saved-data/delete/<str:key>/', delete_saved_data, name='delete_saved_data'),
    
    # API spécifique pour les sélections KSAT (sans authentification requise)
    path('api/ksat-selections/', list_ksat_selections, name='list_ksat_selections'),
    path('api/ksat-selections/save/', save_ksat_selection, name='save_ksat_selection'),
    path('api/ksat-selections/delete/<str:key>/', delete_ksat_selection, name='delete_ksat_selection'),
]