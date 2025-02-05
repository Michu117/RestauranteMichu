from django.contrib import admin
from mesas.models import Mesa, Persona, Cliente, Reserva


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    # Mostrar campos en la lista de mesas
    list_display = ('codigo', 'numero_asientos', 'ubicacion')
    search_fields = ('codigo', 'ubicacion')  # Buscar por código o ubicación
    ordering = ('codigo',)  # Ordenar por código de mesa


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'cedula', 'telefono',)
    list_display = ('nombre', 'cedula', 'telefono',)



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'cedula',)
    list_display = ('nombre', 'cedula',)
   # Puedes añadir un filtro personalizado dependiendo de relaciones.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    # Mostrar campos en la lista de reservas
    list_display = ('cliente', 'mesa', 'fecha', 'hora_inicio', 'hora_fin', 'estado_reserva')
    list_filter = ('fecha', 'mesa', 'hora_inicio', 'hora_fin')  # Filtros para facilitar la búsqueda
    search_fields = ('mesa__codigo',)  # Buscar por nombre del cliente o código de mesa
    ordering = ('fecha', 'hora_inicio')  # Ordenar por fecha y hora de inicio

    # Añadir un campo para mostrar el estado de la reserva (puedes personalizarlo más)
    def estado_reserva(self, obj):
        if obj.hora_inicio < obj.hora_fin:
            return "Disponible"
        return "No disponible"
    estado_reserva.short_description = 'Estado de la Reserva'
