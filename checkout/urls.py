from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
]