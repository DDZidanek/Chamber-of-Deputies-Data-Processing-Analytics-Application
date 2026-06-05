document.addEventListener('DOMContentLoaded', function() {    
  
  console.log(vyboryHistData);
  
  var data = [{
      x: vyboryHistData.osa_x,
      y: vyboryHistData.osa_y,
      type: 'bar',
      marker: {
          color: 'orange',
          line: {
            color: 'black',
            width: 1
          }
      },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: 'Počet poslanců podle počtu výborů',
      xaxis: {title: 'Počet výborů',tickvals: vyboryHistData.osa_x},
      yaxis: {title: 'Počet poslanců',type: 'log',
      autorange: true},
  };

  Plotly.newPlot('vyboryHist', data, layout, config);
});
document.addEventListener('DOMContentLoaded', function() {    
  
  console.log(vyboryHistData);
  
  var data = [{
      x: vyboryHistData.osa_x,
      y: vyboryHistData.osa_y,
      mode: 'markers',
      marker: {
        size: 10,
        color: 'orange'
    },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: 'Počet poslanců podle počtu výborů',
      xaxis: {title: 'Počet výborů',tickvals: vyboryHistData.osa_x},
      yaxis: {title: 'Počet poslanců'},
  };

  Plotly.newPlot('vyboryMarkers', data, layout, config);
});
// ------------------------

document.addEventListener('DOMContentLoaded', function() {    
  
  console.log(podvyboryHistData);
  
  var data = [{
      x: podvyboryHistData.osa_x,
      y: podvyboryHistData.osa_y,
      type: 'bar',
      marker: {
          color: 'blue',
          line: {
            color: 'black',
            width: 1
          }
      },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: 'Počet poslanců podle počtu podvýborů',
      xaxis: {title: 'Počet podvýborů',tickvals: podvyboryHistData.osa_x},
      yaxis: {title: 'Počet poslanců',type: 'log',
      autorange: true},
  };

  Plotly.newPlot('podvyboryHist', data, layout, config);
});

document.addEventListener('DOMContentLoaded', function() {    
  
  console.log(podvyboryHistData);
  
  var data = [{
      x: podvyboryHistData.osa_x,
      y: podvyboryHistData.osa_y,
      mode: 'markers',
      marker: {
        size: 10,
        color: 'blue',
    },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: 'Počet poslanců podle počtu podvýborů',
      xaxis: {title: 'Počet podvýborů',tickvals: podvyboryHistData.osa_x},
      yaxis: {title: 'Počet poslanců'},
  };

  Plotly.newPlot('podvyboryMarkers', data, layout, config);
});

// ------------------------

document.addEventListener('DOMContentLoaded', function() {    
  
  console.log(funkceHistData);
  
  var data = [{
      x: funkceHistData.osa_x,
      y: funkceHistData.osa_y,
      type: 'bar',
      marker: {
          color: 'red',
          line: {
            color: 'black',
            width: 1
          }
      },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: 'Počet funkcí vykonávané poslancem',
      xaxis: {
          title: 'Počet funkcí',
          tickvals: funkceHistData.osa_x,
      },
      yaxis: {
          title: 'Počet poslanců',
          type: 'log',
          autorange: true
      },
  };

  Plotly.newPlot('funkceHist', data, layout, config);
});


document.addEventListener('DOMContentLoaded', function() {    
  
  var data = [{
      x: funkceHistData.osa_x,
      y: funkceHistData.osa_y,
      mode: 'markers',
      marker: {
        size: 10,
        color: 'red'
    },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: 'Počet funkcí vykonávané poslancem',
      xaxis: {title: 'Počet funkcí',tickvals: funkceHistData.osa_x},
      yaxis: {title: 'Počet poslanců'},
  };

  Plotly.newPlot('funkceMarkers', data, layout, config);
});
// ------------------------
document.addEventListener('DOMContentLoaded', function() {    
  
  console.log(poslancemHistData);
  
  var data = [{
      x: poslancemHistData.x,
      y: poslancemHistData.y,
      type: 'bar',
      marker: {
          color: 'cyan',
          line: {
            color: 'black',
            width: 1
          }
      },
  }];
  var config =
  {
    responsive: true,
  }
  var layout = {
      title: "Počet znovuzvolení poslance",
      xaxis: {title: 'Počet znovuzvolení',tickvals: poslancemHistData.x},
      yaxis: {title: 'Počet poslanců',type: 'log',
      autorange: true},
  };

  Plotly.newPlot('poslaciHist', data, layout, config);
});

document.addEventListener('DOMContentLoaded', function() {    
     
  var data = [{
      x: poslancemHistData.x,
      y: poslancemHistData.y,
      mode: 'markers',
      marker: {
          size: 10,
          color: 'cyan'
      },
  }];
  var config =
  {
      responsive: true,
  }
  var layout = {
      title: 'Počet znovuzvolení poslance',
      xaxis: {title: 'Počet znovuzvolení', tickvals: poslancemHistData.x},
      yaxis: {title: 'Počet poslanců',},
  };
  
  Plotly.newPlot('poslaciMarkers', data, layout, config);
});
