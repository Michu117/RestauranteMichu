from django.contrib import admin
from .models import (
    Impuesto, ItemPedido,
    Promocion, Factura, ItemFactura, Mesero, HistorialFactura
)

class MontoTotalFilter(admin.SimpleListFilter):
    title = 'monto total'
    parameter_name = 'monto_total'

    def lookups(self, request, model_admin):
        return [
            ('<100', 'Menos de 100'),
            ('100-500', 'Entre 100 y 500'),
            ('500-1000', 'Entre 500 y 1000'),
            ('>1000', 'Más de 1000'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<100':
            return queryset.filter(factura_total_lt=100)
        if self.value() == '100-500':
            return queryset.filter(factura_totalgte=100, facturatotal_lt=500)
        if self.value() == '500-1000':
            return queryset.filter(factura_totalgte=500, facturatotal_lt=1000)
        if self.value() == '>1000':
            return queryset.filter(factura_total_gte=1000)
        return queryset

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'subtotal', 'impuesto_total', 'descuento', 'total', 'pedido','metodo_pago', 'monto_recibido', 'cambio', 'mesero', 'mesa', )
    search_fields = ('numero',)
    list_filter = ('fecha', 'pedido')
    readonly_fields = ('subtotal', 'impuesto_total', 'descuento', 'total')

    def save_model(self, request, obj, form, change):
        obj.calcular_monto_total()
        super().save_model(request, obj, form, change)

@admin.register(ItemFactura)
class ItemFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'subtotal')
    search_fields = ('factura__numero', 'producto__nombre')
    list_filter = ('factura',)
    readonly_fields = ('subtotal',)

    def save_model(self, request, obj, form, change):
        obj.calcular_subtotal()
        super().save_model(request, obj, form, change)

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    search_fields = ('producto__nombre',)
    list_filter = ('pedido',)
    readonly_fields = ('precio_unitario',)

    def save_model(self, request, obj, form, change):
        obj.precio_unitario = obj.producto.precio
        super().save_model(request, obj, form, change)

@admin.register(Impuesto)
class ImpuestoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porcentaje', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('porcentaje',)



@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'porcentaje_descuento')
    search_fields = ('descripcion',)
    list_filter = ('porcentaje_descuento',)

@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)


@admin.register(HistorialFactura)
class HistorialFacturaAdmin(admin.ModelAdmin):
    # Mostrar los campos básicos en la lista
    list_display = ('fecha_inicio', 'fecha_fin', 'mostrar_facturas_lista')

    # Método para mostrar la lista de códigos de facturas en el AdminIndividual
    def mostrar_facturas_lista(self, obj):
        # Llamamos a facturas_lista que obtiene los códigos de las facturas
        return ', '.join(obj.facturas_lista)
    mostrar_facturas_lista.short_description = 'Códigos de Facturas'  # Título en el AdminIndividual
