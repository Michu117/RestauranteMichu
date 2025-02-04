document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();

    let monto = document.querySelector('[name="monto"]').value;

    if (monto <= 0) {
        alert('El monto a convertir debe ser mayor que 0');
    } else {
        this.submit();
    }
});
