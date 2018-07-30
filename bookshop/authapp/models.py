from django.db import models
from django.contrib.auth.models import User, AbstractUser

class ShopUser(AbstractUser):
    userpic = models.ImageField(upload_to='userpics', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', null=True)

# Create your models here.
