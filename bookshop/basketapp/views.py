from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Basket
from mainapp.models import Book


@login_required
def basket(request):
    basket_items = Basket.objects.filter(user=request.user).order_by('book__category')
    return render(request, 'basketapp/basket.html', {'basket_items': basket_items})


@login_required
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


@login_required
def remove_from_basket(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

