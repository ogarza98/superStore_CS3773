from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Good(models.Model):
    ITEM_FRESHNESS = (
        ('G', 'GOOD'),
        ('N', 'NEW'),
        ('B', 'BAD'),
    )

    item_name = models.CharField(max_length=50)
    freshness = models.CharField(max_length=1, choices=ITEM_FRESHNESS)
    item_stock = models.IntegerField()
    price = models.FloatField()
    goods_image = models.ImageField(null=True, blank=True, upload_to="goods_image")
    description = models.CharField(max_length=280)

    def __str__(self):
        return self.item_name

class Cart(models.Model):

    prodcuts = models.

    def __str__self(self):
        return self.products