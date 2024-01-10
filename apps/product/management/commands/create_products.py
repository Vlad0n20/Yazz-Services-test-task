from django.core.management.base import BaseCommand, CommandError
from apps.product.models import Product
from apps.product.factories import ProductFactory, ProductFactoryWithoutCreatingNewShop
from apps.shop.models import Category


class Command(BaseCommand):
    help_text = "Generate new products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            help="Indicates the number of products to be created",
        )
        parser.add_argument(
            "--without-creating-new-shop",
            action="store_true",
            help="Indicates whether to create a new shop or not",
        )
        parser.add_argument(
            "--without-creating-new-category",
            action="store_true",
            help="Indicates whether to create a new category or not",
        )

    def handle(self, *args, **options):
        for i in range(options["count"]):
            if options["without_creating_new_shop"] and options["without_creating_new_category"]:
                categories = Category.objects.all().order_by('?')[:3]
                product = ProductFactoryWithoutCreatingNewShop(categories=categories)
            elif options["without_creating_new_category"]:
                categories = Category.objects.all()[:3]
                product = ProductFactory(categories=categories)
            elif options["without_creating_new_shop"]:
                product = ProductFactoryWithoutCreatingNewShop()
            else:
                product = ProductFactory()
            self.stdout.write(
                self.style.WARNING(
                    f"Product {product.name} was created successfully!"
                )
            )
