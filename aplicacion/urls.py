from django.urls import path, include
from aplicacion.views import *

#Menú Principal
urlpatterns = [
    path('', home, name='home'),
    path('usuarios/', usuario, name='usuarios'),

    #Formularios
    path('usuario_form/', usuarioForm, name='usuario_form'),
]


