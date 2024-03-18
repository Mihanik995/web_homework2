import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/catalog_data.json', 'rb') as file:
            return [item for item in json.load(file) if len(item['fields']) == 2]

    @staticmethod
    def json_read_products():
        with open('fixtures/catalog_data.json', 'rb') as file:
            return [item for item in json.load(file) if len(item['fields']) == 7]

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'], **category['fields'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product['fields']['category'] = Category.objects.get(pk=product['fields']['category'])
            product_for_create.append(
                Product(pk=product['pk'], **product['fields'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
