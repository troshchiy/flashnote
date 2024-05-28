let noteForm = document.querySelectorAll(".note-form")
let formNum = noteForm.length-1 //Get the number of the last form on the page with zero-based indexing
let formRegex = RegExp(`form-(\\d){1}-`,'g') //Regex to find all instances of the form number

function createForm() {
    let newForm = noteForm[0].cloneNode(true) //Clone the note form
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

    formNum++ //Increment the form number

    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    newForm.querySelector(".question").setAttribute("value", "");
    newForm.querySelector(".question").querySelector("textarea").value = "";
    newForm.querySelector(".note").querySelector("textarea").value = "";
    newForm.querySelector(".question").querySelector("textarea").style.height = "15px";
    newForm.querySelector(".note").querySelector("textarea").style.height = "15px";
    newForm.querySelector(".order").value = formNum+1;

    totalForms.setAttribute("value", `${formNum+1}`) //Increment the number of total forms in the form management

    return newForm;
}


function addForm(){
    event.preventDefault();
    newForm = createForm();

    let container = document.querySelector("#form-container");
    container.appendChild(newForm); //Insert the new form at the end of the list of forms

    newForm.querySelector(".note textarea").focus();
}

document.onkeydown = keydown;

function keydown(){
  if (event.ctrlKey && event.keyCode==13){ //CTRL+ENTER
    element = document.activeElement
    if (element.tagName == "TEXTAREA") {
            newForm = createForm();

            referenceNode = element.parentNode.parentNode
            referenceNode.parentNode.insertBefore(newForm, referenceNode.nextSibling);

            order = 1;
            noteForm.forEach((form) => {
                form.querySelector("input.order").setAttribute("value", order);
                order++;
            });
        if (element.parentNode.classList.contains("note")) {
            newForm.querySelector(".note textarea").focus();
        }
        else {
            qTextarea = newForm.querySelector(".question textarea");
            qTextarea.classList.add("shown");
            qTextarea.addEventListener("blur", addClassShown);
            qTextarea.focus();
        }
    }
    else {
        addForm(event);
    }
  }
}


function addClassShown(e) {
    e.target.classList.remove("shown");
    e.target.removeEventListener("blur", addClassShown);
}