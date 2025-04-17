from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import AnnonceForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecter l'utilisateur immédiatement après l'inscription
            return redirect('home')  # Rediriger vers une page d'accueil
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def locations(request):
    # Afficher les maisons disponibles
    return render(request, 'locations.html')
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Annonce

@login_required
def annonces_list(request):
    # Vérifie si l'utilisateur fait partie du groupe "Locataire"
    if not request.user.groups.filter(name='Locataire').exists():
        return render(request, 'access_denied.html')  # Redirige vers une page d'erreur si l'utilisateur n'est pas locataire

    # Récupère les annonces disponibles
    annonces = Annonce.objects.filter(is_available=True)
    return render(request, 'annonces_list.html', {'annonces': annonces})
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        # Formulaire de connexion
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Si l'utilisateur est un locataire, le rediriger vers la liste des annonces
            if user.groups.filter(name='Locataire').exists():
                return redirect('annonces_list')  # Redirige vers la page des annonces
            else:
                return redirect('home')  # Redirige vers une page par défaut pour les autres utilisateurs (comme les propriétaires ou admins)
        else:
            # Rediriger en cas d'échec de l'authentification
            return redirect('login')
    
    return render(request, 'registration/login.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Annonce

@login_required
def annonces_list(request):
    # Vérifie si l'utilisateur fait partie du groupe "Locataire"
    if not request.user.groups.filter(name='Locataire').exists():
        return render(request, 'access_denied.html')  # Redirige vers une page d'erreur si l'utilisateur n'est pas locataire

    # Récupère les annonces disponibles
    annonces = Annonce.objects.filter(is_available=True)
    return render(request, 'annonces_list.html', {'annonces': annonces})
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        # Formulaire de connexion
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Si l'utilisateur est un locataire, le rediriger vers la liste des annonces
            if user.groups.filter(name='Locataire').exists():
                return redirect('annonces_list')  # Redirige vers la page des annonces
            else:
                return redirect('home')  # Redirige vers une page par défaut pour les autres utilisateurs (comme les propriétaires ou admins)
        else:
            # Rediriger en cas d'échec de l'authentification
            return redirect('login')
    
    return render(request, 'registration/login.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnnonceForm
from django.contrib.auth.models import Group

@login_required
def create_annonce(request):
    # Vérifier si l'utilisateur est un propriétaire
    if not request.user.groups.filter(name='Propriétaire').exists():
        return render(request, 'access_denied.html')  # Page d'accès refusé pour les non-propriétaires
    
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)
        form = AnnonceForm(request.POST)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.proprietaire = request.user  # L'utilisateur connecté devient le propriétaire de l'annonce
            annonce.save()
            return redirect('annonces_list')  # Rediriger vers la liste des annonces après la création
    else:
        form = AnnonceForm()

    return render(request, 'create_annonce.html', {'form': form})
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

def base_generic(request):
    return render(request, 'base_generic.html') 