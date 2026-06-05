document.addEventListener('DOMContentLoaded', function() {    
    
    console.log(vekPoslancuGraphData);
    var config = {
        responsive: true
    };

    var boxTrace = {
        y: vekPoslancuGraphData,
        type: 'box',
        name: 'Věk poslanců',
        boxpoints: 'all',
        jitter: 0.3,
        pointpos: -1.8,
        marker: {color: '#FF4136'},
    };



    var data = [boxTrace];

    var layout = {
        title: 'Rozsah věku poslanců',
        yaxis: {
            title: 'Věk',
            zeroline: true
        }
    };
    
    Plotly.newPlot('vekPoslancuBoxplot', data, layout, config);
});
