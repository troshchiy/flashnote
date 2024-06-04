document.querySelectorAll("textarea").forEach(autoGrow)

function autoGrow(element) {
    element.style.height = "auto";
    element.style.height = (element.scrollHeight-12)+"px";
}


function setParentValue(element) {
    element.parentNode.setAttribute('value', element.value);
}
