from django.core.management.base import BaseCommand, CommandError

from apps.shop.factories import CategoryFactory


class Command(BaseCommand):
    help_text = 'Create new categories'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            help='Indicates the number of categories to be created',
        )

    def handle(self, *args, **options):
        for i in range(options['count']):
            category = CategoryFactory()
            self.stdout.write(
                self.style.WARNING(
                    f'Category {category.name} was created successfully!'
                )
            )