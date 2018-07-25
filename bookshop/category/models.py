from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

# Create your models here.
