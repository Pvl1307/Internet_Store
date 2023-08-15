import json

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    file = f'{BASE_DIR}\data.json'

    @staticmethod
    def json_read():
        with open(Command.file, 'r', encoding='utf-8') as file:
            products = json.load(file)
        return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_for_create = []
        for product in Command.json_read():
            product_for_create.append(
                Product(name_of_product=product['fields']['name_of_product'],
                        description_of_product=product['fields']['description_of_product'],
                        category_of_product=Category.objects.get(pk=product['fields']['category_of_product']),
                        price_of_product=product['fields']['price_of_product'])
            )
        Product.objects.bulk_create(product_for_create)
