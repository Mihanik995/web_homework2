from django.db import models

class Category(models.Model):
    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
