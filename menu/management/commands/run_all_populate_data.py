from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs all populate_data commands in sequence'

    def handle(self, *args, **kwargs):
        for i in range(14):
            try:
                call_command(f'populate_data_{i}')
                self.stdout.write(self.style.SUCCESS(f'Successfully ran populate_data_{i}'))
            except CommandError as e:
                self.stdout.write(self.style.ERROR(f'Error running populate_data_{i}: {e}'))
