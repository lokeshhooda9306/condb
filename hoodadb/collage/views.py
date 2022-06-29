from django.shortcuts import render,HttpResponseRedirect
# from collage.modelform import empolyee_form
from .modelform import empolyee_form
from .models import department,Employee


# Create your views here.
def index(request):
    form_data = empolyee_form()
    db_data= Employee.objects.all()
    if request.method =='POST':
        form_data= empolyee_form(request.POST)
        if form_data.is_valid:
            form_data.save()
            return HttpResponseRedirect('/index/')
    
    # context ={'form':form}
    return render(request, 'index.html', {'form':form_data,'data':db_data})




def update(request,id):
    form_data=empolyee_form()
    db_data=Employee.objects.get(pk=id)
    if request.method=="POST":
        form_data= empolyee_form(request.POST, instance=db_data)
        if form_data.is_valid:
            form_data.save()
            return HttpResponseRedirect("/index/")

    else:
        form_data=empolyee_form(instance= db_data)

    return render(request, 'update.html', {'form':form_data, "data": db_data})




def delete(request, id):
    data= Employee.objects.get(pk =id).delete()
    return HttpResponseRedirect('/index/')