from rest_framework import serializers
from testApp.models import EmployeeModel
def multiple_of_1000(value):
    print('Validation by validator..')
    if value%1000!=0:
        raise serializers.ValidationError('Employee salary shoule be multiple of 1000')

class EmployeeSerializer(serializers.ModelSerializer):
    esal=serializers.IntegerField(validators=[multiple_of_1000])
    class Meta:
        model=EmployeeModel
        fields='__all__'

# class EmployeeSerializer(serializers.Serializer):
#     eno=serializers.IntegerField()
#     ename=serializers.CharField(max_length=256)
#     esal=serializers.IntegerField(validators=[multiple_of_1000])
#     eaddr=serializers.CharField(max_length=256)
#     def validate_esal(self,value):
#         print('Field level validation')
#         if value<5000:
#             raise serializers.ValidationError('Employee salary shoule be minimum 5000')
#         return value
#
#     def validate(self,data):
#         print('Object level validation')
#         ename=data.get('ename')
#         esal=data.get('esal')
#         if ename.lower()=='mukesh':
#             if esal<50000:
#                 raise serializers.ValidationError('Employee salary shoule be minimum 50000f')
#         return data
#
#     def create(self,validated_data):
#         return EmployeeModel.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.ename=validated_data.get('eno',instance.ename)
#         instance.esal=validated_data.get('eno',instance.esal)
#         instance.eaddr=validated_data.get('eno',instance.eaddr)
#         instance.save()
#         return instance
