from django.urls import path
from.import views

urlpatterns=[
    path("top/",views.index1,name="top")
    path("tops/",views.index2,name="top")


    
    ]
