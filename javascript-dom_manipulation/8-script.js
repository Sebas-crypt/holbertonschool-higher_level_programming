document.addEventListener('DOMContentLoaded', () => {
  const api = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  fetch(api)
      .then(response => response.json())
      .then(data => {
          const hello = document.getElementById('hello');
          hello.textContent = data.hello;
      })
      .catch(error => console.error('Error fetching data:', error));
  });
