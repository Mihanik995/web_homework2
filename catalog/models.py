from django.db import models

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
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.price} RUB)'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Publication(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='text')
    preview = models.ImageField(upload_to='catalog/', verbose_name='preview', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    views = models.IntegerField(verbose_name='views', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'notes'
