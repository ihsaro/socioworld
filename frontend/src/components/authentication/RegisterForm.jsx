import { useState } from "react";

import {
  Button,
  IconButton,
  InputAdornment,
  Stack,
  TextField
} from "@mui/material";

import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import DatePicker from '@mui/lab/DatePicker';

import {
  Visibility,
  VisibilityOff
} from "@mui/icons-material";

export const RegisterForm = () => {

  const [states, setStates] = useState({
    showPassword: false,
    showConfirmPassword: false
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
  const handleChangeDateOfBirth = () => {

  }

  const handleClickShowPassword = () => {
    setStates({
      ...states,
      showPassword: !states.showPassword,
    });
  };

  const handleClickShowConfirmPassword = () => {
    setStates({
      ...states,
      showConfirmPassword: !states.showConfirmPassword,
    });
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleMouseDownConfirmPassword = (event) => {
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
        style={styles.formInputField}
      />
      <TextField
        variant="standard"
        label="Last Name"
        style={styles.formInputField}
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DatePicker
          label="Date of Birth"
          onChange={handleChangeDateOfBirth}
          renderInput={(params) => <TextField {...params} variant="standard" style={styles.formInputField} />}
        />
      </LocalizationProvider>
      <TextField
        variant="standard"
        label="Email Address"
        style={styles.formInputField}
      />
      <TextField
        variant="standard"
        label="Username"
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
      <TextField
        variant="standard"
        label="Confirm Password"
        required
        type={states.showConfirmPassword ? 'text' : 'password'}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle confirm password visibility"
                onClick={handleClickShowConfirmPassword}
                onMouseDown={handleMouseDownConfirmPassword}
                edge="end"
              >
                {states.showConfirmPassword ? <VisibilityOff /> : <Visibility />}
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