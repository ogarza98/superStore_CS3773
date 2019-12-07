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
            return render(request,'superStore_website/receipt.html',{"firstName": fname, "lastName": lname,
                          "userName": uname, "email": email})
    else:
        form = cart()
    return render(request,'superStore_website/receipt.html')