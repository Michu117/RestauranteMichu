// Función para alternar la visibilidad de las categorías
document.getElementById('toggle-menu').addEventListener('click', function() {
    const menuCategories = document.getElementById('menu-categories');
    if (menuCategories.style.display === 'none' || menuCategories.style.display === '') {
        menuCategories.style.display = 'block'; // Mostrar el menú
    } else {
        menuCategories.style.display = 'none'; // Ocultar el menú
    }
});

// Inicializar el estado de visibilidad del menú
document.addEventListener('DOMContentLoaded', function() {
    const menuCategories = document.getElementById('menu-categories');
    menuCategories.style.display = 'none'; // Asegurarse de que el menú esté oculto al cargar la página
});
