let answer = document.querySelector("#flashcard-answer");
let showAnswerBtn = document.querySelector("#show-answer-btn");
let grade = document.querySelector("#grade");
let recallTip = document.querySelector("#recall-tip");
let gradeTip = document.querySelector("#grade-tip");
let gradeMeaning = document.querySelector("#grade-meaning");

document.querySelectorAll("textarea").forEach((t) => t.setAttribute("readonly", "true"));

function showAnswer() {
    event.preventDefault();
    answer.classList.add("shown");
    grade.classList.add("shown");
    gradeTip.classList.add("shown");
    gradeMeaning.classList.add("shown");
    showAnswerBtn.style.display = "none";
    recallTip.style.visibility = "hidden";
    recallTip.style.opacity = 0;
}