import {
  Stack,
  Typography
} from "@mui/material";

import {
  HandymanOutlined,
  MessageOutlined,
  StorefrontOutlined
} from "@mui/icons-material";

export const DesktopWelcome = () => {

  const styles = {
    parentStack: {
      width: "100%",
      margin: "1em"
    }
  }

  return (
    <Stack
      direction="column"
      alignItems="flex-start"
      justifyContent="flex-start"
      style={styles.parentStack}
    >
      <DesktopWelcomeItem
        icon="MESSAGE"
        message="Welcome to socioworld, a social media which is just a hobby project"
      />
      <DesktopWelcomeItem
        icon="HANDY"
        message="Welcome to socioworld, a social media which is just a hobby project"
      />
      <DesktopWelcomeItem
        icon="STORE"
        message="Welcome to socioworld, a social media which is just a hobby project"
      />
    </Stack>
  )
}

export const MobileWelcome = () => {
  return (
    <div></div>
  )
}

const DesktopWelcomeItem = (props) => {

  // Styles
  const styles = {
    parentStack: {
      marginBottom: "2em"
    },
    welcomeIcon: {
      marginBottom: "0.5em"
    }
  }

  let Icon = <HandymanOutlined style={styles.welcomeIcon} />;

  switch (props.icon) {
    case "HANDY":
      Icon = <HandymanOutlined style={styles.welcomeIcon} />;
      break;
    case "MESSAGE":
      Icon = <MessageOutlined style={styles.welcomeIcon} />;
      break;
    case "STORE":
      Icon = <StorefrontOutlined style={styles.welcomeIcon} />;
      break;
  }

  return (
    <Stack
      direction="column"
      alignItems="flex-start"
      justifyContent="flex-start"
      style={styles.parentStack}
    >
      {Icon}
      <Typography>
        {props.message}
      </Typography>
    </Stack>
  )
}