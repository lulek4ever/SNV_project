from django.core.management.base import BaseCommand
from mainapp.models import Category, Book
from authapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        books = loadFromJSON('books')

        Book.objects.all().delete()
        for book in books:
            category_name = book['category']

            _category = Category.objects.get(name=category_name)
            book['category'] = _category
            new_book = Book(**book)
            new_book.save()

        ShopUser.objects.all().delete()
        super_user = ShopUser.objects.create_superuser('lulik', 'lulik@bookshop.ru', 'luliksuperuser', age=30)
