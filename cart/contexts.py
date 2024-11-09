from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Calculate and return the cart contents, totals, and delivery information.
    Makes cart data available to all templates.
    """
    cart_items = []
    total = Decimal('0.00')
    product_count = 0
    cart = request.session.get('cart', {})

    FREE_DELIVERY_THRESHOLD = Decimal(str(settings.FREE_DELIVERY_THRESHOLD))
    STANDARD_DELIVERY_PERCENTAGE = Decimal(str(settings.STANDARD_DELIVERY_PERCENTAGE))

    for item_id, quantity in cart.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            subtotal = Decimal(str(product.price)) * Decimal(str(quantity))
            total += subtotal
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            continue

    if total < FREE_DELIVERY_THRESHOLD:
        delivery = (total * STANDARD_DELIVERY_PERCENTAGE) / 100
        free_delivery_delta = FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context