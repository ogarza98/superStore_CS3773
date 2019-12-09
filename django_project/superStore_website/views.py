from .models import Good, Order, OrderItem
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, ListView


def home(request):
    request.session['username'] = 'David'
    context = {
        'goods': Good.objects.all(),
    }

    return render(request, 'superStore_website/home.html', context)


def search_results(request):
    query = request.GET.get('q')
    request.session['username'] = query
    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query))
    }

    return render(request, 'superStore_website/search_results.html', results)


def product(request):
    query = request.GET.get('p')
    cart = request.GET.get('t')
    results = {
        'results': Good.objects.filter(Q(item_name__icontains=query))
    }

    return render(request, 'superStore_website/product.html', results, cart)


def help_pg(request):

    return render(request, 'superStore_website/help.html')


def add_to_cart(request, **kwargs):
    # create orderItem of the selected product
    prod = Good.objects.filter(id=kwargs.get('item_id', "")).first()
    order_item, status = OrderItem.objects.get_or_create(product=prod)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('test:home'))


def get_user_pending_order(request):
    # get order for the correct user
    order = Order.objects.filter(is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'superStore_website/order_summary.html', context)