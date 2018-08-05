from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'basketapp'


urlpatterns = [
    path('add/<int:pk>/', views.add_to_basket, name='add'),
    path('remove/<int:pk>/', views.remove_from_basket, name='remove'),
    url('', views.basket, name='basket_view'),
]
