from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image', 'is_featured']

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].label = 'Product Name'
        self.fields['category'].label = 'Category'
        self.fields['is_featured'].label = 'Feature on Homepage'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'