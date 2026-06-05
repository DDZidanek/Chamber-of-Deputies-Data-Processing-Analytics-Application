document.addEventListener('DOMContentLoaded', function () {
    
    const backgroundColors = [
        '#0dcaf0', // Nebeská modrá
        '#e83e8c', // Růžová
        '#28a745', // Zelená
        '#dc3545', // Červená
        '#ffc107', // Žlutá
        '#6f42c1', // Tmavě fialová
        '#fd7e14', // Oranžová
        '#20c997', // Mátová
        '#17a2b8', // Světle modrá
        '#6610f2', // Fialová
        '#0077b6', // Modrá
        '#6c757d', // Šedá
        '#fd3a69', // Jasně růžová
        '#adb5bd', // Světle šedá
        '#ffc0cb', // Pastelově růžová
        '#ff5733', // Červenooranžová
        '#f8f9fa', // Téměř bílá
        '#343a40', // Tmavě šedá
        '#007bff', // Oceán modrá
        '#f94144'  // Červená oranžová
    ];
    var config = {
        responsive: true
    };
    const krajeLabels = Object.keys(dataKrajeJson);

    const traces = [];
    Object.keys(dataKrajeJson[Object.keys(dataKrajeJson)[0]]).forEach((strana, index) => {
        const x = [];
        const y = krajeLabels.map(kraj => {
            x.push(kraj);
            return dataKrajeJson[kraj][strana] || 0;
        });
        const trace = {
            x: x,
            y: y,
            name: strana,
            type: 'bar',
            marker: {
                color: backgroundColors[index % backgroundColors.length],
            }
        };
        traces.push(trace);
    });

    var layout = {
        barmode: 'stack',
        title: 'Distribuce poslanců podle stran a krajů',
        xaxis: {title: 'Kraje'},
        yaxis: {title: 'Počty', min: 0},

        autosize: true,
        margin: {l: 50, r: 0, b: 100, t: 100, pad: 4}
    };


    Plotly.newPlot('krajeStranyGraf', traces, layout,config);
});
