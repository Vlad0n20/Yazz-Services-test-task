from django.db import models


class Shop(models.Model):
    class ShopTypeChoices(models.TextChoices):
        SPORT = 'sport', 'Sport'
        FOOD = 'food', 'Food'
        ELECTRONICS = 'electronics', 'Electronics'

    name = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(null=True, blank=True, verbose_name='Опис')
    type = models.CharField(max_length=20, choices=ShopTypeChoices.choices, verbose_name='Тип')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Довгота')
    sales_commission = models.SmallIntegerField(default=0, verbose_name='Комісія з продажів (відсоток)')

    def get_category_choices(self):
        return Category.objects.filter(for_shop_type=self.type).values_list('id', 'name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазини'
        ordering = ['name']


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
