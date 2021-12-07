import { 
  Stack,
  Typography,
} from "@mui/material";

import { LoginChildStack } from "components/LoginChildStack";

const Login = () => {

  // Stylesheet
  const styles = {
    parentStack: {
      marginTop: "2em"
    }
  };

  return (
    <Stack
      direction="column"
      alignItems="center"
      justifyContent="flex-start"
      style={styles.parentStack}
    >
      <LoginChildStack />
    </Stack>
  );
}

export default Login;