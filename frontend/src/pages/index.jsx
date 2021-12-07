import {
  useEffect,
  useState
} from "react";

import { GuestHome } from "components/home/GuestHome";
import { ProtectedHome } from "components/home/ProtectedHome";
import * as AuthenticationUtils from "utils/authentication-utils";

function HomePage() {

  const [states, setStates] = useState({
    isAuthenticated: false,
    isLoading: true
  });

  useEffect(() => {
    setStates({
      ...states,
      isAuthenticated: AuthenticationUtils.isUserAuthenticated(),
      isLoading: false
    });
  }, [])

  if (states.isLoading)
    return <div>Loading</div>
  else
    if (states.isAuthenticated)
      return <ProtectedHome />
    else
      return <GuestHome />
}
  
export default HomePage;
