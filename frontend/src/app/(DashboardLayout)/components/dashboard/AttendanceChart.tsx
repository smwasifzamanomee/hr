import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const EmployeeAttendanceChart = () => {
  const [attendanceData, setAttendanceData] = useState([]);

  console.log("a", attendanceData)

  useEffect(() => {
    const fetchAttendanceData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/employee-and-attendance-history/');
        setAttendanceData(response.data.attendance_history);
      } catch (error) {
        console.error('Error fetching attendance data:', error);
      }
    };

    fetchAttendanceData();
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={attendanceData}>
        <XAxis dataKey="date" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="total_present" stroke="#8884d8" />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default EmployeeAttendanceChart;