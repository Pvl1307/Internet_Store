import json

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    category_file = f'{BASE_DIR}/categories_data.json'
    product_file = f'{BASE_DIR}/products_data.json'

    @staticmethod
    def json_read_categories():
        with open(Command.category_file, 'r', encoding='windows-1251') as f:
            categories_list = json.load(f)
        return categories_list

    @staticmethod
    def json_read_products():
        with open(Command.product_file, 'r', encoding='windows-1251') as f:
            product_list = json.load(f)
        return product_list

    def handle(self, *args, **options):

        Product.objects.all().delete()
        product_for_create = []

        Category.objects.all().delete()
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name_of_category=category['fields']['name_of_category'],
                         description_of_category=category['fields']['description_of_category'])
            )

        Category.objects.bulk_create(category_for_create)
        pk_step = len(Command.json_read_categories())

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name_of_product=product['fields']['name_of_product'],
                        description_of_product=product['fields']['description_of_product'],
                        category_of_product=Category.objects.get(pk=product['fields']['category_of_product'] + pk_step),
                        price_of_product=product['fields']['price_of_product'])
            )

        Product.objects.bulk_create(product_for_create)

