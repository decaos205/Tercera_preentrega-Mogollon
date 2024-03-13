from django.shortcuts import render
from aplicacion.forms import *
from aplicacion.models import *

# Create your views here.

def home(request):
    return render(request, 'aplicacion/index.html')

def usuario(request):
    contexto = {'usuarios': Usuario.objects.all()}
    return  render(request, 'aplicacion/usuarios.html', contexto)

#_______ Forms

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get('nombre')
            usuario_apellido = miForm.cleaned_data.get('apellido')
            usuario_email = miForm.cleaned_data.get('email')
            usuario_edad = miForm.cleaned_data.get('edad')

            usuario = Usuario(nombre=usuario_nombre, apellido=usuario_apellido, email=usuario_email, edad=usuario_edad)
            usuario.save()

            contexto = {'usuario': Usuario.objects.all()}

            return render(request, 'aplicacion/usuarios.html', contexto)

    else:
        miForm = UsuarioForm()

    
    return render(request, 'aplicacion/usuariosForm.html', {'miForm': miForm})
