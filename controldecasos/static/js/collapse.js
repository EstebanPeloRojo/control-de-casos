const contenedor = document.querySelector("#container")
const collapseBoton = document.querySelectorAll("#seguimientoCaso")

function collapseHtml(titulo,data)
{
    const collapsecaso = `
    <div class="collapse" id="collapseExample">
        <div class="card card-body">
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
        </div>
    </div>
    `
    
    return collapsecaso
}


collapseBoton.forEach(element => {
    element.addEventListener('click', async function () {
        console.log(this)
        console.log(this.parentElement.parentElement.children[0].innerHTML)

        const numeroTicket = this.parentElement.parentElement.children[0].innerHTML

        const url = `http://127.0.0.1:8000/casos/casos/?id=${numeroTicket}`

        const req = await fetch(url)
        const data = await req.json();

        console.log(data)


        // insertar html antes del div container
        container.insertAdjacentHTML('beforebegin', collapseHtml('Incidencia', data));

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

