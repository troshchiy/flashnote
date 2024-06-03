let form = document.querySelectorAll(".form")
let container = document.querySelector("#container")
let addButton = document.querySelector("#new-btn")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

let formNum = form.length-1 //Get the number of the last form on the page with zero-based indexing
addButton.addEventListener('click', addForm)

function addForm(e){
    e.preventDefault()
    addButton.style.display = "none";

    let newForm = form[0].cloneNode(true) //Clone the form
    let formRegex = RegExp(`form-(\\d){1}-`,'g') //Regex to find all instances of the form number

    formNum++ //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`); //Update the new form to have the correct form number
    newForm.querySelector("input").removeAttribute("readonly");
    outerLink = newForm.querySelector("a");
    outerLink.outerHTML = outerLink.innerHTML;
    newForm.querySelector("input").value = "Untitled";
    newForm.querySelector("input").style.cursor = "text";
    newForm.querySelector(".total-amount").innerText = 0;
    createConfirmInput(newForm.querySelector(".title"));
    container.appendChild(newForm) //Insert the new form at the end of the list of forms
    newForm.querySelector("input").focus();
    newForm.querySelector("input").select();

    totalForms.setAttribute('value', `${formNum+1}`) //Increment the number of total forms in the form management
}

function createConfirmInput(node) {
    const confirmInput = document.createElement('input');
    confirmInput.value = 'Confirm';
    confirmInput.type = 'submit';
    confirmInput.form = "form-container";
    confirmInput.setAttribute("class", "confirm-button");
    node.appendChild(confirmInput);
}

function renameRowForm(form) {
    event.preventDefault();
    form.querySelector("input").removeAttribute("readonly");
    outerLink = form.querySelector("a")
    outerLink.outerHTML = outerLink.innerHTML;
    form.querySelector("input").style.cursor = "text";
    form.querySelector("input").focus();
    form.querySelector("input").select();
    createConfirmInput(form.querySelector(".title"));
}