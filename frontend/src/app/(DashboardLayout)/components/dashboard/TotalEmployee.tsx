import { useTheme } from '@mui/material/styles';
import { Typography} from '@mui/material';
import DashboardCard from '@/app/(DashboardLayout)/components/shared/DashboardCard';

type Props = {
    value: number;
};

const TotalEmployee = ({ value }: Props) => {
  // chart color
  const theme = useTheme();

 

  return (
    <DashboardCard
      title="Total Employee"
    >
      <>
        <Typography variant="h3" fontWeight="700" mt="-20px">
           {value}
        </Typography>
      </>
    </DashboardCard>
  );
};

export default TotalEmployee;
