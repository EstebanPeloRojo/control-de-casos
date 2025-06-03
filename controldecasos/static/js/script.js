let tabla = $('#tablaCaso').DataTable( {
    order: [[ 1, 'asc' ]]
})

//$('#botonPeticion').click(function(event){
  //  $('#modalCrearcaso').modal('show');
//});

 // Búsqueda por oficina (dropdown)
$('#busquedaEstado').on('change', function() {
    tabla.column(4).search(this.value).draw();
});


