from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings
from products.models import Product

class BaseSitemap(Sitemap):
    protocol = 'https'

    def get_domain(self):
        return settings.SITE_DOMAIN

class StaticViewSitemap(BaseSitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'contact', 'products']

    def location(self, item):
        return reverse(item)

    def get_urls(self, **kwargs):
        domain = self.get_domain()
        urls = []
        for item in self.items():
            loc = f"{self.protocol}://{domain}{self.location(item)}"
            url_info = {
                'item': item,
                'location': loc,
                'changefreq': self.changefreq,
                'priority': str(self.priority),
            }
            urls.append(url_info)
        return urls

class ProductSitemap(BaseSitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f'/products/{obj.id}'

    def get_urls(self, **kwargs):
        domain = self.get_domain()
        urls = []
        for item in self.items():
            loc = f"{self.protocol}://{domain}{self.location(item)}"
            url_info = {
                'item': item,
                'location': loc,
                'changefreq': self.changefreq,
                'priority': str(self.priority),
            }
            urls.append(url_info)
        return urls

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}