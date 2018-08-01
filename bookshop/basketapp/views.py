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

    else:
        new_basket_item = Basket(user=request.user, book=book)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

