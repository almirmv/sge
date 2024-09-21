from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = [ 'product', 'quantity', 'description']
        # passando o visual com classes bootstrap
        widgets = {           
            'product': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),            
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {           
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição'
        }
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if quantity > product.quantity:
            raise ValidationError(
                f'O estoque disppnível do produto {product.title} é de {product.quantity} unidades.'
            )
        # passou na validação
        return quantity
