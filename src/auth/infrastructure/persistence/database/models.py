from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Prueba(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
