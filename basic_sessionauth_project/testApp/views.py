from rest_framework.viewsets import ModelViewSet
from testApp.serializers import EmployeeSerializer
from testApp.models import Employee
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[SessionAuthentication,]
    permission_classes=[IsAuthenticated,]
