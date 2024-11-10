from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import UserProfile, Address


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea, required=False, label='Bio'
    )

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']


class AddressForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[a-zA-Z\s]*$',
                'Only letters and spaces allowed.'
            )
        ]
    )

    phone_number = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                r'^\d{7,15}$',
                'Must be 7-15 digits.'
            )
        ]
    )

    postcode = forms.CharField(
        max_length=20,
        required=False,
        validators=[
            RegexValidator(
                r'^[A-Za-z0-9\s-]*$',
                'Letters, digits, spaces, or hyphens only.'
            )
        ]
    )

    country = forms.CharField(
        max_length=40,
        validators=[
            RegexValidator(
                r'^[a-zA-Z\s]*$',
                'Only letters and spaces allowed.'
            )
        ]
    )

    town_or_city = forms.CharField(
        max_length=40,
        validators=[
            RegexValidator(
                r'^[a-zA-Z\s]*$',
                'Only letters and spaces allowed.'
            )
        ]
    )

    street_address1 = forms.CharField(
        max_length=80,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9\s,.-]*$',
                'Letters, digits, commas, hyphens, or periods only.'
            )
        ]
    )

    street_address2 = forms.CharField(
        max_length=80,
        required=False,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9\s,.-]*$',
                'Letters, digits, commas, hyphens, or periods only.'
            )
        ]
    )

    county = forms.CharField(
        max_length=80,
        required=False,
        validators=[
            RegexValidator(
                r'^[a-zA-Z\s]*$',
                'Only letters and spaces allowed.'
            )
        ]
    )

    class Meta:
        model = Address
        fields = [
            'full_name',
            'phone_number',
            'country',
            'postcode',
            'town_or_city',
            'street_address1',
            'street_address2',
            'county'
        ]


class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'aria-label': 'Email',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = False
