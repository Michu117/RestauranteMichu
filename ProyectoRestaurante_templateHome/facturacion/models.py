from django.db import models
from datetime import date
from mesas.models import Persona, Cliente, Mesa
from menu.models import Producto
from pedidos.models import Pedido, ItemPedido

class Impuesto(models.Model):
    nombre = models.CharField(max_length=50)
    porcentaje = models.FloatField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Promocion(models.Model):
    descripcion = models.CharField(max_length=255)
    porcentaje_descuento = models.FloatField()

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
    subtotal = models.FloatField(default=0.0)
    impuesto_total = models.FloatField(default=0.0)
    descuento = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES, default="EFECTIVO")
    monto_recibido = models.FloatField(default=0.0, blank=True)
    cambio = models.FloatField(default=0.0)
    recargo_tarjeta = models.FloatField(default=0.0)
    referencia_transferencia = models.CharField(max_length=50, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, null=True, blank=True, on_delete=models.SET_NULL)
    impuesto = models.ForeignKey(Impuesto, null=True, blank=True, on_delete=models.SET_NULL)
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE, null=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True)

    def calcular_impuesto_total(self):
        self.impuesto_total = self.subtotal * (self.impuesto.porcentaje / 100.0) if self.impuesto else 0.0

    def calcular_monto_total(self):
        self.subtotal = float(self.pedido.total_pedido())
        self.descuento = self.subtotal * (self.promocion.porcentaje_descuento / 100.0) if self.promocion else 0.0
        self.calcular_impuesto_total()
        self.total = self.subtotal - self.descuento + self.impuesto_total
        self.calcular_total_final()

    def calcular_total_final(self):
        if self.metodo_pago == "TARJETA":
            self.recargo_tarjeta = self.total * 0.04
            self.total += self.recargo_tarjeta
        elif self.metodo_pago == "EFECTIVO":
            if self.monto_recibido < self.total:
                raise ValueError("No se canceló el total de la factura.")

            self.cambio = self.monto_recibido - self.total if self.monto_recibido > self.total else 0.0

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
    subtotal = models.FloatField()

    class Meta:
        verbose_name_plural = "Items de Factura"

    def __str__(self):
        return f"Item {self.producto.nombre} - {self.cantidad} unidades"

    def calcular_subtotal(self):
        self.subtotal = self.cantidad * self.producto.precio

    def save(self, *args, **kwargs):
        self.calcular_subtotal()
        super().save(*args, **kwargs)

class HistorialFactura(models.Model):
    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField(default=date.today)

    @property
    def facturas_lista(self):
        facturas = Factura.objects.filter(fecha__range=[self.fecha_inicio, self.fecha_fin])
        return [factura.codigo for factura in facturas]

    def __str__(self):
        return f"Historial desde {self.fecha_inicio} hasta {self.fecha_fin}"
