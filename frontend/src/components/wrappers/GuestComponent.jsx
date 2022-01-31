import { useEffect, useState } from "react";
import { useRouter } from "next/router";

import { LoadingMask } from "components/wrappers/LoadingMask";
import { executeGet } from "utils/api-communication";
import * as API_ENDPOINTS from "configurations/api-endpoints";

export const GuestComponent =
  (Component) =>
  ({ ...props }) => {
    const router = useRouter();
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
      const isUserAuthenticated = async () => {
        let response = await executeGet(API_ENDPOINTS.IS_AUTHENTICATED, {});

        if (response.status == 200) {
          router.replace("/");
        } else if (response.status == 401) setIsLoading(false);
      };

      isUserAuthenticated();
    }, []);

    if (!isLoading) return <Component {...props} />;
    else return <LoadingMask />;
  };
