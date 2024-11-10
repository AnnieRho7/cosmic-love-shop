from django.urls import path
from . import views

urlpatterns = [
    path(
        'privacy-policy/',
        views.privacy_policy,
        name='privacy_policy'
    ),
    path(
        'terms-and-conditions/',
        views.terms_and_conditions,
        name='terms_and_conditions'
    ),
    path(
        'return-refund-policy/',
        views.return_refund_policy,
        name='return_refund_policy'
    ),
    path(
        'cookie-policy/',
        views.cookie_policy,
        name='cookie_policy'
    ),
]
