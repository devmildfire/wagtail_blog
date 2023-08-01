console.log("AJAX is working");

async function makeRequest(url, method, body) {
  let headers = {
    "X-Requested-WIth": "XMLHttpRequest",
    "Content-Type": "application/json",
  };

  if (method == "post") {
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value;
    headers["X-CSRFToken"] = csrf;
  }

  let response = await fetch(url, {
    method: method,
    headers: headers,
    body: body,
  });

  return await response.json();
}

async function getNumber() {
  console.log("gets number");

  const data = await makeRequest("/", "get");

  let ul_left = document.getElementById("left");
  let li = document.createElement("span");

  li.addEventListener("click", getFloatNumber);

  li.innerText = await data["number"];
  ul_left.appendChild(li);

  console.log(await data);
}

async function getFloatNumber(e) {
  console.log("gets FLOAT number");

  let number = e.target.innerText;

  const data = await makeRequest(
    "/",
    "post",
    JSON.stringify({ number: number })
  );

  let ul_right = document.getElementById("right");
  let li2 = document.createElement("span");
  li2.innerText = await data["float"];
  ul_right.appendChild(li2);

  console.log(await data);
}

// async function postCrypto() {
//   console.log("POST request to crypto");

//   let dataString = "popularity";

//   const data = await makeRequest(
//     "/crypto/",
//     "post",
//     JSON.stringify({ sortby: dataString })
//   );

//   let ul_right = document.getElementById("right");
//   let li2 = document.createElement("span");
//   li2.innerText = await data["sorted"];
//   ul_right.appendChild(li2);

//   console.log(await data);
// }

function postCrypto() {
  console.log("POST request to crypto");

  let dataString = "popularity";

  let headers = {
    "X-Requested-WIth": "XMLHttpRequest",
    "Content-Type": "application/json",
  };

  const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value;
  headers["X-CSRFToken"] = csrf;

  fetch("/crypto/", {
    method: "post",
    headers: headers,
    body: JSON.stringify({ sortby: dataString }),
  });
}

function getCrypto() {
  console.log("gets Crypto");

  makeRequest("/", "get");

  // const data = await makeRequest("/", "get");

  // let ul_left = document.getElementById("left");
  // let li = document.createElement("span");

  // li.addEventListener("click", getFloatNumber);

  // li.innerText = await data["number"];
  // ul_left.appendChild(li);

  // console.log(await data);
}

// async function postCryptoPage() {
//   console.log("POST request to crypto");

//   let dataString = "popularity";

//   const data = await makeRequest(
//     "/crypto/",
//     "post",
//     JSON.stringify({ sortby: dataString })
//   );

//   let ul_right = document.getElementById("right");
//   let li2 = document.createElement("span");
//   li2.innerText = await data["sorted"];
//   ul_right.appendChild(li2);

//   console.log(await data);
// }
