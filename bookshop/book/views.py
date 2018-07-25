from django.shortcuts import render
from .models import Book
from category.models import Category

book = Book.objects.get(author="Silvia Federici")
similar_books = Book.objects.all()
links_menu = Category.objects.all()

# links_menu = [{'href': 'philosophy', 'name': 'Фислософия'},
#                {'href': 'economics', 'name': 'Экономика'},
#                {'href': 'anthropology', 'name': 'Антропология'},
#                {'href': 'history', 'name': 'История'},
#                {'href': 'student_books', 'name': 'Учебные пособия'},
#                {'href': 'detectives', 'name': 'Детективы'}]


def product_view(request):

    return render(request, 'book/product.html', {'content': [book, similar_books, links_menu]})

print(links_menu)
