from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name = "index"),
    path("delete/<int:id>/", views.delete , name ="delete"),
    path("update/<int:id>/", views.update, name = "update"),
]
