from django.db import models
from django.conf import settings
from mainapp.models import Book


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def _get_product_price(self):
        return self.book.price * self.quantity

    product_price = property(_get_product_price)

    def _get_total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))

        return _totalquantity

    total_quantity = property(_get_total_quantity)

    def _get_total_price(self):
        _items = Basket.objects.filter(user=self.user)
        _totalprice = sum(list(map(lambda x: x.product_price, _items)))
        return _totalprice

    total_price = property(_get_total_price)






# Create your models here.
