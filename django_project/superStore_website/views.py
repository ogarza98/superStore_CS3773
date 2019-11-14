from .models import Good
from django.shortcuts import render


def home(request):
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)