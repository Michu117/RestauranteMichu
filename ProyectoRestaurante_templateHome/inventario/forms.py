from django import forms
from menu.models import Menu, Categoria, Producto


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
        fields = ['nombre', 'categoria', 'precio', 'descripcion', 'disponibilidad']