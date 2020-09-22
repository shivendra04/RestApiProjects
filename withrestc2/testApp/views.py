from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from testApp.serializers import NameSerializer
# Create your views here.
class TestApiView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'Happy pongal','colors':colors})
    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Happy Janmastami!!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'This respone from put method of APIView'})

    def patch(self,request,*args,**kwargs):
        return Response({'msg':'This respone from patch method of APIView'})


    def delete(self,request,*args,**kwargs):
        return Response({'msg':'This response from delete method of APIView'})

class TestViewSet(ViewSet):
    def list(self,request,*args,**kwargs):
        colors=['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'Happy pongal','colors':colors})
    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} Happy Janmastami!!!'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def retrieve(sellf,request,pk=None):
        return Response({'msg':'This response from retrive method of ViewSet'})

    def update(sellf,request,pk=None):
        return Response({'msg':'This response from update method of ViewSet'})

    def partial_update(sellf,request,pk=None):
        return Response({'msg':'This response from partial_update method of ViewSet'})

    def destroy(sellf,request,pk=None):
        return Response({'msg':'This response from destroy method of ViewSet'})
