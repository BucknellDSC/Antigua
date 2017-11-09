$(document).ready(function() {
  // the list of all mills in the side panel
  // var $mill_list = $('#mill_list');
  // // hidden variable all_mists: a json type variable contaning information of all mills
  // // add all mills to the list of mills on the side panel
  //   for (i in all_mills) {
  //       jQuery('<div/>', {
  //           id: all_mills[i].name,
  //           class: "menu_item",
  //           text: all_mills[i].name,
  //       }).appendTo($mill_list);
  //   }

  // hide the parishes map
  // $("#stjohn_map").hide();
  $("#stgeorge_map").hide();
  $("#stmary_map").hide();
  $("#stpaul_map").hide();
  $("#stpeter_map").hide();
  $("#stphilip_map").hide();
  $("#antigua_map").hide();
  var $current_map = $("#stjohn_map");

  //   hide the dummy elements of html file. They are used as blueprint
  $(".blueprint").hide();

    //   var mill_locaitons which contains all location data of mill_locaitons. declared in mill_location.json file

  /**
   * Create mill markers on a parish from a location json file
   * @param {*} location_array: the json object holding the location data
   */
  function create_mill_marker(location_array) {
    var $marker = $(".marker.blueprint");
    var new_marker;
    for (i in location_array) {
      new_marker = $marker.clone();
      new_marker.removeClass("blueprint");
      var left = location_array[i].left.toString()+"%";
      var top = location_array[i].top.toString() + "%";
      new_marker.css("left", left);
      new_marker.css("top", top);
      $current_map.append(new_marker);
    }
  }

  var $card = $(".blueprint .card");
  var $modal = $(".blueprint .modal");

  $(".menu_button").on("mouseover", function() {
    $(this).css("border", " 1px ridge rgba(242, 207, 141, 1)");
  });

  // menu item focus
  $(".menu_button").on("click", function() {
    $(".expandable_list", this).css({
      height: "30vh",
      "margin-top": "2em"
    });
    $(".menu_title", this).css({
      "border-bottom": "1px ridge rgba(242, 207, 141, 1)"
    });
  });

  $(".menu_button").on("mouseleave", function() {
    $(this).css("border", " 1px ridge transparent");
    $(".expandable_list", this).css({
      height: "0vh",
      "margin-top": "0"
    });
    $(".menu_title", this).css({
      "border-bottom": "none"
    });
  });

  // switch to st.john on click
  $("#stjohn-path").on("click", function() {
    // window.location.href = "stjohn.html"
    $("#stjohn_map").fadeIn();
    $("#antigua_map").fadeOut();
  });

  $("#stpaul-path").on("click", function() {
    window.location.href = "stpaul.html";
  });

  $("#stpeter-path").on("click", function() {
    window.location.href = "stpeter.html";
  });

  $("#stphilip-path").on("click", function() {
    window.location.href = "stphilip.html";
  });

  $("#stmary-path").on("click", function() {
    window.location.href = "stmary.html";
  });

  $("#stgeorge-path").on("click", function() {
    window.location.href = "stgeorge.html";
  });

  $(".marker").bind("click", function() {
    $(".card").addClass("active");
    $(".marker").addClass("inactive");
  });

  $(".card").bind("click", function() {
    $(".card").removeClass("active");
    $(".marker").removeClass("inactive");
  });

  $("#home_button").on("click", function() {
    if ($("#middle-slide").hasClass("active")) {
      $("#middle-slide").removeClass("active");
    } else {
      $("#middle-slide").addClass("active");
    }
    if ($("#middle-slide-content").hasClass("active")) {
      $("#middle-slide-content").removeClass("active");
    } else {
      $("#middle-slide-content").addClass("active");
    }
  });
});

function show_full_info() {
  var modal = document.getElementsByClassName("modal")[0];

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal
  modal.style.display = "block";

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
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
