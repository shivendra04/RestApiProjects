from django.shortcuts import render
from testApp.models import Employee
from testApp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
class EmployeeCRUDCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all() 
