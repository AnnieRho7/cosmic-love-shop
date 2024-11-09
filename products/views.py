from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

def all_products(request):
    """ 
    A view to show a list of products 
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    sort_options = {
        'price': 'price',
        'rating': 'rating',
        'name': 'name',
        'category': 'category__name'
    }

    if request.GET.get('sort') and request.GET.get('direction'):
        sort = request.GET['sort']
        direction = request.GET['direction']
        
        if sort in sort_options:
            sort_field = sort_options[sort]
            if direction == 'desc':
                sort_field = f'-{sort_field}'
            products = products.order_by(sort_field)

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)

    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else 'None_None'

    if categories:
        category_names = ', '.join(categories)
        meta_description = f"Shop our {category_names} collection at Cosmic Love. Handcrafted gemstone jewellery made with love. Unique pieces in silver and brass."
        meta_title = f"Shop {category_names} | Cosmic Love Jewellery"
    elif query:
        meta_description = f"Search results for '{query}' - Handcrafted gemstone jewellery at Cosmic Love. Unique pieces made with love."
        meta_title = f"Search: {query} | Cosmic Love Jewellery"
    else:
        meta_description = "Shop our collection of handmade gemstone jewellery. Featuring unique pieces in silver and brass, each item is handcrafted with love."
        meta_title = "Shop Handmade Jewellery | Cosmic Love"

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'meta_description': meta_description,
        'meta_title': meta_title,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show individual product details 
    """
    
    product = get_object_or_404(Product, pk=product_id)
    
    meta_description = f"{product.name} - {product.description[:100]}... Handcrafted gemstone jewellery by Cosmic Love."
    if len(meta_description) > 160:
        meta_description = meta_description[:157] + "..."
        
    meta_title = f"{product.name} | Cosmic Love Jewellery"
    

    if product.category:
        meta_title = f"{product.name} - {product.category.friendly_name} | Cosmic Love Jewellery"

    context = {
        'product': product,
        'meta_description': meta_description,
        'meta_title': meta_title,
    }

    return render(request, 'products/product_detail.html', context)