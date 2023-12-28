from django.db import models

# Create your models here.

class Employee_data(models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.IntegerField(primary_key=True )

    def __str__(self):
        return self.name
    
        