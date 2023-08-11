console.log("Gallery Select is working");

function toggleSelect(n) {
  console.log("toggling selection on thumbnails");

  const siblings = n.parentElement.children;

  Array.from(siblings).forEach((el) =>
    el.classList.remove("selected-thumbnail")
  );

  n.classList.add("selected-thumbnail");

  const bigImage = document.querySelector(".main-gallery-image");
  bigImage.src = n.src;
}
