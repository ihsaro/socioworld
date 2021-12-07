import { 
  Stack,
  Typography,
} from "@mui/material";

import {
  useEffect,
  useState
} from "react";

import { DesktopWelcome, MobileWelcome } from "components/Welcome";
import { LoginForm } from "components/authentication/LoginForm";

import * as ScreenConfigurations from "configurations/screen-configurations";
import { getScreenSize } from "utils/screen-size";

export const LoginChildStack = () => {

  // States
  const [screenSize, setScreenSize] = useState(ScreenConfigurations.DESKTOP);

  // Effects
  useEffect(() => {
    window.addEventListener("resize", handleScreenResize)
  }, []);

  // Event handlers
  const handleScreenResize = () => {
    setScreenSize(getScreenSize());
  }

  const styles = {
    parentStack: {
      width: "35em",
      marginTop: "2em"
    }
  };

  return (
    <Stack
      direction={screenSize == ScreenConfigurations.DESKTOP ? "row": "column"}
      alignItems="flex-start"
      style={styles.parentStack}
    >
      <LoginForm />
    </Stack>
  )
}