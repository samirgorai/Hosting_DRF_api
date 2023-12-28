from django import forms
from basic_api.models import Employee_data

class Employee_form_create(forms.ModelForm):
    class Meta:
        model=Employee_data
        fields="__all__"


class Employee_form_read(forms.ModelForm):
    class Meta:
        model=Employee_data
        fields=['emp_id']


class Employee_form_update(forms.ModelForm):
    class Meta:
        model=Employee_data
        fields="__all__"

class Employee_form_delete(forms.ModelForm):
    class Meta:
        model=Employee_data
        fields=['emp_id']
