import json

import graphene
from graphene_django.utils.testing import GraphQLTestCase
from django.test import TestCase

from apps.product.factories import ProductFactory
from apps.product.models import Product
from apps.product.schema import Query


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = ProductFactory()

    # Fields

    def test_it_has_name_field(self):
        self.assertEqual("Назва", self.product._meta.get_field("name").verbose_name)
        self.assertEqual("CharField", self.product._meta.get_field("name").get_internal_type())
        self.assertEqual(255, self.product._meta.get_field("name").max_length)

    def test_it_has_description_field(self):
        self.assertEqual("Опис", self.product._meta.get_field("description").verbose_name)
        self.assertEqual("TextField", self.product._meta.get_field("description").get_internal_type())
        self.assertEqual(True, self.product._meta.get_field("description").blank)

    def test_it_has_shop_field(self):
        self.assertEqual("Магазин", self.product._meta.get_field("shop").verbose_name)
        self.assertEqual("ForeignKey", self.product._meta.get_field("shop").get_internal_type())
        self.assertEqual("Shop", self.product._meta.get_field("shop").related_model.__name__)

    def test_it_has_categories_field(self):
        self.assertEqual("Категорії", self.product._meta.get_field("categories").verbose_name)
        self.assertEqual("ManyToManyField", self.product._meta.get_field("categories").get_internal_type())
        self.assertEqual("Category", self.product._meta.get_field("categories").related_model.__name__)

    def test_it_has_price_field(self):
        self.assertEqual("Ціна (грн)", self.product._meta.get_field("price").verbose_name)
        self.assertEqual("DecimalField", self.product._meta.get_field("price").get_internal_type())
        self.assertEqual(10, self.product._meta.get_field("price").max_digits)
        self.assertEqual(2, self.product._meta.get_field("price").decimal_places)

    def test_it_has_weight_field(self):
        self.assertEqual("Вага", self.product._meta.get_field("weight").verbose_name)
        self.assertEqual("FloatField", self.product._meta.get_field("weight").get_internal_type())
        self.assertEqual(True, self.product._meta.get_field("weight").null)
        self.assertEqual(True, self.product._meta.get_field("weight").blank)

    def test_it_has_keywords_field(self):
        self.assertEqual("Ключові слова", self.product._meta.get_field("keywords").verbose_name)
        self.assertEqual("TextField", self.product._meta.get_field("keywords").get_internal_type())
        self.assertEqual(True, self.product._meta.get_field("keywords").null)
        self.assertEqual(True, self.product._meta.get_field("keywords").blank)

    # Methods

    def test_method_str_working(self):
        self.assertEqual(self.product.name, str(self.product))

    def test_default_ordering(self):
        self.assertEqual(["name"], self.product._meta.ordering)

        products = [ProductFactory() for _ in range(10)]
        for index, product in enumerate(products):
            if index == 0:
                continue
            self.assertLessEqual(products[index - 1].name, product.name)


class ProductSchemaTestCase(TestCase):
    fixtures = ['shops.json', 'products.json']
    def setUp(self):
        super().setUp()
        self.query = '''
            query MyQuery {
              expansiveProductsInShop {
                id
                price
                shop {
                  name
                  type
                  id
                }
                categories {
                  name
                  id
                }
                name
                keywords
                description
                weight
              }
            }
            '''

    def test_expansive_products_in_shop_query(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        required_count = len(set(Product.objects.prefetch_related('categories').values_list('shop_id', 'categories__id')))

        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['expansiveProductsInShop']), required_count-1)
