from django.urls import path
from.import views

app_name = 'test'

urlpatterns=[
    path("top/",views.top,name="top"),
    path("guide/",views.guide,name="guide"),
    path("users/",views.users,name="users"),
    path("user/",views.user,name="user"),


    
    ]
