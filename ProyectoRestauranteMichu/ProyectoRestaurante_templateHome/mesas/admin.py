from django.contrib import admin
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Mesa, Persona, Cliente, Personal, Reserva

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'numero_asientos', 'ubicacion', 'estado', 'cantidad_uso', 'ver_mesas_unidas')
    search_fields = ('codigo', 'ubicacion',)
    list_filter = ('estado',)

    # Mostrar las mesas unidas como enlaces en la lista
    def ver_mesas_unidas(self, obj):
        return format_html("<br>".join([mesa.codigo for mesa in obj.mesas_unidas.all()]))

    ver_mesas_unidas.short_description = 'Mesas Unidas'

    actions = ['unir_mesas']

    def unir_mesas(self, request, queryset):
        """
        Acción personalizada para unir mesas seleccionadas
        """
        # Comprobar que se seleccionaron al menos dos mesas
        if queryset.count() < 2:
            self.message_user(request, "Debe seleccionar al menos dos mesas para unir.", level=messages.ERROR)
            return

        # Tomar la primera mesa como principal y las demás como mesas a unir
        mesa_principal = queryset.first()
        mesas_a_unir = queryset.exclude(id=mesa_principal.id)

        try:
            mesa_principal.unir_mesas(mesas_a_unir)
            self.message_user(request,
                              f"Mesas unidas correctamente. La mesa {mesa_principal.codigo} ahora tiene {mesa_principal.numero_asientos} asientos.",
                              level=messages.SUCCESS)
        except ValidationError as e:
            self.message_user(request, str(e), level=messages.ERROR)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'cedula', 'email')
    list_display = ('nombre', 'cedula', 'email', 'telefono')



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'cedula', 'email')
    list_display = ('nombre', 'cedula', 'email')
   # Puedes añadir un filtro personalizado dependiendo de relaciones.



@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre','identificador_Personal', 'cedula', 'email',)
    list_filter = ('identificador_Personal',)
    search_fields = ('nombre', 'email',)



from datetime import timedelta

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'cliente', 'mesa', 'estado', 'fecha_reserva', 'horario_inicio', 'hora_reserva_finalizada', 'duracion')
    list_filter = ('estado', 'fecha_reserva')
    search_fields = (
        'identificador',
        'cliente__nombre',
        'mesa__codigo',
        'cliente__email',
        'cliente__telefono',
        'estado',
        'fecha_reserva',
    )
    ordering = ('fecha_reserva', 'horario_inicio')
    list_editable = ('estado', 'mesa')

    # Campo calculado para la duración de la reserva
    def duracion(self, obj):
        if obj.hora_reserva_finalizada and obj.horario_inicio:
            duracion = obj.hora_reserva_finalizada - obj.horario_inicio
            # Retorna en formato horas:minutos
            return str(timedelta(seconds=duracion.total_seconds()))
        return "Sin finalizar"
    duracion.short_description = "Duración"

    # Campo coloreado para el estado con icono
    def estado_coloreado(self, obj):
        colores = {
            'CONFIRMADA': ('green', '✔️'),
            'CANCELADA': ('red', '❌'),
            'FINALIZADA': ('blue', '✅'),
            'ENCURSO': ('orange', '⏳'),
        }
        color, icono = colores.get(obj.estado, ('black', '❔'))
        return format_html(
            '<span style="color: {};">{} {}</span>',
            color,
            icono,
            obj.estado
        )
    estado_coloreado.short_description = "Estado"

    def cancelar_reserva(self, request, queryset):
        """
        Acción personalizada para cancelar reservas desde el admin.
        """
        for reserva in queryset:
            reserva.cancelar_reserva(reserva.identificador)
        self.message_user(request, f"{queryset.count()} reserva(s) cancelada(s) correctamente.")

    actions = ['cancelar_reserva']  # Registra la acción en el admin.