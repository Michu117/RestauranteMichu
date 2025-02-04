from django.contrib import admin

from .models import (
    Reporte, Estadistica
)

@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin', 'mejor_mesero', 'mesa_mas_usada', 'producto_mas_vendido',)
    search_fields = ('titulo', 'fecha_inicio', 'fecha_fin',)
    list_filter = ('titulo', 'fecha_inicio', 'fecha_fin',)

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin',)
    search_fields = ('titulo', 'fecha_inicio', 'fecha_fin',)
    list_filter = ('titulo', 'fecha_inicio', 'fecha_fin',)
