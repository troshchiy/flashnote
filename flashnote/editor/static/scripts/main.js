document.querySelectorAll("textarea").forEach(auto_grow)

function auto_grow(element) {
    element.style.height = "auto";
    element.style.height = (element.scrollHeight-12)+"px";
}


function set_parent_value(element) {
    element.parentNode.setAttribute('value', element.value);
}
