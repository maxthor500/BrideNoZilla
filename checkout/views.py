from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request,
                        "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JUHHcF0Db8DzO0xALcHxfaNn7cSGeuDv56gWjhxs03AgrnySl2H17qFi2ND3etP2DihnlQ3i408WAIUrBWfUWE400mEONtUV9',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)
