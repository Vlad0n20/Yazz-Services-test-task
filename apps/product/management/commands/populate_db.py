from django.core.management.base import BaseCommand, CommandError

from apps.populate_db import populate_db


class Command(BaseCommand):
    help_text = "Populate database with new data"

    def handle(self, *args, **options):
        try:
            populate_db()
        except Exception as e:
            raise CommandError(e)
        self.stdout.write(
            self.style.WARNING(
                f"Database was populated successfully!"
            )
        )
