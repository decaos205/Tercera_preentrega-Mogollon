from django.contrib import admin
from aplicacion.models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Comentario)