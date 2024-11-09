from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product

import stripe


def view_cart(request):
    """
    A view to render the shopping cart page.
    
    Displays all items currently in the user's shopping cart
    with their quantities and total price.
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping cart 
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('view_cart'))
    size = request.POST.get('product_size')
    cart = request.session.get('cart', {})

    item_id = str(item_id)

    if size:
        if item_id in cart:
            if size in cart[item_id]['items_by_size']:
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
    else:
        if item_id in cart:
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url) 


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 0))
    size = request.POST.get('product_size')
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ 
    Remove a quantity of the specified product from the shopping cart 
    """
    item_id = str(item_id)
    cart = request.session.get('cart', {})


    if item_id in cart:
        if isinstance(cart[item_id], dict) and 'items_by_size' in cart[item_id]:
            for size, quantity in cart[item_id]['items_by_size'].items():
                if quantity > 1:
                    cart[item_id]['items_by_size'][size] -= 1
                    messages.success(request, f'Reduced quantity of size {size.upper()} for {item_id} to {cart[item_id]["items_by_size"][size]} in your cart.')
                else:
                    del cart[item_id]['items_by_size'][size]
                    messages.success(request, f'Removed size {size.upper()} for {item_id} from your cart.')
            if not cart[item_id]['items_by_size']:
                del cart[item_id]
                messages.success(request, f'Removed {item_id} from your cart.')
        else:
            if cart[item_id] > 1:
                cart[item_id] -= 1
                messages.success(request, f'Reduced quantity of {item_id} to {cart[item_id]} in your cart.')
            else:
                del cart[item_id]
                messages.success(request, f'Removed {item_id} from your cart.')
    else:
        messages.warning(request, f'{item_id} not found in your cart.')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

