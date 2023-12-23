from django import forms

from apps.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.shop:
            self.fields['categories'].choices = self.instance.shop.get_category_choices().values_list('id', 'name')

    def clean(self):
        cleaned_data = super().clean()
        if 'shop' in cleaned_data and 'categories' in cleaned_data:
            shop = cleaned_data['shop']
            categories = cleaned_data['categories']
            if not categories.filter(for_shop_type=shop.type).exists():
                self.fields['categories'].choices = shop.get_category_choices().values_list('id', 'name')
                raise forms.ValidationError(
                    'Обрана категорія не підходить для типу магазину'
                )
        return cleaned_data
