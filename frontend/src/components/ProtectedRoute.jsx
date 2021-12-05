import { useEffect, useState } from "react";

import { useRouter } from "next/router";

export const ProtectedRoute = Component => ({ ...props }) => {
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [authenticated, setAuthenticated] = useState(false);

  useEffect(() => {
    const accessToken = localStorage.getItem("JWT-Token");

    if (!accessToken) {
      router.replace("/login");
      setAuthenticated(false);
    }
    else {
      setAuthenticated(true);
    }

    setLoading(false);
  }, []);

  if (loading) {
    return <div>Loading ...</div>
  }
  else if (!loading && authenticated) {
    return <Component {...props} />
  }
  else {
    return null;
  }
}
