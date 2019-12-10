from django.http import HttpResponse

from .models import Good
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.db.models import Q

from django.http import HttpResponseRedirect
from superStore_website.forms import cart


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
def Cart(request):
    return render(request,'superStore_website/cart.html', {'form' : cart})

def receipt(request):
    if request.method == "POST":
        form = cart(request.POST)
        print(request.POST)
        print(form.is_valid())
        #if form.is_valid():
        fname = form.cleaned_data['first_name']
        #print(fname)
        lname = form.cleaned_data['last_name']
        #print(lname)
        email = form.cleaned_data['email']
        #print(email)
        address    = form.cleaned_data['address']
        altaddress = form.cleaned_data['altaddress']
        nameOnCd   = form.cleaned_data['nameOnCd']
        cardNum    = form.cleaned_data['cardNum']
        expireDt   = form.cleaned_data['expireDt']
        cvv        = form.cleaned_data['cvv']
        zipCode    = form.cleaned_data['zipCode']
        country    = request.POST.get('country')
        print(country)
        city       = form.cleaned_data['city']
        print(city)
        card       = request.POST.get('paymentType')
        print(card)
        state      = request.POST.get('state')
        print(state)

        shipAddLine_one = form.cleaned_data['shipAddLine_one']
        shipAddLine_two = form.cleaned_data['shipAddLine_two']
        shipCountry = request.POST.get('shipCountry')
        shipState   = request.POST.get('shipState')
        shipZipCode = form.cleaned_data['shipZipCode']
        shipCity    = form.cleaned_data['shipCity']
        deliveryOpt = request.POST.get('deliveryOpt')
        
        return render(request,'superStore_website/receipt.html',{"firstName": fname, "lastName": lname,
                        "email": email, "address": address, "altaddress": altaddress, "nameOnCd": nameOnCd, 
                        "cardNum": cardNum, "expireDt": expireDt, "cvv": cvv, "card:": card, "zipCode": zipCode, "country": country,
                        "city": city, "state": state, "shipAddLine_one": shipAddLine_one, "shipAddLine_two": shipAddLine_two,
                        "shipCountry": shipCountry, "shipState": shipState, "shipZipCode": shipZipCode, "shipCity": shipCity, 
                        "deliveryOpt": deliveryOpt})
    else:
        form = cart()
    return render(request,'superStore_website/receipt.html')
