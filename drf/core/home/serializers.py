# hyperlink serializer, normal serializer and one model serializer
# for now we are using model serializer

from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        #field =['name', 'age'] #for specifying the requirements
        #exclude=['id', ''] #for excluding some of the fields
        fields ='__all__' #serializes all the fields

    def create(self, validated_data):
        print("Create Method called.. ")
        return Employee.objects.create(**validated_data)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)



