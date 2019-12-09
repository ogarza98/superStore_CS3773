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


class OrderItem(models.Model):
    product = models.OneToOneField(Good, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return self.date_order
