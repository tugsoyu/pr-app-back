from django.db import models

# Create your models here.
class Department(models.Model):
  department_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=20)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=20)
    # name = models.CharField(max_length = 50)
    # duration = models.IntegerField(default =  0)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # price = models.IntegerField(default = 0)
    # level = models.IntegerField(default = 1)
    # recommended_people_no = models.IntegerField(default=1)
    # type = models.CharField(max_length=20)
    # tag1 = models.CharField(max_length=30)
    # tag2 = models.CharField(max_length=30)
    # tag3 = models.CharField(max_length=30)
    # province = models.CharField(max_length=50)
    # district = models.CharField(max_length=50)
    # description = models.CharField(max_length=2000)
    # main_img_path = models.ImageField(blank=True, null=True, upload_to=upload_path)
    # created_date = models.DateTimeField(default =  django.utils.timezone.now)
    # modified_date = models.DateTimeField(default =  django.utils.timezone.now)
class Permission(models.Model):
  perm_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=20)

class EmpPosition(models.Model):
  position_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=20)
  desc = models.CharField(max_length=400)

class Employee(models.Model):
  emp_id = models.IntegerField(primary_key=True)
  pos_id = models.ForeignKey(EmpPosition, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.CharField(max_length=20)
  phone = models.CharField(max_length=20)
  birth_date = models.DateField(null=True, blank=True)
  department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
  password = models.CharField(max_length=50)
  created_by = models.IntegerField()
  created_date = models.DateTimeField()
  modified_by = models.IntegerField()
  modified_date = models.DateTimeField()

class EmpPerm(models.Model):
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  perm_id = models.ForeignKey(Permission, on_delete=models.CASCADE)
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['emp_id', 'perm_id'], name='unique_emp_perm'
      )
    ]

class DepartmentHead(models.Model):
  department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['department_id', 'emp_id'], name='unique_department_head'
      )
    ]
class EmpSalary(models.Model):
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  salary_type = models.IntegerField()
  status = models.IntegerField()
  salary_desc = models.CharField(max_length=400)
  salary_amount = models.IntegerField()
  active_from = models.DateField()
  inactiv_since = models.DateField()
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['emp_id', 'salary_type', 'status'], name='unique_emp_salary'
      )
    ]

class EmpGivenSalary(models.Model):
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  salary_month = models.IntegerField()
  salary_year = models.IntegerField()
  given_amount = models.IntegerField()
  taxes = models.IntegerField()
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['emp_id', 'salary_month', 'salary_year'], name='unique_emp_given_salary'
      )
    ]

class EmpWorkHour(models.Model):
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  work_date = models.DateField()
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  work_start_date = models.DateTimeField()
  work_end_date = models.DateTimeField()
  salary_hour = models.IntegerField()
  late_hour = models.IntegerField()
  leave_hour = models.IntegerField()
  status = models.IntegerField()
  modified_by = models.IntegerField()
  modified_date = models.DateTimeField()
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['emp_id', 'work_date'], name='unique_emp_work_hour'
      )
    ]
class EmpWorkHourLeave(models.Model):
  leave_id = models.IntegerField(primary_key=True)
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  leave_start = models.DateField()
  leave_end = models.DateTimeField()
  leave_duration = models.IntegerField()
  leave_type = models.IntegerField()
  leave_desc = models.CharField(max_length=400)
  is_salary = models.IntegerField()
  status = models.IntegerField()
  approver = models.IntegerField()

class EmpSalaryCalc(models.Model):
  emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  work_date = models.DateField()
  sum_hour = models.IntegerField()
  salaray_hour = models.IntegerField()
  hourly_salary = models.IntegerField()
  salary_sum = models.IntegerField()
  ndsh_tax = models.IntegerField()
  hhot_tax = models.IntegerField()
  status = models.IntegerField()
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['emp_id', 'work_date'], name='unique_emp_salary_calc'
      )
    ]
class SalaryConfig(models.Model):
  config_name = models.CharField(max_length=50, primary_key=True)
  config_value = models.CharField(max_length=100)