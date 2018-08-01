from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Basket
from mainapp.models import Book


def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)


def add_to_basket(request, pk):

    book = get_object_or_404(Book, id=pk)
    old_basket_item = Basket.objects.filter(user=request.user, book=book)

    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Create your views here.
