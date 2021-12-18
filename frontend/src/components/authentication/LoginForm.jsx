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

  const [states, setStates] = useState({
    username: "",
    usernameError: false,
    usernameErrorHelperText: "",
    password: "",
    passwordError: false,
    passwordErrorHelperText: "",
    showPassword: false,
    rememberPassword: false,
    isLoggingIn: false
  });

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
    setStates({
      ...states,
      showPassword: !states.showPassword,
    });
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleRememberPasswordChange = (event) => {
    setStates({
      ...states,
      rememberPassword: event.target.checked
    });
  }

  const performLogin = event => {
    setStates({
      ...states,
      isLoggingIn: true,
      usernameError: false,
      usernameErrorHelperText: "",
      passwordError: false,
      passwordErrorHelperText: ""
    });
    
    if (!isLoginInputValid()) {
      setStates({
        ...states,
        isLoggingIn: false,
      });
    }
  }
  
  const isLoginInputValid = () => {
    setStates({
      ...states,
      usernameError: states.username === "",
      usernameErrorHelperText: states.username === "" ? "Username required": "",
      passwordError: states.password === "",
      passwordErrorHelperText: states.password === "" ? "Password required": "",
    });
    
    return !(states.usernameError || states.passwordError);
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
        error={states.usernameError}
        helperText={states.usernameError ? states.usernameErrorHelperText : ""}
        style={styles.formInputField}
        onChange={e => {
          setStates({
            ...states,
            username: e.target.value,
          });
        }}
      />
      <TextField
        variant="standard"
        label="Password"
        required
        error={states.passwordError}
        helperText={states.passwordError ? states.passwordErrorHelperText : ""}
        type={states.showPassword ? 'text' : 'password'}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                onClick={handleClickShowPassword}
                onMouseDown={handleMouseDownPassword}
                edge="end"
              >
                {states.showPassword ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          )
        }}
        style={styles.formInputField}
        onChange={e => {
          setStates({
            ...states,
            password: e.target.value,
          });
        }}
      />
      <Button
        variant="contained"
        disabled={states.isLoggingIn}
        style={styles.formInputField}
        onClick={performLogin}
      >{states.isLoggingIn ? <CircularProgress style={styles.loginLoadingSpinner} /> : "Login"}</Button>
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
            checked={states.rememberPassword}
            value={states.rememberPassword}
            onChange={handleRememberPasswordChange}
          />
        </Stack>
      </Stack>
    </Stack>
  )
}