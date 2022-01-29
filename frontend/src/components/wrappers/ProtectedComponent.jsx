import { useEffect, useState } from "react";
import { useRouter } from "next/router";

import { LoadingMask } from "components/wrappers/LoadingMask";
import { executeGet } from "utils/api-communication";
import * as API_ENDPOINTS from "configurations/api-endpoints";

export const ProtectedComponent =
  (Component) =>
  ({ ...props }) => {
    const router = useRouter();
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
      const isUserAuthenticated = async () => {
        let response = await executeGet(API_ENDPOINTS.GET_TOKEN, {});

        if (response.status == 401) {
          router.replace("/authentication");
          clearInterval(authenticationPoller);
          return false;
        } else if (response.status == 200) {
          setIsLoading(false);
          return true;
        }
      };

      if (isUserAuthenticated())
        var authenticationPoller = setInterval(isUserAuthenticated, 10000);
    }, []);

    if (!isLoading) return <Component {...props} />;
    else return <LoadingMask />;
  };
