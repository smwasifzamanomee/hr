from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'designations', views.DesignationViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'attendance', views.AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employee-and-attendance/', views.EmployeeAndAttendanceView.as_view(), name='employee-and-attendance'),
    path('employee-and-attendance-history/', views.EmployeeAndAttendanceHistoryView.as_view(), name='employee-and-attendance-history'),
    path('all-employee/', views.EmployeeAPIView.as_view(), name="all-employee")
]