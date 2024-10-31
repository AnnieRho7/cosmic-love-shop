# cart/urls.py
from django.urls import path
from .views import (
    view_cart,
    add_to_cart,
    adjust_cart,
    remove_from_cart,
    create_checkout_session,  # Updated to use the new function name
    checkout_success,
    checkout_cancel,
)

urlpatterns = [
    path('', view_cart, name='view_cart'),  # Matches /cart/
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('adjust/<int:item_id>/', adjust_cart, name='adjust_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', create_checkout_session, name='checkout'),  # Updated to use the new function
    path('checkout/success/', checkout_success, name='checkout_success'),
    path('checkout/cancel/', checkout_cancel, name='checkout_cancel'),
]
