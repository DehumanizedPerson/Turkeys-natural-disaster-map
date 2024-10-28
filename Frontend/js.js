fetch('map-t.svg')
  .then(response => response.text())
  .then(data => {
    const div = document.createElement('div');
    div.innerHTML = data;
    document.body.appendChild(div);

    const provinces = document.querySelectorAll('.region');
    provinces.forEach(province => {
      province.addEventListener('click', () => {
        showProvincePopup(province.id);
      });
    });
  });

function showProvincePopup(provinceId) {
  const popup = document.getElementById('pop');
  const popupContent = popup.querySelector('.pop-body');

  popupContent.textContent = `Information about ${provinceId}`;
  openPop(popup);
}

const closeModelButtons = document.querySelectorAll('[data-pop-close]');
const overlay = document.getElementById('overlay');

closeModelButtons.forEach(button => {
  button.addEventListener('click', () => {
    const pop = button.closest('.pop');
    closePop(pop);
  });
});

overlay.addEventListener('click', () => {
  const activePopups = document.querySelectorAll('.pop.active');
  activePopups.forEach(pop => closePop(pop));
});

function openPop(pop) {
  if (!pop) return;
  pop.classList.add('active');
  overlay.classList.add('active');
}

function closePop(pop) {
  if (!pop) return;
  pop.classList.remove('active');
  overlay.classList.remove('active');
}
