from django.urls import path
from . import views

urlpatterns = [
    path("employee/", views.employee, name = "employee"),
    path("delete/<int:id>/", views.delete , name ="delete"),
    path("update/<int:id>/", views.update, name = "update"),
    path("departmentupdate/<int:id>/", views.departmentupdate, name ="departmentupdate"),
    path("department/", views.department, name="department"),
    path("departmentdelete/<int:id>/", views.departmentdelete, name ="departmentdelete"),
    path("projectupdate/<int:id>/", views.projectupdate, name ="projectupdate"),
    path("project/", views.project, name="project"),
    path("projectdelete/<int:id>/", views.projectdelete, name ="projectdelete"),


]
