const contenedor = document.querySelector("#container")
const collapseBoton = document.querySelectorAll("#seguimientoCaso")

function collapseHtml(titulo,data)
{
    const collapsecaso = `
    <div class="collapse" id="collapseExample">
        <div class="card card-body">
            paspadapsdpasdpadpasdadpojsaop
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

        const closeBtnEquis = document.querySelector("#closeBtnEquis")
        const closeBtnButton = document.querySelector("#closeBtnButton")


        let myModal = new bootstrap.Modal(modalContainer,{
            backdrop: "static",
            keyboard: false,
            focus: true,
        });


        myModal.show()

        // evento para cerrar el modal con click
        closeBtnEquis.addEventListener('click', () => {
            removeModal()
        })

        // evento para cerrar el modal con click
        closeBtnButton.addEventListener('click', () => {
            removeModal()
        })

    })
})

