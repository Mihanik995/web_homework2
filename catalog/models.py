from django.db import models
from datetime import datetime, timezone

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    description = models.TextField(verbose_name='description', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    description = models.TextField(verbose_name='description', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='image', **NULLABLE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='category')
    price = models.IntegerField(verbose_name='price')
    created_at = models.DateTimeField(verbose_name='created at', default=datetime.now(timezone.utc))
    updated_at = models.DateTimeField(verbose_name='updated at', default=datetime.now(timezone.utc))

    def __str__(self):
        return f'{self.name} ({self.price} RUB)'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
