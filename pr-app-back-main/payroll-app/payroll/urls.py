from django.urls import path
from .views import *

urlpatterns = [

    path('login', LoginView.as_view(), name='login'),
    # EmpPerm URLs
    path('empPermList', EmpPermListView.as_view(), name='empPermList'),
    path('empPermDetail/<int:emp_id>/<int:perm_id>', EmpPermDetailView.as_view(), name='empPermDetail'),
    path('empPermInsert', EmpPermListView.as_view(), name='empPermInsert'),
    path('empPermUpdate/<int:emp_id>/<int:perm_id>', EmpPermDetailView.as_view(), name='empPermUpdate'),
    path('empPermDelete/<int:emp_id>/<int:perm_id>', EmpPermDetailView.as_view(), name='empPermDelete'),

    # DepartmentHead URLs
    path('departmentHeadList', DepartmentHeadListView.as_view(), name='departmentHeadList'),
    path('departmentHeadDetail/<int:department_id>/<int:emp_id>', DepartmentHeadDetailView.as_view(), name='departmentHeadDetail'),
    path('departmentHeadInsert', DepartmentHeadListView.as_view(), name='departmentHeadInsert'),
    path('departmentHeadUpdate/<int:department_id>/<int:emp_id>', DepartmentHeadDetailView.as_view(), name='departmentHeadUpdate'),
    path('departmentHeadDelete/<int:department_id>/<int:emp_id>', DepartmentHeadDetailView.as_view(), name='departmentHeadDelete'),

    path('departmentHeadDictList', DepartmentHeadDictListView.as_view(), name='departmentHeadDictList'),
    # EmpSalary URLs
    path('empSalaryList', EmpSalaryListView.as_view(), name='empSalaryList'),
    path('empSalaryDetail/<int:emp_id>', EmpSalaryDetailView.as_view(), name='empSalaryDetail'),
    path('empSalaryInsert', EmpSalaryListView.as_view(), name='empSalaryInsert'),
    path('empSalaryUpdate/<int:emp_id>', EmpSalaryDetailView.as_view(), name='empSalaryUpdate'),
    path('empSalaryDelete/<int:emp_id>', EmpSalaryDetailView.as_view(), name='empSalaryDelete'),

    # EmpGivenSalary URLs
    path('empGivenSalaryList', EmpGivenSalaryListView.as_view(), name='empGivenSalaryList'),
    path('empGivenSalaryBatch', EmpGivenSalaryListView.as_view(), name='empGivenSalaryBatch'),
    path('empGivenSalaryDetail/<int:emp_id>/<int:salary_month>/<int:salary_year>', EmpGivenSalaryDetailView.as_view(), name='empGivenSalaryDetail'),
    path('empGivenSalaryInsert', EmpGivenSalaryListView.as_view(), name='empGivenSalaryInsert'),
    path('empGivenSalaryUpdate/<int:emp_id>/<int:salary_month>/<int:salary_year>', EmpGivenSalaryDetailView.as_view(), name='empGivenSalaryUpdate'),
    path('empGivenSalaryDelete/<int:emp_id>/<int:salary_month>/<int:salary_year>', EmpGivenSalaryDetailView.as_view(), name='empGivenSalaryDelete'),

    # EmpWorkHour URLs
    path('empWorkHourList', EmpWorkHourListView.as_view(), name='empWorkHourList'),
    path('empWorkHourDetail/<int:emp_id>/<str:work_date>', EmpWorkHourDetailView.as_view(), name='empWorkHourDetail'),
    path('empWorkHourInsert', EmpWorkHourListView.as_view(), name='empWorkHourInsert'),
    path('empWorkHourUpdate/<int:emp_id>/<str:work_date>', EmpWorkHourDetailView.as_view(), name='empWorkHourUpdate'),
    path('empWorkHourDelete/<int:emp_id>/<str:work_date>', EmpWorkHourDetailView.as_view(), name='empWorkHourDelete'),

    # EmpWorkHourLeave URLs
    path('empWorkHourLeaveList', EmpWorkHourLeaveListView.as_view(), name='empWorkHourLeaveList'),
    path('empWorkHourLeaveDetail/<int:emp_id>/<str:leave_date>', EmpWorkHourLeaveDetailView.as_view(), name='empWorkHourLeaveDetail'),
    path('empWorkHourLeaveInsert', EmpWorkHourLeaveListView.as_view(), name='empWorkHourLeaveInsert'),
    path('empWorkHourLeaveUpdate/<int:emp_id>/<str:leave_date>', EmpWorkHourLeaveDetailView.as_view(), name='empWorkHourLeaveUpdate'),
    path('empWorkHourLeaveDelete/<int:emp_id>/<str:leave_date>', EmpWorkHourLeaveDetailView.as_view(), name='empWorkHourLeaveDelete'),

    # Department URLs
    path('departmentList', DepartmentListView.as_view(), name='departmentList'),
    path('departmentDetail/<int:department_id>', DepartmentDetailView.as_view(), name='departmentDetail'),
    path('departmentInsert', DepartmentListView.as_view(), name='departmentInsert'),
    path('departmentUpdate/<int:department_id>', DepartmentDetailView.as_view(), name='departmentUpdate'),
    path('departmentDelete/<int:department_id>', DepartmentDetailView.as_view(), name='departmentDelete'),
    path('departmentDictList', DepartmentDictListView.as_view(), name='departmentDictList'),

    # EmpPosition URLs
    path('empPositionList', EmpPositionListView.as_view(), name='empPositionList'),
    path('empPositionDetail/<int:position_id>', EmpPositionDetailView.as_view(), name='empPositionDetail'),
    path('empPositionInsert', EmpPositionListView.as_view(), name='empPositionInsert'),
    path('empPositionUpdate/<int:position_id>', EmpPositionDetailView.as_view(), name='empPositionUpdate'),
    path('empPositionDelete/<int:position_id>', EmpPositionDetailView.as_view(), name='empPositionDelete'),

    # Permission URLs
    path('permissionList', PermissionListView.as_view(), name='permissionList'),
    path('permissionDetail/<int:perm_id>', PermissionDetailView.as_view(), name='permissionDetail'),
    path('permissionInsert', PermissionListView.as_view(), name='permissionInsert'),
    path('permissionUpdate/<int:perm_id>', PermissionDetailView.as_view(), name='permissionUpdate'),
    path('permissionDelete/<int:perm_id>', PermissionDetailView.as_view(), name='permissionDelete'),

    path('permissionDictList', PermissionDictListView.as_view(), name='permissionDictList'),
    # Employee URLs
    path('employeeList', EmployeeListView.as_view(), name='employeeList'),
    path('employeeDetail/<int:emp_id>', EmployeeDetailView.as_view(), name='employeeDetail'),
    path('employeeInsert', EmployeeListView.as_view(), name='employeeInsert'),
    path('employeeUpdate/<int:emp_id>', EmployeeDetailView.as_view(), name='employeeUpdate'),
    path('employeeDelete/<int:emp_id>', EmployeeDetailView.as_view(), name='employeeDelete'),

    path('employeeDictList', EmployeeDictListView.as_view(), name='employeeDictList'),

    
    path('empSalaryCalc/<int:emp_id>/', EmpSalaryCalcView.as_view(), name='employeeDelete'),
    path('empSalaryCalcList/', EmpSalaryCalcListView.as_view(), name='empSalaryCalcList'),
    path('empSalaryCalcDetail/<int:emp_id>/<str:work_date>', EmpSalaryCalcDetailView.as_view(), name='empSalaryCalcDetail'),
    path('empSalaryCalcInsert', EmpSalaryCalcListView.as_view(), name='empSalaryCalcInsert'),
    path('empSalaryCalcUpdate/<int:emp_id>/<str:work_date>', EmpSalaryCalcDetailView.as_view(), name='empSalaryCalcUpdate'),
    path('empSalaryCalcDelete/<int:emp_id>/<str:work_date>', EmpSalaryCalcDetailView.as_view(), name='empSalaryCalcDelete'),

    path('salaryConfigDetail/<str:config_name>', SalaryConfigDetailView.as_view(), name='salaryConfigDetail'),
    path('salaryConfigList/', SalaryConfigListView.as_view(), name='salaryConfigList'),
    path('salaryConfigInsert', SalaryConfigListView.as_view(), name='salaryConfigInsert'),
    path('salaryConfigUpdate', SalaryConfigDetailView.as_view(), name='salaryConfigUpdate'),
    path('salaryConfigDelete/<str:config_name>', SalaryConfigDetailView.as_view(), name='salaryConfigDelete'),

    
    path('getTimeReport', GetTimeReport.as_view(), name='getTimeReport'),
    
]
