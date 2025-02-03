document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form'); // Seleccionamos el formulario
    const usernameInput = document.querySelector('#username'); // Campo de usuario
    const passwordInput = document.querySelector('#password'); // Campo de contraseña
    const loginButton = document.querySelector('.login-btn'); // Botón de inicio de sesión

    // Función para validar los campos
    function validateForm() {
        // Comprobar si los campos de usuario y contraseña están vacíos
        if (usernameInput.value.trim() === '' || passwordInput.value.trim() === '') {
            alert('Por favor, complete todos los campos.');
            return false; // No enviar el formulario si los campos están vacíos
        }
        return true; // Si todo está bien, permitir enviar el formulario
    }

    // Agregar un evento de submit al formulario
    form.addEventListener('submit', function (e) {
        if (!validateForm()) {
            e.preventDefault(); // Prevenir el envío del formulario si hay un error
        }
    });

    // Si quieres un evento de clic en el botón
    loginButton.addEventListener('click', () => {
        if (!validateForm()) {
            // Aquí se puede hacer algo más, como agregar un mensaje de error visualmente
        }
    });
});
