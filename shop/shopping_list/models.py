from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Shopping(models.Model):
    name = models.CharField(max_length=100)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shopping_list:index')

    def __str__(self):
        return self.name


class ShopItems(models.Model):
    items = models.CharField(max_length=100)
    shopping_title = models.ForeignKey(Shopping, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shopping_list:index')

    def __str__(self):
        return self.items
