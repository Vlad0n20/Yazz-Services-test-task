import graphene
from django.db.models import Prefetch, F
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
    # in these next two fields you can see the name of the store and the name of the category
    # in graphql for the most expensive products in the store and category
    shop_name = graphene.String()
    category_name = graphene.String()

    class Meta:
        model = Product
        fields = '__all__'

    def resolve_shop(self, info):
        return self.shop

    def resolve_categories(self, info):
        return self.categories.all()


class Query(graphene.ObjectType):
    cheapest_products_in_shop = graphene.List(ProductType)

    def resolve_cheapest_products_in_shop(self, info, **kwargs):
        expensive_products = []
        unique_shop_category_pairs = Product.objects.prefetch_related(
            Prefetch('categories', queryset=Category.objects.all())
        ).values_list('shop_id', 'categories__id')
        for shop_id, category_id in set(unique_shop_category_pairs):
            expensive_product = Product.objects.filter(
                shop_id=shop_id,
                categories__id=category_id
            ).annotate(
                shop_name=F('shop__name'),
                category_name=F('categories__name')
            ).order_by('-price').first()
            if expensive_product:
                expensive_products.append(expensive_product)
        return expensive_products


schema = graphene.Schema(query=Query)
