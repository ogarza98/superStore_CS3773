from django.shortcuts import render
from .models import Good, Order, OrderItem
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages


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
    # messages.info(request, "item added to cart")
    return redirect(reverse('home'))


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
    return render(request, 'cart/order_summary.html', context)
