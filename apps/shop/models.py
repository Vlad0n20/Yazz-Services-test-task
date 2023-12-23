from django.db import models


class Shop(models.Model):
    class ShopTypeChoices(models.TextChoices):
        SPORT = 'sport', 'Sport'
        FOOD = 'food', 'Food'
        ELECTRONICS = 'electronics', 'Electronics'

    name = models.CharField('Назва', max_length=255)
    description = models.TextField(blank=True, verbose_name='Опис')
    type = models.CharField('Тип', max_length=20, choices=ShopTypeChoices.choices)
    latitude = models.DecimalField('Широта', max_digits=9, decimal_places=6)
    longitude = models.DecimalField('Довгота', max_digits=9, decimal_places=6)
    sales_commission = models.SmallIntegerField('Комісія з продажів (відсоток)', default=0)

    def get_category_choices(self):
        return Category.objects.filter(for_shop_type=self.type)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазини'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=255)
    for_shop_type = models.CharField('Для типу магазину', max_length=20, choices=Shop.ShopTypeChoices.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']
