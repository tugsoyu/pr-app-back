from datetime import timedelta
from payroll.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.http import JsonResponse
from django.db.models import Sum


class LoginView(APIView):

    def post(self, request):
        emp_id = request.data.get('emp_id')
        password = request.data.get('password')

        # Validate input
        if not emp_id or not password:
            return JsonResponse({'error': 'emp_id and password are required'}, status=400)

        try:
            # Get the employee record
            employee = Employee.objects.get(emp_id=emp_id)
            
            # Check if the password matches
            if password == employee.password:
                response = JsonResponse({'message': 'Login successful'})
                # Set the emp_id in a cookie
                response.set_cookie(key='emp_id', value=emp_id, httponly=True, max_age=24 * 60 * 60, samesite='None', secure=True)
                return response
            else:
                return JsonResponse({'error': 'Invalid password'}, status=401)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        
class DepartmentDictListView(APIView):
    # GET: List all departments
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentDictSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)


class DepartmentListView(APIView):
    # GET: List all departments
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)

    # POST: Create a new department
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetailView(APIView):
    # GET: Retrieve a specific department
    def get(self, request, department_id):
        try:
            department = Department.objects.get(department_id=department_id)
        except Department.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department)
        return JsonResponse(serializer.data)

    # PUT: Update a specific department
    def put(self, request, department_id):
        try:
            department = Department.objects.get(department_id=department_id)
        except Department.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a specific department
    def delete(self, request, department_id):
        try:
            department = Department.objects.get(department_id=department_id)
        except Department.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        department.delete()
        return JsonResponse({"message": "Department deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class PermissionDictListView(APIView):
    def get(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionDictSerializer(permissions, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class PermissionListView(APIView):
    def get(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PermissionDetailView(APIView):
    def get(self, request, perm_id):
        try:
            permission = Permission.objects.get(perm_id=perm_id)
        except Permission.DoesNotExist:
            return JsonResponse({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PermissionSerializer(permission)
        return JsonResponse(serializer.data)

    def put(self, request, perm_id):
        try:
            permission = Permission.objects.get(perm_id=perm_id)
        except Permission.DoesNotExist:
            return JsonResponse({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, perm_id):
        try:
            permission = Permission.objects.get(perm_id=perm_id)
        except Permission.DoesNotExist:
            return JsonResponse({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)

        permission.delete()
        return JsonResponse({"message": "Permission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class EmpPositionListView(APIView):
    def get(self, request):
        positions = EmpPosition.objects.all()
        serializer = EmpPositionSerializer(positions, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = EmpPositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpPositionDetailView(APIView):
    def get(self, request, position_id):
        try:
            position = EmpPosition.objects.get(position_id=position_id)
        except EmpPosition.DoesNotExist:
            return JsonResponse({"error": "Position not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpPositionSerializer(position)
        return JsonResponse(serializer.data)

    def put(self, request, position_id):
        try:
            position = EmpPosition.objects.get(position_id=position_id)
        except EmpPosition.DoesNotExist:
            return JsonResponse({"error": "Position not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpPositionSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, position_id):
        try:
            position = EmpPosition.objects.get(position_id=position_id)
        except EmpPosition.DoesNotExist:
            return JsonResponse({"error": "Position not found"}, status=status.HTTP_404_NOT_FOUND)

        position.delete()
        return JsonResponse({"message": "Position deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        if(request.data['birth_date']):
            request.data['birth_date'] = request.data['birth_date'][:10]
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    def get(self, request, emp_id):
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id):
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id):
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return JsonResponse({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EmployeeDictListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeDictSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class EmpPermListView(APIView):
    def get(self, request):
        emp_perms = EmpPerm.objects.all()
        serializer = EmpPermSerializer(emp_perms, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = EmpPermSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpPermDetailView(APIView):
    def get(self, request, emp_id, perm_id):
        try:
            emp_perm = EmpPerm.objects.get(emp_id=emp_id, perm_id=perm_id)
        except EmpPerm.DoesNotExist:
            return JsonResponse({"error": "EmpPerm not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpPermSerializer(emp_perm)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id, perm_id):
        try:
            emp_perm = EmpPerm.objects.get(emp_id=emp_id, perm_id=perm_id)
        except EmpPerm.DoesNotExist:
            return JsonResponse({"error": "EmpPerm not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpPermSerializer(emp_perm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id, perm_id):
        try:
            emp_perm = EmpPerm.objects.get(emp_id=emp_id, perm_id=perm_id)
        except EmpPerm.DoesNotExist:
            return JsonResponse({"error": "EmpPerm not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_perm.delete()
        return JsonResponse({"message": "EmpPerm deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class DepartmentHeadDictListView(APIView):
    def get(self, request):
        dept_heads = DepartmentHead.objects.all()
        serializer = DepartmentHeadDictSerializer(dept_heads, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class DepartmentHeadListView(APIView):
    def get(self, request):
        dept_heads = DepartmentHead.objects.all()
        
        serializer = DepartmentHeadSerializer(dept_heads, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = DepartmentHeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentHeadDetailView(APIView):
    def get(self, request, department_id, emp_id):
        try:
            dept_head = DepartmentHead.objects.get(department_id=department_id, emp_id=emp_id)
        except DepartmentHead.DoesNotExist:
            return JsonResponse({"error": "DepartmentHead not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentHeadSerializer(dept_head)
        return JsonResponse(serializer.data)

    def put(self, request, department_id, emp_id):
        try:
            dept_head = DepartmentHead.objects.get(department_id=department_id, emp_id=emp_id)
        except DepartmentHead.DoesNotExist:
            return JsonResponse({"error": "DepartmentHead not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentHeadSerializer(dept_head, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, department_id, emp_id):
        try:
            dept_head = DepartmentHead.objects.get(department_id=department_id, emp_id=emp_id)
        except DepartmentHead.DoesNotExist:
            return JsonResponse({"error": "DepartmentHead not found"}, status=status.HTTP_404_NOT_FOUND)

        dept_head.delete()
        return JsonResponse({"message": "DepartmentHead deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EmpSalaryListView(APIView):
    def get(self, request):
        emp_salaries = EmpSalary.objects.all()
        serializer = EmpSalarySerializer(emp_salaries, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        if(request.data['active_from']):
            request.data['active_from'] = request.data['active_from'][:10]
        if(request.data['inactiv_since']):
            request.data['inactiv_since'] = request.data['inactiv_since'][:10]
        serializer = EmpSalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpSalaryDetailView(APIView):
    def get(self, request, emp_id):
        try:
            emp_salary = EmpSalary.objects.get(emp_id=emp_id)
        except EmpSalary.DoesNotExist:
            return JsonResponse({"error": "EmpSalary not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpSalarySerializer(emp_salary)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id):
        try:
            emp_salary = EmpSalary.objects.get(emp_id=emp_id)
        except EmpSalary.DoesNotExist:
            return JsonResponse({"error": "EmpSalary not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpSalarySerializer(emp_salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id):
        try:
            emp_salary = EmpSalary.objects.get(emp_id=emp_id)
        except EmpSalary.DoesNotExist:
            return JsonResponse({"error": "EmpSalary not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_salary.delete()
        return JsonResponse({"message": "EmpSalary deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EmpGivenSalaryListView(APIView):
    def get(self, request):
        emp_given_salaries = EmpGivenSalary.objects.all()
        serializer = EmpGivenSalarySerializer(emp_given_salaries, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = EmpGivenSalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        calced_salaries = EmpSalaryCalc.objects.filter(status = 1)
        for calced_salary in calced_salaries:
            defaults = {
                "given_amount": calced_salary.salary_sum,
                "taxes": calced_salary.ndsh_tax + calced_salary.hhot_tax,
            }

            # Update or create the EmpSalaryCalc record
            emp_given_sal, created = EmpGivenSalary.objects.update_or_create(
                emp_id=calced_salary.emp_id,  # Lookup field(s) to find the object
                salary_month=calced_salary.work_date.month,
                salary_year=calced_salary.work_date.year,  # Additional lookup field(s)
                defaults=defaults,  # Fields to update if found
            )
            calced_salary.status = 2
            calced_salary.save()
        return JsonResponse({"success":"true"})

class EmpGivenSalaryDetailView(APIView):
    def get(self, request, emp_id, salary_month, salary_year):
        try:
            emp_given_salary = EmpGivenSalary.objects.get(emp_id=emp_id, salary_month=salary_month, salary_year=salary_year)
        except EmpGivenSalary.DoesNotExist:
            return JsonResponse({"error": "EmpGivenSalary not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpGivenSalarySerializer(emp_given_salary)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id, salary_month, salary_year):
        try:
            emp_given_salary = EmpGivenSalary.objects.get(emp_id=emp_id, salary_month=salary_month, salary_year=salary_year)
        except EmpGivenSalary.DoesNotExist:
            return JsonResponse({"error": "EmpGivenSalary not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpGivenSalarySerializer(emp_given_salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id, salary_month, salary_year):
        try:
            emp_given_salary = EmpGivenSalary.objects.get(emp_id=emp_id, salary_month=salary_month, salary_year=salary_year)
        except EmpGivenSalary.DoesNotExist:
            return JsonResponse({"error": "EmpGivenSalary not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_given_salary.delete()
        return JsonResponse({"message": "EmpGivenSalary deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EmpWorkHourListView(APIView):
    
    def get(self, request):
        emp_work_hours = EmpWorkHour.objects.all()
        serializer = EmpWorkHourSerializer(emp_work_hours, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        datetimeFormat = '%Y-%m-%dT%H:%M'
        if(request.data['work_date']):
            request.data['work_date'] = request.data['work_date'][:10]
        if(request.data['start_date']):
            request.data['start_date'] = datetime.datetime.strptime(request.data['start_date'], datetimeFormat)
        if(request.data['end_date']):
            request.data['end_date'] = datetime.datetime.strptime(request.data['end_date'], datetimeFormat)
        if(request.data['work_start_date']):
            request.data['work_start_date'] = datetime.datetime.strptime(request.data['work_start_date'], datetimeFormat)
        if(request.data['work_end_date']):
            request.data['work_end_date'] = datetime.datetime.strptime(request.data['work_end_date'], datetimeFormat)
        print(request.data)
        serializer = EmpWorkHourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpWorkHourDetailView(APIView):
    def get(self, request, emp_id, work_date):
        try:
            emp_work_hour = EmpWorkHour.objects.get(emp_id=emp_id, work_date=work_date)
        except EmpWorkHour.DoesNotExist:
            return JsonResponse({"error": "EmpWorkHour not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpWorkHourSerializer(emp_work_hour)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id, work_date):
        try:
            emp_work_hour = EmpWorkHour.objects.get(emp_id=emp_id, work_date=work_date)
        except EmpWorkHour.DoesNotExist:
            return JsonResponse({"error": "EmpWorkHour not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpWorkHourSerializer(emp_work_hour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id, work_date):
        try:
            emp_work_hour = EmpWorkHour.objects.get(emp_id=emp_id, work_date=work_date)
        except EmpWorkHour.DoesNotExist:
            return JsonResponse({"error": "EmpWorkHour not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_work_hour.delete()
        return JsonResponse({"message": "EmpWorkHour deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class EmpWorkHourLeaveListView(APIView):
    def get(self, request):
        emp_work_hour_leaves = EmpWorkHourLeave.objects.all()
        serializer = EmpWorkHourLeaveSerializer(emp_work_hour_leaves, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        datetimeFormat = '%Y-%m-%dT%H:%M'
        if(request.data['leave_start']):
            print(request.data['leave_start'])
            request.data['leave_start'] = request.data['leave_start'][:10]
            print(request.data['leave_start'])
        if(request.data['leave_end']):
            request.data['leave_end'] = datetime.datetime.strptime(request.data['leave_end'], datetimeFormat)
        serializer = EmpWorkHourLeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpWorkHourLeaveDetailView(APIView):
    def get(self, request, emp_id, leave_date):
        try:
            emp_work_hour_leave = EmpWorkHourLeave.objects.get(emp_id=emp_id, leave_date=leave_date)
        except EmpWorkHourLeave.DoesNotExist:
            return JsonResponse({"error": "EmpWorkHourLeave not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpWorkHourLeaveSerializer(emp_work_hour_leave)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id, leave_date):
        try:
            emp_work_hour_leave = EmpWorkHourLeave.objects.get(emp_id=emp_id, leave_date=leave_date)
        except EmpWorkHourLeave.DoesNotExist:
            return JsonResponse({"error": "EmpWorkHourLeave not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpWorkHourLeaveSerializer(emp_work_hour_leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id, leave_date):
        try:
            emp_work_hour_leave = EmpWorkHourLeave.objects.get(emp_id=emp_id, leave_date=leave_date)
        except EmpWorkHourLeave.DoesNotExist:
            return JsonResponse({"error": "EmpWorkHourLeave not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_work_hour_leave.delete()
        return JsonResponse({"message": "EmpWorkHourLeave deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
def first_or_last_of_month(date: datetime):
    """
    Determines the first day of the month if the day is <= 15,
    otherwise the last day of the month.

    Args:
        date (datetime): The input date.

    Returns:
        datetime: The first or last day of the month based on the condition.
    """
    if date.day <= 15:
        # Return the first day of the month
        return date.replace(day=1), True
    else:
        # Find the last day of the month
        next_month = date.replace(day=28) + timedelta(days=4)  # Ensures we go to the next month
        last_day = next_month - timedelta(days=next_month.day)  # Backtrack to the last day of the current month
        return last_day, False


def get_weekdays_count(start_date, end_date):
    """
    Returns the number of weekdays between two dates.
    
    Parameters:
        start_date (date): The start date.
        end_date (date): The end date.
    
    Returns:
        int: The number of weekdays between the two dates.
    """
    weekdays_count = 0
    current_date = start_date

    while current_date <= end_date:
        # Check if the day is a weekday (Monday=0, ..., Sunday=6)
        if current_date.weekday() < 5:  # 0-4 are weekdays
            weekdays_count += 1
        current_date += timedelta(days=1)
    
    return weekdays_count

class EmpSalaryCalcView(APIView):
    def post(self, request, emp_id):
        salary = EmpSalary.objects.filter(emp_id = emp_id, status = 1)
        total_salary = 0
        for sal in salary:
            total_salary += sal.salary_amount
        if(request.data['work_date']):
            request.data['work_date'] = request.data['work_date'][:10]
            workDate = datetime.datetime.strptime(request.data['work_date'], '%Y-%m-%d').date()
        else:
            workDate = datetime.date.today()
        
        work_date_start, is_first = first_or_last_of_month(workDate)
        print(request.data['work_date'] )
        print(workDate)
        print(emp_id)
        employee = Employee.objects.get(emp_id=emp_id)
        if(is_first):
            workhour = EmpWorkHour.objects.filter(emp_id = emp_id, work_date__gte = work_date_start, work_date__lte = workDate)
            weekdays = get_weekdays_count(work_date_start, workDate)
        else:
            workhour = EmpWorkHour.objects.filter(emp_id = emp_id, work_date__gte = workDate, work_date__lte = work_date_start)
            weekdays = get_weekdays_count(workDate, work_date_start)
        total_hours = weekdays * 8
        hourly_salary = total_salary / total_hours
        total_work_hours= 0
        for wh in workhour:
            total_work_hours += wh.salary_hour

        calced_salary = total_work_hours * hourly_salary
        try:
            ndshConfig = SalaryConfig.objects.get(config_name = 'NDSH')
        except:
            ndshConfig = 15
        try:
            hhotConfig = SalaryConfig.objects.get(config_name = 'HHOT')
        except:
            hhotConfig = 5
        

        defaults = {
            "sum_hour": total_hours,
            "salaray_hour": total_work_hours,
            "hourly_salary": hourly_salary,
            "salary_sum": calced_salary,
            "ndsh_tax": calced_salary * int(ndshConfig.config_value) / 100,
            "hhot_tax": calced_salary * int(hhotConfig.config_value) / 100,
            "status": 1,
        }

        # Update or create the EmpSalaryCalc record
        emp_salary_calc, created = EmpSalaryCalc.objects.update_or_create(
            emp_id=employee,  # Lookup field(s) to find the object
            work_date=workDate,  # Additional lookup field(s)
            defaults=defaults,  # Fields to update if found
        )

        # Serialize the updated or created object
        json_calc = EmpSalaryCalcSerializer(emp_salary_calc)

        # Return the serialized data in the response
        return JsonResponse(json_calc.data, status=status.HTTP_201_CREATED)
        
class EmpSalaryCalcDetailView(APIView):
    def get(self, request, emp_id, work_date):
        try:
            emp_salary_calc = EmpSalaryCalc.objects.get(emp_id=emp_id, work_date=work_date)
        except EmpSalaryCalc.DoesNotExist:
            return JsonResponse({"error": "EmpSalaryCalc not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpSalaryCalcSerializer(emp_salary_calc)
        return JsonResponse(serializer.data)

    def put(self, request, emp_id, work_date):
        try:
            emp_salary_calc = EmpSalaryCalc.objects.get(emp_id=emp_id, work_date=work_date)
        except EmpSalaryCalc.DoesNotExist:
            return JsonResponse({"error": "EmpSalaryCalc not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpSalaryCalcSerializer(emp_salary_calc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id, work_date):
        try:
            emp_salary_calc = EmpSalaryCalc.objects.get(emp_id=emp_id, work_date=work_date)
        except EmpSalaryCalc.DoesNotExist:
            return JsonResponse({"error": "EmpSalaryCalc not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_salary_calc.delete()
        return JsonResponse({"message": "EmpSalaryCalc deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class EmpSalaryCalcListView(APIView):
    def get(self, request):
        emp_salary_calcs = EmpSalaryCalc.objects.all()
        serializer = EmpSalaryCalcSerializer(emp_salary_calcs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = EmpSalaryCalcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SalaryConfigListView(APIView):
    def get(self, request):
        salary_configs = SalaryConfig.objects.all()
        serializer = SalaryConfigSerializer(salary_configs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = SalaryConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SalaryConfigDetailView(APIView):
    def get(self, request, config_name):
        try:
            salary_config = SalaryConfig.objects.get(config_name=config_name)
        except SalaryConfig.DoesNotExist:
            return JsonResponse({"error": "SalaryConfig not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SalaryConfigSerializer(salary_config)
        return JsonResponse(serializer.data)

    def put(self, request):
        try:
            salary_config = SalaryConfig.objects.get(config_name=request.data['config_name'])
        except SalaryConfig.DoesNotExist:
            return JsonResponse({"error": "SalaryConfig not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SalaryConfigSerializer(salary_config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, config_name):
        try:
            salary_config = SalaryConfig.objects.get(config_name=config_name)
        except SalaryConfig.DoesNotExist:
            return JsonResponse({"error": "SalaryConfig not found"}, status=status.HTTP_404_NOT_FOUND)
        
        salary_config.delete()
        return JsonResponse({"message": "SalaryConfig deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class GetTimeReport(APIView):
    def post(self, request):
        # Get the data from the request
        emp_id = request.data.get('emp_id')
        work_date_start = request.data.get('work_date_start')
        work_date_end = request.data.get('work_date_end')

        # Make sure all parameters are present
        if not emp_id or not work_date_start or not work_date_end:
            return Response({'error': 'emp_id, work_date_start, and work_date_end are required'}, status=400)

        # Query the EmpWorkHour model and annotate the sum of late_hour
        result = (
            EmpWorkHour.objects.filter(
                emp_id=emp_id,
                work_date__gt=work_date_start,
                work_date__lt=work_date_end
            )
            # .values('emp_id')  # You can group by work_date here
            .aggregate(
                total_late=Sum('late_hour'),  # Sum the late_hour field
                total_work_hours=Sum('salary_hour'),  # Assuming you want to sum work_hours as well
                total_leave_hours=Sum('leave_hour')  # Assuming you want to sum work_hours as well
            )
            # .order_by('work_date')  # Optional: order by the work_date
        )
        result['emp_id'] = emp_id
        return Response(result)