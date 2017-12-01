$(document).ready(function () {
  // -------------- VARIABLE DECLARATION --------------------

  // the map which is currently active and show on the screen. jquery object
  var $current_map;
  // The name of the current map. Use for functions which require current map information
  // possible value: stgeorge|stmary|stpaul|stpeter|stphilip|stjohn|antigua
  var current_map;
  // the array of all parishes
  var parishes_array = [];
  // the aray of all mills
  var mills_array = [];
  // the dictionary of all mills, sorted according to parishes
  var mills_by_parishes_array = {};
  // the array of all mills we are currently working with
  var current_mills_array = [];
  //   var mill_locaitons, which contains all location data of mills. Declared in mill_location.json file
  // var mill_data, which contains all data of mills. Declared in mill_data.js file

  // -------------- MENU BUTTONS STYLING AND FUNCTIONS ---------------------

  /**
   * Menu button styling on mouse over
   */
  $(".menu_button").on("mouseover", function () {
    $(this).css("border", " 1px ridge rgba(242, 207, 141, 1)");
  });

  // menu item focus
  $(".menu_button").on("click", function () {
    var distance_to_bottom = $(window).height() - $('#credit_button')[0].getBoundingClientRect().bottom - $('#credit_button').outerHeight() ;
    console.log(distance_to_bottom);
    $(".expandable_list", this).css({
      "height": distance_to_bottom.toString(),
      "margin-top": "2em"
    });
    if ($(".menu_title", this).attr("id") !== "info_button") {
      if ($(".menu_title", this).attr("id") !== "map_button") {
        if ($(".menu_title", this).attr("id") !== "biblio_button") {
          if ($(".menu_title", this).attr("id") !== "credit_button") {
            $(".menu_title", this).css({
              "border-bottom": "1px ridge rgba(242, 207, 141, 1)"
            });
          }
        }
      }
    }
  });

  /**
   * Menu button styling on mouse over
   */
  $(".menu_button").on("mouseleave", function () {
    $(this).css("border", " 1px ridge transparent");
    $(".expandable_list", this).css({
      height: "0vh",
      "margin-top": "0"
    });
    $(".menu_title", this).css({
      "border-bottom": "none"
    });
  });

  /**
   * What to do when info button is clicked. Doesn't require any data from .js file
   */
  $("#info_button").on("click", function () {
    if (!$("#middle-slide").hasClass("active")) {
      $("#middle-slide").addClass("active");
      $("#middle-slide-title").addClass("active");
      $("#middle-slide-content").addClass("active");
    } else if ($("#middle-slide").hasClass("active")) {
      $("#middle-slide").removeClass("active");
      $("#middle-slide-title").removeClass("active");
      $("#middle-slide-content").removeClass("active");
    }
  });


  // -------------- INIT CALLS. RUN WHEN WEBSITE STARTS ---------------------

  // show main map and hide other maps. We have to do this because they live on the same page
  $("#stjohn_map").hide();
  $("#stgeorge_map").hide();
  $("#stmary_map").hide();
  $("#stpaul_map").hide();
  $("#stpeter_map").hide();
  $("#stphilip_map").hide();
  $("#antigua_map").show();
  $current_map = $("#antigua_map");

  // Process mill data into different form.
  // Specifically, we need a list of mill names | a list of parishes name | a list of mill names based on parishes
  for (var index in mill_data) {
    var a_mill = mill_data[index];
    var parish = a_mill.parish;
    var mill_name = a_mill.name;
    mills_array.push(mill_name);
    // if we haven't stored the parish yet, add it to parish list and mills by parishes dict
    if (parishes_array.indexOf(parish) < 0) {
      parishes_array.push(parish);
      mills_by_parishes_array[parish] = [mill_name];
    } else {
      // else, add the mill to the dictionary of parishes
      mills_by_parishes_array[parish].push(mill_name);
    }
  }

  // sort the mill names inside the list
  mills_array.sort();
  parishes_array.sort();
  for (var key in mills_by_parishes_array) {
    mills_by_parishes_array[key].sort();
  }

  // add parishes to menu
  var $parish_list = $("#parish_list");
  for (var a_parish in mills_by_parishes_array) {
    jQuery("<div/>", {
      id: a_parish,
      class: "menu_list_item",
      text: a_parish
    }).appendTo($parish_list);
  }

  // start with main map, current list of mills is list of all mills
  current_mills_array = mills_array;

  // add mills to menu. start with all mills
  add_mills_to_menu();


  // ------------------ MAIN FUNCTIONS --------------------------

  /**
   * Add list of mills to menu based on the current map.
   * Depends on global current_mills_array
   */
  function add_mills_to_menu() {
    // get element which contains the list in html
    var $mill_list = $("#mill_list");
    // add list of mills to html element
    console.log(current_mills_array);
    for (mill_name of current_mills_array) {
      jQuery("<div/>", {
        id: mill_name,
        class: "menu_list_item",
        text: mill_name
      }).appendTo($mill_list);
    }
  }

  /**
   * Create mill markers on a parish from a location json file
   * @param {*} location_array: the json object holding the location data
   */
  function create_mill_marker(location_array) {
    var $marker = $(".marker.blueprint");
    var new_marker;
    for (var i in location_array) {
      new_marker = $marker.clone();
      new_marker.removeClass("blueprint");
      new_marker.attr("onclick", "$('.card').addClass('active'); $('.marker').addClass('inactive');");
      var left = location_array[i].left.toString() + "%";
      var top = location_array[i].top.toString() + "%";
      new_marker.css("left", left);
      new_marker.css("top", top);
      $current_map.append(new_marker);
    }
  }


  // ------------------ MAP FUNCTIONS --------------------------

  /**
   * switch to different parishes on click
   */
  $("#stjohn-path").on("click", function () {
    $current_map.fadeOut();
    $("#stjohn_map").fadeIn();
    $current_map = $("#stjohn_map");
    create_mill_marker(stjohn_mill_locations);
  });

  $("#stpaul-path").on("click", function () {
    $current_map.fadeOut();
    $("#stpaul_map").fadeIn();
    $current_map = $("#stpaul_map");
    create_mill_marker(stpaul_mill_locations);
  });

  $("#stpeter-path").on("click", function () {
    $current_map.fadeOut();
    $("#stpeter_map").fadeIn();
    $current_map = $("#stpeter_map");
    create_mill_marker(stpeter_mill_locations);
  });

  $("#stphilip-path").on("click", function () {
    $current_map.fadeOut();
    $("#stphilip_map").fadeIn();
    $current_map = $("#stphilip_map");
    create_mill_marker(stphilip_mill_locations);
  });

  $("#stmary-path").on("click", function () {
    $current_map.fadeOut();
    $("#stmary_map").fadeIn();
    $current_map = $("#stmary_map");
    create_mill_marker(stmary_mill_locations);
  });

  $("#stgeorge-path").on("click", function () {
    $current_map.fadeOut();
    $("#stgeorge_map").fadeIn();
    $current_map = $("#stgeorge_map");
    create_mill_marker(stgeorge_mill_locations);
  });

  /**
   * What to do when map button is clicked.
   *
   */
  $("#map_button").on("click", function () {
    if ($current_map[0] != $("#antigua_map")[0]) {
      $current_map.fadeOut();
      $("#antigua_map").fadeIn();
      $current_map = $("#antigua_map");
    }
    if ($("#middle-slide").hasClass("active")) {
      $("#middle-slide").removeClass("active");
      $("#middle-slide-title").removeClass("active");
      $("#middle-slide-content").removeClass("active");
    }
  });

  var $card = $(".blueprint .card");
  var $modal = $(".blueprint .modal");

  /**
   * Card active and inactive.
   */
  $(".marker").bind("click", function () {
    $(".card").addClass("active");
    $(".marker").addClass("inactive");
  });

  $(".card .button-secondary").on("click", function () {
    $(".card").removeClass("active");
    $(".marker").removeClass("inactive");
  });

  $(".card .button-primary").on("click", function () {
    show_full_info();
  });

  /**
   * Show the modal with all the information
   */
  function show_full_info() {
    var modal = $(".modal");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    modal.css("transform", "translateY(0)");

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
      modal.css("transform", "translateY(100%)");
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

});