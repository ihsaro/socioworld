import { useState } from "react";

import {
  Button,
  CircularProgress,
  Checkbox,
  IconButton,
  InputAdornment,
  Stack,
  TextField,
  Typography
} from "@mui/material";

import {
  Visibility,
  VisibilityOff
} from "@mui/icons-material";

export const LoginForm = () => {

  const [username, setUsername] = useState("");
  const [usernameError, setUsernameError] = useState(false);
  const [usernameErrorHelperText, setUsernameErrorHelperText] = useState("");
  const [password, setPassword] = useState("");
  const [passwordError, setPasswordError] = useState(false);
  const [passwordErrorHelperText, setPasswordErrorHelperText] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [rememberPassword, setRememberPassword] = useState(false);
  const [isLoggingIn, setIsLoggingIn] = useState(false);

  // Styles
  const styles = {
    parentStack: {
      width: "30em",
      marginTop: "2em"
    },
    secondaryUserActionsStack: {
      width: "75%"
    },
    formInputField: {
      width: "75%",
      marginBottom: "2em"
    },
    loginLoadingSpinner: {
      color: "white",
      width: "25px",
      height: "25px"
    }
  }

  // Events
  const handleClickShowPassword = () => {
    setShowPassword(!showPassword);
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleRememberPasswordChange = (event) => {
    setRememberPassword(event.target.checked);
  }

  const performLogin = event => {
    setIsLoggingIn(true);
    setUsernameError(false);
    setUsernameErrorHelperText("");
    setPasswordError(false);
    setPasswordErrorHelperText("");
    
    if (!isLoginInputValid()) {
      setIsLoggingIn(false);
    }
  }
  
  const isLoginInputValid = () => {

    let usernameEmpty = username === "";
    let passwordEmpty = password === "";

    setUsernameError(usernameEmpty);
    setUsernameErrorHelperText(usernameEmpty ? "Username required": "");
    setPasswordError(passwordEmpty);
    setPasswordErrorHelperText(passwordEmpty ? "Password required": "");

    return !(usernameEmpty || passwordEmpty);
  }

  return (
    <Stack
      direction="column"
      alignItems="center"
      style={styles.parentStack}
    >
      <TextField
        variant="standard"
        label="Username"
        required
        error={usernameError}
        helperText={usernameError ? usernameErrorHelperText : ""}
        style={styles.formInputField}
        onChange={e => setUsername(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Password"
        required
        error={passwordError}
        helperText={passwordError ? passwordErrorHelperText : ""}
        type={showPassword ? 'text' : 'password'}
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
          )
        }}
        style={styles.formInputField}
        onChange={e => setPassword(e.target.value)}
      />
      <Button
        variant="contained"
        disabled={isLoggingIn}
        style={styles.formInputField}
        onClick={performLogin}
      >{isLoggingIn ? <CircularProgress style={styles.loginLoadingSpinner} /> : "Login"}</Button>
      <Stack
        direction="row"
        justifyContent="space-between"
        style={styles.secondaryUserActionsStack}
      >
        <Button
          variant="text"
          color="error"
        >Forgot Password</Button>
        <Stack direction="row">
          <Checkbox
            checked={rememberPassword}
            value={rememberPassword}
            onChange={handleRememberPasswordChange}
          />
        </Stack>
      </Stack>
    </Stack>
  )
}