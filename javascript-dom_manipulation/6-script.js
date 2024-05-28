const api = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(api)
  .then(response => response.json())
  .then(data => {
    const character = document.getElementById('character');
    character.textContent = data.name;
  })
  .catch(error => console.error('Error fetching data:', error));
