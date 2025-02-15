from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class VideoJuegos(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=20)
    divertido = models.BooleanField()
    contenido = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre}'


class Peliculas(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    divertida = models.BooleanField()

    def __str__(self):
        return f'{self.nombre}'


class Series(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    divertida = models.BooleanField()

    def __str__(self):
        return f'{self.nombre}'