from django import forms
from django.forms.widgets import RadioSelect
from django.forms import widgets

class cart(forms.Form):
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

    first_name = forms.CharField(max_length=80)
    last_name  = forms.CharField(max_length=80)
    user_name  = forms.CharField(max_length=80)
    email      = forms.CharField(max_length=80)
    address    = forms.CharField(max_length=100)
    altaddress = forms.CharField(max_length=100, required=False)
    #country    = forms.CharField(max_length=20, choices=COUNTRY, default='Choose')
    #state      = forms.CharField(max_length=2, choices=STATES, default='State')
    paymentType = forms.ChoiceField(choices=PAYMENT_TYPE,widget=RadioSelect())
    zipCode     = forms.CharField(max_length=20)
    cardNum     = forms.CharField(max_length=20)
    expireDt    = forms.CharField(max_length=6)
    cvv         = forms.CharField(max_length=6)