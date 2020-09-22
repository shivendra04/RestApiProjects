from django.shortcuts import render
from rest_framework.views import APIView
from testApp.models import Employee
from testApp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins


# Create your views here.
# class EmployeeListApiView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         serializer=EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)

# class EmployeeListApiView(ListAPIView):
#     #queryset=Employee.objects.all()#queryset and serializer_class predefined
#     serializer_class=EmployeeSerializer
#     def get_queryset(self):
#         qs=Employee.objects.all()
#         name=self.request.GET.get('ename')
#         if name is not None:
#             qs=qs.filter(ename__icontains=name)
#         return qs

# class EmployeeCreateAPIView(CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

# class EmployeeRetriveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
# class EmployeeRetriveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

# class EmployeeRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
class EmployeeListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeRetrieveUpdateDestroyModelMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(self,request,*args,**kwargs)
