from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    edad = forms.IntegerField(required=True)

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=50, required=True)
    editorial = forms.CharField(max_length=50, required=True)

class comentarioForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True)
    comentario = forms.CharField(max_length=100, required=True)
    