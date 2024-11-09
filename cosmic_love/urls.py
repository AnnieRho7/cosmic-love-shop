from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, ProductSitemap

# Define the sitemaps dictionary
sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('about/', include('about.urls')),
    path('users/', include('users.urls')),
    path('checkout/', include('checkout.urls')),
    path('contact/', include('contact.urls')),
    path('legal/', include('legal.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)