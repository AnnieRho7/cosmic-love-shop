# products/models.py
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('earrings', 'Earrings'),
        ('necklaces', 'Necklaces'),
        ('bracelets', 'Bracelets'),
    ]
    MATERIAL_CHOICES = [
        ('silver', 'Silver'),
        ('brass', 'Brass'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    material = models.CharField(choices=MATERIAL_CHOICES, max_length=20)
    gemstone_type = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/images/')  # Store your images here

    def __str__(self):
        return self.name
