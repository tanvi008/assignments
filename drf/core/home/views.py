from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.

@api_view(['GET','POST'])
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, safe=False)
    
    elif request.method == 'POST':
    
        serializer  = EmployeeSerializer(data= request.data)
        #print(jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE','GET','POST'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        #return JsonResponse("Employee"+str(pk), safe=False)
    except Employee.DoesNotExist:
        return Response(status=404)

    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
       
        serializer = EmployeeSerializer(employee, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors )


def UserListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data)