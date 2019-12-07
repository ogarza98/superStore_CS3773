from django.http import HttpResponse

from .models import Good
from django.shortcuts import render
from django.db.models import Q


def home(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home_Daniel.html', context)


def gallery(request):
    context = {
        'goods':Good.objects.all(),
    }

    return render(request, 'superStore_website/gallery.html', context)


#def home(request):
#    return render(request, 'superStore_website/imported_home.html')


def login(request):
    return HttpResponse('<h1>Login Page<h1>')


def checkout(request):
    return HttpResponse('<h1>Checkout Page<h1>')


def search_results(request):
    query = request.GET.get('q')
    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query))
    }

    return render(request, 'superStore_website/search_results.html', results)
