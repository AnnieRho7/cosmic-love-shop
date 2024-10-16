from django.shortcuts import render
from .models import Product  # Import your Product model

def index(request):
    """ A view to return the index page """
    # Query the database for featured products
    featured_products = Product.objects.filter(is_featured=True)  # Adjust according to your model

    return render(request, 'home/index.html', {
        'featured_products': featured_products,
    })