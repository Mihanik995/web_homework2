# Generated by Django 5.0.3 on 2024-03-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
    ]