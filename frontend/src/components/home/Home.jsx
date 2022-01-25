import { useEffect, useState } from "react";

import {
  SpeedDial,
  SpeedDialAction,
  SpeedDialIcon,
  Stack,
} from "@mui/material";

import { executeGet } from "utils/api-communication";
import * as APIEndpoints from "configurations/api-endpoints";

import { getScreenSize } from "utils/screen-size";
import * as ScreenConfigurations from "configurations/screen-configurations";

export const Home = () => {

  const [feeds, setFeeds] = useState([]);
  const [screenSize, setScreenSize] = useState(ScreenConfigurations.DESKTOP);

  useEffect(() => {
    
    const fetchFeeds = async() => {
      let response = await executeGet(APIEndpoints.LIST_FRIEND_FEEDS, {});
      if (response && response.data) {
        debugger;
      }
    }

    fetchFeeds();

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