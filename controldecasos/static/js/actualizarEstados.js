const offcanvasBody = document.querySelector("#offcanvasBody")
const offcanvasExample = document.querySelector("#offcanvasExample")
const estadoCaso  = document.querySelectorAll("#estadoCaso")

function ActualizarEstadoHtml(ticket)
{
    const html = `
    <div>
        
        <h2>Estados</h2>
        <form action="" id="actualizarEstadoForm" method="post">
            <label for="">Ticket: </label>
            <input type="text" class="form-control" name="solicitud_soporte" id="solicitud_soporte" value="${ticket}" readonly>
            
            <label for="estadoCaso">Nuevo estado del caso</label>
            <select class="form-select form-select-lg mb-3" aria-label="Large select example" name="estado" id="estado">
                <option value="" selected>-- Seleccione un estado --</option>
                <option value="Pendiente">Pendiente</option>
                <option value="En proceso">En Proceso</option>
                <option value="Resuelto">Resuelto</option>
            </select>

            <label for="comentario">Feedback tecnico</label>
            <textarea class="form-control" name="comentario" id="comentario"></textarea>

            <input type="submit" value="Aniadir feedback" class="btn btn-primary mt-3" >
        </form>
        
    </div>
    <div class="dropdown mt-3">
      <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown">
        
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
      </ul>
    </div>
    `
    
    return html
}


estadoCaso.forEach(element => {
    element.addEventListener('click', async function () {
        console.log(this)
        console.log(this.parentElement.parentElement.children[0].innerHTML)
       // const filaTabla = this.parentElement.parentElement

        const numeroTicket = this.parentElement.parentElement.children[0].innerHTML

       // const url = `http://127.0.0.1:8000/casos/casos/?id=${numeroTicket}`

       // const req = await fetch(url)
       // const data = await req.json();

       // console.log(data)


        // insertar html antes del div container
        offcanvasBody.insertAdjacentHTML('beforeend', ActualizarEstadoHtml(numeroTicket));

        // llamamos el container del modal desde el dom
        const OffCanvasjs = document.querySelector("#offcanvasBody")

         const removeOffcanvas = () =>{
             offcanvasExample.remove();
         }

        
        const closeBtnButton = document.querySelector("#seguimientoCaso")


        let myOffCanvas = new bootstrap.Offcanvas(offcanvasExample,{
            backdrop: false,
            keyboard: false,
            focus: true,
        });


        myOffCanvas.show()

        offcanvasExample.addEventListener('hidden.bs.offcanvas', event => {
            // do something...
           // removeOffcanvas();
           console.log("Offcanvas closed")
            
           offcanvasBody.innerHTML = "";
        })

        const actualizarEstadoForm = document.querySelector("#actualizarEstadoForm")


        actualizarEstadoForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const formData = new FormData(actualizarEstadoForm);

            // const url = actualizarEstadoForm.action;
            const url = 'http://127.0.0.1:8000/casos/actualizarEstadosTicket/'

            try {

                const csrftoken = getCookie('csrftoken');
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        // "Content-Type": "application/json",
                        'X-CSRFToken': csrftoken,
                        'mode': 'same-origin',
                        'Connection': 'keep-alive',
                        'Cache-Control' : 'no-cache',
                    },
                });

                if (response.status == 200) {
                    const data = await response.json();
                    console.log(data);
                    // Aquí puedes manejar la respuesta del servidor
                    // alert("Estado actualizado correctamente");
                    await swalConfirmation("Estado actualizado correctamente", "success");
                    // removeOffcanvas();

                    window.location.reload(); // Recargar la página para ver los cambios
                } else {
                    console.error('Error al actualizar el estado');
                }
            } catch (error) {
                console.error('Error en la solicitud:', error);
            }


        })
        

        // evento para cerrar el modal con click
        // closeBtnButton.addEventListener('click', () => {
        //     removeOffcanvas()
        // })

    })
})