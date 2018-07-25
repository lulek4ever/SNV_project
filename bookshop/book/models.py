from django.db import models


class Book(models.Model):

    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.IntegerField()
    page_amount = models.IntegerField(null=True)
    publisher = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='.')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

