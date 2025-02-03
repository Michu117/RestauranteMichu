from django.db import models
from datetime import date, datetime
from mesas.models import Cliente
from menu.models import Producto
from django.db.models.signals import post_save
from django.dispatch import receiver
from inventario.models import MovimientoInventario, Insumo


class Pedido(models.Model):

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
        ('ENPROCESO', 'En Proceso'),
    ]
    codigo = models.CharField(max_length=50, unique=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='PENDIENTE')
    fecha = models.DateField(default=date.today)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    productos = models.ManyToManyField(Producto, through='ItemPedido')

    def total_pedido(self):
        return sum(item.subtotal() for item in self.itempedido_set.all())

    def __str__(self):
        return self.codigo

class ItemPedido(models.Model):
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.FloatField()

    def save(self, *args, **kwargs):
        # Asignamos el precio unitario si no está definido
        if not self.precio_unitario and self.producto.precio:
            self.precio_unitario = self.producto.precio  # Asignamos el precio del producto

        super().save(*args, **kwargs)  # Guardamos el objeto

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.pedido.codigo} - {self.producto.nombre}"

    def actualizar_cantidad_vendida(self):
        self.producto.cantidad_vendida = ItemPedido.objects.filter(producto=self).aggregate(cantidad_vendida=models.Sum('cantidad'))['cantidad_vendida'] or 0
        self.save()


class HistorialPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='historial', verbose_name="Pedido")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Historial")
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Total")

    class Meta:
        verbose_name_plural = "Historial de Pedidos"

    def __str__(self):
        return f"Historial del Pedido {self.pedido.id} - {self.fecha}"

    def save(self, *args, **kwargs):
        # Calcula el monto total del pedido antes de guardar
        self.monto_total = self.pedido.total_pedido()
        super().save(*args, **kwargs)

class Receta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="receta")
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad_necesaria = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.insumo.nombre}: {self.cantidad_necesaria} {self.insumo.unidad_medida}"

@receiver(post_save, sender=Pedido)
def registrar_movimiento_insumos(instance, **kwargs):
    if instance.estado == 'COMPLETADO':  # Solo si el pedido está completado
        for item in instance.itempedido_set.all():
            producto = item.producto
            receta_insumos = Receta.objects.filter(producto=producto)

            for receta in receta_insumos:
                insumo = receta.insumo
                cantidad_total_a_descontar = receta.cantidad_necesaria * item.cantidad

                # Registrar movimiento de salida (inventario se actualizará en la otra señal)
                MovimientoInventario.objects.create(
                    insumo=insumo,
                    tipo='salida',
                    cantidad=cantidad_total_a_descontar,
                    fecha=datetime.now(),
                    descripcion=f"Salida por producción de {producto.nombre} en pedido {instance.codigo}"
                )

@receiver(post_save, sender=MovimientoInventario)
def actualizar_inventario(instance, **kwargs):
    if instance.insumo.cantidad_disponible is None:
        instance.insumo.cantidad_disponible = 0

    if instance.tipo == 'entrada':
        instance.insumo.cantidad_disponible += instance.cantidad
    elif instance.tipo == 'salida':
        instance.insumo.cantidad_disponible -= instance.cantidad

    instance.insumo.save()
    print(f"Inventario actualizado: {instance.insumo.nombre} - {instance.insumo.cantidad_disponible}")