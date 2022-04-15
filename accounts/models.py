from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtension(models.Model):
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    more_description = models.TextField(max_length=150)