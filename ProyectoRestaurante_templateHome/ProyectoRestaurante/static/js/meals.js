// meals.js

document.addEventListener("DOMContentLoaded", function () {
    // Agregar interactividad al hacer hover sobre los elementos de los platos
    const mealItems = document.querySelectorAll('.meal-item');

    mealItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            item.style.transform = 'translateY(-10px)';
            item.style.boxShadow = '0 8px 20px rgba(0, 0, 0, 0.2)';
        });

        item.addEventListener('mouseleave', () => {
            item.style.transform = 'translateY(0)';
            item.style.boxShadow = '0 4px 10px rgba(0, 0, 0, 0.1)';
        });
    });

    // Botón de regreso
    const backButton = document.querySelector('.back-button a');
    if (backButton) {
        backButton.addEventListener('click', (e) => {
            e.preventDefault();
            window.history.back();  // Vuelve a la página anterior
        });
    }
});
