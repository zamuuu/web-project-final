from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    image_page = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    datetimecreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title