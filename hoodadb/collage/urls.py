from django.urls import path
from . import views

urlpatterns = [
    path("indexm/", views.indexm, name = "indexm"),
    path("delete/<int:id>/", views.delete , name ="delete"),
    path("update/<int:id>/", views.update, name = "update"),
    path("depupdate/<int:id>/", views.depupdate, name ="depupdate"),
    path("department/", views.department, name="department"),
    path("depdelete/<int:id>/", views.depdelete, name ="depdelete"),

]
