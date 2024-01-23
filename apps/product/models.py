import os
import json

from django.db import models

from apps.shop.models import Shop, Category
from apps.product.services import get_product_photo_upload_path


class Product(models.Model):
    name = models.CharField('Назва', max_length=255)
    description = models.TextField('Опис', blank=True)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name='Магазин'
    )
    categories = models.ManyToManyField(Category, verbose_name='Категорії')
    price = models.DecimalField('Ціна (грн)', max_digits=10, decimal_places=2)
    weight = models.FloatField('Вага', null=True, blank=True)
    keywords = models.TextField('Ключові слова', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ['name']


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos', verbose_name='Продукт')
    photo = models.ImageField('Фото', upload_to=get_product_photo_upload_path)

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Фото продукту'
        verbose_name_plural = 'Фото продуктів'
