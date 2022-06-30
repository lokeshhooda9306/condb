from django.shortcuts import render,HttpResponseRedirect
# from collage.modelform import empolyee_form
from .modelform import empolyee_form, department_form
from .models import Employee,Department


# Create your views here.
def indexm(request):
    form_data = empolyee_form()
    db_data= Employee.objects.all()
    if request.method =='POST':
        form_data= empolyee_form(request.POST)
        if form_data.is_valid:
            form_data.save()
            return HttpResponseRedirect('/indexm/')
    
    # context ={'form':form}
    return render(request, 'indexm.html', {'form':form_data,'data':db_data})




def update(request,id):
    form_data=empolyee_form()
    db_data=Employee.objects.get(pk=id)
    if request.method=="POST":
        form_data= empolyee_form(request.POST, instance=db_data)
        if form_data.is_valid:
            form_data.save()
            return HttpResponseRedirect("/indexm/")

    else:
        form_data=empolyee_form(instance= db_data)

    return render(request, 'update.html', {'form':form_data, "data": db_data})




def delete(request, id):
    data = Employee.objects.get(pk =id).delete()
    return HttpResponseRedirect('/indexm/')

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

def depupdate(request, id):
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



def depdelete(request, id):
    data = Department.objects.get(id=id).delete()
    return HttpResponseRedirect('/department/')








