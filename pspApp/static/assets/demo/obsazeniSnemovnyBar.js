var data = [{
  x: grafData.labels,
  y: grafData.data,
  type: 'bar',
  marker: {
    color: [
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
    ]
  }
}];
var config = {
  responsive: true
};
var layout = {
  xaxis: { title: 'Kategorie' },
  yaxis: { title: 'Hodnoty' }
};

Plotly.newPlot('obsazeniSnemovnyBar', data, layout,config);