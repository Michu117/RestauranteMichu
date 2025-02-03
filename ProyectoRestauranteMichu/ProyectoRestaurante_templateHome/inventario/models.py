from django.db import models
from django.db.models.signals import post_save
from datetime import date
from django.dispatch import receiver
from typing import Any

class InventarioPrincipal(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Inventarios Principales"

    def __str__(self):
        return self.nombre

class CategoriaInventario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    inventario = models.ForeignKey(InventarioPrincipal, on_delete=models.CASCADE, related_name='categorias', null=True)

    class Meta:
        verbose_name_plural = "Categorias de Inventario"

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.insumo_set = None

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    categoria = models.ForeignKey(CategoriaInventario, on_delete=models.CASCADE, related_name='insumos')
    cantidad_disponible = models.PositiveIntegerField(default=0)
    unidad_medida = models.CharField(max_length=50)
    nivel_reorden = models.FloatField()

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible} {self.unidad_medida})"

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Movimientos de Inventario"

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.insumo.nombre} ({self.cantidad} {self.insumo.unidad_medida})"

class ReporteConsumo(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name_plural = "Reportes de Consumo"

    @property
    def cantidad_consumida(self):
        # Sumar todas las salidas del insumo en el rango de fechas
        total_consumo = MovimientoInventario.objects.filter(
            insumo=self.insumo,
            tipo='salida',
            fecha__range=[self.fecha_inicio, self.fecha_fin]
        ).aggregate(total=models.Sum('cantidad'))['total']

        return total_consumo or 0  # Si no hay movimientos, devuelve 0

    def __str__(self):
        return f"{self.insumo.nombre}: {self.cantidad_consumida} {self.insumo.unidad_medida} ({self.fecha_inicio} - {self.fecha_fin})"


@receiver(post_save, sender=MovimientoInventario)
def generar_reporte_consumo(instance, sender, **kwargs):
    if instance.tipo == 'salida':
        hoy = date.today()
        fecha_inicio = date(hoy.year, hoy.month, 1)  # Primer día del mes
        fecha_fin = date(hoy.year, hoy.month, 28)  # Ajustar según el mes

        # Buscar si ya existe un reporte para este insumo en el mes actual
        reporte, creado = ReporteConsumo.objects.get_or_create(
            insumo=instance.insumo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )

        # Si el reporte ya existía, se actualizará dinámicamente al consultarlo
        print(f"Reporte de consumo actualizado para {instance.insumo.nombre}")

class ReporteInventario(models.Model):
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    inventario = models.ForeignKey(InventarioPrincipal, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reportes de Inventario"

    def generar_reporte(self):
        insumos = Insumo.objects.filter(categoria__inventario=self.inventario)
        return [
            {
                "nombre": insumo.nombre,
                "cantidad_disponible": insumo.cantidad_disponible,
                "unidad_medida": insumo.unidad_medida,
                "nivel_reorden": insumo.nivel_reorden,
            }
            for insumo in insumos
        ]

    def __str__(self):
        return f"Reporte de Inventario - {self.inventario.nombre} ({self.fecha_generacion})"

