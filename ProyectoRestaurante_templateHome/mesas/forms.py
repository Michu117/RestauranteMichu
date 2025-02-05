from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from mesas.models import Mesa, Reserva

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['codigo', 'ubicacion', 'numero_asientos']

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
        fields = ['mesa', 'cliente', 'fecha', 'hora_inicio', 'hora_fin']

    widgets = {
        'fecha': forms.DateInput(attrs={'type': 'date'}),  # Selector de fecha (calendario)
        'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),  # Selector de hora (reloj)
        'hora_fin': forms.TimeInput(attrs={'type': 'time'}),  # Selector de hora (reloj)
    }

    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get("mesa")
        fecha = cleaned_data.get("fecha")
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_fin = cleaned_data.get("hora_fin")

        # Validar que la hora de inicio sea antes que la hora de fin
        if hora_inicio >= hora_fin:
            raise forms.ValidationError("La hora de inicio debe ser antes que la hora de fin.")

        # Validar si ya existe una reserva para la misma mesa y hora
        reservas_conflictivas = Reserva.objects.filter(
            mesa=mesa,
            fecha=fecha
        ).exclude(id=self.instance.id)  # Excluir la reserva actual si ya existe

        for reserva in reservas_conflictivas:
            if hora_inicio < reserva.hora_fin and hora_fin > reserva.hora_inicio:
                raise forms.ValidationError(f"La mesa {mesa.codigo} ya está reservada en ese horario.")

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


