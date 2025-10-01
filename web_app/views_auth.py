from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models.user import User
from .models.user_saved_data import UserSavedData


def main_view(request):
    """Vue pour la page principale avec les formulaires de connexion et d'inscription."""
    context = {
        'login_error': request.session.pop('login_error', None),
        'signup_error': request.session.pop('signup_error', None),
    }
    return render(request, 'web_app/main/main.html', context)


def login_view(request):
    """Vue pour gérer la connexion des utilisateurs."""
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        password = request.POST.get('password')
        
        try:
            # Vérifier si l'utilisateur existe avec ce matricule
            user = User.objects.get(matricule=matricule)
            
            # Corriger automatiquement les utilisateurs sans rôle
            if not user.role or user.role == '':
                from .helpers.user_roles import get_role_from_matricule
                user.role = get_role_from_matricule(user.matricule)
                user.save()
            
            # Authentifier l'utilisateur
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                request.session['login_error'] = "Mot de passe incorrect."
        except User.DoesNotExist:
            request.session['login_error'] = "Matricule inconnu."
        
        return redirect('main')
    
    return redirect('main')


def signup_view(request):
    """Vue pour gérer l'inscription des utilisateurs."""
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        matricule = request.POST.get('matricule')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Vérifier que les mots de passe correspondent
        if password != password_confirm:
            request.session['signup_error'] = "Les mots de passe ne correspondent pas."
            return redirect('main')
        
        # Vérifier que le matricule a le bon format
        if not matricule.isdigit() or len(matricule) != 7:
            request.session['signup_error'] = "Le matricule doit contenir exactement 7 chiffres."
            return redirect('main')
        
        # Vérifier que le matricule n'est pas déjà utilisé
        if User.objects.filter(matricule=matricule).exists():
            request.session['signup_error'] = "Ce matricule est déjà utilisé."
            return redirect('main')
        
        # Créer l'utilisateur
        try:
            username = f"user_{matricule}"  # Générer un nom d'utilisateur unique
            
            # Créer l'utilisateur avec le rôle détecté automatiquement
            user = User.objects.create(
                username=username,
                last_name=last_name,
                matricule=matricule,
                password=make_password(password)  # Chiffrer le mot de passe
            )
            
            # Détecter et assigner le rôle automatiquement
            detected_role = user.detect_role_from_matricule()
            user.role = detected_role
            user.save()
            
            # Connecter automatiquement l'utilisateur après l'inscription
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        except Exception as e:
            request.session['signup_error'] = f"Erreur lors de l'inscription: {str(e)}"
        
        return redirect('main')
    
    return redirect('main')


def logout_view(request):
    """Vue pour déconnecter l'utilisateur."""
    logout(request)
    return redirect('main')


@login_required
def account_options_view(request):
    """Vue pour afficher les options du compte."""
    user = request.user
    
    # Récupérer les statistiques
    ksat_saves = UserSavedData.objects.filter(user=user, key__startswith='ksat_').count()
    general_saves = UserSavedData.objects.filter(user=user).exclude(key__startswith='ksat_').count()
    
    # Récupérer le numéro de poste actuel (depuis localStorage côté client)
    current_job_number = request.session.get('current_job_number', 'Non défini')
    
    context = {
        'user': user,
        'ksat_saves': ksat_saves,
        'general_saves': general_saves,
        'current_job_number': current_job_number,
    }
    
    return render(request, 'web_app/auth/account_options.html', context)


@login_required
def change_password_view(request):
    """Vue pour changer le mot de passe."""
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Vérifier l'ancien mot de passe
        if not request.user.check_password(current_password):
            return JsonResponse({'success': False, 'message': 'Mot de passe actuel incorrect.'})
        
        # Vérifier que les nouveaux mots de passe correspondent
        if new_password != confirm_password:
            return JsonResponse({'success': False, 'message': 'Les nouveaux mots de passe ne correspondent pas.'})
        
        # Changer le mot de passe
        request.user.set_password(new_password)
        request.user.save()
        
        # Reconnecter l'utilisateur
        user = authenticate(username=request.user.username, password=new_password)
        if user is not None:
            login(request, user)
        
        return JsonResponse({'success': True, 'message': 'Mot de passe changé avec succès.'})
    
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'})


@login_required
def delete_account_view(request):
    """Vue pour supprimer le compte."""
    if request.method == 'POST':
        confirm_password = request.POST.get('confirm_password')
        
        # Vérifier le mot de passe
        if not request.user.check_password(confirm_password):
            return JsonResponse({'success': False, 'message': 'Mot de passe incorrect.'})
        
        # Supprimer l'utilisateur
        user_matricule = request.user.matricule
        request.user.delete()
        
        return JsonResponse({
            'success': True, 
            'message': f'Compte supprimé avec succès. Le matricule {user_matricule} reste disponible pour une nouvelle inscription.'
        })
    
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'})
