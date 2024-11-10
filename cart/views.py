from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from django.conf import settings


def view_cart(request):
    cart_items = []
    total = 0
    

    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    free_delivery_delta = 0
    delivery = 0
    
    if total < free_delivery_threshold:
        free_delivery_delta = free_delivery_threshold - total
    else:
        delivery = 0
    
    grand_total = total + delivery
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }
    
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """Add a specific quantity of a product to the shopping cart."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('view_cart'))
    size = request.POST.get('product_size')
    cart = request.session.get('cart', {})

    item_id = str(item_id)

    try:
        if size:
            if item_id in cart:
                if size in cart[item_id]['items_by_size']:
                    cart[item_id]['items_by_size'][size] += quantity
                    messages.success(
                        request,
                        f'Updated size {size.upper()} {product.name} '
                        f'quantity to {cart[item_id]["items_by_size"][size]}'
                    )
                else:
                    cart[item_id]['items_by_size'][size] = quantity
                    messages.success(
                        request,
                        f'Added size {size.upper()} {product.name} to your cart'
                    )
            else:
                cart[item_id] = {'items_by_size': {size: quantity}}
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your cart'
                )
        else:
            if item_id in cart:
                cart[item_id] += quantity
                messages.success(
                    request,
                    f'Updated {product.name} quantity to {cart[item_id]}'
                )
            else:
                cart[item_id] = quantity
                messages.success(
                    request,
                    f'Added {product.name} to your cart!'
                )

        request.session['cart'] = cart
        return redirect(redirect_url)

    except Exception as e:
        messages.error(
            request,
            f'Error adding item to cart: {str(e)}'
        )
        return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of a specific product in the cart."""
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity', 0))
        size = request.POST.get('product_size')
        cart = request.session.get('cart', {})

        item_id = str(item_id)

        if not cart.get(item_id):
            messages.error(request, 'Item not found in cart')
            return redirect(reverse('view_cart'))

        if size:
            if quantity > 0:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} '
                    f'quantity to {quantity}'
                )
            else:
                del cart[item_id]['items_by_size'][size]
                if not cart[item_id]['items_by_size']:
                    cart.pop(item_id)
                messages.success(
                    request,
                    f'Removed size {size.upper()} {product.name} from cart'
                )
        else:
            if quantity > 0:
                cart[item_id] = quantity
                messages.success(
                    request,
                    f'Updated {product.name} quantity to {quantity}'
                )
            else:
                cart.pop(item_id)
                messages.success(
                    request,
                    f'Removed {product.name} from cart'
                )

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        messages.error(
            request,
            f'Error updating cart: {str(e)}'
        )
        return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove an item from the shopping cart."""
    try:
        item_id = str(item_id)
        cart = request.session.get('cart', {})

        if not cart.get(item_id):
            messages.error(request, 'Item not found in cart')
            return redirect(reverse('view_cart'))

        if isinstance(cart[item_id], dict) and 'items_by_size' in cart[item_id]:
            del cart[item_id]
            messages.success(request, 'Item removed from cart')
        else:
            cart.pop(item_id)
            messages.success(request, 'Item removed from cart')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        messages.error(
            request,
            f'Error removing item: {str(e)}'
        )
        return redirect(reverse('view_cart'))
