import { useEffect, useState } from "react";

import {
  SpeedDial,
  SpeedDialAction,
  SpeedDialIcon,
  Stack,
} from "@mui/material";

import { getScreenSize } from "utils/screen-size";
import * as ScreenConfigurations from "configurations/screen-configurations";

export const ProtectedHome = () => {

  const [screenSize, setScreenSize] = useState(ScreenConfigurations.DESKTOP);

  useEffect(() => {
    window.addEventListener("resize", () => {
      setScreenSize(getScreenSize());
    });
  }, []);

  if (screenSize == ScreenConfigurations.DESKTOP) {
    return (
      <Stack
        direction="row"
      >
        <Stack
          direction="column"
        >
          feeds
        </Stack>
        <Stack
          direction="column"
        >

        </Stack>
      </Stack>
    )
  }
  else {
    return <div>Mobile</div>
  }
}