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

import * as APIEndpoints from "configurations/api-endpoints";
import { executePost } from "utils/api-communication";

export const RegisterForm = () => {

  // States
  const [firstName, setFirstName] = useState("");
  const [firstNameError, setFirstNameError] = useState(false);
  const [firstNameErrorHelperText, setFirstNameErrorHelperText] = useState("");
  const [lastName, setLastName] = useState("");
  const [lastNameError, setLastNameError] = useState(false);
  const [lastNameErrorHelperText, setLastNameErrorHelperText] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState(new Date());
  const [dateOfBirthError, setDateOfBirthError] = useState(false);
  const [dateOfBirthErrorHelperText, setDateOfBirthErrorHelperText] = useState("");
  const [emailAddress, setEmailAddress] = useState("");
  const [emailAddressError, setEmailAddressError] = useState(false);
  const [emailAddressErrorHelperText, setEmailAddressErrorHelperText] = useState("");
  const [username, setUsername] = useState("");
  const [usernameError, setUsernameError] = useState(false);
  const [usernameErrorHelperText, setUsernameErrorHelperText] = useState("");
  const [password, setPassword] = useState("");
  const [passwordError, setPasswordError] = useState(false);
  const [passwordErrorHelperText, setPasswordErrorHelperText] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState(false);
  const [confirmPasswordErrorHelperText, setConfirmPasswordErrorHelperText] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [isRegistering, setIsRegistering] = useState(false);


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

  const handleClickShowPassword = () => {
    setShowPassword(!showPassword);
  };

  const handleClickShowConfirmPassword = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleMouseDownConfirmPassword = (event) => {
    event.preventDefault();
  };

  const performRegister = async () => {
    setIsRegistering(true);
    setFirstNameError(false);
    setFirstNameErrorHelperText("");
    setLastNameError(false);
    setLastNameErrorHelperText("");
    setDateOfBirthError(false);
    setDateOfBirthErrorHelperText("");
    setEmailAddressError(false);
    setEmailAddressErrorHelperText("");
    setUsernameError(false);
    setUsernameErrorHelperText("");
    setPasswordError(false);
    setPasswordErrorHelperText("");
    setConfirmPasswordError(false);
    setConfirmPasswordErrorHelperText("");
    
    if (!isRegisterInputValid()) {
      setIsRegistering(false);
    }
    else {
      let response = await executePost(
        APIEndpoints.REGISTER_CLIENT, 
        {},
        {
          requireAuthentication: false
        }
      );

      if (response.status === 201 && response.data) {
        router.reload(window.location.pathname);
      }
      else if (response.data && response.data["detail"]) {
        /*
        setSnackbarSeverity("error");
        setSnackbarMessage(response.data["detail"]);
        setSnackbarOpened(true);
        */
      }
      setIsRegistering(false);
    }
  }

  const isRegisterInputValid = () => {
    let firstNameEmpty = firstName === "";
    let lastNameEmpty = lastName === "";
    let dateOfBirthEmpty = dateOfBirth === null || "";
    let emailAddressEmpty = emailAddress === "";
    let usernameEmpty = username === "";
    let passwordEmpty = password === "";
    let confirmPasswordEmpty = confirmPassword === "";
    let passwordNotEqualsToConfirmPassword = password !== confirmPassword;

    setFirstNameError(firstNameEmpty);
    setFirstNameErrorHelperText(firstNameEmpty ? "First name required": "");

    setLastNameError(lastNameEmpty);
    setLastNameErrorHelperText(lastNameEmpty ? "Last name required": "");

    setDateOfBirthError(dateOfBirthEmpty);
    setDateOfBirthErrorHelperText(dateOfBirthEmpty ? "Date of birth required": "");

    setEmailAddressError(emailAddressEmpty);
    setEmailAddressErrorHelperText(emailAddressEmpty ? "Email address required": "");

    setUsernameError(usernameEmpty);
    setUsernameErrorHelperText(usernameEmpty ? "Username required": "");
    
    setPasswordError(passwordEmpty);
    setPasswordErrorHelperText(passwordEmpty ? "Password required": "");
    
    setConfirmPasswordError(confirmPasswordEmpty || passwordNotEqualsToConfirmPassword);

    if (confirmPasswordEmpty)
      setConfirmPasswordErrorHelperText("Please confirm your password");
    else if (passwordNotEqualsToConfirmPassword)
      setConfirmPasswordErrorHelperText("Passwords do not match");
    else
      setConfirmPasswordErrorHelperText("");

    return !(
      firstNameEmpty ||
      lastNameEmpty ||
      dateOfBirthEmpty ||
      emailAddressEmpty ||
      usernameEmpty ||
      passwordEmpty ||
      confirmPasswordEmpty ||
      passwordNotEqualsToConfirmPassword
    );
  }

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
        error={firstNameError}
        helperText={firstNameErrorHelperText}
        style={styles.formInputField}
        value={firstName}
        onChange={e => setFirstName(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Last Name"
        required
        error={lastNameError}
        helperText={lastNameErrorHelperText}
        style={styles.formInputField}
        value={lastName}
        onChange={e => setLastName(e.target.value)}
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DatePicker
          label="Date of Birth"
          value={dateOfBirth}
          maxDate={new Date()}
          onChange={newDate => setDateOfBirth(newDate)}
          renderInput={(params) => <TextField {...params} variant="standard" required error={dateOfBirthError} helperText={dateOfBirthErrorHelperText} style={styles.formInputField} />}
        />
      </LocalizationProvider>
      <TextField
        variant="standard"
        label="Email Address"
        required
        error={emailAddressError}
        helperText={emailAddressErrorHelperText}
        style={styles.formInputField}
        value={emailAddress}
        onChange={e => setEmailAddress(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Username"
        required
        error={usernameError}
        helperText={usernameErrorHelperText}
        style={styles.formInputField}
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Password"
        required
        error={passwordError}
        helperText={passwordErrorHelperText}
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
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Confirm Password"
        required
        error={confirmPasswordError}
        helperText={confirmPasswordErrorHelperText}
        type={showConfirmPassword ? 'text' : 'password'}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle confirm password visibility"
                onClick={handleClickShowConfirmPassword}
                onMouseDown={handleMouseDownConfirmPassword}
                edge="end"
              >
                {showConfirmPassword ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          )
        }}
        style={styles.formInputField}
        value={confirmPassword}
        onChange={e => setConfirmPassword(e.target.value)}
      />
      <Button
        variant="contained"
        style={styles.formInputField}
        onClick={performRegister}
      >Register</Button>
    </Stack>
  )
}