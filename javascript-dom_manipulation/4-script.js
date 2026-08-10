// Adds a new <li>Item</li> to .my_list when clicking #add_item
document.querySelector('#add_item').addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
