from django.contrib import admin
from testApp.models import EmployeeModel

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(EmployeeModel,EmployeeAdmin)
