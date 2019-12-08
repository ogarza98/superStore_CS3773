from .models import Good
from django.shortcuts import render
from django.http import HttpResponseRedirect
from superStore_website.forms import cart


def home(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)

def Cart(request):
    return render(request,'superStore_website/cart.html')

def receipt(request):
    if request.method == "POST":
        form = cart(request.POST)
        print(form.is_valid())
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            #print(fname)
            lname = form.cleaned_data['last_name']
            #print(lname)
            uname = form.cleaned_data['user_name']
            #print(uname)
            email = form.cleaned_data['email']
            #print(email)
            address    = form.cleaned_data['address']
            altaddress = form.cleaned_data['altaddress']
            nameOnCd   = form.cleaned_data['nameOnCd']
            cardNum    = form.cleaned_data['cardNum']
            expireDt   = form.cleaned_data['expireDt']
            cvv        = form.cleaned_data['cvv']
            cardType   = request.POST['paymentMethod']
            print(cardType)
            return render(request,'superStore_website/receipt.html',{"firstName": fname, "lastName": lname,
                          "userName": uname, "email": email, "address": address, "altaddress": altaddress,
                          "nameOnCd": nameOnCd, "cardNum": cardNum, "expireDt": expireDt, "cvv": cvv})
    else:
        form = cart()
    return render(request,'superStore_website/receipt.html')