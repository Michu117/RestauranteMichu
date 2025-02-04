# menu/forms.py
from django import forms
from .models import Menu, Categoria, Producto

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nombre', 'estado']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'menu']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'disponibilidad', 'categoria']

class ConversionForm(forms.Form):
    MONEDAS = [
        ('USD', 'Dólar Estadounidense'),
        ('EUR', 'Euro'),
        ('COP', 'Peso Colombiano'),
        ('PEN', 'Sol Peruano'),
        ('VES', 'Bolívar Venezolano'),
        ('BRL', 'Real Brasileño'),
        ('ARS', 'Peso Argentino'),
        ('CLP', 'Peso Chileno'),
        ('PAB', 'Balboa Panameño'),
        ('UYU', 'Peso Uruguayo'),
        ('CAD', 'Dólar Canadiense'),
        ('HNL', 'Lempira Hondureño'),
        ('KRW', 'Won Surcoreano'),
        ('JPY', 'Yen Japonés'),
        ('CNY', 'Yuan Chino (Renminbi)'),
        # En este apartado podemos agregar más monedas
    ]

    moneda_origen = forms.ChoiceField(choices=MONEDAS, label='Moneda de Origen')
    moneda_destino = forms.ChoiceField(choices=MONEDAS, label='Moneda de Destino')
    monto = forms.DecimalField(min_value=0, label='Monto a Convertir')
