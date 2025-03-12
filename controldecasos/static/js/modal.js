
const container = document.querySelector("#container")
const modalButtons = document.querySelectorAll("#modalButton")



function modalHtml (titulo, data){

    const htmlData = ` <div 
        class="modal fade" id="modalContainer"
        tabindex="-1"
        aria-labelledby="modalContainerLabel"
        aria-hidden="false"
    >
     <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="modalContainerLabel">${titulo}</h1>
          <button type="button" class="btn-close" id="closeBtnEquis" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <h4>Ticket: ${data.ticket}</h4>
          <p> Incidencia: ${data.incidencia} </p>
          <p> Estado: ${data.estado} </p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" id="closeBtnButton" data-bs-dismiss="modal">Close</button>
          <button type="button" id="submibtn"  class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
    </div>

    `

    return htmlData
} 

modalButtons.forEach(element => {
    element.addEventListener('click', async function () {
        console.log(this)
        console.log(this.parentElement.parentElement.children[0].innerHTML)

        const numeroTicket = this.parentElement.parentElement.children[0].innerHTML

        const url = `http://127.0.0.1:8000/casos/casos/?id=${numeroTicket}`

        const req = await fetch(url)
        const data = await req.json();

        console.log(data)


        // insertar html antes del div container
        container.insertAdjacentHTML('beforebegin', modalHtml("modal daniel", data));

        // llamamos el container del modal desde el dom
        const modalContainer = document.querySelector("#modalContainer")

        const removeModal = () =>{
            modalContainer.remove();
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