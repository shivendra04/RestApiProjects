from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=256)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=256)