import { Button } from "@mui/material";
import { AuthenticatedAppBar } from "components/AuthenticatedAppBar";

import { ProtectedRoute } from "components/ProtectedRoute";

function HomePage() {
  return (
    <>
      <AuthenticatedAppBar />
    </>
  );
}
  
export default ProtectedRoute(HomePage);
