import * as ApplicationVariables from "configurations/application-variables";

export const executeDelete = async () => {

}

export const executeGet = async (
  url,
  {
    mode = "cors", 
    credentials = "include",
  }
  ) => {
  try {
    const response = await fetch(`${ApplicationVariables.APPLICATION_URL}${url}`, {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: mode, // no-cors, *cors, same-origin
      credentials: credentials, // include, *same-origin, omit
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
    credentials = "include",
    headers = {
      "Content-Type": "application/json"
    },
  }
  ) => {
  if (headers["Content-Type"] === "application/json") {
    data = JSON.stringify(data);
  }
  else if (headers["Content-Type"] === null) {
    delete headers["Content-Type"];
  }

  try {
    const response = await fetch(`${ApplicationVariables.APPLICATION_URL}${url}`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      body: data, // body data type must match "Content-Type" header
      mode: mode, // no-cors, *cors, same-origin
      credentials: credentials, // include, *same-origin, omit
      headers: headers,
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