document.addEventListener('DOMContentLoaded', function () {
    var trace1 = {
        x: Object.keys(legendaData).map(k => k),
        y: Object.values(vyboryData),
        type: 'bar',
        marker: {
            color: colorArray,
        },
        name: 'Počet poslanců',
        hovertext: Object.keys(legendaData).map(k => `${legendaData[k]} (${k})`),
        hoverinfo: 'y+text',
    };
    var config = {
        responsive: true
    };
    var layout = {
        title: {
            text: 'Obsazení poslanců ve výboech',
            font: {
                size: 24
            }
        },
        autosize: true,
        xaxis: {
            tickangle: -45
        },
        yaxis: {
            title: 'Počet poslanců',
            type: 'linear'
        },
        legend: {
            orientation: 'h',
            x: 0.5,
            xanchor: 'center',
            y: -0.3,
            yanchor: 'top'
        },
    };

    Plotly.newPlot('vyboryGraf', [trace1], layout, config);
});
