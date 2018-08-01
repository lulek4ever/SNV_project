from django.conf.urls import url
from . import views

app_name = 'basketapp'

urlpatterns = [
    url('', views.basket, name='basket_view'),
    url('add/<int:pk>/', views.add_to_basket, name='add')
]