import { useTheme } from '@mui/material/styles';
import { Typography} from '@mui/material';
import DashboardCard from '@/app/(DashboardLayout)/components/shared/DashboardCard';

type Props = {
    value: number;
};

const Absent = ({ value }: Props) => {
  // chart color
  const theme = useTheme();

 

  return (
    <DashboardCard
      title="Absent"
    >
      <>
        <Typography variant="h3" fontWeight="700" mt="-20px">
          {value}
        </Typography>
      </>
    </DashboardCard>
  );
};

export default Absent;
