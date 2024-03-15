from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.IntegerField()

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)

class Comentario(models.Model):
    usuario = models.CharField(max_length=50)
    comentario = models.CharField(max_length=50)