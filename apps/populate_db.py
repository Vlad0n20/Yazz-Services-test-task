import random

from faker import Faker

from apps.product.models import Product, Category
from apps.shop.models import Shop

fake = Faker('uk_UA')


def creat_shop(count: int = 10):
    for _ in range(count):
        Shop.objects.create(
            name=fake.company(),
            type=fake.random_element(elements=Shop.ShopTypeChoices.choices)[0],
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            sales_commission=fake.random_int(min=0, max=30)
        )


def create_categories():
    data = {
        'sport': ['Зима', 'Літо', 'Футбол'],
        'food': ['Випічка', 'Солодощі', 'Алкоголь'],
        'electronics': ['Ноутбуки', 'Смартфони', 'Навушники']
    }
    for key, value in data.items():
        for item in value:
            Category.objects.create(
                name=item,
                for_shop_type=key
            )


def create_random_category(count: int = 10):
    for _ in range(count):
        Category.objects.create(
            name=fake.word(),
            for_shop_type=fake.random_element(elements=Shop.ShopTypeChoices.choices)[0]
        )


def create_product(count: int = 10):
    shops_list_ids = Shop.objects.values_list('id', flat=True)
    for _ in range(count):
        new_product = Product.objects.create(
            name=fake.word(),
            description=fake.text(),
            price=fake.random_int(min=1, max=1000),
            weight=fake.pydecimal(left_digits=2, right_digits=2),
            shop_id=fake.random_element(elements=shops_list_ids),
        )
        categories_list_ids = list(Category.objects.filter(for_shop_type=new_product.shop.type).values_list('id', flat=True))
        for i in random.sample(categories_list_ids, random.randint(1, 3)):
            new_product.categories.add(i)


def populate_db():
    creat_shop(5)
    create_categories()
    create_product(10)
