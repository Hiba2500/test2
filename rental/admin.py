from django.contrib import admin

# Register your models here.
from .models import Annonce
from .models import Locataire
from .models import Proprietaire
admin.site.register(Annonce)
admin.site.register(Locataire)
admin.site.register(Proprietaire)