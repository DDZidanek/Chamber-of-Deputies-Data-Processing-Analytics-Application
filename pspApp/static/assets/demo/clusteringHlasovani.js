document.addEventListener('DOMContentLoaded', function() {
    var sse_trace = {
        x: Object.keys(sse_hl_pos_data),
        y: Object.values(sse_hl_pos_data),
        type: 'scatter',
        mode: 'lines+markers',
        marker: { size: 8 }
    };

    var sse_data = [sse_trace];

    var config = {
        autosize: true,
        responsive: true,
    };

    var sse_layout = {
        title: 'Optimální počet shluků (Elbow Method)',
        xaxis: {
            title: 'ID shluku',
            type: 'category',
        },
        yaxis: {
            title: 'Sum of Squared Errors (SSE)'
        },
    };

    Plotly.newPlot('sse_plot', sse_data, sse_layout, config);
});
