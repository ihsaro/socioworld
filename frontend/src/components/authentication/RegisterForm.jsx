import { useState } from "react";

import {
  Button,
  IconButton,
  InputAdornment,
  Stack,
  TextField
} from "@mui/material";

import {
  Visibility,
  VisibilityOff
} from "@mui/icons-material";

export const RegisterForm = () => {

  const [states, setStates] = useState({
    showPassword: false
  });

  // Styles
  const styles = {
    parentStack: {
      width: "30em",
      marginTop: "2em"
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

  return (
    <Stack
      direction="column"
      alignItems="center"
      style={styles.parentStack}
    >
      <TextField
        variant="standard"
        label="First Name"
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
      >Register</Button>
    </Stack>
  )
}