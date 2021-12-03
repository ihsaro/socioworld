import { useState } from "react";

import {
  Alert,
  Button,
  Grid,
  Snackbar,
  TextField,
  Typography
} from "@mui/material";

import * as APIEndpoints from "configurations/api-endpoints";
import { executePost } from "utils/api-communication";

function Login() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [snackbarOpened, setSnackbarOpened] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState("success");
  const [snackbarMessage, setSnackbarMessage] = useState("");

  const styles = {
    parentContainer: {
      marginTop: "5em"
    },
    itemContainer: {
      width: "20em"
    },
    inputField: {
      width: "100%"
    }
  };

  const performLogin = async () => {
    // validateLogin();
    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    let response = await executePost(APIEndpoints.LOGIN, formData, { headers: { "Content-Type": null } });

    console.log(response);

    if (response.status === 200 && response.data) {
      localStorage.setItem("JWT-Token", response.data["access_token"]);
    }
    else if (response.data && response.data["detail"]) {
      setSnackbarSeverity("error");
      setSnackbarMessage(response.data["detail"]);
      setSnackbarOpened(true);
    }
  }

  const handleSnackbarClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setSnackbarOpened(false);
  }

  const validateLogin = () => {

  }

  return (
    <Grid 
      container
      spacing={5}
      direction="column"
      alignItems="center"
      style={styles.parentContainer}
    >
      <Grid item xs={12}>
        <Typography variant="h2">Login</Typography>
      </Grid>
      <Grid item xs={12} style={styles.itemContainer}>
        <TextField 
          label="Username" 
          variant="standard" 
          value={username} 
          onChange={e => setUsername(e.target.value)}
          required
          style={styles.inputField} 
        />
      </Grid>
      <Grid item xs={12} style={styles.itemContainer}>
        <TextField 
          label="Password" 
          variant="standard" 
          type="password" 
          value={password} 
          onChange={e => setPassword(e.target.value)} 
          required 
          style={styles.inputField}
        />
      </Grid>
      <Grid item container xs={12} justifyContent="space-between" style={styles.itemContainer}>
        <Button variant="contained" onClick={performLogin}>Login</Button>
        <Button color="error">Forgot password</Button>
      </Grid>
      <Snackbar open={snackbarOpened} autoHideDuration={6000} onClose={handleSnackbarClose}>
        <Alert onClose={handleSnackbarClose} severity={snackbarSeverity} sx={{ width: '100%' }}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </Grid>
  )
}
  
export default Login;
