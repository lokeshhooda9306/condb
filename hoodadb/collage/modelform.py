from django import forms
from .models import Employee, department


class empolyee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields="__all__"
        
