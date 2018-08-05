import json
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from . import models


def api_product_list(request):

    query = get_list_or_404(models.Book)

    data = list(map(lambda itm: {
        'id': itm.id,
        'name': itm.name,
        'author': itm.author,
        'price': float(itm.price),
        'page_amount': itm.page_amount,
        'publisher': itm.publisher,
        'description': itm.description,
        'image': itm.image.name
        }, query))

    context = json.dumps({'results': data})

    return HttpResponse(context)

