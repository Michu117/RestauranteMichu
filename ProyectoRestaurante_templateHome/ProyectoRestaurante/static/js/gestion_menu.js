// Función para alternar la visibilidad de las categorías
document.getElementById('toggle-menu').addEventListener('click', function() {
    const menuCategories = document.getElementById('menu-categories');
    if (menuCategories.style.display === 'none') {
        menuCategories.style.display = 'block'; // Mostrar el menú
    } else {
        menuCategories.style.display = 'none'; // Ocultar el menú
    }
});
