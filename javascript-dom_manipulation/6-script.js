// Fetches character name from Star Wars API and displays it in #character
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  });
