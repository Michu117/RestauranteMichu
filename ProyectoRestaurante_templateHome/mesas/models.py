from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum
from django.db.models import Manager
from abc import ABC, abstractmethod


class EstadoMesa(Enum):
    LIBRE = "LIBRE"
    OCUPADA = "OCUPADA"
    RESERVADA = "RESERVADA"

class EstadoReserva(Enum):
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    FINALIZADA = "FINALIZADA"
    ENCURSO = "ENCURSO"


class Mesa(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=True)
    numero_asientos = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    cantidad_uso = models.PositiveIntegerField(default=0)
    estado = models.CharField(
        max_length=10,
        choices=[(tag.name, tag.value) for tag in EstadoMesa],
        default=EstadoMesa.LIBRE.name,
        verbose_name="Estado"
    )
    mesas_unidas: Manager = models.ManyToManyField('self', blank=True, symmetrical=False)
    hora_disponible = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Mesa {self.codigo} - Capacidad {self.numero_asientos}"

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de la mesa al nuevo estado dado.
        Valida que el nuevo estado sea válido antes de realizar el cambio.
        """
        if nuevo_estado not in [estado.name for estado in EstadoMesa]:
            raise ValueError(
                f"Estado '{nuevo_estado}' no es válido. Los estados válidos son: {[estado.name for estado in EstadoMesa]}")
        self.estado = nuevo_estado
        self.save()

    def validar_disponibilidad(self, horario_inicio):
        return self.hora_disponible > horario_inicio

    def unir_mesas(self, otras_mesas):
        total_asientos = self.numero_asientos
        for mesa in otras_mesas:
            if mesa.estado != EstadoMesa.LIBRE.name:
                raise ValidationError(f"La mesa {mesa.codigo} no está libre para ser unida.")
            total_asientos += mesa.numero_asientos
            mesa.cantidad_uso += 1
            mesa.save()

        # Actualizamos la mesa principal
        self.numero_asientos = total_asientos
        self.cantidad_uso += 1
        self.save()

        # Agregamos las mesas unidas a la relación ManyToMany
        self.mesas_unidas.add(*otras_mesas)
        self.save()

        return self


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15, unique=True)


class Cliente(Persona):
    def __str__(self):
        return self.nombre

    def actualizar_informacion(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.save()

    def ver_reservas(self):
        return self.reserva_set.all()

    def consultar_disponibilidad(self, mesa):
        return mesa.validar_disponibilidad()

    def hacer_reserva(self, datos_reserva):
        """
        Crear una nueva reserva asociada al cliente.
        """
        reserva = Reserva.objects.create(
            cliente=self,
            mesa=datos_reserva['mesa'],
            cantidad_personas=datos_reserva['cantidad_personas'],
            fecha_reserva=datos_reserva['fecha_reserva'],
            horario_inicio=datos_reserva['horario_inicio']
        )
        reserva.save()
        return reserva

    def cancelar_reserva(self, identificador_reserva):
        """
        Cancelar una reserva existente asociada al cliente.
        """
        try:
            reserva = Reserva.objects.get(identificador=identificador_reserva, cliente=self)
            reserva.estado = EstadoReserva.CANCELADA.name
            reserva.save()
        except Reserva.DoesNotExist:
            raise ValueError("No se encontró la reserva especificada o no pertenece a este cliente.")


from django.core.exceptions import ValidationError
from django.db import models


class Reserva(models.Model):
    identificador = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cantidad_personas = models.IntegerField()
    fecha_reserva = models.DateField()
    estado = models.CharField(
        max_length=15,
        choices=[(tag.name, tag.value) for tag in EstadoReserva],
        default=EstadoReserva.CONFIRMADA.name
    )

    def __str__(self):
        return f'{self.cliente.nombre} - {self.fecha_reserva}'

    def modificar_reserva(self, nuevos_datos):
        for key, value in nuevos_datos.items():
            setattr(self, key, value)
        self.save()

    def verificar_disponibilidad(self, mesa, fecha_reserva):
        # Verificar si hay otras reservas en la misma mesa para la misma fecha
        reservas_conflictivas = Reserva.objects.filter(
            mesa=mesa,
            fecha_reserva=fecha_reserva,
            estado__in=[EstadoReserva.CONFIRMADA.name, EstadoReserva.ENCURSO.name]
        )
        return reservas_conflictivas.count() == 0

    def finalizar_reserva(self):
        self.estado = EstadoReserva.FINALIZADA.name
        self.save()

    def hacer_reserva(self, datos_reserva):
        """
        Crear una nueva reserva basada en los datos proporcionados.
        """
        if not self.verificar_disponibilidad(
                datos_reserva['mesa'],
                datos_reserva['fecha_reserva']
        ):
            raise ValidationError(f"La mesa {datos_reserva['mesa'].codigo} ya está reservada para esa fecha.")

        reserva = Reserva.objects.create(
            cliente=datos_reserva['cliente'],
            mesa=datos_reserva['mesa'],
            cantidad_personas=datos_reserva['cantidad_personas'],
            fecha_reserva=datos_reserva['fecha_reserva'],
        )
        reserva.save()
        return reserva

    def cancelar_reserva(self, identificador_reserva):
        """
        Cancelar la reserva actual si coincide con el identificador.
        """
        if self.identificador == identificador_reserva:
            self.estado = EstadoReserva.CANCELADA.name
            self.save()
        else:
            raise ValueError("El identificador de reserva no coincide.")

    def save(self, *args, **kwargs):
        # Validar que la mesa tenga suficiente capacidad antes de guardar la reserva
        if self.cantidad_personas > self.mesa.numero_asientos:
            raise ValidationError(
                f"La mesa {self.mesa.codigo} solo tiene capacidad para {self.mesa.numero_asientos} personas.")

        # Verificar que la mesa esté libre
        if self.mesa.estado != "LIBRE":
            raise ValidationError(f"La mesa {self.mesa.codigo} no está disponible para reservas.")

        # Verificación de disponibilidad para la fecha
        if not self.verificar_disponibilidad(self.mesa, self.fecha_reserva):
            raise ValidationError("La mesa ya está reservada para esa fecha.")

        super().save(*args, **kwargs)



class Personal(Persona):
    identificador_Personal = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name_plural = "Personal"

    def notificar_mesa_lista(self, mesas):
        """
        Genera una notificación indicando que las mesas están listas.
        """
        for mesa in mesas:
            if mesa.estado == EstadoMesa.LIBRE.name:
                print(f"Mesa {mesa.identificador} está lista para ser ocupada.")

    def __str__(self):
        return f"{self.nombre} ({self.identificador_Personal})"

class iReserva(ABC):
    @abstractmethod
    def hacer_reserva(self, datos_reserva):
        """
        Realizar una nueva reserva.
        Parámetros:
        - datos_reserva: dict con la información necesaria para crear la reserva.
        """
        reserva = Reserva.objects.create(
            cliente=datos_reserva['cliente'],
            mesa=datos_reserva['mesa'],
            cantidad_personas=datos_reserva['cantidad_personas'],
            fecha_reserva=datos_reserva['fecha_reserva'],
            horario_inicio=datos_reserva['horario_inicio']
        )
        reserva.save()
        return reserva

    @abstractmethod
    def cancelar_reserva(self, identificador_reserva):
        """
        Cancelar una reserva existente.
        Parámetros:
        - identificador_reserva: ID único de la reserva a cancelar.
        """
        reserva = Reserva.objects.get(identificador=identificador_reserva)
        reserva.estado = EstadoReserva.CANCELADA.name
        reserva.save()
