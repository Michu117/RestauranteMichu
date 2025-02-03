from django import forms

class CedulaForm(forms.Form):
    cedula = forms.CharField(label="Número de Cédula", max_length=20)
