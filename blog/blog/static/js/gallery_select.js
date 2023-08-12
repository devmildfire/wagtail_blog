console.log("Gallery Select is working");

function toggleSelect(n) {
  console.log("toggling selection on thumbnails");

  const siblings = n.parentElement.children;

  Array.from(siblings).forEach((el) =>
    el.classList.remove("selected-thumbnail")
  );

  n.classList.add("selected-thumbnail");

  let bigImageDiv = document.querySelector(".big-iamge-div");
  bigImageDiv.innerHTML = n.outerHTML;

  bigImage = document.querySelector(".big-iamge-div").firstElementChild;

  bigImage.classList.remove("selected-thumbnail");
  bigImage.classList.remove("thumbnail-gallery-image");
  bigImage.classList.add("main-gallery-image");
  bigImage.removeAttribute("onclick");
}
