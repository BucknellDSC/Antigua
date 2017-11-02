

$(document).ready(function () {
    $("#searchIcon").on('click', function () {
        search();
    });
    $("#sidepanel-toggle").on('click', function () {
        toggleSidePanel();
    });
    $("#stjohn-path").on('click', function() {
        window.location.href = "stjohn.html"
    });
});

function toggleSidePanel () {
    if($("#sidepanel").hasClass('active')) {
        $("#sidepanel").removeClass('active');
    } else {
        $("#sidepanel").addClass('active');
    }
}

$('.marker').bind('click', function() {
    $('.card').addClass('active');
    $('.marker').addClass('inactive');
});

$('.card').bind('click', function() {
    $('.card').removeClass('active');
    $('.marker').removeClass('inactive');
});

function show_full_info() {
    console.log("eyyy");
    var modal = document.getElementsByClassName("modal")[0];


// Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
    modal.style.display = "block";

// When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    };
}

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();