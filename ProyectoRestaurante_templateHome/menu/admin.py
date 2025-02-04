from django.contrib import admin, messages
from .models import Menu, Categoria, Producto
from .services import MenuService


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    actions = ["agregar_categorias_automaticas"]

    def agregar_categorias_automaticas(self, request, queryset):
        """Agrega categorías y productos predeterminados a cada menú seleccionado."""
        menu_service = MenuService()
        categorias_predeterminadas = ["Entrantes", "Platos principales", "Postres"]

        for menu in queryset:
            for categoria_nombre in categorias_predeterminadas:
                categoria = menu_service.agregar_categoria(menu.id, categoria_nombre)
                self.message_user(request, f"Categoría '{categoria_nombre}' agregada a '{menu.nombre}'",
                                  messages.SUCCESS)

                # Agregar productos automáticos
                productos_predeterminados = [
                    {"nombre": "Plato Especial", "descripcion": "Delicioso plato gourmet", "precio": 15.0,
                     "disponibilidad": True},
                    {"nombre": "Bebida Premium", "descripcion": "Refrescante bebida", "precio": 5.0,
                     "disponibilidad": True}
                ]

                for prod_data in productos_predeterminados:
                    menu_service.agregar_producto(categoria.id, prod_data)
                    self.message_user(request, f"Producto '{prod_data['nombre']}' agregado a '{categoria_nombre}'",
                                      messages.SUCCESS)

    agregar_categorias_automaticas.short_description = "Agregar categorías y productos predeterminados"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "menu")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "disponibilidad", "categoria")
