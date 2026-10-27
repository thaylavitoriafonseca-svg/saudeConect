from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Personal(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='personal')
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)