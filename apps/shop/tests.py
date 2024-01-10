from django.test import TestCase

from apps.shop.factories import ShopFactory, CategoryFactory
from apps.shop.models import Category, Shop


class ShopModelTestCase(TestCase):
    fixtures = ['shops.json']

    def setUp(self):
        self.shop = ShopFactory()

    # Fields

    def test_it_has_name_field(self):
        self.assertEqual("Назва", self.shop._meta.get_field("name").verbose_name)
        self.assertEqual("CharField", self.shop._meta.get_field("name").get_internal_type())
        self.assertEqual(255, self.shop._meta.get_field("name").max_length)

    def test_it_has_description_field(self):
        self.assertEqual("Опис", self.shop._meta.get_field("description").verbose_name)
        self.assertEqual("TextField", self.shop._meta.get_field("description").get_internal_type())
        self.assertEqual(True, self.shop._meta.get_field("description").blank)

    def test_it_has_type_field(self):
        self.assertEqual("Тип", self.shop._meta.get_field("type").verbose_name)
        self.assertEqual("CharField", self.shop._meta.get_field("type").get_internal_type())

    def test_it_has_latitude_field(self):
        self.assertEqual("Широта", self.shop._meta.get_field("latitude").verbose_name)
        self.assertEqual("DecimalField", self.shop._meta.get_field("latitude").get_internal_type())

    def test_it_has_longitude_field(self):
        self.assertEqual("Довгота", self.shop._meta.get_field("longitude").verbose_name)
        self.assertEqual("DecimalField", self.shop._meta.get_field("longitude").get_internal_type())

    def test_it_has_sales_commission_field(self):
        self.assertEqual("Комісія з продажів (відсоток)", self.shop._meta.get_field("sales_commission").verbose_name)
        self.assertEqual("SmallIntegerField", self.shop._meta.get_field("sales_commission").get_internal_type())

    # Methods

    def test_method_get_category_choices_working(self):
        count_categories = Category.objects.filter(for_shop_type=self.shop.type).count()
        self.assertEqual(count_categories, self.shop.get_category_choices().count())

    def test_method_str_working(self):
        self.assertEqual(self.shop.name, str(self.shop))

    def test_ordering(self):
        shops = Shop.objects.all()
        for index, shop in enumerate(shops):
            if index == 0:
                continue
            self.assertGreaterEqual(shop.name, shops[index - 1].name)


class CategoryModelTestCase(TestCase):
    fixtures = ['shops.json']

    def setUp(self):
        self.category = CategoryFactory()

    # Fields

    def test_it_has_name_field(self):
        self.assertEqual("Назва категорії", self.category._meta.get_field("name").verbose_name)
        self.assertEqual("CharField", self.category._meta.get_field("name").get_internal_type())
        self.assertEqual(255, self.category._meta.get_field("name").max_length)

    def test_it_has_for_shop_type_field(self):
        self.assertEqual("Для типу магазину", self.category._meta.get_field("for_shop_type").verbose_name)
        self.assertEqual("CharField", self.category._meta.get_field("for_shop_type").get_internal_type())

    # Methods

    def test_method_str_working(self):
        self.assertEqual(self.category.name, str(self.category))
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_ordering(self):
        categories = Category.objects.all()
        for index, category in enumerate(categories):
            if index == 0:
                continue
            self.assertGreaterEqual(category.name, categories[index - 1].name)
