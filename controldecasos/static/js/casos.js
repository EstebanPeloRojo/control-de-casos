const crearCaso = document.querySelector("#crearCaso");
const formCrearCaso = document.querySelector("#formCrearCaso");

 // aqui querySelector all por que son varios botones eliminar

const csrftoken = getCookie('csrftoken');

formCrearCaso.addEventListener("submit", async (e) => {
    
    e.preventDefault();
    const formData = new FormData(formCrearCaso);

    // descomentar para ver los valores de formdata
    // for (const [key, value] of formData.entries()) {
    //     console.log(`${key}:  ${value}`);
    // }

    const incidencia = formData.get("incidencia");
    const descripcion = formData.get("descripcion");
    const ticket_tilena = formData.get("ticket_tilena");
    if (incidencia == '') {
        await swalErr("Debe seleccionar una incidencia.");
        return;
    }

    if (descripcion == '') {
        await swalErr("La descripción debe tener al menos 10 caracteres.");
        return;
    }

    if (ticket_tilena == '') {
        await swalErr("Debe digitar el ticket.");
        return;
    }

    


    // const data = Object.fromEntries(formData.entries());

    // Enviar la consulta al backend con javascript
    const response = await fetch("/casos/crearcaso/", {
        method: "POST",
        body: formData,
        headers: {
            // "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
            'mode': 'same-origin',
            'Connection': 'keep-alive',
            'Cache-Control' : 'no-cache',
        },
    });

    // obtener el json de la consulta
    const result = await response.json();



    if (response.status === 201) {
        // await alert("Caso creado exitosamente");
        await swalConfirmationAndReload("Caso creado exitosamente");
        window.location.reload();
    } else {
        await swalErr("Error al crear el caso: " + result.error);
    }

})


const eliminarIncidentes = document.querySelectorAll("#eliminarIncidente");


eliminarIncidentes.forEach((eliminarIncidente) => {
    // eliminarIncidente.addEventListener("click", async (e) =>  {

    eliminarIncidente.addEventListener("click", async function (e)  {

        console.log(this)
        console.log(this.parentElement.parentElement.children[0].innerText)

        e.preventDefault();
        const id = this.parentElement.parentElement.children[0].innerText;
        const url = '/casos/casos/';

        const result = await swalQuestion("Eliminar incidente", "¿Está seguro de que desea eliminar el incidente?");

        if (!result) {
            return;
        }

        const response = await fetch(url, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
                // 'mode': 'same-origin',
                // 'Connection': 'keep-alive',
                // 'Cache-Control' : 'no-cache',
            },
            body: JSON.stringify({ id: id })
        });

        // const data = await response.json();

        if (response.status === 204) {
            await swalConfirmationAndReload("Incidente eliminado exitosamente");
            window.location.reload();
        } else {
            await swalErr("no se pudo eliminar");
        }
    })
})