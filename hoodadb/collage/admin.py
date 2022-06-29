from django.contrib import admin
from .models import Employee, department


admin.site.register(department)
admin.site.register(Employee)

# Register your models here.

