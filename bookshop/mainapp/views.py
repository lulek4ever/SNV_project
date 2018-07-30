from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Book
from .models import Category


bestsellers = get_list_or_404(Book)
new_books = get_list_or_404(Book)
links_menu = get_list_or_404(Category)


def index_view(request):

    return render(request, 'mainapp/index.html', {'content': [bestsellers, new_books, links_menu]})


def contacts_view(request):

    return render(request, 'mainapp/contacts.html', {'content': [bestsellers, new_books, links_menu]})


# moved from book.app

def product_view(request, pk=None):
    book = get_object_or_404(Book, id=pk)
    similar_books = get_list_or_404(Book)

    return render(request, 'mainapp/product.html', {'content': [book, similar_books, links_menu]})

