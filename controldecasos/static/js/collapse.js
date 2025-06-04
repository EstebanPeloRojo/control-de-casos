const contenedor = document.querySelector("#container")
const collapseBoton = document.querySelectorAll("#seguimientoCaso")

var toggle = false;

function collapseHtml(titulo,data)
{
    const collapsecaso = `
    <tr class="collapse" id="collapseExample">
        <td colspan="6" class="card-body">
            <div class="row align-items-start">
            <div class="col">
              <p>Ticket: ${data.ticket}</p>
            </div>
            <div class="col">
              <p> Solicitado por: ${data.caso_usuario}</p>
            </div>
            <div class="col">
              <p> Descripcion: ${data.descripcion}</p>
            </div>
            <div class="col">
              <p> Incidencia: ${data.incidencia_id} </p>
            </div>
            <div class="col">
              <p> Fecha: ${data.creado_en}</p>
            </div>
            <div class="col">
              <p> Estado: ${data.estado} </p>
            </div>
              <button type="button" id="cerrar" class="btn-close" aria-label="Close"></button>
            </button>
        </div
        </td>
    </tr>
    `
    
    return collapsecaso
}


collapseBoton.forEach(element => {
    element.addEventListener('click', async function () {

        toggle = !toggle;

        if (toggle == false){
          document.querySelector("#collapseExample").remove()
          return
        }
        

        console.log(this)
        console.log(this.parentElement.parentElement.children[0].innerHTML)
        const filaTabla = this.parentElement.parentElement

        const numeroTicket = this.parentElement.parentElement.children[0].innerHTML

        const url = `http://127.0.0.1:8000/casos/casos/?id=${numeroTicket}`

        const req = await fetch(url)
        const data = await req.json();

        console.log(data)


        // insertar html antes del div container
        filaTabla.insertAdjacentHTML('afterend', collapseHtml('Incidencia', data));

        // llamamos el container del modal desde el dom
        const collapsejs = document.querySelector("#collapseExample")

        const removeCollapse = () =>{
            collapsejs.remove();
        }

        
        const cerrarButton = document.querySelector("#cerrar")


        let myCollapse = new bootstrap.Collapse(collapsejs,{
            backdrop: "static",
            keyboard: false,
            focus: true,
        });


        myCollapse.show()

        

        // evento para cerrar el modal con click
        cerrarButton.addEventListener('click', () => {
            removeCollapse()
        })

    })
})

