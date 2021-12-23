import * as ApplicationVariables from "configurations/application-variables";

export const executeDelete = async () => {

}

export const executeGet = async (
  url,
  {
    mode = "cors", 
    cache = "no-cache", 
    credentials = "include",
    headers = {
      "Authorization": "Bearer "
    },
    redirect = "follow",
    referrerPolicy = "no-referrer-when-downgrade",
    requireAuthentication = true
  }
  ) => {
  if (requireAuthentication && localStorage && localStorage.getItem(ApplicationVariables.JWT_TOKEN_NAME)) {
    headers["Authorization"] = headers["Authorization"].concat(localStorage.getItem(ApplicationVariables.JWT_TOKEN_NAME))
  }
  else {
    delete headers["Authorization"];
  }

  try {
    const response = await fetch(`${ApplicationVariables.APPLICATION_URL}${url}`, {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
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
  catch (exception) {
    return {
      "data": {
        "detail": "Server error, please try again"
      },
      "status": 500
    };
  }
}

export const executePatch = async () => {

}

export const executePost = async (
  url, 
  data, 
  {
    mode = "cors", 
    cache = "no-cache", 
    credentials = "include",
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer "
    },
    redirect = "follow",
    referrerPolicy = "no-referrer",
    requireAuthentication = true
  }
  ) => {
  if (headers["Content-Type"] === "application/json") {
    data = JSON.stringify(data);
  }
  else if (headers["Content-Type"] === null) {
    delete headers["Content-Type"];
  }

  if (requireAuthentication && localStorage && localStorage.getItem(ApplicationVariables.JWT_TOKEN_NAME)) {
    headers["Authorization"] = headers["Authorization"].concat(localStorage.getItem(ApplicationVariables.JWT_TOKEN_NAME))
  }
  else {
    delete headers["Authorization"];
  }

  try {
    const response = await fetch(`${ApplicationVariables.APPLICATION_URL}${url}`, {
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
  catch (exception) {
    return {
      "data": {
        "detail": "Server error, please try again"
      },
      "status": 500
    };
  }
}