window.onload = function () {
    var test_img = document.getElementById('test-img');
    var n,
        areas = document.getElementById('test-map').getElementsByTagName('area'),
        len = areas.length,
        coords = [],
        previousWidth = test_img.width;
    for (n = 0; n < len; n++) {
        coords[n] = areas[n].coords.split(',');
    }

    test_img.height = window.innerHeight;
    test_img.width = window.innerWidth;

    console.log(test_img.offsetWidth);

    console.log(test_img.width);
    var m, clen,
        x = test_img.offsetWidth / previousWidth;
    for (n = 0; n < len; n++) {
        clen = coords[n].length;
        for (m = 0; m < clen; m++) {
            coords[n][m] *= x;
        }
        areas[n].coords = coords[n].join(',');
    }
    console.log(areas[0]);
};
