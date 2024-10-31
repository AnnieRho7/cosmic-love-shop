from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart, checkout, checkout_success, checkout_cancel

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('adjust/<int:item_id>/', adjust_cart, name='adjust_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('checkout/success/', checkout_success, name='checkout_success'),  # Ensure this line exists
    path('checkout/cancel/', checkout_cancel, name='checkout_cancel'),      # Ensure this line exists
]
