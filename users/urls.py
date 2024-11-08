from django.urls import path
from .views import (
    user_profile, 
    manage_addresses, 
    newsletter_signup, 
    toggle_newsletter_subscription,
    delete_account,
    add_to_wishlist,
    remove_from_wishlist,
    is_in_wishlist,
)

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('addresses/', manage_addresses, name='manage_addresses'),
    path('delete-account/', delete_account, name='delete_account'),
    path('newsletter/signup/', newsletter_signup, name='newsletter_signup'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/check/<int:product_id>/', is_in_wishlist, name='is_in_wishlist'),
]