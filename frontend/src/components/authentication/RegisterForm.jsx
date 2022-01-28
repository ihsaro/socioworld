import { useState } from "react";

import { useRouter } from "next/router";

import {
  Alert,
  Button,
  CircularProgress,
  IconButton,
  InputAdornment,
  Snackbar,
  Stack,
  TextField,
} from "@mui/material";

import AdapterDateFns from "@mui/lab/AdapterDateFns";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import DatePicker from "@mui/lab/DatePicker";

import { Visibility, VisibilityOff } from "@mui/icons-material";

import * as APIEndpoints from "configurations/api-endpoints";
import { executePost } from "utils/api-communication";

export const RegisterForm = () => {
  // States
  const [firstName, setFirstName] = useState("frontend");
  const [firstNameError, setFirstNameError] = useState(false);
  const [firstNameErrorHelperText, setFirstNameErrorHelperText] = useState("");
  const [lastName, setLastName] = useState("test");
  const [lastNameError, setLastNameError] = useState(false);
  const [lastNameErrorHelperText, setLastNameErrorHelperText] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState(new Date());
  const [dateOfBirthError, setDateOfBirthError] = useState(false);
  const [dateOfBirthErrorHelperText, setDateOfBirthErrorHelperText] =
    useState("");
  const [emailAddress, setEmailAddress] = useState("frontend");
  const [emailAddressError, setEmailAddressError] = useState(false);
  const [emailAddressErrorHelperText, setEmailAddressErrorHelperText] =
    useState("");
  const [username, setUsername] = useState("frontend");
  const [usernameError, setUsernameError] = useState(false);
  const [usernameErrorHelperText, setUsernameErrorHelperText] = useState("");
  const [password, setPassword] = useState("1");
  const [passwordError, setPasswordError] = useState(false);
  const [passwordErrorHelperText, setPasswordErrorHelperText] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("1");
  const [confirmPasswordError, setConfirmPasswordError] = useState(false);
  const [confirmPasswordErrorHelperText, setConfirmPasswordErrorHelperText] =
    useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [isRegistering, setIsRegistering] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [snackbarOpened, setSnackbarOpened] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState("success");
  const [registerButtonText, setRegisterButtonText] = useState("Register");
  const [successfulRegistration, setSuccessfulRegistration] = useState(false);

  const router = useRouter();

  // Styles
  const styles = {
    parentStack: {
      width: "30em",
      marginTop: "2em",
    },
    formInputField: {
      width: "75%",
      marginBottom: "2em",
    },
    registerLoadingSpinner: {
      color: "white",
      width: "25px",
      height: "25px",
    },
  };

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
    } else {
      let response = await executePost(
        APIEndpoints.REGISTER_CLIENT,
        {
          first_name: firstName,
          last_name: lastName,
          date_of_birth: `${dateOfBirth.getFullYear()}-${dateOfBirth.getMonth()}-${dateOfBirth.getDate()}`,
          email: emailAddress,
          username: username,
          password: password,
        },
        {
          requireAuthentication: false,
        }
      );

      if (response.status === 201 && response.data) {
        setSuccessfulRegistration(true);
        setRegisterButtonText(
          "Registration successful, redirecting to login page"
        );
        router.reload(window.location.pathname);
        return;
      } else if (response.status === 422) {
        setSnackbarSeverity("error");
        setSnackbarMessage(
          "Input format error, please check your data and try again"
        );
        setSnackbarOpened(true);
      } else if (response.data && response.data["detail"]) {
        setSnackbarSeverity("error");
        setSnackbarMessage(response.data["detail"]);
        setSnackbarOpened(true);
      }
      setIsRegistering(false);
    }
  };

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
    setFirstNameErrorHelperText(firstNameEmpty ? "First name required" : "");

    setLastNameError(lastNameEmpty);
    setLastNameErrorHelperText(lastNameEmpty ? "Last name required" : "");

    setDateOfBirthError(dateOfBirthEmpty);
    setDateOfBirthErrorHelperText(
      dateOfBirthEmpty ? "Date of birth required" : ""
    );

    setEmailAddressError(emailAddressEmpty);
    setEmailAddressErrorHelperText(
      emailAddressEmpty ? "Email address required" : ""
    );

    setUsernameError(usernameEmpty);
    setUsernameErrorHelperText(usernameEmpty ? "Username required" : "");

    setPasswordError(passwordEmpty);
    setPasswordErrorHelperText(passwordEmpty ? "Password required" : "");

    setConfirmPasswordError(
      confirmPasswordEmpty || passwordNotEqualsToConfirmPassword
    );

    if (confirmPasswordEmpty)
      setConfirmPasswordErrorHelperText("Please confirm your password");
    else if (passwordNotEqualsToConfirmPassword)
      setConfirmPasswordErrorHelperText("Passwords do not match");
    else setConfirmPasswordErrorHelperText("");

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
  };

  const handleSnackbarClose = (event, reason) => {
    if (reason !== "clickaway") {
      setSnackbarOpened(false);
    }
  };

  return (
    <Stack direction="column" alignItems="center" style={styles.parentStack}>
      <TextField
        variant="standard"
        label="First Name"
        required
        error={firstNameError}
        helperText={firstNameErrorHelperText}
        style={styles.formInputField}
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Last Name"
        required
        error={lastNameError}
        helperText={lastNameErrorHelperText}
        style={styles.formInputField}
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DatePicker
          label="Date of Birth"
          value={dateOfBirth}
          maxDate={new Date()}
          onChange={(newDate) => setDateOfBirth(newDate)}
          renderInput={(params) => (
            <TextField
              {...params}
              variant="standard"
              required
              error={dateOfBirthError}
              helperText={dateOfBirthErrorHelperText}
              style={styles.formInputField}
            />
          )}
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
        onChange={(e) => setEmailAddress(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Username"
        required
        error={usernameError}
        helperText={usernameErrorHelperText}
        style={styles.formInputField}
        value={username}
        onChange={(e) => setUsername(e.target.value)}
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
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <TextField
        variant="standard"
        label="Confirm Password"
        required
        error={confirmPasswordError}
        helperText={confirmPasswordErrorHelperText}
        type={showConfirmPassword ? "text" : "password"}
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
          ),
        }}
        style={styles.formInputField}
        value={confirmPassword}
        onChange={(e) => setConfirmPassword(e.target.value)}
      />
      <Button
        variant="contained"
        disabled={isRegistering}
        style={styles.formInputField}
        onClick={performRegister}
      >
        {!isRegistering || successfulRegistration ? (
          registerButtonText
        ) : (
          <CircularProgress style={styles.registerLoadingSpinner} />
        )}
      </Button>
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
