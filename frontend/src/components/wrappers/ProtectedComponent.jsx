import { useEffect, useState } from "react";
import { useRouter } from "next/router";

import { executeGet } from "utils/api-communication";
import * as API_ENDPOINTS from "configurations/api-endpoints";

export const ProtectedComponent = Component => ({ ...props }) => {

    const router = useRouter();
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const isUserAuthenticated = async () => {
            let response = await executeGet(API_ENDPOINTS.GET_TOKEN, {});

            if (response.status == 401) {
                router.replace("/authentication");
                console.log("HOC");
            }
            else if (response.status == 200)
                setIsLoading(false);
        }

        isUserAuthenticated();
    }, []);

    if (!isLoading)
        return <Component {...props} />
    else
        return <div>Loading ...</div>
}