console.log("AJAX is working");

function httpGet(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, false); // false for synchronous request
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

async function makeGetRequest(url, returnType = "json") {
  let headers = {
    "X-Requested-WIth": "XMLHttpRequest",
    "Content-Type": "application/json",
  };

  let response = await fetch(url, {
    method: "get",
    headers: headers,
  });

  if (returnType == "html") {
    return await response.text(); //returning HTML response instead of JSON
  }

  if (returnType == "json") {
    return await response.json();
  }
}

async function makeRequest(url, method, body = null, returnType = "json") {
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

  const html = document.querySelectorAll("html")[0];

  html.innerHTML = data;

  window.location.href = "/crypto/";
}

async function postRevealAllTags() {
  console.log("POST request to root for showing all tags");

  const data = await makeRequest(
    "/crypto/",
    "post",
    JSON.stringify({ showAll: true }),
    "html"
  );

  const html = document.querySelectorAll("html")[0];

  html.innerHTML = data;

  window.location.href = "/crypto/";
}

//  функция перенаправляет пользователя на страницу с url, если его текущая страница отличается от этого url
function moveToPage(url) {
  const path = window.location.pathname;

  console.log(`path ${path}`);

  console.log(`url ${url}`);

  if (path !== url) {
    window.location.pathname = url;
    console.log(`moving to ${url} Page`);
  } else {
    console.log(`allready at Page ${url}`);
  }
}
