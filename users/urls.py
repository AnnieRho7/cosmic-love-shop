from django.urls import path
from .views import (
    user_profile, 
    manage_addresses, 
    newsletter_signup, 
    toggle_newsletter_subscription,
    delete_account,
)

app_name = 'users'

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('addresses/', manage_addresses, name='manage_addresses'),
    path('delete-account/', delete_account, name='delete_account'),
    path('newsletter/signup/', newsletter_signup, name='newsletter_signup'),
    path('newsletter/toggle/', toggle_newsletter_subscription, name='toggle_newsletter'),
]