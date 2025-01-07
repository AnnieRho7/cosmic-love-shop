from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image', 'is_featured']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        self.fields['name'].label = 'Product Name'
        self.fields['is_featured'].label = 'Feature on Homepage'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'