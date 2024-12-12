let provinceData = {};
fetch('provinceData.json')
  .then(response => response.json())
  .then(data => {
    provinceData = data;
    return fetch('map-t.svg');
  })
fetch('map-t.svg')
 .then(response => response.text())
 .then(data => {
 const div = document.createElement('div');
 div.innerHTML = data;
 const svgContainer = document.getElementById('svg-container');
 svgContainer.appendChild(div);

 const provinces = document.querySelectorAll('.region');
 provinces.forEach(province => {
   province.addEventListener('click', () => {
    showProvincePopup(province.id);
      });
    });
  })
.catch(error => console.error('Error loading SVG:', error));

function showProvincePopup(provinceId) {
  const popup = document.getElementById('pop');
  const popupTitle = popup.querySelector('.title');
  const popupContent = popup.querySelector('.pop-body');
  const { title, content } = provinceData[provinceId] || { title: `Unknown Province`, content: `No specific information for ${provinceId}.` };
  popupTitle.textContent = title;
  popupContent.textContent = content;
  openPop(popup);
}
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
