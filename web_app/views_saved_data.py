from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
import json

from .models.user_saved_data import UserSavedData


@login_required
@require_http_methods(["GET"])
def get_saved_data(request, key):
    """
    Récupère les données sauvegardées pour une clé donnée.
    """
    try:
        saved_data = UserSavedData.objects.get(user=request.user, key=key)
        return JsonResponse({"status": "success", "data": saved_data.value})
    except UserSavedData.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Données introuvables"}, status=404)


@login_required
@require_http_methods(["GET"])
def list_saved_data(request):
    """
    Liste toutes les clés de données sauvegardées pour l'utilisateur.
    """
    saved_data = UserSavedData.objects.filter(user=request.user)
    data_list = [{"key": item.key, "updated_at": item.updated_at} for item in saved_data]
    return JsonResponse({"status": "success", "data": data_list})


@login_required
@require_http_methods(["POST"])
@ensure_csrf_cookie
def save_data(request):
    """
    Sauvegarde les données pour une clé donnée.
    """
    try:
        data = json.loads(request.body)
        key = data.get("key")
        value = data.get("value")
        
        if not key or value is None:
            return JsonResponse({"status": "error", "message": "La clé et la valeur sont requises"}, status=400)
        
        # Utiliser update_or_create pour mettre à jour si la clé existe déjà
        user_data, created = UserSavedData.objects.update_or_create(
            user=request.user,
            key=key,
            defaults={"value": value}
        )
        
        status = "created" if created else "updated"
        return JsonResponse({"status": "success", "message": f"Données {status}"})
    
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Format JSON invalide"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


@login_required
@require_http_methods(["DELETE"])
def delete_saved_data(request, key):
    """
    Supprime les données sauvegardées pour une clé donnée.
    """
    try:
        data = UserSavedData.objects.get(user=request.user, key=key)
        data.delete()
        return JsonResponse({"status": "success", "message": "Données supprimées"})
    except UserSavedData.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Données introuvables"}, status=404) 