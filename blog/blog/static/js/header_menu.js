//  скрипт для управления меню хедера в мобильной версии

const dropdown = document.querySelector(".dropdown");
const hamburger = document.querySelector(".svg_hamburger");
const cross = document.querySelector(".svg_cross");

function hamburgerClick() {
  dropdown.classList.toggle("active");
  hamburger.classList.toggle("hidden");
  cross.classList.toggle("hidden");
}
