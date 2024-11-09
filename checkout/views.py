import stripe
import json
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from users.models import Order, OrderLineItem
from .forms import OrderForm
from .webhook import stripe_webhook
from cart.contexts import cart_contents
from products.models import Product

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_secret_key:
        messages.error(request, "Stripe secret key is missing.")
        return redirect(reverse('products'))

    stripe.api_key = stripe_secret_key

    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    # Initialize order_form here
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)

            if request.user.is_authenticated:
                order.user = request.user
            else:
                order.user = None

            # Save order first to get an ID
            order.save()

            # Create payment intent after saving order
            payment_intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                metadata={
                    'order_id': str(order.id),
                    'username': request.user.username if request.user.is_authenticated else 'guest'
                }
            )

            # Update order with cart and payment info
            order.original_cart = json.dumps(cart)
            order.stripe_pid = payment_intent.id
            order.save()

            # Create order line items
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(quantity, int):
                        # If quantity is just an integer
                        line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                    else:
                        # If quantity is a dictionary
                        line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity.get('quantity', 1),
                        )
                    line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your cart wasn't found.")
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Save the info to the user's profile if all went well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There was an error with your form. Please double-check your information.")

    # Create payment intent for new checkout session
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        metadata={
            'username': request.user.username if request.user.is_authenticated else 'guest'
        }
    )
    
    # Add cart items to context
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'cart_items': current_cart['cart_items'],
        'total': total,
        'product_count': current_cart['product_count'],
        'delivery': current_cart['delivery'],
        'grand_total': total,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """View for displaying order success page."""
    try:
        order = Order.objects.get(order_number=order_number)
        if request.user.is_authenticated and order.user != request.user:
            return redirect(reverse('home'))

        if 'cart' in request.session:
            del request.session['cart']

    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect(reverse('home'))

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    return render(request, 'checkout/checkout_success.html', {'order': order})

def checkout_success(request, order_number):
    """View for displaying order success page."""
    try:
        order = Order.objects.get(order_number=order_number)
        if request.user.is_authenticated and order.user != request.user:
            return redirect(reverse('home'))
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect(reverse('home'))

    return render(request, 'checkout/checkout_success.html', {'order': order})
