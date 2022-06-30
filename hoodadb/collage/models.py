from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
class Employee(models.Model):
    gender_choose=[("m","male"),("f","female"),]
    first_name=models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField()
    gender=models.CharField(max_length=20,choices=gender_choose,)
    email_id = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_department_head = models.BooleanField()
    postition = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name

