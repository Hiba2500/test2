# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Annonce(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    adresse = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='annonces/', null=True, blank=True)

    def __str__(self):
        return self.titre

class Locataire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True, null=True) 

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Proprietaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True, null=True) 
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"




