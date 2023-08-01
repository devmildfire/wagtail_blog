console.log("AJAX is working");

async function makeRequest(url, method, body) {
  let headers = {
    "X-Requested-WIth": "XMLHttpRequest",
    "Content-Type": "application/json",
  };

  if ((method = "post")) {
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

  //   let ul_left = document.getElementById("left");
  //   let li = document.createElement("span");
  //   li.innerText = await data["number"];
  //   ul_left.appendChild(li);

  //   console.log(await data);
}
