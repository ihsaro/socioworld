import { useEffect, useState } from "react";

import Stack from "@mui/material/Stack";

import { ApplicationBottomNavigation } from "components/home/ApplicationBottomNavigation";
import { LogoutDialog } from "components/home/LogoutDialog";
import { ProtectedComponent } from "components/wrappers/ProtectedComponent";

import { getScreenSize } from "utils/screen-size";

function index() {
  const [logoutDialogOpen, setLogoutDialogOpen] = useState(false);
  const [selectedFeature, setSelectedFeature] = useState(<div>Feeds</div>);

  useEffect(() => {
    window.addEventListener("resize", () => {
      setScreenSize(getScreenSize());
    });
  }, []);

  return (
    <Stack direction="column">
      {selectedFeature}
      <ApplicationBottomNavigation setLogoutDialogOpen={setLogoutDialogOpen} setSelectedFeature={setSelectedFeature} />
      <LogoutDialog logoutDialogOpen={logoutDialogOpen} setLogoutDialogOpen={setLogoutDialogOpen} />
    </Stack>
  );
}

export default ProtectedComponent(index);
