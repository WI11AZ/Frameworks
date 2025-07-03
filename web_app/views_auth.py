from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models.user import User


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
            User.objects.create(
                username=username,
                last_name=last_name,
                matricule=matricule,
                password=make_password(password)  # Chiffrer le mot de passe
            )
            
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
