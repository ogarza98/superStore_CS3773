from .models import Good
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User





def home(request):

    # user = get_object_or_404(User, username=self.kwargs.get('username'))

    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)

