from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:pk>/', views.add_to_basket, name='add'),
    url('', views.basket, name='basket_view')
]