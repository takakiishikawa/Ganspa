from django.urls import path
from.import views

urlpatterns=[
    path("top/",views.index1,name="index")
    path("guide/",views.index2,name="index")    
    ]
