from rest_framework import serializers
from basic_api.models import Employee_data

class Employee_data_serializer(serializers.ModelSerializer):
    class Meta:
        model=Employee_data
        fields=['name','emp_id']
