from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mesa, Reserva, Cliente
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.core.exceptions import ValidationError
from .forms import ReservaForm, MesaForm
from django.contrib import messages
from .forms import RegistroClienteForm
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

def home(request):
    return render(request, 'home.html')  # Página principal después de iniciar sesión

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)  # Usando el formulario personalizado
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('home')  # Redirige al home después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas. Intenta de nuevo.')

    else:
        form = CustomAuthenticationForm()  # Formulario vacío para el login

    return render(request, 'login.html', {'form': form})  # Renderiza el formulario de login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda al nuevo usuario
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después de registrarse
        else:
            messages.error(request, 'Por favor, completa todos los campos correctamente.')

    else:
        form = CustomUserCreationForm()  # Forma vacía para el registro

    return render(request, 'register.html', {'form': form})  # Renderiza el formulario de registro

def logout_view(request):  # Vista para cerrar sesión
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('login')  # Redirige a la página de login

class listar_mesas(ListView):
    model = Mesa
    template_name = 'admin/mesas/listar_mesas.html'
    context_object_name = 'mesas'
    paginate_by = 10

    def get_queryset(self):
        return Mesa.objects.all()

class edicion_mesas(UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'admin/mesas/editar_mesas.html'
    success_url = reverse_lazy('listar_mesas')

    def form_valid(self, form):
        return super().form_valid(form)

class crear_mesa(CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'admin/mesas/crear_mesa.html'
    success_url = reverse_lazy('listar_mesas')

def eliminar_mesa(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    mesa.delete()
    return redirect('listar_mesas')

def gestionar_reservas(request):
    reservas = Reserva.objects.all()  # Recuperar todas las reservas de la base de datos
    return render(request, 'mesas/gestionar_reservas.html', {'reservas': reservas})

def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    mesa = reserva.mesa

    # Cambiar el estado de la mesa a LIBRE cuando se cancela la reserva
    mesa.cambiar_estado("LIBRE")

    # Eliminar la reserva
    reserva.delete()

    messages.success(request, f"La reserva de la mesa {mesa.codigo} ha sido cancelada.")
    return redirect('gestionar_reservas')


def nueva_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                reserva = form.save(commit=False)  # Crear la reserva, pero no guardar aún
                mesa = reserva.mesa

                if mesa.estado == "LIBRE":  # Verificar que la mesa esté disponible
                    mesa.cambiar_estado("RESERVADA")  # Cambiar estado de la mesa a RESERVADA
                    reserva.save()  # Guardar la reserva después de modificar el estado de la mesa
                    messages.success(request, 'Reserva creada exitosamente.')
                    return redirect('index')
                else:
                    messages.error(request, 'La mesa seleccionada no está disponible.')
                    return redirect('index')
            except ValidationError as e:
                messages.error(request, e.message)

    else:
        form = ReservaForm()
    return render(request, 'mesas/nueva_reserva.html', {'form': form})

def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)  # Cargar la reserva actual en el formulario
        if form.is_valid():
            try:
                # Guardar los cambios
                reserva_modificada = form.save(commit=False)
                mesa = reserva_modificada.mesa

                # Verificar disponibilidad de la nueva mesa seleccionada antes de guardar
                if mesa.estado == "LIBRE" or mesa == reserva.mesa:
                    if mesa.estado == "LIBRE" and mesa != reserva.mesa:
                        # Si se selecciona una nueva mesa, liberar la mesa anterior
                        reserva.mesa.cambiar_estado("LIBRE")
                        mesa.cambiar_estado("RESERVADA")
                    reserva_modificada.save()
                    messages.success(request, 'Reserva modificada exitosamente.')
                else:
                    messages.error(request, f'La mesa seleccionada ({mesa.identificador}) no está disponible.')
                    return redirect('modificar_reserva', reserva_id=reserva.id)

                return redirect('gestionar_reservas')
            except ValidationError as e:
                messages.error(request, e.message)
        else:
            messages.error(request, 'Por favor, corrige los errores abajo.')
    else:
        form = ReservaForm(instance=reserva)  # Precargar el formulario con los datos existentes

    return render(request, 'mesas/modificar_reserva.html', {'form': form, 'reserva': reserva})

def homeAdmin(request):
    return render(request, 'Admin/homeAdmin.html')

def login_view(request):
    return render(request, 'login.html')

# Vista para la página de registro
def registrar_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Crear Cliente con los datos del formulario
            Cliente.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                cedula=form.cleaned_data['cedula'],
                telefono=form.cleaned_data['telefono'],
                email=form.cleaned_data['email']
            )

            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('inicio')
        else:
            messages.error(request, "Hubo un error en el registro. Verifica los datos.")
    else:
        form = RegistroClienteForm()

    return render(request, 'register.html', {'form': form})