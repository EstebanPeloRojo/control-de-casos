let tabla = $('#tablaCaso').DataTable( {
    order: [[ 2, 'asc' ]]
})

let tabla2 = $('#tablaCasoActual').DataTable( {
    order: [[ 0, 'dsc' ]]
})

console.log(tabla2)

tabla2.column(4).search('en proceso').draw()
//$('#botonPeticion').click(function(event){
  //  $('#modalCrearcaso').modal('show');
//});

 // Búsqueda por oficina (dropdown)


