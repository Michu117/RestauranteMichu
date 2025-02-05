from django.contrib.auth import authenticate, logout
from django.http import HttpResponse

from mesas.forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MesaForm
from .models import Mesa, Cliente
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from mesas.admin import Reserva
from .forms import ReservaForm
from django.http import HttpResponse

def homeAdmin(request):
    return render(request, 'Admin/homeAdmin.html')
def home(request):
    return render(request, 'user/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # ✅ Usando .get() para evitar KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('home')  # ✅ Redirige al home después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas. Intenta de nuevo.')

    return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Por si acaso necesita hacer más operaciones
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.id_number = form.cleaned_data.get('id_number')
            user.phone = form.cleaned_data.get('phone')
            user.save()  # Ahora guardamos el usuario completo

            # Guardar también al Usuario como un Cliente
            Cliente.objects.create(
                nombre=user.first_name,
                apellido=user.last_name,
                cedula=user.id_number,
                telefono=user.phone,

            )

            messages.success(request, f'Cuenta creada para {user.username}! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después de registrarse
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def logout_view(request):  # ✅ Nueva vista para cerrar sesión
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('login')

class listar_mesas(ListView):
    model = Mesa
    template_name = 'AdminIndividual/mesas/listar_mesas.html'
    context_object_name = 'mesas'
    paginate_by = 10

    def get_queryset(self):
        return Mesa.objects.all()

class edicion_mesas(UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'AdminIndividual/mesas/editar_mesas.html'
    success_url = reverse_lazy('listar_mesas')

    def form_valid(self, form):
        return super().form_valid(form)

class crear_mesa(CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'AdminIndividual/mesas/crear_mesa.html'
    success_url = reverse_lazy('listar_mesas')

def eliminar_mesa(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    mesa.delete()
    return redirect('listar_mesas')

def listar_reservas(request):
    reservas = Reserva.objects.all().order_by('-fecha')
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva creado exitosamente.")
            return redirect('listar_reservas')  # Redirigir a una página de éxito
        else:
            messages.success(request, "Ingrese datos correctos")
            # Si el formulario no es válido, vuelve a mostrarlo con errores
            return render(request, 'reservas/crear_reserva.html', {'form': form})
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})

def reserva_exito(request):
    return HttpResponse("Reserva realizada con éxito!")

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('listar_reservas')

