import { 
  AppBar,
  Button,
  Toolbar,
  Typography
} from "@mui/material";

import HomeIcon from '@mui/icons-material/Home';

export const AuthenticatedAppBar = () => {
  return (
    <AppBar position="fixed">
      <Toolbar>
        <Typography variant="h6">Socioworld</Typography>
        <Button sx={{ color: 'white' }} startIcon={<HomeIcon />}>
          Home
        </Button>
      </Toolbar>
    </AppBar>
  )
}