from django import forms
from .models import Annonce
from django.contrib.auth.models import User
from .models import Locataire
from .models import Proprietaire

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre', 'description', 'prix','adresse','image']
        widgets = {
            'image': forms.FileInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Requis. Entrez une adresse email valide.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Requis.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requis.')
    
    # Choix de type d'utilisateur
    USER_TYPE_CHOICES = [
        ('locataire', 'Je suis locataire'),
        ('proprietaire', 'Je suis propriétaire'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type')





    