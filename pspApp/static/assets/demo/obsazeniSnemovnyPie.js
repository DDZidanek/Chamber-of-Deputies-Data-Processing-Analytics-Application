document.addEventListener('DOMContentLoaded', function() {

    var config = {
        responsive: true
    };

    var data = [{
        values: grafData.data,
        labels: grafData.labels,
        type: 'pie', 
        textinfo: 'label+percent', 
        insidetextorientation: 'radial',
        hoverinfo: 'label+percent',
        textposition: 'inside'
    }];

    var layout = {
        showlegend: true,
        legend: {position: 'top'},
    };

    Plotly.newPlot('obsazeniSnemovnyPie', data, layout,config);
});