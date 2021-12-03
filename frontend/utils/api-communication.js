import { APPLICATION_URL } from "configurations/application-variables";

export const executeDelete = async () => {

}

export const executeGet = async () => {

}

export const executePatch = async () => {

}

export const executePost = async (
  url, 
  data, 
  {
    mode = "cors", 
    cache = "no-cache", 
    credentials = "same-origin",
    headers = {
      "Content-Type": "application/json"
    },
    redirect = "follow",
    referrerPolicy = "no-referrer"
  }
  ) => {
  if (headers["Content-Type"] === "application/json") {
    data = JSON.stringify(data);
  }
  else if (headers["Content-Type"] === null) {
    delete headers["Content-Type"];
  }

  const response = await fetch(`${APPLICATION_URL}${url}`, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    body: data, // body data type must match "Content-Type" header
    mode: mode, // no-cors, *cors, same-origin
    cache: cache, // *default, no-cache, reload, force-cache, only-if-cached
    credentials: credentials, // include, *same-origin, omit
    headers: headers,
    redirect: redirect, // manual, *follow, error
    referrerPolicy: referrerPolicy, // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  });
  return {
    "data": await response.json(),
    "status": response.status
  };
}