from django.db import models
from decimal import Decimal
from datetime import date
from facturacion.models import Factura, ItemFactura, Mesero
from mesas.models import Mesa
from menu.models import Producto
from pedidos.models import ItemPedido


# Clase base para todas las estadísticas
class Estadistica(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField(default=date.today)

    # Campos para almacenar los datos calculados
    mejor_mesero = models.CharField(max_length=50, blank=True, null=True)
    mesa_mas_usada = models.CharField(max_length=50, blank=True, null=True)
    producto_mas_vendido = models.CharField(max_length=50, blank=True, null=True)
    ventas_totales = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.titulo} ({self.fecha_inicio} - {self.fecha_fin})"

    def calcular_mejor_mesero(self):
        facturas = Factura.objects.filter(fecha__range=[self.fecha_inicio, self.fecha_fin])
        mejor_mesero = (
            facturas.values('mesero')
            .annotate(total=models.Count('numero'))
            .order_by('-total')
            .first()
        )
        if mejor_mesero:
            mesero = Mesero.objects.get(id=mejor_mesero['mesero'])
            return mesero.nombre
        return "No hay datos"

    def calcular_mesa_mas_usada(self):
        facturas = Factura.objects.filter(fecha__range=[self.fecha_inicio, self.fecha_fin])
        mesa_mas_usada = (
            facturas.values('mesa')
            .annotate(total=models.Count('numero'))
            .order_by('-total')
            .first()
        )
        if mesa_mas_usada:
            mesa = Mesa.objects.get(id=mesa_mas_usada['mesa'])
            return mesa.codigo
        return "No hay datos"

    def calcular_producto_mas_vendido(self):
        item_facturas = ItemPedido.objects.filter(
            pedido__factura__fecha__range=[self.fecha_inicio, self.fecha_fin]
        )
        producto_mas_vendido = (
            item_facturas.values('producto')
            .annotate(total_vendido=models.Sum('cantidad'))
            .order_by('-total_vendido')
            .first()
        )
        if producto_mas_vendido:
            producto = Producto.objects.get(id=producto_mas_vendido['producto'])
            return producto.nombre
        return "No hay datos"

    def calcular_ventas_totales(self):
        facturas = Factura.objects.filter(fecha__range=[self.fecha_inicio, self.fecha_fin])
        ventas_totales = facturas.aggregate(total=models.Sum('total'))['total']
        if ventas_totales is None:
            ventas_totales = Decimal('0.00')
        return ventas_totales


    def save(self, *args, **kwargs):
        # Realizar cálculos antes de guardar
        self.mejor_mesero = self.calcular_mejor_mesero()
        self.mesa_mas_usada = self.calcular_mesa_mas_usada()
        self.producto_mas_vendido = self.calcular_producto_mas_vendido()
        self.ventas_totales = self.calcular_ventas_totales()
        super().save(*args, **kwargs)

# Modelo para Reporte
class Reporte(models.Model):
    titulo = models.CharField(max_length=50)

    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField(default=date.today)

    class TipoArchivo(models.TextChoices):
        PDF = 'PDF'

    def generar_estadisticas(self):
        datos = {
            "mejor_mesero": {},
            "mesas_usadas": [],
            "productos_vendidos": []
        }

        # Obtener datos para "Mejor Mesero"
        facturas = Factura.objects.filter(fecha__range=[self.fecha_inicio, self.fecha_fin])
        meseros = (
            facturas.values('mesero__nombre')
            .annotate(total=models.Count('numero'))
            .order_by('-total')
        )
        if meseros.exists():
            datos["mejor_mesero"]["nombre"] = meseros[0]['mesero__nombre']
            datos["mejor_mesero"]["cantidad"] = meseros[0]['total']
            datos["mejor_mesero"]["detalles"] = list(meseros)

        # Obtener datos para "Mesa más usada"
        mesas = (
            facturas.values('mesa__codigo')
            .annotate(total=models.Count('numero'))
            .order_by('-total')
        )
        if mesas.exists():
            datos["mesas_usadas"] = list(mesas)

        # Obtener datos para "Producto más vendido"
        item_facturas = ItemFactura.objects.filter(factura__fecha__range=[self.fecha_inicio, self.fecha_fin])
        productos = (
            item_facturas.values('producto__nombre')
            .annotate(total_vendido=models.Sum('cantidad'))
            .order_by('-total_vendido')
        )
        if productos.exists():
            datos["productos_vendidos"] = list(productos)

        return datos
