from .models import Good
from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)

def cart(request):
    return HttpResponseRedirect('superStore_website/cart.html')