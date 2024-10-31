from django import forms
from users.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 
            'email', 
            'phone_number',
            'street_address1', 
            'street_address2',
            'town_or_city', 
            'postcode', 
            'country',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True  # Set autofocus on the full_name field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'  # Append '*' for required fields
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'  # Add CSS class for styling
            self.fields[field].label = False  # Remove labels for a cleaner look

