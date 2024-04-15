# Generated by Django 5.0.3 on 2024-04-15 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_publication_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(verbose_name='number')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('is_current_version', models.BooleanField(verbose_name='current version')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='product')),
            ],
            options={
                'verbose_name': 'version',
                'verbose_name_plural': 'versions',
            },
        ),
    ]
