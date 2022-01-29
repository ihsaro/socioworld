import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";

import { BLACKLIST_TOKEN } from "configurations/api-endpoints";
import { executePost } from "utils/api-communication";

export const LogoutDialog = ({ logoutDialogOpen, setLogoutDialogOpen }) => {

  const logout = () => {
    executePost(BLACKLIST_TOKEN, {}, {}).then(response => {
      debugger;
    });
  };

  return (
    <Dialog
      fullWidth
      maxWidth="sm"
      open={logoutDialogOpen}
      onClose={() => setLogoutDialogOpen(false)}
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
        <Button onClick={() => setLogoutDialogOpen(false)}>NO</Button>
        <Button onClick={() => logout()} autoFocus>
          YES
        </Button>
      </DialogActions>
    </Dialog>
  );
};
