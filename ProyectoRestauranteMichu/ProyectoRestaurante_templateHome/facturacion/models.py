from django.db import models
from datetime import date
from mesas.models import Persona, Cliente, Mesa
from menu.models import Producto
from pedidos.models import Pedido, ItemPedido
from decimal import Decimal

class Impuesto(models.Model):
    nombre = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)  # Usamos DecimalField en lugar de FloatField
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Promocion(models.Model):
    descripcion = models.CharField(max_length=255)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)  # DecimalField

    class Meta:
        verbose_name_plural = "Promociones"

    def __str__(self):
        return self.descripcion


class Mesero(Persona):
    pedidosAtendidos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    def actualizar_pedidos_atendidos(self):
        self.pedidosAtendidos = Factura.objects.filter(mesero=self).count()
        self.save()


class Factura(models.Model):
    METODO_PAGO_CHOICES = [
        ("EFECTIVO", "Efectivo"),
        ("TARJETA", "Tarjeta"),
        ("TRANSFERENCIA", "Transferencia"),
    ]

    numero = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True, null=True)
    fecha = models.DateField(default=date.today)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # DecimalField
    impuesto_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # DecimalField
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # DecimalField
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # DecimalField
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES, default="EFECTIVO")
    monto_recibido = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), blank=True)  # DecimalField
    cambio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # DecimalField
    recargo_tarjeta = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # DecimalField
    referencia_transferencia = models.CharField(max_length=50, blank=True, null=True)  # Solo para transferencia
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, null=True, blank=True, on_delete=models.SET_NULL)
    impuesto = models.ForeignKey(Impuesto, null=True, blank=True, on_delete=models.SET_NULL)
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE, null=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True)

    def calcular_impuesto_total(self):
        self.impuesto_total = self.subtotal * (
                    self.impuesto.porcentaje / Decimal('100.00')) if self.impuesto else Decimal('0.00')

    def calcular_monto_total(self):
        self.subtotal = Decimal(self.pedido.total_pedido())  # Asegúrate de convertir el subtotal a Decimal
        self.descuento = self.subtotal * (
                    self.promocion.porcentaje_descuento / Decimal('100.00')) if self.promocion else Decimal('0.00')
        self.calcular_impuesto_total()
        self.total = self.subtotal - self.descuento + self.impuesto_total
        self.calcular_total_final()

    def calcular_total_final(self):
        if self.metodo_pago == "TARJETA":
            self.recargo_tarjeta = self.total * Decimal('0.04')  # 4% de recargo
            self.total += self.recargo_tarjeta
        elif self.metodo_pago == "EFECTIVO":
            if self.monto_recibido < self.total:
                raise ValueError("No se canceló el total de la factura.")  # Pago insuficiente

            self.cambio = self.monto_recibido - self.total if self.monto_recibido > self.total else Decimal('0.00')

        elif self.metodo_pago == "TRANSFERENCIA":
            if not self.referencia_transferencia:
                raise ValueError("Se requiere una referencia para la transferencia.")

    def save(self, *args, **kwargs):
        self.calcular_monto_total()
        super().save(*args, **kwargs)
        self.crear_item_factura()

    def crear_item_factura(self):
        for item_pedido in self.pedido.itempedido_set.all():
            ItemFactura.objects.create(
                factura=self,
                producto=item_pedido.producto,
                cantidad=item_pedido.cantidad,
                subtotal=item_pedido.subtotal()
            )

    def __str__(self):
        return str(self.codigo) if self.codigo else f"Factura {self.numero}"


class ItemFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="item")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Items de Factura"

    def __str__(self):
        return f"Item {self.producto.nombre} - {self.cantidad} unidades"

    def calcular_subtotal(self):
        self.subtotal = self.cantidad * self.producto.precio

    def save(self, *args, **kwargs):
        self.calcular_subtotal()
        super().save(*args, **kwargs)

# Modelo para el historial de facturas
class HistorialFactura(models.Model):
    fecha_inicio = models.DateField(default=date.today)  # Fecha de inicio del rango
    fecha_fin = models.DateField(default=date.today)    # Fecha de fin del rango

    @property
    def facturas_lista(self):
        # Filtramos las facturas por el rango de fechas
        facturas = Factura.objects.filter(fecha__range=[self.fecha_inicio, self.fecha_fin])
        # Devolvemos una lista de códigos de las facturas
        return [factura.codigo for factura in facturas]

    def __str__(self):
        return f"Historial desde {self.fecha_inicio} hasta {self.fecha_fin}"