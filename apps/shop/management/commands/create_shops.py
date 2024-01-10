from django.core.management.base import BaseCommand, CommandError
from apps.shop.factories import ShopFactory, CategoryFactory


class Command(BaseCommand):
    help_text = "Generate new shops"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            help="Indicates the number of products to be created",
        )

    def handle(self, *args, **options):
        for i in range(options["count"]):
            shop = ShopFactory()
            self.stdout.write(
                self.style.WARNING(
                    f"Shop {shop.name} was created successfully!"
                )
            )
