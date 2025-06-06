
//variables tabla busca en casos.html con el respectivo id y aplica la libreria datatables
let tabla = $('#tablaCaso').DataTable( {
    order: [[ 0, 'dsc' ]]
})
//variables tabla2 busca en casosactuales.html con el respectivo id y aplica la libreria datatables
let tabla2 = $('#tablaCasoActual').DataTable( {
    order: [[ 0, 'dsc' ]]
})
//variables tabla3 busca en casohistorico.html con el respectivo id y aplica la libreria datatables
let tabla3 = $('#tablaCasoHistorico').DataTable( {
    order: [[ 0, 'dsc' ]]
})

console.log(tabla2)

// Filtra la tabla del template casosactuales.html para que muestre los casos en estado "Pendiente" o "En proceso"
tabla2.column(4).search('en proceso|pendiente', true, false).draw()
tabla3.column(4).search('resuelto', true, false).draw()



