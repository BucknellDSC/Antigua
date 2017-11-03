
$(document).ready(function () {
    // the list of all mills in the side panel
    var $mill_list = $('#mill_list');
    // hidden variable all_mists: a json type variable contaning information of all mills
    
    // add all mills to the list of mills on the side panel
    for (i in all_mills) {
        jQuery('<div/>', {
            id: all_mills[i].name,
            class: "menu_item",
            text: all_mills[i].name,
        }).appendTo($mill_list);
    }
    // switch to st.john on click
    $("#stjohn-path").on('click', function() {
        window.location.href = "stjohn.html"
    });
});

$('.marker').bind('click', function() {
    $('.card').addClass('active');
    $('.marker').addClass('inactive');
});

$('.card').bind('click', function() {
    $('.card').removeClass('active');
    $('.marker').removeClass('inactive');
});

function show_full_info() {
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
