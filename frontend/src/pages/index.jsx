import { Button } from "@mui/material";

import { ProtectedRoute } from "components/ProtectedRoute";

function HomePage() {
  return <Button>Home</Button>
}
  
export default ProtectedRoute(HomePage);
