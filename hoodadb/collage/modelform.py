from itertools import product
from django import forms
from .models import Employee, Department, Project



class DateInput(forms.DateInput):
    input_type = 'date'

class empolyee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields="__all__"
        widgets = {
            'date_of_birth': DateInput
        }
    
    # def save(self, commit: bool = ...) -> _M:
    #     return super().save(commit)
        
class department_form(forms.ModelForm):
    class Meta:
        model = Department
        fields="__all__"


class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields ="__all__"