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


