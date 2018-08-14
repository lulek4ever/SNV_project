from django.urls import path
from . import views
from . import endpoints

app_name = 'product'

# endpoints = [
#     path('api/', endpoints.api_product_list, name='api_list'),
# ]

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:pk>/', views.product_view, name='detail')
]
