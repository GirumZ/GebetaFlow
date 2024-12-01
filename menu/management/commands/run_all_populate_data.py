from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs all populate_menu_item_ingredient commands in sequence'

    def handle(self, *args, **kwargs):
        for i in range(13):
            try:
                call_command(f'populate_menu_item_ingredient_{i}')
                self.stdout.write(self.style.SUCCESS(f'Successfully ran populate_menu_item_ingredient_{i}'))
            except CommandError as e:
                self.stdout.write(self.style.ERROR(f'Error running populate_data_{i}: {e}'))
