import { useEffect, useState } from "react";

import Stack from "@mui/material/Stack";

import { ApplicationBottomNavigation } from "components/home/ApplicationBottomNavigation";
import { LogoutDialog } from "components/home/LogoutDialog";
import { ProtectedComponent } from "components/wrappers/ProtectedComponent";

import { getScreenSize } from "utils/screen-size";
import * as ScreenConfigurations from "configurations/screen-configurations";

function index() {
  const [screenSize, setScreenSize] = useState(ScreenConfigurations.DESKTOP);
  const [logoutDialogOpen, setLogoutDialogOpen] = useState(false);

  useEffect(() => {
    window.addEventListener("resize", () => {
      setScreenSize(getScreenSize());
    });
  }, []);

  if (screenSize == ScreenConfigurations.DESKTOP)
    return (
      <Stack direction="column">
        <ApplicationBottomNavigation setLogoutDialogOpen={setLogoutDialogOpen} />
        <LogoutDialog logoutDialogOpen={logoutDialogOpen} setLogoutDialogOpen={setLogoutDialogOpen} />
      </Stack>
    );
  else return <div>Hello world!</div>;
}

export default ProtectedComponent(index);
