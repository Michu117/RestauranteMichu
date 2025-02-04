from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pedido, ItemPedido
from .forms import PedidoForm, ItemPedidoForm

def gestionar_pedidos(request):
    if request.method == 'POST':
        # Si se está creando un nuevo pedido
        if 'crear_pedido' in request.POST:
            form = PedidoForm(request.POST)
            if form.is_valid():
                # Guardamos el pedido
                pedido = form.save()  # Guardamos el pedido con cliente
                producto = form.cleaned_data.get('producto')  # Obtenemos el producto
                cantidad = form.cleaned_data.get('cantidad')  # Obtenemos la cantidad

                # Creamos el ItemPedido
                ItemPedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad, precio_unitario=producto.precio)

                messages.success(request, 'Pedido creado con éxito.')
                return redirect('gestionar_pedidos')

    else:
        form = PedidoForm()  # Formulario para crear un nuevo pedido

    pedidos = Pedido.objects.all().order_by('-fecha')  # Obtener todos los pedidos
    return render(request, 'user/pedidos.html', {
        'pedidos': pedidos,
        'form': form,
    })
