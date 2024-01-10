import factory.django
from faker import Faker

from apps.shop.models import Shop, Category

fake = Faker("uk_UA")


class CategoryFactory(factory.django.DjangoModelFactory):
    name = fake.word()
    for_shop_type = fake.random_element(elements=Shop.ShopTypeChoices.choices)[0]

    class Meta:
        model = Category


class ShopFactory(factory.django.DjangoModelFactory):
    name = fake.company()
    type = fake.random_element(elements=Shop.ShopTypeChoices.choices)[0]
    latitude = fake.latitude()
    longitude = fake.longitude()
    sales_commission = fake.random_int(min=0, max=30)

    class Meta:
        model = Shop
