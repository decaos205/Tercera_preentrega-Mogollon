from django.shortcuts import render
from aplicacion.forms import *
from aplicacion.models import *

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView

# Create your views here.

#_______________________________________________________________________________ Menú Principal
def home(request):
    return render(request, 'aplicacion/index.html')

#_______________________________________________________________________________ Buscar

def buscarLibros(request):
    return render(request, 'aplicacion/buscar.html')

def encontrarLibros(request):
    if request.GET['buscar']:
        patron=request.GET['buscar']
        libros=Libro.objects.filter(titulo__icontains=patron)
        contexto={'libros':libros}
        return render(request, 'aplicacion/libro_list.html', contexto)
    
    contexto={'libros':Libro.objects.all()}
    return render(request, 'aplicacion/buscar.html', contexto)


#___________________________________________________________________________ Usuarios

def usuario(request):
    contexto = {'usuarios': Usuario.objects.all()}
    
    return  render(request, 'aplicacion/usuarios.html', contexto)

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get('nombre')
            usuario_apellido = miForm.cleaned_data.get('apellido')
            usuario_email = miForm.cleaned_data.get('email')
            usuario_edad = miForm.cleaned_data.get('edad')

            usuario = Usuario(nombre=usuario_nombre, 
                              apellido=usuario_apellido, 
                              email=usuario_email, 
                              edad=usuario_edad)
            usuario.save()

            contexto = {'usuarios': Usuario.objects.all()}

            return render(request, 'aplicacion/usuarios.html', contexto)

    else:
        miForm = UsuarioForm()
    
    return render(request, 'aplicacion/usuariosForm.html', {'miForm': miForm})

#______________________________________________________________________________ Libros

class LibroList(ListView):
    model = Libro

class LibroCreate(CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'editorial']
    success_url = reverse_lazy('libros')

#_______________________________________________________________________________ Comentarios
    
class ComentarioList(ListView):
    model = Comentario

class ComentarioCreate(CreateView):
    model = Comentario
    fields = ['usuario', 'comentario']
    success_url = reverse_lazy('comentarios')

