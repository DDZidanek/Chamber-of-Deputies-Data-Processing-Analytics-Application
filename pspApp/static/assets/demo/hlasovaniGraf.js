document.addEventListener('DOMContentLoaded', function () {

    const backgroundColors = [
        '#28a745', // Zelená
        '#dc3545', // Červená
        '#ffc107', // Žlutá
        '#6f42c1', // Tmavě fialová
    ];
    const hlasyLabels = Object.keys(hlasovaniStranyData);
    const datasets = Object.keys(hlasovaniStranyData[hlasyLabels[0]]).map((typHlasu, index) => ({
        x: hlasyLabels,
        y: hlasyLabels.map(strana => hlasovaniStranyData[strana][typHlasu]),
        type: 'bar',
        name: typHlasu,
        marker: {
            color: backgroundColors[index % backgroundColors.length],
        },
    }));

    const layout = {
        title: 'Výsledky hlasování podle stran',
        barmode: 'group',
        yaxis: {
            type: 'log',
            title: 'Počet hlasů',
        },
    };
    var config = {
        responsive: true
    };
    Plotly.newPlot('hlasovaniStranyGrafBar', datasets, layout,config);
});

document.addEventListener('DOMContentLoaded', function () {
    const backgroundColors = [
        '#28a745', // Zelená
        '#dc3545', // Červená
        '#ffc107', // Žlutá
        '#6f42c1', // Tmavě fialová
    ];
    var config = {
        responsive: true
    };
    const hlasyLabels = Object.keys(hlasovaniStranyData);
    const datasets = Object.keys(hlasovaniStranyData[hlasyLabels[0]]).map((typHlasu, index) => ({
        x: hlasyLabels,
        y: hlasyLabels.map(strana => hlasovaniStranyData[strana][typHlasu]),
        type: 'line',
        name: typHlasu,
        marker: {
            color: backgroundColors[index % backgroundColors.length],
        },
    }));

    const layout = {
        title: 'Výsledky hlasování podle stran',
        barmode: 'group',
        yaxis: {
            type: 'log',
            title: 'Počet hlasů',
        },
    };

    Plotly.newPlot('hlasovaniStranyGrafLine', datasets, layout,config);
});
