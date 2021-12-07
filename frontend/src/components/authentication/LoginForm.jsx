import { useState } from "react";

import {
  Button,
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
    showPassword: false,
    rememberPassword: false
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
        style={styles.formInputField}
      />
      <TextField
        variant="standard"
        label="Password"
        required
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
      />
      <Button
        variant="contained"
        style={styles.formInputField}
      >Login</Button>
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