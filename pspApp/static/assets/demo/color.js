function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

var colorArray = [];
for (var i = 0; i < Object.keys(vyboryData).length; i++) {
    colorArray.push(getRandomColor());
}