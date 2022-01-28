import { useEffect, useState } from "react";

import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import Stack from "@mui/material/Stack";

import FeedIcon from "@mui/icons-material/Feed";
import LogoutIcon from "@mui/icons-material/Logout";
import PeopleIcon from "@mui/icons-material/People";

import { ProtectedComponent } from "components/wrappers/ProtectedComponent";

import { getScreenSize } from "utils/screen-size";
import * as ScreenConfigurations from "configurations/screen-configurations";

function index() {
  const [tabSelected, setTabSelected] = useState(0);
  const [screenSize, setScreenSize] = useState(ScreenConfigurations.DESKTOP);
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  useEffect(() => {
    window.addEventListener("resize", () => {
      setScreenSize(getScreenSize());
    });
  }, []);

  if (screenSize == ScreenConfigurations.DESKTOP)
    return (
      <Stack direction="column">
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
              onClick={handleClickOpen}
            />
          </BottomNavigation>
        </Box>
        <Dialog
          open={open}
          onClose={handleClose}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
        >
          <DialogTitle id="alert-dialog-title">{"Logout?"}</DialogTitle>
          <DialogContent>
            <DialogContentText id="alert-dialog-description">
              Do you want to logout?
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose}>NO</Button>
            <Button onClick={handleClose} autoFocus>
              YES
            </Button>
          </DialogActions>
        </Dialog>
      </Stack>
    );
  else return <div>Hello world!</div>;
}

export default ProtectedComponent(index);
