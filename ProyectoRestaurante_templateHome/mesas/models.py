from django.core.exceptions import ValidationError
from django.db import models
from enum import Enum

class EstadoReserva(Enum):
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    FINALIZADA = "FINALIZADA"
    ENCURSO = "ENCURSO"


class Mesa(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=True)
    numero_asientos = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"Mesa {self.codigo} - Capacidad {self.numero_asientos}"


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


class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name="reservas")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas", null=True)
    fecha = models.DateField(null=True)
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)

    def clean(self):
        # Validar si el horario de la reserva se solapa con otras reservas para la misma mesa en la misma fecha
        reservas_conflictivas = Reserva.objects.filter(
            mesa=self.mesa,
            fecha=self.fecha
        ).exclude(id=self.id)  # Excluir la reserva actual si ya existe

        for reserva in reservas_conflictivas:
            if self.hora_inicio < reserva.hora_fin and self.hora_fin > reserva.hora_inicio:
                raise ValidationError(f"La mesa {self.mesa.codigo} ya está reservada en ese horario.")

    def __str__(self):
        return f"Reserva de {self.cliente} - Mesa {self.mesa.codigo} - {self.fecha} {self.hora_inicio}-{self.hora_fin}"
