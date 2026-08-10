// Updates text of header element when clicking #update_header
document.querySelector('#update_header').addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
