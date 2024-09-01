'use client'
import { Grid, Box, Typography, Modal, TableContainer, Table, TableHead, TableRow, TableCell, TableBody, TextField, InputAdornment, IconButton, TablePagination } from '@mui/material';
import PageContainer from '@/app/(DashboardLayout)/components/container/PageContainer';
// components
import SalesOverview from '@/app/(DashboardLayout)/components/dashboard/SalesOverview';
import YearlyBreakup from '@/app/(DashboardLayout)/components/dashboard/YearlyBreakup';
import RecentTransactions from '@/app/(DashboardLayout)/components/dashboard/RecentTransactions';
import ProductPerformance from '@/app/(DashboardLayout)/components/dashboard/ProductPerformance';
import Blog from '@/app/(DashboardLayout)/components/dashboard/Blog';
import MonthlyEarnings from '@/app/(DashboardLayout)/components/dashboard/MonthlyEarnings';
import TotalEmployee from './components/dashboard/TotalEmployee';
import Present from './components/dashboard/Present';
import Absent from './components/dashboard/Absent';
import AttendentPercentage from './components/dashboard/AttendentPercentage';
import { PieChart } from '@mui/x-charts/PieChart';
import { LineChart } from '@mui/x-charts';

import axios from "axios";
import { useEffect, useState } from 'react';
import AttendanceChart from './components/dashboard/AttendanceChart';
import { SearchOffOutlined } from '@mui/icons-material';

type dataProps = {
  total_employees: number,
  total_present: number,
  total_absent: number,
  attendance_percentage: number
}

type employeeProps = [{
  id: number;
  name: string;
  address: string;
  qualification: string;
  department_name: string;
  designation_name: string;
  salary: number;
  shift: string;
  employee_type: string;
  office_start_time: string;
}];



const Dashboard = () => {
  const [open, setOpen] = useState(false);
  const [employees, setEmployees] = useState<employeeProps>();

  console.log("employe", employees)

  const [page, setPage] = useState(1);
  const [rowsPerPage, setRowsPerPage] = useState(10);

  const handleOpen = () => {
    setOpen(true);
    fetchEmployees();
  };

  const handleClose = () => setOpen(false);

  const fetchEmployees = async (page: number, rowsPerPage: number) => {
    try {
      const response = await axios.get<employeeProps>(`http://127.0.0.1:8000/api/employees/?page=${page}&page_size=${rowsPerPage}`);
      console.log("res", response)
      setEmployees(response?.data?.results);
    } catch (error) {
      console.error(error);
    }
  };
  const [data, setData] = useState<dataProps>({
    total_employees: 0,
    total_present: 0,
    total_absent: 0,
    attendance_percentage: 0
  });

  useEffect(() => {
    const options = {
      method: 'GET',
      url: 'http://127.0.0.1:8000//api/employee-and-attendance/',
    };

    axios.request(options).then(function (response) {
      setData(response.data);
    }).catch(function (error) {
      console.error(error);
    });
  }, [])

  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
    fetchEmployees(newPage + 1, rowsPerPage);
  };

  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
    fetchEmployees(1, parseInt(event.target.value, 10));
  };


  return (
    <PageContainer title="Dashboard" description="this is Dashboard">
      <Box>
        <Grid container spacing={3}>

          <Grid item xs={12} lg={4}>
            <Grid container spacing={3}>
              <Grid item xs={12} onClick={() => handleOpen()}>
                <TotalEmployee value={data?.total_employees} />
              </Grid>
              <Grid item xs={12}>
                <Present value={data?.total_present} />
              </Grid>
              <Grid item xs={12}>
                <Absent value={data?.total_absent} />
              </Grid>
              <Grid item xs={12}>
                <AttendentPercentage value={data?.attendance_percentage} />
              </Grid>
            </Grid>
          </Grid>
          <Grid item xs={12} lg={8}>
            <PieChart
              series={[
                {
                  data: [
                    { id: 0, value: data.total_employees, label: `Total Employee: ${data.total_employees}` },
                    { id: 1, value: data.total_present, label: `Present: ${data.total_present}` },
                    { id: 2, value: data.total_absent, label: `Absent: ${data.total_absent}` },
                  ],
                },
              ]}
              width={700}
              height={300}
            />
            {/* <LineChart
              xAxis={[{ data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] }]}
              series={[
                {
                  data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
                },
              ]}
              width={800}
              height={400}
            /> */}
            <Typography sx={{
              height: "10vh"
            }}>
            </Typography>
            <AttendanceChart />
          </Grid>
        </Grid>
      </Box>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '80%',
          bgcolor: 'background.paper',
          boxShadow: 24,
          p: 4,
          overflow: "hidden",
          overflowY: "scroll",
          maxHeight: "80Vh"
        }}>
          <Box sx={{ mb: 2 }}>
            <TextField
              placeholder="Search employees"
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <IconButton>
                      <SearchOffOutlined />
                    </IconButton>
                  </InputAdornment>
                ),
              }}
              variant="outlined"
              fullWidth
            />
          </Box>
          <TableContainer sx={{
            bgcolor: "#EEE3DE"
          }}>
            <Table>
              <TableHead sx={{
                bgcolor: "#DEE7EE"
              }}>
                <TableRow >
                  <TableCell style={{ border: '1px solid #ddd' }}>ID</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Name</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Address</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Qualification</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Department</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Designation</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Salary</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Shift</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Employee Type</TableCell>
                  <TableCell style={{ border: '1px solid #ddd' }}>Office Start Time</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {employees?.map((employee) => (
                  <TableRow key={employee.id}>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.id}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.name}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.address}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.qualification}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.department_name}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.designation_name}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.salary}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.shift}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.employee_type}</TableCell>
                    <TableCell style={{ border: '1px solid #ddd' }}>{employee.office_start_time}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[5, 10, 25]}
            component="div"
            count={data.total_employees}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </Box>
      </Modal>
    </PageContainer>
  )
}

export default Dashboard;
