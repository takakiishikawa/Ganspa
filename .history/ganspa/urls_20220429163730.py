from django.urls import path
from.import views

urlpatterns=[
    path("top/",views.index,name="index")
    path("guide/",views.index,name="index")    
    ]