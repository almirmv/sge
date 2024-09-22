from django import forms
from django.core.exceptions import ValidationError
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = [ 'title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price',]
        # passando o visual com classes bootstrap
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'brand' : forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class':'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class':'form-control'}),           
        }
        labels = {           
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Número de série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
            
        }

    #def clean_quantity(self):
    #    quantity = self.cleaned_data.get('quantity')
    #    product = self.cleaned_data.get('product')
    #    if quantity > product.quantity:
    #        raise ValidationError(
    #            f'O estoque disppnível do produto {product.title} é de {product.quantity} unidades.'
    #        )
    #    # passou na validação
    #    return quantity
