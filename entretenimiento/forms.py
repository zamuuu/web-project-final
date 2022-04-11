from django import forms
from ckeditor.fields import RichTextFormField

class VideoJuegosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=20)
    divertido = forms.BooleanField(required=False)
    contenido = RichTextFormField(required=False)

class VideoJuegosBusqueda(forms.Form):
    nombre = forms.CharField(max_length=40)

class PeliculasForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=20)
    divertida = forms.BooleanField(required=False)

class SeriesForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=20)
    divertida = forms.BooleanField(required=False)