from django.contrib import admin
from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'quantity']


admin.site.register(Basket, BasketAdmin)

# Register your models here.
