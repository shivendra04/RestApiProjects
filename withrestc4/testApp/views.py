from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testApp.serializers import EmployeeSerializer
from testApp.models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testApp.permissions import IsReadOnly,IsGetOrPatch,ShivendraPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testApp.authentications import CustomAuthentication,CustomAuthentication2

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #authentication_classes=[TokenAuthentication,]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
    #authentication_classes=[JSONWebTokenAuthentication,]
    authentication_classes=[CustomAuthentication2,]
    permission_classes=[IsAuthenticated,]
