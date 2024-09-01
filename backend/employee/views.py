from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import DepartmentSerializer, DesignationSerializer, EmployeeSerializer, AttendanceSerializer
from .models import Department, Designation, Employee, Attendance
from rest_framework.response import Response
from rest_framework import generics
from datetime import date, timedelta
from utils.pagination import CustomPageNumberPagination
from rest_framework import status

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        paginator = CustomPageNumberPagination()

        employees = Employee.objects.all().order_by('-id')
        paginated_employees = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(paginated_employees, many=True)
        data = serializer.data
        result = {
            "results": data,
            "message": "All Employee list",
            "status": status.HTTP_200_OK,
            "count": employees.count(),
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),

        }
        return Response(result, status=status.HTTP_200_OK)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class EmployeeAndAttendanceView(APIView):
    def get(self, request):
        today = date.today()
        total_employees = Employee.objects.count()
        present_employees = Attendance.objects.filter(date=today, is_present=True).count()
        absent_employees = total_employees - present_employees
        attendance_percentage = (present_employees / total_employees) * 100 if total_employees else 0

        return Response({
            "total_employees": total_employees,
            "total_present": present_employees,
            "total_absent": absent_employees,
            "attendance_percentage": attendance_percentage
        })

class EmployeeAndAttendanceHistoryView(APIView):
    def get(self, request):
        today = date.today()
        last_5_days = [today - timedelta(days=i) for i in range(5, -1, -1)]

        attendance_history = []
        for day in last_5_days:
            total_employees = Employee.objects.count()
            present_employees = Attendance.objects.filter(date=day, is_present=True).count()
            absent_employees = total_employees - present_employees
            attendance_percentage = (present_employees / total_employees) * 100 if total_employees else 0

            attendance_history.append({
                "date": day,
                "total_employees": total_employees,
                "total_present": present_employees,
                "total_absent": absent_employees,
                "attendance_percentage": attendance_percentage
            })

        # Save the attendance history to the database
        # for data in attendance_history:
        #     AttendanceHistory.objects.create(
        #         date=data["date"],
        #         total_employees=data["total_employees"],
        #         total_present=data["total_present"],
        #         total_absent=data["total_absent"]
        #     )

        return Response({
            "attendance_history": attendance_history
        })

