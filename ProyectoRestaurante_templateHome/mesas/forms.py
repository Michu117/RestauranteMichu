from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import Reserva, Mesa, Cliente


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
    class Meta:
        model = Reserva
        fields = ['cliente', 'mesa', 'cantidad_personas', 'fecha_reserva']  # Eliminamos horario
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'mesa': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'fecha_reserva': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get('mesa')
        cantidad_personas = cleaned_data.get('cantidad_personas')
        fecha_reserva = cleaned_data.get('fecha_reserva')

        # Verifica si la mesa está disponible para la fecha seleccionada
        if mesa:
            if mesa.estado != "LIBRE":
                raise forms.ValidationError(f"La mesa {mesa.codigo} no está disponible para reservas.")
            if cantidad_personas and cantidad_personas > mesa.numero_asientos:
                raise forms.ValidationError(
                    f"La mesa {mesa.codigo} solo tiene capacidad para {mesa.numero_asientos} personas.")

            # Verifica la disponibilidad de la mesa para esa fecha
            if not Reserva().verificar_disponibilidad(mesa, fecha_reserva):
                raise forms.ValidationError("La mesa no está disponible para la fecha seleccionada.")

        return cleaned_data


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    id_number = forms.CharField(max_length=20, required=True)  # Cédula
    phone = forms.CharField(max_length=15, required=True)  # Teléfono
    username = forms.CharField(max_length=150, required=True)  # Cambié email por username

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id_number', 'phone', 'password1', 'password2')


