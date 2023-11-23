from decimal import Decimal

from django.core.management import BaseCommand

from doors.models import Door


class Command(BaseCommand):
    help = 'Update product prices by applying a percentage increase'

    def add_arguments(self, parser):
        parser.add_argument('door', type=int, help='Door Id')
        parser.add_argument('percentage_increase', type=float, help='Percentage increase for product prices')

    def handle(self, *args, **options):
        percentage_increase = options['percentage_increase']
        door_id = options['door']

        if percentage_increase <= 0:
            self.stdout.write(self.style.ERROR('Percentage increase should be a positive number.'))
            return

        try:
            product = Door.objects.get(pk=door_id)
            updated_products = 0
            updated_price = product.price * Decimal(1 + percentage_increase / 100)
            product.price = updated_price
            product.save()
            updated_products += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully updated price for {product.title}.'))
            self.stdout.write(self.style.SUCCESS(f'New price: {product.price}.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
