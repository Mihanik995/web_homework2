from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.IntegerField(verbose_name='phone number', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)

    email = models.EmailField(verbose_name='e-mail', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
