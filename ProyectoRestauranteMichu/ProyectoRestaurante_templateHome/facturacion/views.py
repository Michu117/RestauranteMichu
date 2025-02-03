from django.shortcuts import render
from .models import Cliente, Factura
from .forms import CedulaForm

def visualizarFacturas(request):
    facturas = None
    if request.method == "POST":
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data["cedula"]
            try:
                cliente = Cliente.objects.get(cedula=cedula)
                facturas = Factura.objects.filter(pedido__cliente=cliente)
            except Cliente.DoesNotExist:
                facturas = []
    else:
        form = CedulaForm()

    return render(request, "visualizar_facturas.html", {"form": form, "facturas": facturas})
