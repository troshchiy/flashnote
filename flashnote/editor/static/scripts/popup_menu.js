function show_popup_menu(element) {
    event.stopPropagation()

    var current_popup_menu = element.querySelector(".popup-menu");
    if (current_popup_menu.classList.contains("show")) {
      current_popup_menu.classList.remove("show");
      element.classList.remove("shown");
    }
    else {
      hide_all_popup_menus();
      current_popup_menu.classList.add("show");
      element.classList.add("shown");
    }
}

function hide_all_popup_menus() {
    var popup_menus = document.querySelectorAll(".popup-menu");

    popup_menus.forEach(function(pm) {
        pm.classList.remove("show");
        pm.parentElement.classList.remove("shown");
    })
}

document.onclick = hide_all_popup_menus


function delete_form(form) {
    event.preventDefault();
    form.style.display = "none";
    form.querySelector("input[class=deletion]").checked = "true";
}


function delete_row_form(row_form) {
    event.preventDefault();
    row_form.querySelector("input[class=deletion]").checked = "true";
    document.querySelector("#form-container").submit();
}