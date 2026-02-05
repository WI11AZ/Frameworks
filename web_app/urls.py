from django.urls import path
from .views import (
    home, work_role, compare, get_modal_info_json_view, get_select_options_json_view, ksat_compare_details, etape_deux, 
    saved_ksat_selections, resume_step2, summary_chart_view, summary_mil_view, project_recap_view, etape2_first_step, 
    save_ksat_selection, list_ksat_selections, delete_ksat_selection, attributs_part_deux, attributs_part_deux_opm_id,
    nf_com_007_details, nf_com_002_details, models_2025, download_file, dcwf_finder_view,
    dcwf_finder_css, dcwf_finder_js, dcwf_finder_data, check_saved_selections, convert_t1_codes_to_ids,
    step0_baseline_view, step0_baseline_json, get_ksat_data_view, sfia_generic_attributes_json,
    dcwf_explorer_view, atlas_explorer_view, atlas_explorer_static, technologia_song_view, output_json, sfia_skills_json, idf_json, military_skills_json,
    qf_viewer_view, qf_download_view
)
from .views_auth import main_view, login_view, signup_view, logout_view, account_options_view, change_password_view, delete_account_view
from .views_saved_data import get_saved_data, list_saved_data, save_data, delete_saved_data, get_all_saved_data

urlpatterns = [
    # Page principale et authentification
    path('', main_view, name='main'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    
    # Options du compte
    path('account/options/', account_options_view, name='account_options'),
    path('account/change-password/', change_password_view, name='change_password'),
    path('account/delete/', delete_account_view, name='delete_account'),
    
    # Routes existantes
    path('home/', home, name='home'),
    path('models-2025/', models_2025, name='models_2025'),
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
    path('summary_mil/', summary_mil_view, name='summary_mil'),
    path('project_recap/', project_recap_view, name='project_recap'),
    path('attributs-part-deux/', attributs_part_deux, name='attributs_part_deux'),
    path('attributs-part-deux-opm-id/', attributs_part_deux_opm_id, name='attributs_part_deux_opm_id'),
    path('download/<str:filename>/', download_file, name='download_file'),
    
    # API pour les données sauvegardées utilisateur
    path('api/saved-data/', list_saved_data, name='list_saved_data'),
    path('api/saved-data/all/', get_all_saved_data, name='get_all_saved_data'),
    path('api/saved-data/<str:key>/', get_saved_data, name='get_saved_data'),
    path('api/saved-data/save/', save_data, name='save_data'),
    path('api/saved-data/delete/<str:key>/', delete_saved_data, name='delete_saved_data'),
    
    # API spécifique pour les sélections KSAT (sans authentification requise)
    path('api/ksat-selections/', list_ksat_selections, name='list_ksat_selections'),
    path('api/ksat-selections/save/', save_ksat_selection, name='save_ksat_selection'),
    path('api/ksat-selections/delete/<str:key>/', delete_ksat_selection, name='delete_ksat_selection'),
    
    # API pour vérifier les sauvegardes
    path('check-saved-selections/', check_saved_selections, name='check_saved_selections'),
    
    # API pour convertir les codes de t1.html en IDs
    path('api/convert-t1-codes/', convert_t1_codes_to_ids, name='convert_t1_codes'),
    
    # Nouvelles routes
    path('ksat/nf-com-007-details/', nf_com_007_details, name='nf_com_007_details'),
    path('ksat/nf-com-002-details/', nf_com_002_details, name='nf_com_002_details'),
    
    # DCWF Finder
    path('dcwf-finder/', dcwf_finder_view, name='dcwf_finder'),
    
    # DCWF Finder - Fichiers statiques
    path('dcwf-finder/css/', dcwf_finder_css, name='dcwf_finder_css'),
    path('dcwf-finder/js/', dcwf_finder_js, name='dcwf_finder_js'),
    path('dcwf-finder/data/', dcwf_finder_data, name='dcwf_finder_data'),
    
    # Explorateur DCWF Pro v3
    path('dcwf-explorer/', dcwf_explorer_view, name='dcwf_explorer'),
    # Explorateur ATLAS
    path('atlas-explorer/', atlas_explorer_view, name='atlas_explorer'),
    path('atlas-explorer/<str:filename>', atlas_explorer_static, name='atlas_explorer_static'),
    path('technologia-song/', technologia_song_view, name='technologia_song'),
    
    # Step0 Baseline
    path('step0-baseline/', step0_baseline_view, name='step0_baseline'),
    path('step0-baseline/json/', step0_baseline_json, name='step0_baseline_json'),
    
    # API pour les données KSAT
    path('api/ksat-data/<str:framework>/', get_ksat_data_view, name='get_ksat_data'),
    
    # API pour les attributs génériques SFIA
    path('api/sfia-generic-attributes/', sfia_generic_attributes_json, name='sfia_generic_attributes_json'),
    path('api/output-json/', output_json, name='output_json'),
    path('api/sfia-skills/', sfia_skills_json, name='sfia_skills_json'),
    path('api/idf-json/', idf_json, name='idf_json'),
    path('api/military-skills/', military_skills_json, name='military_skills_json'),
    
    # QF Viewer
    path('qf/', qf_viewer_view, name='qf_viewer'),
    path('qf/download/<str:filename>/', qf_download_view, name='qf_download'),
]