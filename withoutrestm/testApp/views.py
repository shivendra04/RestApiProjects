from django.shortcuts import render
from django.views.generic import View
from testApp.models import employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testApp.mixins import SerializeMixin,HttpResponseMixin

from django.views.decorators.csrf import  csrf_exempt
from django.utils.decorators import method_decorator
from testApp.utils import is_json
from testApp.forms import EmployeeForm

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(SerializeMixin,HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=employee.objects.get(id=id)
        except employee.DoesNotExist:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        qs=employee.objects.all()
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only.'})
            return self.render_to_http_response(json_data,status=200)
            p_data=json.loads(data)
            id=p_data.get('id',None)
            if id is not None:
                emp=self.get_object_by_id(id)
                if emp is None:
                    json_data=json.dumps({'msg':'The requested resources is not availabe.'})
                    return self.render_to_http_response(json_data,status=404)
                    json_data=self.serialize([emp,])
                    return self.render_to_http_response(json_data)
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource created successfully.'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only.'})
            return self.render_to_http_response(json_data,status=200)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'To perform updation id is mondatory, please provide..'})
            return self.render_to_http_response(json_data,status=404)
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'No resource with matched id, not possilbe updation'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        original_data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource updated successfully.'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only.'})
            return self.render_to_http_response(json_data,status=200)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The requested resources is not availabe.'})
                return self.render_to_http_response(json_data,status=404)
            status,deleted_item=emp.delete()
            if status==1:
                json_data=json.dumps({'msg':'Resources deleted successfully.'})
                return self.render_to_http_response(json_data)
            json_data=json.dumps({'msg':'Unable to delete...Please ty again.'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'To perform updation id is mondatory, please provide..'})
        return self.render_to_http_response(json_data,status=404)


# Create your views here.
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeDetailCBV(SerializeMixin,HttpResponseMixin,View):
#     def get_object_by_id(self,id):
#         try:
#             emp=employee.objects.get(id=id)
#         except employee.DoesNotExist:
#             emp=None
#         return emp
#
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp=employee.objects.get(id=id)
#         except employee.DoesNotExist:
#             json_data=json.dumps({'msg':'The requested resources is not availabe.'})
#             #return HttpResponse(json_data,content_type='application/json',status=400)
#             return self.render_to_http_response(json_data,status=404)
#         else:
#             json_data=self.serialize([emp,])
#             #return HttpResponse(json_data,content_type='application/json',status=200)
#             return self.render_to_http_response(json_data)
#         return HttpResponse(json_data,content_type='application/json')
#
#     def put(self,request,id,*args,**kwargs):
#         emp=self.get_object_by_id(id)
#         if emp is None:
#             json_data=json.dumps({'msg':'No Matched record found, not possible\
#             to perform updation.'})
#             return self.render_to_http_response(json_data,status=200)
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'Please send valid json data only.'})
#             return self.render_to_http_response(json_data,status=200)
#         provided_data=json.loads(data)
#         original_data={
#         'eno':emp.eno,
#         'ename':emp.ename,
#         'esal':emp.esal,
#         'eaddr':emp.eaddr,
#         }
#         original_data.update(provided_data)
#         form=EmployeeForm(original_data,instance=emp)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'Resource updated successfully.'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
#
#     def delete(self,request,id,*args,**kwargs):
#         emp=self.get_object_by_id(id)
#         if emp is None:
#             json_data=json.dumps({'msg':'No Matched record found, not possible\
#             to perform deletion.'})
#             return self.render_to_http_response(json_data,status=404)
#         status,deleted_item=emp.delete()
#         if status==1:
#             json_data=json.dumps({'msg':'Resources deleted successfully.'})
#             return self.render_to_http_response(json_data)
#         json_data=json.dumps({'msg':'Unable to delete...Please ty again.'})
#         return self.render_to_http_response(json_data)
#
#
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeListCBV(SerializeMixin,HttpResponseMixin,View):
#     def get(self,request,*args,**kwargs):
#         qs=employee.objects.all()
#         json_data=self.serialize(qs )
#         return HttpResponse(json_data,content_type='application/json')
#
#     def post(self,request,*args,**kwargs):
#         #return self.render_to_http_response(json_data)
#         #json_data=json.dumps({'msg':'This is from post'})
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'Please send valid json data only'})
#             return self.render_to_http_response(json_data,status=400)
#         #json_data=json.dumps({'msg':'You Provides valid json data only'})
#         #return self.render_to_http_response(json_data)
#         empdata=json.loads(data)
#         form=EmployeeForm(empdata)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'Resource created successfully.'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
