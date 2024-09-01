from django.db import models
from datetime import time

class Department(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}.  id = {self.id}"

class Designation(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}.  id = {self.id}"

class EmploymentType(models.TextChoices):
    ot = "ot"
    non_ot = "non_ot"

class Shift(models.TextChoices):
    day = "day"
    night = "night"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    shift = models.CharField(choices=Shift.choices, max_length=20, blank=True)
    employee_type = models.CharField(choices=EmploymentType.choices, max_length=20, blank=True)
    office_start_time = models.TimeField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}.  id = {self.id}"

    def get_day_shift_start_time(self):
        return time(8, 0, 0)  # 8:00 AM

    def get_night_shift_start_time(self):
        return time(20, 0, 0)  # 8:00 PM

    def save(self, *args, **kwargs):
        if self.shift == 'day':
            self.office_start_time = self.get_day_shift_start_time()
        elif self.shift == 'night':
            self.office_start_time = self.get_night_shift_start_time()
        super(Employee, self).save(*args, **kwargs)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

    @property
    def attendance_status(self):
        return "Present" if self.is_present else "Absent"

    @classmethod
    def get_attendance_statistics(cls, date):
        total_employees = Employee.objects.count()
        present_employees = cls.objects.filter(date=date, is_present=True).count()
        absent_employees = total_employees - present_employees
        attendance_percentage = (present_employees / total_employees) * 100
        return {
            "total_employees": total_employees,
            "present_employees": present_employees,
            "absent_employees": absent_employees,
            "attendance_percentage": attendance_percentage
        }