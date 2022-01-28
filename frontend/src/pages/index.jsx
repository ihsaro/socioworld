import {
  useEffect,
  useState
} from "react";

import { Home } from "components/home/Home";

import { ProtectedComponent } from "components/wrappers/ProtectedComponent";

import { getScreenSize } from "utils/screen-size";
import * as ScreenConfigurations from "configurations/screen-configurations";

function index() {

  const [screenSize, setScreenSize] = useState(ScreenConfigurations.DESKTOP);

  useEffect(() => {
    window.addEventListener('resize', () => {
      setScreenSize(getScreenSize())
    })
  }, [])

  if (screenSize == ScreenConfigurations.DESKTOP)
    return <div>Hello desktop!</div>
  else
    return <div>Hello world!</div>
}
  
export default ProtectedComponent(index);
