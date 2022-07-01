from django.shortcuts import render,HttpResponseRedirect
# from collage.modelform import empolyee_form
from .modelform import empolyee_form, department_form,project_form
from .models import Employee,Department,Project


# Create your views here.
def employee(request):
    form_data = empolyee_form()
    db_data= Employee.objects.all()
    if request.method =='POST':
        form_data= empolyee_form(request.POST)
        if form_data.is_valid:
            form_data.save()
            return HttpResponseRedirect('/employee/')
    
    # context ={'form':form}
    return render(request, 'employee.html', {'form':form_data,'data':db_data})




def update(request,id):
    form_data=empolyee_form()
    db_data=Employee.objects.get(pk=id)
    if request.method=="POST":
        form_data= empolyee_form(request.POST, instance=db_data)
        if form_data.is_valid:
            form_data.save()
            return HttpResponseRedirect("/employee/")

    else:
        form_data=empolyee_form(instance= db_data)

    return render(request, 'update.html', {'form':form_data, "data": db_data})




def delete(request, id):
    data = Employee.objects.get(pk =id).delete()
    return HttpResponseRedirect('/employee/')

# function for department update and delete
def department(request):
    dep_form = department_form()
    depdata = Department.objects.all()
    if request.method =='POST':
        dep_form= department_form(request.POST)
        if dep_form.is_valid:
            dep_form.save()
            return HttpResponseRedirect('/department/')

    return render(request, 'department.html',{"dform":dep_form, "date": depdata})

def departmentupdate(request, id):
    dep_form = department_form()
    dep_data = Department.objects.get(id=id)
    if request.method=="POST":
        dep_form= department_form(request.POST, instance=dep_data)
        if dep_form.is_valid:
            dep_form.save()
            return HttpResponseRedirect("/department/")

    else:
        dep_form=department_form(instance= dep_data)

    return render(request, 'departmentupdate.html', {'dform':dep_form, "data": dep_data})



def departmentdelete(request, id):
    data = Department.objects.get(id=id).delete()
    return HttpResponseRedirect('/department/')



# function for project update and delete

def project(request):
    pro_form = project_form()
    prodata = Project.objects.all()
    if request.method =='POST':
        pro_form= project_form(request.POST)
        if pro_form.is_valid:
            pro_form.save()
            return HttpResponseRedirect('/project/')

    return render(request, 'project.html',{"pform":pro_form, "date": prodata})




def projectupdate(request, id):
    pro_form = project_form()
    pro_data = Project.objects.get(id=id)
    if request.method=="POST":
        pro_form= project_form(request.POST, instance=pro_data)
        if pro_form.is_valid:
            pro_form.save()
            return HttpResponseRedirect("/project/")

    else:
        pro_form=project_form(instance= pro_data)

    return render(request, 'projectupdate.html', {'pform':pro_form, "data": pro_data})



def projectdelete(request, id):
    data = Project.objects.get(id=id).delete()
    return HttpResponseRedirect('/project/')
