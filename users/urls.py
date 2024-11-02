from django.urls import path  # Make sure to import path
from .views import user_profile, manage_addresses  # Import your views

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('addresses/', manage_addresses, name='manage_addresses'),  # Add this line
]
