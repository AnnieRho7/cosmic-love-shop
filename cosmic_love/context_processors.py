def meta_tags(request):
    """
    Context processor to provide default meta descriptions
    """
    path = request.path
    meta_descriptions = {
        '/': 'Discover handcrafted gemstone jewellery at Cosmic Love. Unique boho and minimal designs featuring earrings, bracelets, and necklaces. Handmade with love for the free-spirited woman.',
        '/products/': 'Shop our collection of handmade gemstone jewellery. Featuring unique pieces in silver and brass, each item is handcrafted with love. Browse earrings, necklaces, and bracelets.',
        '/about/': 'Learn about Cosmic Love\'s journey in creating unique handmade gemstone jewellery. Each piece is crafted with intention and love.',
        '/contact/': 'Get in touch with Cosmic Love. Connect with us on Instagram, Facebook, and Pinterest for the latest handmade jewellery designs.',
    }
    
    default_description = 'Cosmic Love - Handcrafted gemstone jewellery made with love. Discover unique, bohemian and minimal designs in our collection.'
    
    return {
        'meta_description': meta_descriptions.get(path, default_description),
        'meta_title': get_meta_title(request),
    }

def get_meta_title(request):
    """
    Generate appropriate meta titles based on the current page
    """
    path = request.path
    base_title = 'Cosmic Love | Handcrafted Gemstone Jewellery'
    
    titles = {
        '/': base_title,
        '/products/': 'Shop Handmade Jewellery | ' + base_title,
        '/about/': 'About Us | ' + base_title,
        '/contact/': 'Contact Us | ' + base_title,
    }
    
    return titles.get(path, base_title)