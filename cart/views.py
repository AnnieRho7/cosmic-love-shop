from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import stripe

from products.models import Product
from .contexts import cart_contents

# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def view_cart(request):
    """ A view that renders the cart content page """
    cart = request.session.get('cart', {})  # Get the current session cart
    cart_items = []  # Initialize the cart_items list

    # Check if there are items in the cart
    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)  # Fetch the product

        # Check if item_data has sizes
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'size': size,
                })
        else:
            # Assuming item_data is the quantity when not using sizes
            cart_items.append({
                'product': product,
                'quantity': item_data,
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

    item_id = str(item_id)  # Ensure item_id is a string

    if size:
        if item_id in cart.keys():
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
        if item_id in cart.keys():
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
    """ Remove a quantity of the specified product from the shopping cart """
    item_id = str(item_id)  # Ensure item_id is a string
    cart = request.session.get('cart', {})  # Retrieve cart from session

    # Check if the item exists in the cart
    if item_id in cart:
        # If quantity is greater than 1, reduce it by 1
        if cart[item_id] > 1:
            cart[item_id] -= 1
            messages.success(request, f'Reduced quantity of {item_id} to {cart[item_id]} in your cart.')
        else:
            # If only 1 item remains, remove it from the cart
            del cart[item_id]
            messages.success(request, f'Removed {item_id} from your cart.')
    else:
        messages.warning(request, f'{item_id} not found in your cart.')

    # Update session cart
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))  # Redirect back to the cart view

def checkout(request):
    """ A view that processes the checkout and Stripe payment """
    cart = request.session.get('cart', {})
    cart_items = []  # Initialize list to hold items for Stripe

    # Prepare items for Stripe
    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)

        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                cart_items.append({
                    'price_data': {
                        'currency': 'usd',  # Change currency as needed
                        'product_data': {
                            'name': product.name,
                            'images': [product.image.url],  # Assuming product has an image field
                        },
                        'unit_amount': int(product.price * 100),  # Convert to cents
                    },
                    'quantity': quantity,
                })
        else:
            quantity = item_data
            cart_items.append({
                'price_data': {
                    'currency': 'usd',  # Change currency as needed
                    'product_data': {
                        'name': product.name,
                        'images': [product.image.url],  # Assuming product has an image field
                    },
                    'unit_amount': int(product.price * 100),  # Convert to cents
                },
                'quantity': quantity,
            })

    try:
        # Create a Checkout Session with the cart items
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=cart_items,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('checkout_success')),
            cancel_url=request.build_absolute_uri(reverse('view_cart')),
        )

        # Redirect to Stripe's hosted checkout page
        return redirect(session.url, code=303)

    except Exception as e:
        messages.error(request, f'Error during checkout: {str(e)}')
        return redirect(reverse('view_cart'))  # Redirect back to cart on error

def checkout_success(request):
    """ A view to display a successful checkout """
    return render(request, 'checkout/success.html')  # Ensure this template exists


def checkout_cancel(request):
    """ A view to handle checkout cancellation """
    messages.info(request, 'Checkout was canceled. You can continue shopping!')
    return redirect(reverse('view_cart'))  # Redirect to the cart view
