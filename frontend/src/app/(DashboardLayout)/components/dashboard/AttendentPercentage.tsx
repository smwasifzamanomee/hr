import { useTheme } from '@mui/material/styles';
import { Typography} from '@mui/material';
import DashboardCard from '@/app/(DashboardLayout)/components/shared/DashboardCard';

type Props = {
    value: number;
};

const AttendentPercentage = ({ value }: Props) => {
  // chart color
  const theme = useTheme();

 

  return (
    <DashboardCard
      title="Attendance Percentage"
    >
      <>
        <Typography variant="h3" fontWeight="700" mt="-20px">
          {value.toFixed()} %
        </Typography>
      </>
    </DashboardCard>
  );
};

export default AttendentPercentage;
