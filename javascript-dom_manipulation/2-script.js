// Adds class red to header element when clicking #red_header
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});
