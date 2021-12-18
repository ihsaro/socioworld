import * as ApplicationVariables from "configurations/application-variables";

export const isUserAuthenticated = () => {
  if (localStorage && localStorage.getItem(ApplicationVariables.JWT_TOKEN_NAME)) {
    
  }
  else return false;
}