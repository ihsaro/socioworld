import Stack from '@mui/material/Stack';
import LinearProgress from '@mui/material/LinearProgress';
import Typography from '@mui/material/Typography';

export const LoadingMask = () => {
    return (
        <Stack sx={{ width: '50%', margin: '40vh auto' }} spacing={2} direction="column">
            <LinearProgress color="primary" />
            <Typography variant="h6">LOADING</Typography>
        </Stack>
    )
};
