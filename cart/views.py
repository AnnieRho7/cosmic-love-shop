from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from .contexts import cart_contents

# Create your views here.

def view_cart(request):
    """ A view that renders the cart content page """
    cart = request.session.get('cart', {})  # Get the current session cart

    # Initialize the cart_items list
    cart_items = []

    # Check if there are items in the cart
    for item_id, item_data in cart.items():  # Iterate over the cart items
        product = get_object_or_404(Product, pk=item_id)  # Fetch the product

        # Check if item_data has sizes
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'size': size,  # Include size if applicable
                })
        else:
            # Assuming item_data is the quantity when not using sizes
            cart_items.append({
                'product': product,
                'quantity': item_data,  # Single quantity case
            })

    context = {
        'cart_items': cart_items,  # Pass the cart items to the template
    }

    return render(request, 'cart/cart.html', context)  # Render the template with context


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
    redirect_url = request.POST.get('redirect_url', reverse('view_cart'))  # Fallback to cart view
    size = request.POST.get('product_size')  # Get size if available
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)  # Redirect to the specified URL


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 0))  # Default to 0 if quantity is not provided
    size = request.POST.get('product_size')  # Get size if available
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:  # If no sizes left, remove item
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))  # Redirect back to the cart view


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)  # Ensure the product exists
        size = request.POST.get('product_size')  # Get size if available
        cart = request.session.get('cart', {})  # Retrieve cart from session

        # Debugging: Print current cart state
        print(f"Current cart before removal: {cart}")

        # Handle size-based items
        if size and item_id in cart and 'items_by_size' in cart[item_id]:
            del cart[item_id]['items_by_size'][size]  # Remove the specific size
            if not cart[item_id]['items_by_size']:  # Check if no sizes are left
                cart.pop(item_id)  # Remove item from cart if no sizes left
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
        else:
            if item_id in cart:
                cart.pop(item_id)  # Remove the item if it exists
                messages.success(request, f'Removed {product.name} from your cart')

        # Update session cart
        request.session['cart'] = cart
        print(f"Updated cart after removal: {cart}")  # Debugging output

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')

    return redirect(reverse('view_cart'))  # Redirect back to the cart view
