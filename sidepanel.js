function add_mills() {
    var mill_list = document.getElementById("mill_list");
    var new_mill;
    console.log(all_mills);
    for (i in all_mills){
        console.log(all_mills[i]);
        new_mill = document.createElement('div');
        new_mill.innerHTML =  all_mills[i].name;
        new_mill.id = all_mills[i].name;
        new_mill.class = "menu_item";
        mill_list.appendChild(new_mill);
    }
}


