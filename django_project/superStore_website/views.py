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
            return render(request,'superStore_website/receipt.html',{"firstName": fname})
    else:
        form = cart()
    return render(request,'superStore_website/receipt.html')