const addItem = document.getElementById('add_item');
addItem.addEventListener('click', function () {
  const listItem = document.createElement('li');
  listItem.innerText = 'Item';
  document.querySelector('.my_list').appendChild(listItem);
});
