# Generated by Django 4.2 on 2023-12-19 13:32

import apps.product.services
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна (грн)')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Вага')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Ключові слова')),
                ('categories', models.ManyToManyField(to='shop.category', verbose_name='Категорії')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=apps.product.services.get_product_photo_upload_path, verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='product.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Фото продукту',
                'verbose_name_plural': 'Фото продуктів',
            },
        ),
    ]
