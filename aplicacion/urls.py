from django.urls import path, include
from aplicacion.views import *


#Menú Principal
urlpatterns = [
    path('', home, name='home'),
    path('usuarios/', usuario, name='usuarios'),

    #___________ Usuarios
    path('usuario_form/', usuarioForm, name='usuarios_form'),

    #___________ Libros
    path('libros/', LibroList.as_view(), name='libros'),
    path('lib_create/', LibroCreate.as_view(), name='lib_create'),

    #___________ Comentarios
    path('comentarios/', ComentarioList.as_view(), name='comentarios'),
    path('comm_create/', ComentarioCreate.as_view(), name='comm_create'),

    #___________Busqueda
    path('buscar_libros/', buscarLibros, name='buscar_libros'),
    path('encontrar_libros/', encontrarLibros, name='encontrar_libros')
]


