from django.http import HttpResponse

from .models import Good
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.db.models import Q

from django.http import HttpResponseRedirect
from .forms import cart
from cart.models import Order


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
    check = Good.objects.filter(Q(item_name__icontains=query))

    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query)),
    }

    if not check:
        return render(request, 'superStore_website/no_results.html')

    else:
        return render(request, 'superStore_website/search_results.html', results)


def no_results(request):
    return render(request, 'superStore_website/no_results.html')


def get_user_pending_order(request):
    # get order for the correct user
    order = Order.objects.filter(is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def Cart(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'superStore_website/cart.html', context)


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
            return render(request,'superStore_website/receipt.html',{"firstName": fname, "lastName": lname,
                          "userName": uname, "email": email, "address": address, "altaddress": altaddress,
                          "nameOnCd": nameOnCd, "cardNum": cardNum, "expireDt": expireDt, "cvv": cvv})
    else:
        form = cart()
    return render(request,'superStore_website/receipt.html')
