from django import forms

from catalog.models import Product

UNACCEPTABLE_NAMES = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data in UNACCEPTABLE_NAMES:
            raise forms.ValidationError('Unacceptable product name')

        return cleaned_data
