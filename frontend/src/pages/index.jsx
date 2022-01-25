import {
  useEffect,
  useState
} from "react";

import { Home } from "components/home/Home";

import { ProtectedComponent } from "components/wrappers/ProtectedComponent";

function index() {

  const [states, setStates] = useState({
    isAuthenticated: false,
    isLoading: true
  });

  useEffect(() => {
    setStates({
      ...states,
      isLoading: false
    });

    console.log("Not HOC");
  }, [])

  if (states.isLoading)
    return <div>Loading</div>
  else
    return <Home />
}
  
export default ProtectedComponent(index);
