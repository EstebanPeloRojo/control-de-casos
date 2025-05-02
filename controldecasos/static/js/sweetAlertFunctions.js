async function swalErr(falla) {
    const result = await Swal.fire({
    //  type: 'error',
    icon:'error',
    title: 'Error',
    text: falla,
   });
}

async function swalAdvice(falla) {

  const result = await Swal.fire({
   icon: 'warning',
   title: 'Error',
   text: falla,
 });
}

async function swalQuestion(title, text){
  const {value: confirmation} = await Swal.fire({
    title: title,
    text: text,
    // icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#0f362d', //'#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Confirmar!'
  })

  if (!confirmation) {
    return false
  }

  return true
}

async function swalConfirmation(text){
  await Swal.fire(
    'Completado!',
    text,
    'success'
  );
  // setTimeout( () => {document.location.reload(true)}, 1500);
}

async function swalConfirmationAndReload(text){
  await Swal.fire(
    'Completado!',
    text,
    'success'
  );
  setTimeout( () => {document.location.reload(true)}, 1500);
}