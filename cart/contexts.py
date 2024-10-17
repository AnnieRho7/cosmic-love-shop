from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    cart_items = []
    total = Decimal('0.00')  # Initialize total as Decimal
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        
        # Convert product.price to Decimal and calculate total
        total += quantity * Decimal(product.price)  # Ensure product.price is Decimal
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Ensure settings.FREE_DELIVERY_THRESHOLD is also a Decimal
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)

    if total < free_delivery_threshold:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)  # Ensure delivery is Decimal
        # Now both total and free_delivery_threshold are Decimal
        free_delivery_delta = free_delivery_threshold - total  # This should be Decimal now
    else:
        delivery = Decimal('0.00')  # Set delivery to Decimal
        free_delivery_delta = Decimal('0.00')  # Ensure free_delivery_delta is Decimal

    grand_total = delivery + total  # grand_total should also be Decimal now

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
