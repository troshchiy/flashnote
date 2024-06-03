function showPopupMenu(element) {
    event.stopPropagation()

    var currentPopupMenu = element.querySelector(".popup-menu");
    if (currentPopupMenu.classList.contains("show")) {
      currentPopupMenu.classList.remove("show");
      element.classList.remove("shown");
    }
    else {
      hideAllPopupMenus();
      currentPopupMenu.classList.add("show");
      element.classList.add("shown");
    }
}

function hideAllPopupMenus() {
    var popupMenus = document.querySelectorAll(".popup-menu");

    popupMenus.forEach(function(pm) {
        pm.classList.remove("show");
        pm.parentElement.classList.remove("shown");
    })
}

document.onclick = hideAllPopupMenus


function deleteForm(form) {
    event.preventDefault();
    form.style.display = "none";
    form.querySelector("input[class=deletion]").checked = "true";
}


function deleteRowForm(row_form) {
    event.preventDefault();
    row_form.querySelector("input[class=deletion]").checked = "true";
    document.querySelector("#form-container").submit();
}