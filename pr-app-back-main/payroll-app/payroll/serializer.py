from rest_framework import serializers
from .models import (
    Department, EmpSalaryCalc, Permission, EmpPosition, Employee, EmpPerm,
    DepartmentHead, EmpSalary, EmpGivenSalary, EmpWorkHour, 
    EmpWorkHourLeave, SalaryConfig
)
import datetime

# Serializer for Department model
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentDictSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source = 'department_id')
    class Meta:
        model = Permission
        fields = ['id', 'name']  # Include only `id` and custom `name`

# Serializer for Permission model
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionDictSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source = 'perm_id')
    class Meta:
        model = Permission
        fields = ['id', 'name']  # Include only `id` and custom `name`

# Serializer for EmpPosition model
class EmpPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpPosition
        fields = '__all__'

# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(default=datetime.datetime.now)
    modified_date = serializers.DateTimeField(default=datetime.datetime.now)
    birth_date = serializers.DateField(
        default=datetime.date.today,
    )
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeDictSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    id = serializers.IntegerField(source = 'emp_id')
    class Meta:
        model = Employee
        fields = ['id', 'name']  # Include only `id` and custom `name`

    def get_name(self, obj):
        # Get the first letter of first name and last name
        first_name = obj.first_name
        last_initial = obj.last_name[0].upper() if obj.last_name else ""
        return f"{first_name} .{last_initial}"

# Serializer for EmpPerm model
class EmpPermSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpPerm
        fields = '__all__'

# Serializer for DepartmentHead model
class DepartmentHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentHead
        fields = '__all__'

class DepartmentHeadDictSerializer(serializers.ModelSerializer):
    name = serializers.IntegerField(source = 'emp_id.emp_id')
    id = serializers.IntegerField(source = 'department_id.department_id')
    class Meta:
        model = DepartmentHead
        fields = ['id', 'name'] 

# Serializer for EmpSalary model
class EmpSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpSalary
        fields = '__all__'

# Serializer for EmpGivenSalary model
class EmpGivenSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpGivenSalary
        fields = '__all__'

# Serializer for EmpWorkHour model
class EmpWorkHourSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(default=datetime.datetime.now)
    end_date = serializers.DateTimeField(default=datetime.datetime.now)
    work_start_date = serializers.DateTimeField(default=datetime.datetime.now)
    work_end_date = serializers.DateTimeField(default=datetime.datetime.now)
    modified_date = serializers.DateTimeField(default=datetime.datetime.now)

    class Meta:
        model = EmpWorkHour
        fields = '__all__'

# Serializer for EmpWorkHourLeave model
class EmpWorkHourLeaveSerializer(serializers.ModelSerializer):
    leave_start = serializers.DateField(default=datetime.date.today)
    leave_end = serializers.DateTimeField(default=datetime.datetime.now)

    class Meta:
        model = EmpWorkHourLeave
        fields = '__all__'

class EmpSalaryCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpSalaryCalc
        fields = '__all__'
        
class SalaryConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryConfig
        fields = '__all__'
