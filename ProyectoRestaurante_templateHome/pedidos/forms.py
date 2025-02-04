from django import forms
from .models import Pedido, ItemPedido
from menu.models import Producto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente']  # Solo dejamos el cliente, ya que el producto y la cantidad se manejan a través de ItemPedido

    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
    )
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si ya hay un pedido existente, limitar los productos disponibles a aquellos que no se han añadido aún
        if self.instance.pk:
            self.fields['producto'].queryset = Producto.objects.exclude(itempedido__pedido=self.instance)

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si el formulario tiene un producto, agregar la funcionalidad de actualizar el precio
        if 'producto' in self.fields:
            self.fields['producto'].widget.attrs.update({'onchange': 'updatePrice()'})

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        if producto:
            cleaned_data['precio_unitario'] = producto.precio  # Asignar automáticamente el precio del producto
        return cleaned_data
