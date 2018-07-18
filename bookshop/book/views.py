from django.shortcuts import render


def product_view(request):

    return render(request, 'book/product.html')

# Create your views here.
