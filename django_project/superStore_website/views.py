from django.http import HttpResponse

from .models import Good
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User



from django.db.models import Q


def home(request):

    # user = get_object_or_404(User, username=self.kwargs.get('username'))

    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)


def gallery(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/gallery.html', context)


def login(request):
    return HttpResponse('<h1>Login Page<h1>')


def checkout(request):
    return HttpResponse('<h1>Checkout Page<h1>')


def search_results(request):
    query = request.GET.get('q')
    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query))
    }

    if not query:
        no_results()

    else:
        return render(request, 'superStore_website/search_results.html', results)


def no_results(request):
    return render(request, 'superStore_website/no_results.html')
