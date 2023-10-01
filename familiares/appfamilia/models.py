from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    
class Hijo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Representante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    FechaDeEntrega = models.DateField()
    email = models.EmailField()
    entregado = models.BooleanField()
    