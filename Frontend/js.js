fetch('map-t.svg')
  .then(response => response.text())
  .then(data => {
    const div = document.createElement('div');
    div.innerHTML = data;
    document.body.appendChild(div);
  });
