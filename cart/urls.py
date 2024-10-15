from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart  # Import view_cart here

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', adjust_cart, name='adjust_cart'),  # Ensure the view function is correctly referenced
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),  # Change product_id to item_id to match your views
]
