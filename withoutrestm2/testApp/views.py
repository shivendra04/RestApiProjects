from django.shortcuts import render
from django.views.generic import View
from testApp.utils import is_json
from testApp.mixins import HttpResponseMixin
from testApp.mixins import SerializeMixin
import json
from testApp.models import student
from django.views.decorators.csrf import  csrf_exempt
from django.utils.decorators import method_decorator
from testApp.forms import StudentForm
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(View,SerializeMixin,HttpResponseMixin):
    def get_object_by_id(self,id):
        try:
            std=student.objects.get(id=id)
        except student.DoesNotExist:
            std=None
        return std

    def get(self,request,*args,**kwargs):
         if id is not None:
             data=request.body
             valid_json=is_json(data)
             if not valid_json:
                 return self.render_to_http_response(json.dumps({'msg':'Please provide valid json only'}),status=404)
                 p_data=json.loads(data)
                 id=p_data.get('id',None)
             std=self.get_object_by_id(id)
             if std is None:
                 return self.render_to_http_response(json.dumps({'msg':'No Matched record with provided id'}),status=404)
             json_data=self.serialize([std,])
             return self.render_to_http_response(json_data)
         qs=student.objects.all()
         json_data=self.serialize(qs)
         return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
         data=request.body
         valid_json=is_json(data)
         if not valid_json:
             return self.render_to_http_response(json.dumps({'msg':'Please provide valid json only'}),status=404)
         std_data=json.loads(data)
         form=StudentForm(std_data)
         if form.is_valid():
             form.save(commit=True)
             return self.render_to_http_response(json.dumps({'msg':'Resource created successfully'}))
         if form.errors:
             json_data=json.dumps(form.errors)
             return self.render_to_http_response(json_data,status=404)

    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please provide valid json only'}),status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'To perform id is must.'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
             return self.render_to_http_response(json.dumps({'msg':'No matched resource is found with the provided id.'}),status=400)
        original_data={
        'name':std.name,
        'rollno':std.rollno,
        'marks':std.marks,
        'gf':std.gf,
        'bf':std.bf,
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Resource updated successfully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please provide valid json only'}),status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'To perform deletion id is must.'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
             return self.render_to_http_response(json.dumps({'msg':'No matched resource is found with the provided id.'}),status=400)
        status, deleted_item=std.delete()
        if status==1:
            json_data=json.dumps({'msg':'Resource delted successfully'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'Unable to delete.. plz try again.'})
        return self.render_to_http_response(json_data,status=400)
