console.log('HELs')

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    /*document.getElementById("down-arrow").style.top = "0";*/
    document.getElementById("down-arrow").style.border = "black";
    
    
  } else {
    /*document.getElementById("down-arrow").style.top = "-50px";*/
    document.getElementById("down-arrow").style.border = "black";
  }
  prevScrollpos = currentScrollPos;
}

/*
// get a reference to the slider container and all of the slides
const sliderContainer = document.querySelector('.container');
const slides = sliderContainer.querySelectorAll('.box');

// set up a counter to keep track of the current slide
let currentSlide = 0;
console.log(currentSlide);
// define a function to show the next slide
function showNextSlide() {
  // hide the current slide
  slides[currentSlide].style.opacity = 0;
  slides[currentSlide].style.visibility = 'hidden';

  // update the counter
  currentSlide = (currentSlide + 1) % slides.length;

  // show the next slide
  slides[currentSlide].style.opacity = 1;
  slides[currentSlide].style.visibility = 'visible';
}

// define a function to show the previous slide
function showPrevSlide() {
  // hide the current slide
  slides[currentSlide].style.opacity = 0;
  slides[currentSlide].style.visibility = 'hidden';

  // update the counter
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;

  // show the previous slide
  slides[currentSlide].style.opacity = 1;
  slides[currentSlide].style.visibility = 'visible';
}
// show the next slide every 3 seconds
setInterval(showNextSlide, 3000);


// set up event listeners for the navigation buttons
// document.querySelector('.next-button').addEventListener('click', showNextSlide);
// document.querySelector('.prev-button').addEventListener('click', showPrevSlide);
*/


let slideIndex = 1;
showSlides(slideIndex);


function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("box");
  
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  slides[slideIndex-1].style.display = "block";  
  
}

