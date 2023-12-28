
from rest_framework.response import Response
from rest_framework import viewsets
from employee_api.serializers import Employee_data_serializer
from basic_api.models import Employee_data
from django.shortcuts import get_object_or_404
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee_data.objects.all()
    serializer_class=Employee_data_serializer


    def list(self,request):
        queryset=Employee_data.objects.all()#all data is fetched from Database
        serializer=Employee_data_serializer(queryset,many=True) #it is serialized
        return Response(serializer.data)# serialized data is sent as a response
    
    def retrive(self,request,pk=None):
        queryset=Employee_data.objects.all()#all data is fetched from Database
        user=get_object_or_404(queryset,pk=pk)#a particular data is fetched with pk ID 
        serialize=Employee_data_serializer(user)# result is serialized
        return Response(serialize.data)# response is send back to user to make a request we have to provide URL as http://127.0.0.1:8000/employeeapi/<1>/ <change according to data needed>
    

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=200)
    

