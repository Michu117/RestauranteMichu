from django.contrib import admin
from .models import  Pedido, HistorialPedido, ItemPedido, Receta



class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    readonly_fields = ('precio_unitario',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'estado', 'fecha', 'cliente', )
    search_fields = ('codigo', 'cliente__nombre')
    list_filter = ('estado', 'fecha')
    inlines = [ItemPedidoInline]

    # Método personalizado para mostrar el monto total en el admin
    def monto_total(self, obj):
        return f"${obj.monto_total()}"

    monto_total.short_description = 'Monto Total'

    # Método personalizado para mostrar el monto total en el admin
    def monto_total(self, obj):
        return f"${obj.monto_total()}"
    monto_total.short_description = 'Monto Total'

# Configuración del admin para el modelo HistorialPedido
@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'fecha', 'monto_total')  # Columnas mostradas en la lista
    search_fields = ('pedido__estado',)  # Campos de búsqueda
    list_filter = ('fecha',)  # Filtros laterales
    date_hierarchy = 'fecha'  # Navegación por fechas


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'insumo',  'cantidad_necesaria')  # Columnas mostradas en la lista
    search_fields = ('producto__nombre',)  # Campos de búsqueda
    list_filter = ('producto',)  # Filtros laterales
