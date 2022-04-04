from django import forms
from . import models

class PageForm(forms.ModelForm):
    class Meta:
        model = models.Page
        fields = ['title', 'subtitle', 'author', 'image_page', 'content']
        