from django import forms
from django.forms.widgets import RadioSelect

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
        ('Credit/Debit Card', 'Credit/Debit Card'),
        ('PayPal', 'PayPal'),
        ('Store Credit', 'Store Credit'),
    )
    DELIVERY_TYPE = (
        ('Quick Delivery', 'Quick Delivery'),
        ('No Rush', 'No Rush'),
    )
    first_name = forms.CharField(max_length=80)
    last_name  = forms.CharField(max_length=80)
    email      = forms.CharField(max_length=80)
    address    = forms.CharField(max_length=100)
    altaddress = forms.CharField(max_length=100, required=False)
    country    = forms.ChoiceField(choices=COUNTRY)
    state      = forms.ChoiceField(choices=STATES)
    zipCode    = forms.CharField(max_length=20)
    paymentType  = forms.ChoiceField(choices=PAYMENT_TYPE,widget=forms.RadioSelect())
    nameOnCd    = forms.CharField(max_length=160)
    cardNum     = forms.CharField(max_length=20)
    expireDt    = forms.CharField(max_length=6)
    cvv         = forms.CharField(max_length=6)
    shipAddLine_one = forms.CharField(max_length=100)
    shipAddLine_two = forms.CharField(max_length=100, required=False)
    shipCountry = forms.ChoiceField(choices=COUNTRY)
    shipState   = forms.ChoiceField(choices=STATES)
    shipZipCode = forms.CharField(max_length=20)
    deliveryOpt = forms.ChoiceField(choices=DELIVERY_TYPE, widget=RadioSelect())