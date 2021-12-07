import { useState } from "react";

import {
  Box,
  Stack,
  Tab,
  Tabs,
  Typography
} from "@mui/material";

import { LoginForm } from "components/authentication/LoginForm";
import { RegisterForm } from "components/authentication/RegisterForm";

export const GuestHome = () => {

  const [states, setStates] = useState({
    currentTabIndex: 0
  });

  const styles = {
    parentStack: {
      marginTop: "2em"
    },
    title: {
      textAlign: "center"
    }
  }

  const handleTabChange = (event, selectedTabIndex) => {
    setStates({
      ...states,
      currentTabIndex: selectedTabIndex
    });
  };

  return (
    <Stack
      direction="column"
      alignItems="center"
      style={styles.parentStack}
    >
      <Typography variant="h2" style={styles.title}>Welcome to Socioworld</Typography>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={states.currentTabIndex} onChange={handleTabChange}>
          <Tab label="Login" />
          <Tab label="Register" />
        </Tabs>
      </Box>
      {states.currentTabIndex == 0 ? <LoginForm /> : <RegisterForm />}
    </Stack>
  );
}