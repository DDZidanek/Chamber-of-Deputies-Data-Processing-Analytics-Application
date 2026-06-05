document.addEventListener('DOMContentLoaded', function() {
    var data = [{
        values: genderPieGraph.values,
        labels: genderPieGraph.labels,
        type: 'pie',
        textinfo: 'label+percent',
        insidetextorientation: 'radial'
    }];
    var config = {
        responsive: true
    };
    var layout = {
        showlegend: true,
        legend: {position: 'top'}
    };

    Plotly.newPlot('genderPie', data, layout,config);
});
