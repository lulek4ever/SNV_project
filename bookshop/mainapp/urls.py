from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:pk>/', views.product_view, name='detail')
]
