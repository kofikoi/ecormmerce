from django.core.management.base import BaseCommand, CommandError
from orders.models import Vehicle, Details
import json
import sys

class Command(BaseCommand):
    help = 'Loads data from a JSON file into the Vehicle and Details models'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        json_file = options['json_file']
        try:
            with open(json_file) as f:
                data = json.load(f)
        except FileNotFoundError:
            raise CommandError(f'File not found: {json_file}')
        except json.JSONDecodeError:
            raise CommandError(f'Invalid JSON file: {json_file}')

        vehicles = {}
        count = 0
        total = len(data)
        for item in data:
            vehicle_name = item['Make'] + ' ' + item['Model']
            if vehicle_name not in vehicles:
                vehicles[vehicle_name] = Vehicle.objects.create(name=vehicle_name)

            Details.objects.create(
                year=int(item['Year']),
                vehicle=vehicles[vehicle_name],
                model=item['Model'],
                price=float(item['Price'])
            )

            count += 1
            progress = count / total * 100
            sys.stdout.write(f"\rProgress: {progress:.2f}%")
            sys.stdout.flush()

        self.stdout.write(self.style.SUCCESS('\nData loaded successfully.'))
