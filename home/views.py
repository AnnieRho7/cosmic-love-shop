from django.shortcuts import render
from .models import Product


def index(request):
    """
    A view to return the index page
    """
    featured_products = Product.objects.filter(is_featured=True)

    return render(request, 'home/index.html', {
        'featured_products': featured_products,
    })
