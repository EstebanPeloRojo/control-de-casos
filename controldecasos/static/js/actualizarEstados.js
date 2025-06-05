const offcanvasBody = document.querySelector("#offcanvasBody")
const offcanvasExample = document.querySelector("#offcanvasExample")
const estadoCaso  = document.querySelectorAll("#estadoCaso")
const labelHistorico = document.querySelector("#labelHistorico")
const historicoBody = document.querySelector("#historicoBody")



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

            <input type="submit" value="Añadir feedback" class="btn btn-primary mt-3" >
        </form>
        
    </div>
    `
    return html
}

function seguimientoCasoHtml(registros)
{
    
    let html = ''
    
    registros.forEach(registro => html += `
    
    <tr class="collapse" id="collapseExample">
        <td colspan="6" class="card-body">
            <div class="row align-items-start">
            <div class="col">
              <p>Fecha: ${formatearFecha(registro.fecha_cambio)}</p>
            </div>
            <div class="col">
              <p> Estado: ${registro.estado}</p>
            </div>
            <div class="col">
              <p> Observaciones:${registro.comentario}</p>
            </div>
            <div class="col">
              <p> Publicado por: ${registro.usuario} </p>
            </div>
           
              <button type="button" id="cerrar" class="btn-close" aria-label="Close"></button>
            </button>
        </div
        </td>
    </tr>
    
    `)

    console.log(html)
    return html

    
}



//const offcanvasCerrar =  document.querySelector("#offcanvasCerrar")

//const removeSeguimiento = () =>{
//            labelHistorico.remove();
//        }

//offcanvasCerrar.ddEventListener('click', () => {
 //           removeSeguimiento()
 //       })

estadoCaso.forEach(element => {
    element.addEventListener('click', async function () {
        console.log(this)
        console.log(this.parentElement.parentElement.children[0].innerHTML)
       // const filaTabla = this.parentElement.parentElement

        const numeroTicket = this.parentElement.parentElement.children[0].innerHTML

       const url = `http://127.0.0.1:8000/casos/VerEstadosTicket/1`

       const req = await fetch(url)
       const data = await req.json();

       console.log(data)

       


        // insertar html antes del div container
        historicoBody.insertAdjacentHTML('beforeend', seguimientoCasoHtml(data));
        labelHistorico.insertAdjacentHTML('beforebegin', ActualizarEstadoHtml(numeroTicket));

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