from django import forms

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
    #user_name  = forms.CharField(max_length=80)
    #email      = forms.CharField(max_length=80)
    #street     = forms.CharField(max_length=100)
    #country    = forms.CharField(max_length=20, choices=COUNTRY, default='Choose')
    #state      = forms.CharField(max_length=2, choices=STATES, default='State')
    #zipCode    = forms.IntegerField()
    #paymentTyp = forms.ChoiceField(choices=PAYMENT_TYPE, widget=forms.RadioSelect)
    #nameOnCd   = forms.CharField(max_length=160)
    #cardNum    = forms.IntegerField()
    #expireDt   = forms.IntegerField()
    #cvv        = forms.CharField(max_length=5)