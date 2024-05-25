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
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`) //Update the new form to have the correct form number
    newForm.querySelector("input").value = "Untitled";
    newForm.querySelector("input").removeAttribute("readonly");
    newForm.querySelector("a").setAttribute("onclick", "return false;");
    newForm.querySelector(".total-amount").innerText = 1;

    const confirmInput = document.createElement('input');
    confirmInput.value = 'Confirm';
    confirmInput.type = 'submit';
    confirmInput.form = "form-container";
    confirmInput.setAttribute("class", "confirm-button");
    newForm.querySelector(".title").appendChild(confirmInput);
    container.appendChild(newForm) //Insert the new form at the end of the list of forms
    newForm.querySelector("input").focus();

    totalForms.setAttribute('value', `${formNum+1}`) //Increment the number of total forms in the form management
}
