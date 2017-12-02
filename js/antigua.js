$(document).ready(function() {
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
  // the new variable to content mill data. Use dictionary type for easy reference
  var new_mill_data = {};
  // -------------- MENU BUTTONS STYLING AND FUNCTIONS ---------------------

  /**
   * Menu button styling on mouse over
   */
  $(".menu_button").on("mouseover", function() {
    $(this).css("border", " 1px ridge rgba(242, 207, 141, 1)");
  });

  // menu item focus
  $(".menu_button").on("click", function() {
    var distance_to_bottom =
      $(window).height() -
      $("#credit_button")[0].getBoundingClientRect().bottom -
      $("#credit_button").outerHeight();
    $(".expandable_list", this).css({
      height: distance_to_bottom.toString(),
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

  /**
   * What to do when info button is clicked. Doesn't require any data from .js file
   */
  $("#info_button").on("click", function() {
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
    // only add in if mill have enough information
    if (parish != "") {
      mills_array.push(mill_name);
      new_mill_data[mill_name] = a_mill;
      // if we haven't stored the parish yet, add it to parish list and mills by parishes dict
      if (parishes_array.indexOf(parish) < 0) {
        parishes_array.push(parish);
        mills_by_parishes_array[parish] = [mill_name];
      } else {
        // else, add the mill to the dictionary of parishes
        mills_by_parishes_array[parish].push(mill_name);
      }
    }
  }

  // sort the mill names inside the list
  mills_array.sort();
  parishes_array.sort();
  for (var key in mills_by_parishes_array) {
    mills_by_parishes_array[key].sort();
  }

  // start with main map, current list of mills is list of all mills
  current_mills_array = mills_array;

  // add mills to menu. start with all mills
  add_mills_to_menu();

  // ------------------ MAIN FUNCTIONS --------------------------

  // add parishes to menu
  var $parish_list = $("#parish_list");
  for (var a_parish in mills_by_parishes_array) {
    jQuery("<div/>", {
      id: a_parish,
      class: "menu_list_item",
      text: a_parish
    }).appendTo($parish_list);
  }

  /**
   * Add list of mills to menu based on the current map.
   * Depends on global current_mills_array
   */
  function add_mills_to_menu() {
    // get element which contains the list in html
    var $mill_list = $("#mill_list");
    // add list of mills to html element
    $mill_list.empty();
    for (mill_name of current_mills_array) {
      jQuery("<div/>", {
        id: mill_name,
        class: "menu_list_item",
        text: new_mill_data[mill_name].display_name
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
      if (mills_array.indexOf(location_array[i].name) != -1) {
        new_marker = $marker.clone();
        new_marker.removeClass("blueprint");
        new_marker.attr("id", location_array[i].name + "_marker");
        var left = location_array[i].left.toString() + "%";
        var top = location_array[i].top.toString() + "%";
        new_marker.css("left", left);
        new_marker.css("top", top);
        $current_map.append(new_marker);
      }
    }
    /**
     * Card active and inactive.
     */
    $(".marker").bind("click", function() {
      var t = $(this)[0];
      $(".card").addClass("active");
      $(".card").attr("id", t.id);
      $(".marker").each(function() {
        if ($(this)[0] != t) {
          $(this).addClass("inactive");
        }
      });
      var element = $(".content-text")[0];
      var mill_name = t.id.replace("_marker", "");
      var a_mill = new_mill_data[mill_name];
      var display_name = a_mill.display_name;
      var parish = a_mill.parish;
      var extant = a_mill.extant_or_ruin;
      var founding_date = a_mill.date_of_establishment;
      var lat = a_mill.lat;
      var long = a_mill.long;
      $(".card .title")[0].innerHTML = display_name;
      $(".card .subtitle")[0].innerHTML = extant;
      element.innerHTML =
        "This mill was founded in <b>" +
        founding_date +
        "</b>. It belongs to <b>" +
        parish +
        "</b> parish, and it's precise GPS location is <b>" +
        long +
        "</b> longitude and <b>" +
        lat +
        "</b> latitude.";
    });
  }

  // ------------------ MAP FUNCTIONS --------------------------

  /**
   * switch to different parishes on click
   */
  $("#stjohn-path").on("click", function() {
    $current_map.fadeOut();
    $("#stjohn_map").fadeIn();
    $current_map = $("#stjohn_map");
    create_mill_marker(stjohn_mill_locations);
    current_mills_array = mills_by_parishes_array["St.John"];
    add_mills_to_menu();
  });

  $("#stpaul-path").on("click", function() {
    $current_map.fadeOut();
    $("#stpaul_map").fadeIn();
    $current_map = $("#stpaul_map");
    create_mill_marker(stpaul_mill_locations);
    current_mills_array = mills_by_parishes_array["St.Paul"];    
    add_mills_to_menu();
  });

  $("#stpeter-path").on("click", function() {
    $current_map.fadeOut();
    $("#stpeter_map").fadeIn();
    $current_map = $("#stpeter_map");
    create_mill_marker(stpeter_mill_locations);
    current_mills_array = mills_by_parishes_array["St.Peter"];    
    
    add_mills_to_menu();
  });

  $("#stphilip-path").on("click", function() {
    $current_map.fadeOut();
    $("#stphilip_map").fadeIn();
    $current_map = $("#stphilip_map");
    create_mill_marker(stphilip_mill_locations);
    current_mills_array = mills_by_parishes_array["St.Philip"];        
    add_mills_to_menu();
  });

  $("#stmary-path").on("click", function() {
    $current_map.fadeOut();
    $("#stmary_map").fadeIn();
    $current_map = $("#stmary_map");
    create_mill_marker(stmary_mill_locations);
    current_mills_array = mills_by_parishes_array["St.Mary"];        
    add_mills_to_menu();
  });

  $("#stgeorge-path").on("click", function() {
    $current_map.fadeOut();
    $("#stgeorge_map").fadeIn();
    $current_map = $("#stgeorge_map");
    current_mills_array = mills_by_parishes_array["St.George"];
    create_mill_marker(stgeorge_mill_locations);
    add_mills_to_menu();
  });

  /**
   * What to do when map button is clicked.
   *
   */
  $("#map_button").on("click", function() {
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

  $(".card .button-secondary").on("click", function() {
    $(".card").removeClass("active");
    $(".marker").removeClass("inactive");
  });

  $(".card .button-primary").on("click", function() {
    show_full_info();
  });

  /**
   * Show the modal with all the information
   */
  function show_full_info() {
    var modal = $(".modal");
    var element = $(".card")[0];
    var mill_name = element.id.replace("_marker", "");
    var a_mill = new_mill_data[mill_name];
    var a_mill = new_mill_data[mill_name];
    var display_name = a_mill.display_name;
    var parish = a_mill.parish;
    var extant = a_mill.extant_or_ruin;
    var founding_date = a_mill.date_of_establishment;
    var lat = a_mill.lat;
    var long = a_mill.long;
    var description = a_mill.additional_info;
    var chronology = a_mill.chronology;
    // update name
    $(".modal-title")[0].innerHTML = display_name;
    // update general info
    $(".modal-genInfo")[0].innerHTML =
      "<b>Type: </b>" +
      extant +
      "<br> <b>Parish: </b>" +
      parish +
      " <br> <b>Founding date: </b>" +
      founding_date +
      "<br> <b>Long, lat: </b>" +
      long +
      ", " +
      lat;
    // update description
    $(".modal-desc")[0].innerHTML = description;
    // update the chronology
    // clear the ul content
    // $(".timeline").empty();
    // for (var year in chronology) {
    //   $(".timeline").append(
    //     $("<li>")
    //       .attr({ class: "event", "data-date": year.toString() })
    //       .append($("<p>").text(chronology[year]))
    //   );
    // }

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    modal.css("transform", "translateY(0)");

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.css("transform", "translateY(100%)");
    };
  }
});
/**
 * Switch to another tab with tab_name in the modal
 * @param {*Ch} evt
 * @param {*} tab_name: the tab to switch to
 */
function change_tab(evt, tab_name) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tab_name).style.display = "block";
  evt.currentTarget.className += " active";
}
