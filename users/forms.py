from django import forms
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
    class Meta:
        model = Address
        fields = ['full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county']

