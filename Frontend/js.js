const provinceData = {
 izmir: {title: "İzmir", content: "2020 İzmir Depremi: 30 Ekim’de 7.0 büyüklüğünde meydana gelen deprem, İzmir’de 100’den fazla kişinin ölümüne ve birçok binanın yıkılmasına neden olmuştur."},
 ankara: { title: "Ankara", content: "deneme" },
 trabzon: { title: "Trabzon", content: "2019 Trabzon Heyelanı: Trabzon’da meydana gelen aşırı yağış sonrası oluşan heyelan, köy yollarını kapatmış ve bazı yerleşim yerlerine zarar vermiştir." },
 adana: { title: "adana", content: "deneme3" },
 van: { title: "Van", content: "2011 Van Depremi:  23 Ekim’de 7.1 büyüklüğünde meydana gelen depremde yaklaşık 600 kişi yaşamını yitirmiş, 4.000'den fazla kişi yaralanmıştır."}
};
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
