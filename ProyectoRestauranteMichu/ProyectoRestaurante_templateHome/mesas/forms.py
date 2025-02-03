from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import Reserva, Mesa

# Formulario de creación de usuario personalizado
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    id_number = forms.CharField(max_length=20, required=True)  # Cédula
    phone = forms.CharField(max_length=15, required=True)  # Teléfono

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id_number', 'phone', 'password1', 'password2')  # Campos necesarios

# Formulario de autenticación personalizado
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}),
        label="Nombre de Usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}),
        label="Contraseña"
    )

    class Meta:
        fields = ['username', 'password']  # Campos que se incluirán en el formulario



class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['codigo', 'ubicacion', 'numero_asientos', 'cantidad_uso', 'estado']

class RegistroClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirmar_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    cedula = forms.CharField(max_length=10, required=True)
    telefono = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirmar_password")

        if password != confirmar_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class ReservaForm(forms.ModelForm):
    def hacer_reserva(self):
        self.mesa.cambiar_estado("RESERVADA")
        self.save()
    class Meta:
        model = Reserva
        fields = ['cliente', 'mesa', 'cantidad_personas', 'fecha_reserva', 'horario_inicio']

        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'horario_inicio': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local', 'placeholder': 'AAAA-MM-DD hh:mm'}
            ),
        }

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        # Mostrar solo las mesas disponibles (en estado LIBRE)
        self.fields['mesa'].queryset = Mesa.objects.filter(estado="LIBRE")

    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get('mesa')
        cantidad_personas = cleaned_data.get('cantidad_personas')

        # Verificar si la mesa está disponible de manera explícita
        if mesa.estado != "LIBRE":
            raise ValidationError(f'La mesa {mesa.identificador} no está disponible para reservas.')

        # Verificar si la cantidad de personas excede la capacidad de la mesa
        if cantidad_personas > mesa.numero_asientos:
            raise ValidationError(
                f'La mesa seleccionada tiene una capacidad máxima de {mesa.numero_asientos} personas.')

        return cleaned_data

def nueva_reserva(request, mesa=None):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                # Guardar la reserva
                reserva = form.save(commit=False)
                reserva.hacer_reserva()

                # Cambiar el estado de la mesa a RESERVADA
                if mesa.estado == "LIBRE":
                    mesa.cambiar_estado("RESERVADA")
                else:
                    messages.error(request, f"La mesa {mesa.identificador} ya no está disponible.")
                    return redirect('gestionar_reservas')

                reserva.save()
                messages.success(request, 'Reserva creada exitosamente.')
                return redirect('gestionar_reservas')
            except ValidationError as e:
                # Si ocurre un error de validación
                messages.error(request, e.message)
        else:
            # Si hay errores en el formulario
            messages.error(request, 'Por favor, corrige los errores mostrados en el formulario.')
    else:
        form = ReservaForm()

    return render(request, 'mesas/nueva_reserva.html', {'form': form})

def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    mesa = reserva.mesa

    # Cambiar el estado de la mesa a LIBRE
    mesa.cambiar_estado("LIBRE")

    # Eliminar la reserva
    reserva.delete()

    messages.success(request, f"La reserva de la mesa {mesa.codigo} ha sido cancelada.")
    return redirect('gestionar_reservas')