from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None

    avatar = models.ImageField(upload_to='users/', verbose_name='avatar')
    phone = models.IntegerField(verbose_name='phone number')
    country = models.CharField(max_length=50, verbose_name='country')

    email = models.EmailField(verbose_name='e-mail', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
