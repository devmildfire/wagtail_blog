//  скрипт для управления меню хедера в мобильной версии
console.log("test of js file for header");

const dropdown = document.querySelector(".dropdown");
const hamburger = document.querySelector(".svg_hamburger");
const cross = document.querySelector(".svg_cross");

console.log(dropdown);

function hamburgerClick() {
  dropdown.classList.toggle("active");
  hamburger.classList.toggle("hidden");
  cross.classList.toggle("hidden");
}
