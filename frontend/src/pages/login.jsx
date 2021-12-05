import { useState } from "react";

import { useRouter } from "next/router";

import {
  Alert,
  Button,
  CircularProgress,
  Grid,
  Snackbar,
  TextField,
  Typography
} from "@mui/material";

import * as APIEndpoints from "configurations/api-endpoints";
import { executePost } from "utils/api-communication";

function Login() {

  const router = useRouter();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [usernameHelperText, setUsernameHelperText] = useState("");
  const [passwordHelperText, setPasswordHelperText] = useState("");
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [snackbarSeverity, setSnackbarSeverity] = useState("success");

  const [usernameInvalid, setUsernameInvalid] = useState(false);
  const [passwordInvalid, setPasswordInvalid] = useState(false);
  const [snackbarOpened, setSnackbarOpened] = useState(false);
  const [isLoginLoading, setIsLoginLoading] = useState(false);

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
    resetFormInputErrorStates();
    if (!validateLogin()) return;

    setIsLoginLoading(true);
    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    let response = await executePost(APIEndpoints.LOGIN, formData, { headers: { "Content-Type": null } });

    console.log(response);

    if (response.status === 200 && response.data) {
      localStorage.setItem("JWT-Token", response.data["access_token"]);
      router.replace("/");
      return;
    }
    else if (response.data && response.data["detail"]) {
      setSnackbarSeverity("error");
      setSnackbarMessage(response.data["detail"]);
      setSnackbarOpened(true);
    }
    setIsLoginLoading(false);
  }

  const handleSnackbarClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setSnackbarOpened(false);
  }

  const validateLogin = () => {
    let errorState = false;
    if (username === "") {
      errorState = true;
      setUsernameInvalid(true);
      setUsernameHelperText("Username is required");
    }
    if (password === "") {
      errorState = true;
      setPasswordInvalid(true);
      setPasswordHelperText("Password is required");
    }
    return !errorState;
  }

  const resetFormInputErrorStates = () => {
    setUsernameInvalid(false);
    setUsernameHelperText("");
    
    setPasswordInvalid(false);
    setPasswordHelperText("");
  }

  return (
    <Grid 
      container
      spacing={5}
      direction="column"
      alignItems="center"
      component="form"
      style={styles.parentContainer}
    >
      <Grid item xs={12}>
        <Typography variant="h2">Login</Typography>
      </Grid>
      <Grid item xs={12} style={styles.itemContainer}>
        <TextField 
          error={usernameInvalid}
          helperText={usernameHelperText}
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
          error={passwordInvalid}
          helperText={passwordHelperText}
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
        {isLoginLoading ? <CircularProgress /> : <Button variant="contained" onClick={performLogin}>Login</Button>}
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
