from django.shortcuts import render
from testApp.models import Employee
from testApp.serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from testApp.pagination import MyPagination,MyPagination2,MyPagination3
class EmployeeListView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    search_fields=('eno',)
    ordering_fields=('eno','esal')# default value is '__all__'
    #pagination_class=MyPagination
    #pagination_class=MyPagination3
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__contains=name)
    #     return qs
