import graphene
from django.db import connection
from django.db.models import Prefetch, F, Max, Subquery, OuterRef, Q
from graphene_django import DjangoObjectType

from apps.product.models import Product
from apps.shop.models import Category, Shop


class ShopForProductType(DjangoObjectType):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'type')


class CategoryForProductType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductType(DjangoObjectType):
    shop = graphene.Field(ShopForProductType)
    categories = graphene.List(CategoryForProductType)

    class Meta:
        model = Product
        fields = '__all__'

    def resolve_shop(self, info):
        return self.shop

    def resolve_categories(self, info):
        return self.categories.all()


class Query(graphene.ObjectType):
    expansive_products_in_shop = graphene.List(ProductType)

    def resolve_expansive_products_in_shop(self, info, **kwargs):
        the_expensive_product_in_shop_and_category = Product.objects.prefetch_related('categories').filter(
            shop_id=OuterRef('shop_id'),
            categories__id=OuterRef('categories__id'),
        ).order_by('-price')[0:1]
        expansive_products_in_shop = Product.objects.filter(
            pk=Subquery(the_expensive_product_in_shop_and_category.values('id'))
        )
        return expansive_products_in_shop


schema = graphene.Schema(query=Query)
