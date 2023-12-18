from django.db import models


class Shop(models.Model):
    class ShopTypeChoices(models.TextChoices):
        SPORT = 'sport', 'Sport'
        FOOD = 'food', 'Food'
        ELECTRONICS = 'electronics', 'Electronics'

    name = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(null=True, blank=True, verbose_name='Опис')
    shop_type = models.CharField(max_length=20, choices=ShopTypeChoices, verbose_name='Тип')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Довгота')
    sales_commission = models.SmallIntegerField(default=0, verbose_name='Комісія з продажів (відсоток)')
