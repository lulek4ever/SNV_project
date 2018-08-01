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


# Create your models here.
