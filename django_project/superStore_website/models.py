from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

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

    def __str__(self):
        return self.item_name

class Cart(models.Model):
    STATES = (
        ('AL','AL'), ('AK','AK'), ('AZ','AZ'), ('AR','AR'), ('CA','CA'), ('CO','CO'), ('CT','CT'), 
        ('DE','DE'), ('FL','FL'), ('GA','GA'), ('HI','HI'), ('ID','ID'), ('IL','IL'), ('IN','IN'),
        ('IA','IA'), ('KS','KS'), ('KY','KY'), ('LA','LA'), ('ME','ME'), ('MD','MD'), ('MA','MA'), 
        ('MI','MI'), ('MN','MN'), ('MS','MS'), ('MO','MO'), ('MT','MT'), ('NE','NE'), ('NV','NV'), 
        ('NH','NH'), ('NJ','NJ'), ('NM','NM'), ('NY','NY'), ('NC','NC'), ('ND','ND'), ('OH','OH'),
        ('OK','OK'), ('OR','OR'), ('PA','PA'), ('RI','RI'), ('SC','SC'), ('SD','SD'), ('TN','TN'),
        ('TX','TX'), ('UT','UT'), ('VT','VT'), ('VA','VA'), ('WA','WA'), ('WV','WV'), ('WI','WI'),
        ('WY','WY'),
    )

    COUNTRY = (
        ('United States','United States'),
    )

    PAYMENT_TYPE = (
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
    )

    first_name = models.CharField(max_length=80)
    last_name  = models.CharField(max_length=80)
    user_name  = models.CharField(max_length=80)
    email      = models.CharField(max_length=80)
    street     = models.CharField(max_length=100)
    country    = models.CharField(max_length=20, choices=COUNTRY, default='Choose')
    state      = models.CharField(max_length=2, choices=STATES, default='State')
    zipCode    = models.IntegerField()
    nameOnCd   = models.CharField(max_length=160)
    cardNum    = models.IntegerField()
    expireDt   = models.IntegerField()
    cvv        = models.CharField(max_length=5)