from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getdemo", views.demoget, name="demoget"),
    path("getdemoval",views.demogetval,name="getdemoval"),
    path("demopost",views.demopost,name="demopost"),
    path("save",views.save,name="save"),
    path("getone",views.getone,name="getone"),
    path("deleteone",views.deleteone,name="deleteone"),
    path("updateone",views.updateone,name="updateone")
]
