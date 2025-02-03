from django.shortcuts import render, redirect, get_object_or_404
from .forms import MenuForm, CategoriaForm, ProductoForm
import requests
from menu.forms import ConversionForm
from menu.services import obtener_tasas_de_cambio
from django.contrib import messages
from .models import Menu, Categoria, Producto
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView


class listar_menu(ListView):
    model = Menu
    template_name = 'admin/menu/listar_menus.html'
    context_object_name = 'menus'
    paginate_by = 10

    def get_queryset(self):
        return Menu.objects.all()

def crear_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menú creado exitosamente.")
            return redirect('listar_menu')  # Aquí rediriges a la lista de menús, sin necesidad de 'pk'
    else:
        form = MenuForm()

    return render(request, 'admin/menu/crear_menu.html', {'form': form})

class edicion_menu(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'admin/menu/editar_menu.html'
    success_url = reverse_lazy('listar_menu')

    def form_valid(self, form):
        return super().form_valid(form)

def eliminar_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('listar_menu')

class listar_categorias(ListView):
    model = Categoria
    template_name = 'admin/menu/listar_categorias.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self):
        menu_pk = self.kwargs.get('pk')  # Obtiene el ID del menú desde la URL
        return Categoria.objects.filter(menu_id=menu_pk)  # Filtra categorías por menú

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_object_or_404(Menu, pk=self.kwargs.get('pk'))  # Agrega el menú al contexto
        return context


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria creada exitosamente.")
            return redirect('listar_menu')  # Aquí rediriges a la lista de menús, sin necesidad de 'pk'
    else:
        form = CategoriaForm()

    return render(request, 'admin/menu/crear_categoria.html', {'form': form})

class edicion_categoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'admin/menu/editar_categoria.html'
    success_url = reverse_lazy('listar_menu')

    def form_valid(self, form):
        return super().form_valid(form)

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('listar_menu')


THEMEALDB_API_URL = "https://www.themealdb.com/api/json/v1/1/"


def get_categories():
    response = requests.get(f"{THEMEALDB_API_URL}categories.php")
    if response.status_code == 200:
        return response.json().get("categories", [])
    return []


def get_meals_by_category(category):
    response = requests.get(f"{THEMEALDB_API_URL}filter.php?c={category}")
    if response.status_code == 200:
        return response.json().get("meals", [])
    return []


def get_meal_details(meal_id):
    response = requests.get(f"{THEMEALDB_API_URL}lookup.php?i={meal_id}")
    if response.status_code == 200:
        meals = response.json().get("meals", [])
        return meals[0] if meals else None
    return None


def gestionar_menu(request):
    if request.method == "POST":
        if 'crear_menu' in request.POST:
            menu_form = MenuForm(request.POST)
            if menu_form.is_valid():
                menu_form.save()
        elif 'crear_categoria' in request.POST:
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
        elif 'crear_producto' in request.POST:
            producto_form = ProductoForm(request.POST)
            if producto_form.is_valid():
                producto_form.save()

        return redirect('gestionar_menu')  # Redirigir a la misma página para reflejar los cambios

    else:
        menu_form = MenuForm()
        categoria_form = CategoriaForm()
        producto_form = ProductoForm()

    # Obtener todos los menús y productos desde la base de datos
    menus = Menu.objects.all()
    productos = Producto.objects.all()

    # Obtener las categorías desde la API
    categorias = get_categories()

    context = {
        'menu_form': menu_form,
        'categoria_form': categoria_form,
        'producto_form': producto_form,
        'menus': menus,
        'categorias': categorias,  # Ahora contiene datos de la API
        'productos': productos,
    }

    return render(request, 'menu/gestionar_menu.html', context)


def categories_view(request):
    categories = get_categories()
    return render(request, 'api/categorias.html', {"categories": categories})


def meals_view(request, category_name):
    meals = get_meals_by_category(category_name)
    return render(request, 'api/meals.html', {"meals": meals, "category": category_name})


def meal_detail_view(request, meal_id):
    meal = get_meal_details(meal_id)

    # Extraer los ingredientes y medidas en una lista
    ingredients = []
    if meal:
        for i in range(1, 21):  # Hay hasta 20 ingredientes en la API
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():  # Ignorar ingredientes vacíos
                ingredients.append(f"{measure} {ingredient}".strip())

    return render(request, 'api/meal_detail.html', {"meal": meal, "ingredients": ingredients})


def convertir_divisa(request):
    resultado = None
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            moneda_origen = form.cleaned_data['moneda_origen']
            moneda_destino = form.cleaned_data['moneda_destino']
            monto = form.cleaned_data['monto']
            tasas = obtener_tasas_de_cambio(moneda_origen)
            if tasas and 'conversion_rates' in tasas:
                tasa_cambio = tasas['conversion_rates'].get(moneda_destino)
                if tasa_cambio:
                    resultado = float(monto) * tasa_cambio

    else:
        form = ConversionForm()
    return render(request, 'api/convertir_moneda.html', {'form': form, 'resultado': resultado})
