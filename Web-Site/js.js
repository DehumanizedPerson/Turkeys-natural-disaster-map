document.addEventListener('DOMContentLoaded', function() {
    const modeToggleButton = document.getElementById('mode-s');
    const body = document.body;
    const header = document.querySelector('header');
    const pop = document.getElementById('pop');
    const overlay = document.getElementById('overlay');

    modeToggleButton.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        header.classList.toggle('dark-mode');
        pop.classList.toggle('dark-mode');
        overlay.classList.toggle('dark-mode');
    });

    let provinceData = {};

    fetch('provinceData.json')
      .then(response => response.json())
      .then(data => {
        provinceData = data;
        return fetch('map-t.svg');
      })
      .then(response => response.text())
      .then(data => {
        const div = document.createElement('div');
        div.classList.add('svg-image');
        div.innerHTML = data;
        document.getElementById('svg-container').appendChild(div);

        const provinces = document.querySelectorAll('.ege, .marmara, .karadeniz, .i_anadolu, .akdeniz, .g_anadolu, .d_anadolu');
        provinces.forEach(province => {
          province.addEventListener('click', () => {
            showProvincePopup(province.id);
          });
        });
      })
      .catch(error => console.error('Error loading data:', error));

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
});
