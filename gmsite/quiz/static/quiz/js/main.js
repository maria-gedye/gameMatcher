console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>?"</div>
        <div class="text-muted">
            <ul>
                <li>Total questions: <b>${numQuestions}</b></li>
                <li>Time: <b>${time} min</b></li>
            </ul>
    `
}))

/*
$( document ).ready(function() {

});

let questionIndex = 1;
showSlides(questionIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(questionIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(questionIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("question")
  console.log(slides);
  if (n > slides.length) {questionIndex = 1}
  if (n < 1) {questionIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[questionIndex-1].style.display = "block";
}


*/
