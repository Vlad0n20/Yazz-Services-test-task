from django.db import models

from apps.shop.models import Shop
from apps.product.services import get_product_photo_upload_path


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва категорії')
    for_shop_type = models.CharField(max_length=20, choices=Shop.ShopTypeChoices.choices,
                                     verbose_name='Для типу магазину')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(null=True, blank=True, verbose_name='Опис')
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name='Магазин'
    )
    categories = models.ManyToManyField(Category, verbose_name='Категорії')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна (грн)')
    weight = models.FloatField(null=True, blank=True, verbose_name='Вага')
    keywords = models.TextField(null=True, blank=True, verbose_name='Ключові слова')

    def get_category_choices(self):
        return Category.objects.filter(for_shop_type=self.shop.type).values_list('name', flat=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ['name']


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos', verbose_name='Продукт')
    photo = models.ImageField(upload_to=get_product_photo_upload_path, verbose_name='Фото')

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Фото продукту'
        verbose_name_plural = 'Фото продуктів'
