from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import UserProfile, Address

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False, label='Bio')

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']

class AddressForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Full name should contain only letters and spaces.')]
    )
    phone_number = forms.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\d{7,15}$', 'Phone number should contain only digits and be 7-15 characters long.')]
    )
    postcode = forms.CharField(
        max_length=20,
        required=False,
        validators=[RegexValidator(r'^[A-Za-z0-9\s-]*$', 'Postcode should contain letters, digits, spaces, or hyphens.')]
    )
    country = forms.CharField(
        max_length=40,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Country name should contain only letters and spaces.')]
    )
    town_or_city = forms.CharField(
        max_length=40,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Town or city name should contain only letters and spaces.')]
    )
    street_address1 = forms.CharField(
        max_length=80,
        validators=[RegexValidator(r'^[a-zA-Z0-9\s,.-]*$', 'Street address can contain letters, digits, commas, hyphens, or periods.')]
    )
    street_address2 = forms.CharField(
        max_length=80,
        required=False,
        validators=[RegexValidator(r'^[a-zA-Z0-9\s,.-]*$', 'Street address can contain letters, digits, commas, hyphens, or periods.')]
    )
    county = forms.CharField(
        max_length=80,
        required=False,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'County should contain only letters and spaces.')]
    )

    class Meta:
        model = Address
        fields = [
            'full_name', 'phone_number', 'country', 'postcode', 
            'town_or_city', 'street_address1', 'street_address2', 'county'
        ]
        