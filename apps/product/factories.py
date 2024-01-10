import factory.django
from faker import Faker

from apps.shop.factories import ShopFactory, CategoryFactory
from apps.product.models import Product
from apps.shop.models import Shop, Category

fake = Faker("uk_UA")


class ProductFactory(factory.django.DjangoModelFactory):
    name = fake.word()
    description = fake.text()
    shop = factory.SubFactory(ShopFactory)
    price = fake.random_int(min=1, max=1000)
    weight = fake.pydecimal(left_digits=2, right_digits=2)
    keywords = fake.text()

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
        else:
            for _ in range(1, fake.random_int(min=1, max=4)):
                self.categories.add(CategoryFactory.create())

    class Meta:
        model = Product


class ProductFactoryWithoutCreatingNewShop(ProductFactory):
    shop = factory.Iterator(Shop.objects.all())
