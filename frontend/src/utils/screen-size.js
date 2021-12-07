import * as ScreenConfigurations from "configurations/screen-configurations";

export const getScreenSize = () => {
  if (window.innerWidth < 768) {
    return ScreenConfigurations.MOBILE
  } else {
    return ScreenConfigurations.DESKTOP
  }
}