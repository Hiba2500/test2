from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from .views import annonces_list
from . import views



urlpatterns = [
   
    path('home/', views.home, name='home'),
    path('base_generic/', views.base_generic, name='base_generic'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_annonce, name='create_annonce'),
    path('annonces/', views.annonces_list, name='annonces_list'),
]
# Ajout de la gestion des fichiers médias
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
