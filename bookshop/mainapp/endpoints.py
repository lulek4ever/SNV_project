import json
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookModelSet(ModelViewSet):

    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filter_fields = ('category', )
    search_fields = ('name', 'author', 'description')


# def api_product_list(request):
#
#     query = get_list_or_404(models.Book)
#
#     serializer = serializers.BookSerializer(query, many=True)
#
#
#     data = list(map(lambda itm: {
#         'id': itm.id,
#         'name': itm.name,
#         'author': itm.author,
#         'price': float(itm.price),
#         'page_amount': itm.page_amount,
#         'publisher': itm.publisher,
#         'description': itm.description,
#         'image': itm.image.name
#         }, query))
#
#     context = json.dumps({'results': data})
#
#     context = json.dumps({'results': serializer.data})
#
#
#     return HttpResponse(context)
#
