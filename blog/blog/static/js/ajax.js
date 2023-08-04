console.log("AJAX is working");

async function makeRequest(url, method, body, returnType) {
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

  if (returnType == "html") {
    return await response.text(); //returning HTML response instead of JSON
  }

  if (returnType == "json") {
    return await response.json();
  }
}

//  make a post request to crypto page to change it's sorting from default to chosen via select on page
async function postCrypto(selectObject) {
  console.log("POST request to crypto");

  var value = selectObject.value;
  console.log(value);

  let dataString = value;

  const data = await makeRequest(
    "/crypto/",
    "post",
    JSON.stringify({ sortby: dataString }),
    "html"
  );

  const html = document.querySelectorAll("html")[0];

  // console.log('replacing HTML')

  html.innerHTML = data;
}

//  make a post request to crypto page to add a tag to taglist
async function postAddTag(tag) {
  console.log("POST request to root for tag addition");

  console.log("toggling tag...", tag);

  const data = await makeRequest(
    "/crypto/",
    "post",
    JSON.stringify({ addTag: tag }),
    "html"
  );

  // await data["addedTag"];
  // console.log(await data);

  const html = document.querySelectorAll("html")[0];

  // console.log('replacing HTML')

  html.innerHTML = data;
}

// async function getNumber() {
//   console.log("gets number");

//   const data = await makeRequest("/", "get");

//   let ul_left = document.getElementById("left");
//   let li = document.createElement("span");

//   li.addEventListener("click", getFloatNumber);

//   li.innerText = await data["number"];
//   ul_left.appendChild(li);

//   console.log(await data);
// }

// async function getFloatNumber(e) {
//   console.log("gets FLOAT number");

//   let number = e.target.innerText;

//   const data = await makeRequest(
//     "/",
//     "post",
//     JSON.stringify({ number: number })
//   );

//   let ul_right = document.getElementById("right");
//   let li2 = document.createElement("span");
//   li2.innerText = await data["float"];
//   ul_right.appendChild(li2);

//   console.log(await data);
// }

//  функция перенаправляет пользователя на страницу с url, если его текущая страница отличается от этого url
function moveToPage(url) {
  
  
  const path = window.location.pathname
  
  console.log(`path ${path}`);

  console.log(`url ${url}`);

  if (path !== url) {
    window.location=url;
    console.log(`moving to ${url} Page`);
  } else {
    console.log(`allready at Page ${url}`);
  }

}


