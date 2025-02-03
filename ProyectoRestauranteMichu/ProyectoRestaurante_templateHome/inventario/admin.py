from django.contrib import admin
from .models import InventarioPrincipal, CategoriaInventario, Insumo, MovimientoInventario, ReporteConsumo, ReporteInventario

@admin.register(InventarioPrincipal)
class InventarioPrincipalAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(CategoriaInventario)
class CategoriaInventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'inventario')
    search_fields = ('nombre',)
    list_filter = ('inventario',)

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'cantidad_disponible', 'unidad_medida', 'nivel_reorden')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
    readonly_fields = ('cantidad_disponible',)  # Se actualiza con movimientos

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'tipo', 'cantidad', 'fecha', 'descripcion')
    search_fields = ('insumo__nombre',)
    list_filter = ('tipo', 'fecha')
    ordering = ('-fecha',)

@admin.register(ReporteConsumo)
class ReporteConsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'cantidad_consumida', 'fecha_inicio', 'fecha_fin')
    search_fields = ('insumo__nombre',)
    list_filter = ('fecha_inicio', 'fecha_fin')

@admin.register(ReporteInventario)
class ReporteInventarioAdmin(admin.ModelAdmin):
    list_display = ('inventario', 'fecha_generacion')
    search_fields = ('inventario__nombre',)
    list_filter = ('fecha_generacion',)
