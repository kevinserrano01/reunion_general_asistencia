const btnDelete = document.querySelectorAll('.btn-delete')
const fecha = document.getElementById('fechaActual')
const fechaActual = new Date();
const dia = fechaActual.getDate();
const mes = fechaActual.getMonth() + 1; // Los meses comienzan desde 0, así que sumamos 1
const año = fechaActual.getFullYear();
// Formatea la fecha en el formato "Dia-Mes-Año"
const fechaFormateada = `${dia}-${mes}-${año}`;


if (btnDelete) {
    const btnArray = Array.from(btnDelete)
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Estas seguro de deseas eliminarlo?')) {
                e.preventDefault();
            }
        });
    });
}


// Muestra la fecha actual en la pantalla principal
fecha.innerHTML = `Fecha: ${fechaFormateada}`