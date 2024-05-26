let noteForm = document.querySelectorAll(".note-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-note-btn")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

let formNum = noteForm.length-1 //Get the number of the last form on the page with zero-based indexing
addButton.addEventListener('click', addForm)

function addForm(e){
    e.preventDefault()

    let newForm = noteForm[0].cloneNode(true) //Clone the note form
    let formRegex = RegExp(`form-(\\d){1}-`,'g') //Regex to find all instances of the form number

    formNum++ //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`) //Update the new form to have the correct form number
    newForm.querySelector(".question").setAttribute('value', "");
    newForm.querySelector(".question").querySelector("textarea").value = "";
    newForm.querySelector(".note").querySelector("textarea").value = "";
    newForm.querySelector(".order").value = formNum+1;
    container.appendChild(newForm) //Insert the new form at the end of the list of forms

    totalForms.setAttribute('value', `${formNum+1}`) //Increment the number of total forms in the form management
}