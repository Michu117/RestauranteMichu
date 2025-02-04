document.addEventListener('DOMContentLoaded', function () {
    // Obtener el formulario y el mensaje de éxito
    const form = document.querySelector('form');
    const mensajeExito = document.getElementById('mensaje-exito');
    const clienteInput = document.getElementById('cliente');
    const productoSelect = document.getElementById('producto');
    const cantidadInput = document.getElementById('cantidad');

    // Función para manejar el envío del formulario
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevenir el envío por defecto

        // Mostrar mensaje de éxito
        mensajeExito.style.display = 'block';

        // Limpiar los campos del formulario después de un breve retraso
        setTimeout(function () {
            // Limpiar los campos
            clienteInput.value = '';
            productoSelect.value = '';
            cantidadInput.value = '';

            // Ocultar el mensaje de éxito
            mensajeExito.style.display = 'none';
        }, 3000); // Esperar 3 segundos antes de limpiar
    });
});
