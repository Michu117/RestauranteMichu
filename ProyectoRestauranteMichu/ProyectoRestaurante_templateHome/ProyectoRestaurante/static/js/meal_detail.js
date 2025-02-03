document.addEventListener('DOMContentLoaded', function() {
    // Puedes agregar cualquier interactividad aquí
    console.log('Página de detalles del plato cargada');

    // Ejemplo de interactividad: Desplegar/ocultar instrucciones con un botón
    const instructionsButton = document.querySelector('.meal-instructions');
    instructionsButton.addEventListener('click', function() {
        const instructionsText = document.querySelector('.meal-instructions p');
        instructionsText.style.display = (instructionsText.style.display === 'none' ? 'block' : 'none');
    });
});
