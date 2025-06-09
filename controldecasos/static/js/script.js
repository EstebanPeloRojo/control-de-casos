
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
tabla2.column(4).search('en proceso|en progreso|pendiente', true, false).draw()
tabla3.column(4).search('resuelto', true, false).draw()


// // variable que contiene la estructura del gráfico
const chart = Highcharts.chart('graficoEstados', {
    chart: {
        type: 'pie',
        styledMode: true
    },
    title: {
        text: 'Grafico de Casos por Estado'
    },
    series: [
        {
            data: chartData(tabla)
        }
    ]
});

// Obtiene los datos de la tabla y actualiza el gráfico al cargar la página
tabla.on('draw', function () {
    chart.series[0].setData(chartData(tabla));
});
 
function chartData(tabla) {
    var counts = {};

     var estadosNormalizados = {
        'pendiente': 'Pendiente',
        'en proceso': 'En proceso',
        'en progreso': 'En proceso', // Normalizar "En progreso" a "En proceso"
        'resuelto': 'Resuelto'
    };
 
    // Count the number of entries for each position
    tabla
        .column(4, { search: 'applied' })
        .data()
        .each(function (val) {
        if (val){
            var cleanVal = val.toString().trim().toLowerCase();
            // Normalizar el estado usando el mapeo
             var normalizedState = estadosNormalizados[cleanVal] || val.toString().trim();
            if (counts[normalizedState]) {
                counts[normalizedState] += 1;
            }
            else {
                counts[normalizedState] = 1;
            }
        }
        });

        console.log('Estados contados:', counts);
 
    return Object.entries(counts).map((e) => ({
        name: e[0],
        y: e[1]
    }));
}


