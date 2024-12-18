from django.contrib import admin

from payroll.models import Department, EmpPosition, EmpSalary, EmpSalaryCalc, EmpWorkHour, Employee, Permission

# Register your models here.
admin.site.register(Department)
admin.site.register(EmpPosition)
admin.site.register(Employee)
admin.site.register(EmpWorkHour)
admin.site.register(EmpSalary)
admin.site.register(EmpSalaryCalc)
admin.site.register(Permission)