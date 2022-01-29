import { useState } from "react";

import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";
import Box from "@mui/material/Box";

import FeedIcon from "@mui/icons-material/Feed";
import LogoutIcon from "@mui/icons-material/Logout";
import PeopleIcon from "@mui/icons-material/People";

export const ApplicationBottomNavigation = ({ setLogoutDialogOpen }) => {
  const [tabSelected, setTabSelected] = useState(0);

  return (
    <Box sx={{ width: "99.5%", position: "absolute", bottom: "0" }}>
      <BottomNavigation
        showLabels
        value={tabSelected}
        onChange={(event, newValue) => {
          setTabSelected(newValue);
        }}
      >
        <BottomNavigationAction label="Feeds" icon={<FeedIcon />} />
        <BottomNavigationAction label="Friends" icon={<PeopleIcon />} />
        <BottomNavigationAction
          label="Logout"
          icon={<LogoutIcon />}
          onClick={() => setLogoutDialogOpen(true)}
        />
      </BottomNavigation>
    </Box>
  );
};
