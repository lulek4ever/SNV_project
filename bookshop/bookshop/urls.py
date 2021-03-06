"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import index_view
from mainapp.views import contacts_view
from mainapp.views import product_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from mainapp.endpoints import BookModelSet

router = DefaultRouter()
router.register('books', BookModelSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    # path('book/', product_view, name='product'),
    path('', include('mainapp.urls')),
    path('contacts/', contacts_view, name='contacts'),
    url('auth/', include('authapp.urls', namespace='auth')),
    url('orders/', include('basketapp.urls', namespace='orders')),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
