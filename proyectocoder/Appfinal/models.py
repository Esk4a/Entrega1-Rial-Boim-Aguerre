from django.db import models

# Create your models here.


class Peliculas(models.Model):
    titulo = models.CharField(max_length=40)
    duracion = models.IntegerField()
    emision = models.DateField()

class Sucursales(models.Model):
    ciudad = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()

class Contactos(models.Model):
    social = models.CharField(max_length=40)
    Telefono = models.IntegerField()
    