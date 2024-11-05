from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'pk_test_51ISm5fLmWB97vAlrI5lqluX9YlozQHZMN161VlBBPZ5eGwnLrx1bqVcE3cihZkFiCxzqlxb7lmcEFukYdRNyzAIC00cc5HSwhT'
    }

    return render(request, template, context)