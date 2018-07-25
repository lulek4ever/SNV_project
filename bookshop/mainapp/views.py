from django.shortcuts import render
from book.models import Book
from category.models import Category


bestsellers = Book.objects.all()
new_books = Book.objects.all()
links_menu = Category.objects.all()


# links_menu = [{'href': 'philosophy', 'name': 'Фислософия'},
#                {'href': 'economics', 'name': 'Экономика'},
#                {'href': 'anthropology', 'name': 'Антропология'},
#                {'href': 'history', 'name': 'История'},
#                {'href': 'student_books', 'name': 'Учебные пособия'},
#                {'href': 'detectives', 'name': 'Детективы'}]


def index_view(request):

    return render(request, 'mainapp/index.html', {'content': [bestsellers, new_books, links_menu]})


def contacts_view(request):

    return render(request, 'mainapp/contacts.html', {'content': [bestsellers, new_books, links_menu]})
