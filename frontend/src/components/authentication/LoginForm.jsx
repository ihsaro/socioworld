import { useState } from "react";

import { useRouter } from "next/router";

import {
  Alert,
  Button,
  CircularProgress,
  Checkbox,
  IconButton,
  InputAdornment,
  Snackbar,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

import { Visibility, VisibilityOff } from "@mui/icons-material";

import * as APIEndpoints from "configurations/api-endpoints";
import * as ApplicationVariables from "configurations/application-variables";
import { executePost } from "utils/api-communication";

export const LoginForm = () => {
  // States
  const [username, setUsername] = useState("");
  const [usernameError, setUsernameError] = useState(false);
  const [usernameErrorHelperText, setUsernameErrorHelperText] = useState("");
  const [password, setPassword] = useState("");
  const [passwordError, setPasswordError] = useState(false);
  const [passwordErrorHelperText, setPasswordErrorHelperText] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [rememberPassword, setRememberPassword] = useState(false);
  const [isLoggingIn, setIsLoggingIn] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [snackbarOpened, setSnackbarOpened] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState("success");
  const [loginButtonText, setLoginButtonText] = useState("Login");
  const [successfulLogin, setSuccessfulLogin] = useState(false);

  // Router
  const router = useRouter();

  // Styles
  const styles = {
    parentStack: {
      width: "30em",
      marginTop: "2em",
    },
    secondaryUserActionsStack: {
      width: "75%",
    },
    formInputField: {
      width: "75%",
      marginBottom: "2em",
    },
    loginLoadingSpinner: {
      color: "white",
      width: "25px",
      height: "25px",
    },
  };

  // Events
  const handleClickShowPassword = () => {
    setShowPassword(!showPassword);
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleRememberPasswordChange = (event) => {
    setRememberPassword(event.target.checked);
  };

  const handleSnackbarClose = (event, reason) => {
    if (reason !== "clickaway") {
      setSnackbarOpened(false);
    }
  };

  const performLogin = async () => {
    setIsLoggingIn(true);
    setUsernameError(false);
    setUsernameErrorHelperText("");
    setPasswordError(false);
    setPasswordErrorHelperText("");

    if (!isLoginInputValid()) {
      setIsLoggingIn(false);
    } else {
      let loginFormData = new FormData();
      loginFormData.append("username", username);
      loginFormData.append("password", password);

      let response = await executePost(APIEndpoints.LOGIN, loginFormData, {
        headers: {
          "Content-Type": null,
        },
        requireAuthentication: false,
      });

      if (response.status === 200 && response.data) {
        localStorage.setItem(
          ApplicationVariables.JWT_TOKEN_NAME,
          response.data["access_token"]
        );
        setSuccessfulLogin(true);
        setLoginButtonText("Login successful, redirecting to homepage");
        router.reload(window.location.pathname);
        return;
      } else if (response.data && response.data["detail"]) {
        setSnackbarSeverity("error");
        setSnackbarMessage(response.data["detail"]);
        setSnackbarOpened(true);
      }
      setIsLoggingIn(false);
    }
  };

  const isLoginInputValid = () => {
    let usernameEmpty = username === "";
    let passwordEmpty = password === "";

    setUsernameError(usernameEmpty);
    setUsernameErrorHelperText(usernameEmpty ? "Username required" : "");
    setPasswordError(passwordEmpty);
    setPasswordErrorHelperText(passwordEmpty ? "Password required" : "");

    return !(usernameEmpty || passwordEmpty);
  };

  return (
    <Stack direction="column" alignItems="center" style={styles.parentStack}>
      <TextField
        variant="standard"
        label="Username"
        required
        error={usernameError}
        helperText={usernameErrorHelperText}
        style={styles.formInputField}
        onChange={(e) => setUsername(e.target.value)}
        onKeyUp={e => {
          if (e.key === "Enter")
            performLogin()
        }}
      />
      <TextField
        variant="standard"
        label="Password"
        required
        error={passwordError}
        helperText={passwordErrorHelperText}
        type={showPassword ? "text" : "password"}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                onClick={handleClickShowPassword}
                onMouseDown={handleMouseDownPassword}
                edge="end"
              >
                {showPassword ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          ),
        }}
        style={styles.formInputField}
        onChange={(e) => setPassword(e.target.value)}
        onKeyUp={e => {
          if (e.key === "Enter")
            performLogin()
        }}
      />
      <Button
        variant="contained"
        disabled={isLoggingIn}
        style={styles.formInputField}
        onClick={performLogin}
      >
        {!isLoggingIn || successfulLogin ? (
          loginButtonText
        ) : (
          <CircularProgress style={styles.loginLoadingSpinner} />
        )}
      </Button>
      <Stack
        direction="row"
        justifyContent="space-between"
        style={styles.secondaryUserActionsStack}
      >
        <Button variant="text" color="error">
          Forgot Password
        </Button>
        <Stack direction="row">
          <Checkbox
            checked={rememberPassword}
            value={rememberPassword}
            onChange={handleRememberPasswordChange}
          />
        </Stack>
      </Stack>
      <Snackbar
        open={snackbarOpened}
        autoHideDuration={6000}
        onClose={handleSnackbarClose}
      >
        <Alert
          onClose={handleSnackbarClose}
          severity={snackbarSeverity}
          sx={{ width: "100%" }}
        >
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </Stack>
  );
};
