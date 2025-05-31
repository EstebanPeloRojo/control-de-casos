const contenedor = document.querySelector("#container")
const collapseBoton = document.querySelectorAll("#seguimientoCaso")

function collapseHtml(titulo,data)
{
    const collapsecaso = `
    <tr class="collapse" id="collapseExample">
        <td colspan="6" >
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
        </div
        </td>
    </tr>
    `
    
    return collapsecaso
}


collapseBoton.forEach(element => {
    element.addEventListener('click', async function () {
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

        
        const closeBtnButton = document.querySelector("#seguimientoCaso")


        let myCollapse = new bootstrap.Collapse(collapsejs,{
            backdrop: "static",
            keyboard: false,
            focus: true,
        });


        myCollapse.show()

        

        // evento para cerrar el modal con click
        closeBtnButton.addEventListener('click', () => {
            removeCollapse()
        })

    })
})

