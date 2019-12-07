from .models import Good
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView


def home(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)


def search_results(request):
    query = request.GET.get('q')
    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query))
    }

    return render(request, 'superStore_website/search_results.html', results)


def product(request):
    query = request.GET.get('p')
    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query))
    }

    return render(request, 'superStore_website/product.html', results)


def help_pg(request):

    return render(request, 'superStore_website/help.html')
