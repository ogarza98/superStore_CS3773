from .models import Good
from django.shortcuts import render
from django.http import HttpResponseRedirect
from superStore_website.forms import cart


def home(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)

def cart(request):
    return render(request,'superStore_website/cart.html')

def receipt(request):
    if request.method == "POST":
        form = cart(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
    else:
        form = cart()
    return render(request,'superStore_website/receipt.html',{"firstName": fname})